#include <assert.h>
#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define Extend(type, size, max, ptr)                                           \
  if (size == max) {                                                           \
    max *= 2;                                                                  \
    ptr = (type *)realloc(ptr, sizeof(type) * max);                            \
  }

// Extendable sequence

#define NewSeq(type, name)                                                     \
  size_t name##_max = 8, name##_size = 0;                                      \
  type *name##_val = (type *)malloc(sizeof(type) * name##_max)

#define FreeSeq(name) free(name##_val)

#define SeqNth(name, n) (name##_val[n])

#define SeqAppend(type, name, val)                                             \
  Extend(type, name##_size, name##_max, name##_val);                           \
  name##_val[name##_size++] = val

#define SeqSize(name) (name##_size)

#define SeqPop(name) (name##_val[--name##_size])

char *str_copy(char *base) {
  assert(base);
  char *new = (char *)malloc(sizeof(char) * (strlen(base) + 1));
  strcpy(new, base);
  return new;
}

bool contains(char ch, char *base) {
  for (char *i = base; *i; i++) {
    if (*i == ch)
      return true;
  }
  return false;
}

typedef struct Val Val;

typedef enum ValType {
  INT_V,
  STR_V,
  LIST_V,
  NULL_V,
  FUNC_V,
  CFUNC_V,
  CSTMT_V,
} ValType;

typedef struct String {
  char *val;
  size_t size, max;
} String;

String *String_new(char *base);
String *String_copy(String *base);
void String_free(String *str);
void String_append(String *str, char ch);
void String_extend(String *str, String *other);

typedef struct List {
  Val *val;
  size_t size, max;
  size_t *rc;
} List;

List *List_new();
List *List_copy(List *base);
List *List_pass(List *base);
void List_append(List *base, Val val);
void List_free(List *list);

typedef struct AST AST;
typedef struct Scope Scope;

typedef struct Func Func;
typedef Val (*CFunc)(long long, Val *);
typedef Val (*CStmt)(long long, AST *, Scope *);

typedef struct Val {
  ValType tp;
  union {
    long long i;
    String *s;
    List *l;
    Func *f;
    CFunc cf;
    CStmt cs;
  };
} Val;

Val INT_Val(long long i);
Val STR_Val(String *s);
Val LIST_Val(List *l);
Val NULL_Val();
Val Val_copy(Val base);
Val Val_pass(Val base);
void Val_free(Val val);
void Val_print(Val v);

typedef struct Map {
  struct Map **children;
  Val v;
  bool is_end;
} Map;

Map *Map_new();
void Map_free(Map *map);
void Map_insert(Map *map, char *k, Val v);
Val *Map_find(Map *map, char *k);

typedef enum TokenType {
  INT_T,
  STR_T,
  SYM_T,
  SP_T,
  EOF_T,
} TokenType;

typedef enum SPToken {
  LPAREN_T,
  RPAREN_T,
} SPToken;

typedef struct Token {
  TokenType tp;
  union {
    long long i;
    String *s;
    SPToken sp;
  };
} Token;

Token Token_new(TokenType tp);
Token Token_INT(long long i);
Token Token_STR(String *s);
Token Token_SYM(String *s);
Token Token_SP(SPToken sp);
void Token_free(Token t);

typedef struct Lexer {
  String *code;
  char *cur;
  Token token;
} Lexer;

Lexer *Lexer_new(String *code);
void Lexer_free(Lexer *l);
void Lexer_next(Lexer *l);
void Lexer_skip(Lexer *l);

typedef enum ASType {
  NUM_AST,
  STR_AST,
  LIST_AST,
  SYM_AST,
} ASType;

typedef struct AST {
  ASType tp;
  long long len;
  union {
    long long i;
    String *s;
    struct AST *l;
  };
} AST;

void AST_free(AST ast);
AST parse(Lexer *l);

typedef struct Scope {
  struct Scope *parent;
  Map *vars;
  size_t *rc;
} Scope;

Scope *Scope_new(Scope *parent);
Scope *Scope_pass(Scope *base);
void Scope_free(Scope *scope);
Val *Scope_find(Scope *scope, char *name);
void Scope_define(Scope *scope, char *name, Val val);

typedef struct Func {
  long long body_len;
  AST params;
  Scope *closure;
  AST *body;
} Func;

Val eval(AST ast, Scope *scope);
Scope *std_scope();

void test_map() {
  Map *map = Map_new();
  Map_insert(map, "a", INT_Val(1));
  Map_insert(map, "b", INT_Val(2));
  // printf("%lld\n", Map_find(map, "a"));
}

int main(int argc, char *argv[]) {
  assert(argc == 2);
  // test_map();
  FILE *f = fopen(argv[1], "r");
  if (f == NULL) {
    printf("Failed to open.\n");
    exit(-1);
  }
  String *code = String_new("");
  while (!feof(f)) {
    String_append(code, fgetc(f));
  }
  code->size--;
  code->val[code->size] = '\0';
  // puts(code->val);
  Lexer *l = Lexer_new(code);
  AST ast = parse(l);
  Scope *scope = std_scope();
  Val res = eval(ast, scope);
  printf("Ret = ");
  Val_print(res);
  printf("\n");
  Val_free(res);
  Lexer_free(l);
  AST_free(ast);
  return 0;
}

// String

String *String_new(char *base) {
  String *new = (String *)malloc(sizeof(String));
  new->max = new->size = strlen(base);
  if (new->max == 0) {
    new->max = 8;
  }
  new->val = (char *)malloc(sizeof(char) * (new->max + 1));
  strcpy(new->val, base);
  return new;
}

String *String_copy(String *base) { return String_new(base->val); }

void String_free(String *str) {
  assert(str);
  free(str->val);
  free(str);
}

void String_append(String *str, char ch) {
  assert(str);
  if (str->max == str->size) {
    str->max *= 2;
    str->val = realloc(str->val, sizeof(char) * (str->max + 1));
  }
  str->val[str->size++] = ch;
  str->val[str->size] = 0;
}

void String_extend(String *str, String *other) {
  assert(str && other);
  size_t new_size = str->size + other->size;
  if (new_size > str->max) {
    str->max = new_size;
    str->val = realloc(str->val, sizeof(char) * (str->max + 1));
  }
  strcpy(str->val + str->size, other->val);
  str->size = new_size;
}

// List

List *List_new() {
  List *list = (List *)malloc(sizeof(List));
  list->max = 8;
  list->size = 0;
  list->val = (Val *)malloc(sizeof(Val) * list->max);
  list->rc = (size_t *)malloc(sizeof(size_t));
  *list->rc = 1;
  return list;
}

List *List_pass(List *base) {
  (*base->rc)++;
  return base;
}

List *List_copy(List *base) {
  List *list = (List *)malloc(sizeof(List));
  list->max = base->max;
  list->size = base->size;
  list->rc = (size_t *)malloc(sizeof(size_t));
  *list->rc = 1;
  list->val = (Val *)malloc(sizeof(Val) * list->max);
  for (size_t i = 0; i < list->size; i++)
    list->val[i] = Val_copy(base->val[i]);
  return list;
}

void List_append(List *list, Val v) {
  assert(list);
  if (list->max == list->size) {
    list->max *= 2;
    list->val = realloc(list->val, sizeof(Val) * list->max);
  }
  list->val[list->size++] = v;
}

void List_free(List *list) {
  assert(list);
  (*list->rc)--;
  if (!*list->rc) {
    // printf("free!\n");
    free(list->rc);
    for (size_t i = 0; i < list->size; i++)
      Val_free(list->val[i]);
    free(list->val);
    free(list);
  }
}

// Val

Val INT_Val(long long i) {
  Val v;
  v.tp = INT_V;
  v.i = i;
  return v;
}

Val STR_Val(String *s) {
  Val v;
  v.tp = STR_V;
  v.s = s;
  return v;
}

Val LIST_Val(List *l) {
  Val v;
  v.tp = LIST_V;
  v.l = l;
  return v;
}

Val NULL_Val() {
  Val v;
  v.tp = NULL_V;
  return v;
}

Val Val_pass(Val base) {
  Val v = base;
  switch (v.tp) {
  case INT_V:
    break;
  case STR_V:
    v.s = String_copy(v.s);
    break;
  case LIST_V:
    v.l = List_pass(v.l);
    break;
  case FUNC_V:
    v.f->closure = Scope_pass(v.f->closure);
    break;
  default:
    break;
  }
  return v;
}

Val Val_copy(Val base) {
  Val v = base;
  switch (v.tp) {
  case INT_V:
    break;
  case STR_V:
    v.s = String_copy(v.s);
    break;
  case LIST_V:
    v.l = List_copy(v.l);
    break;
  default:
    break;
  }
  return v;
}

void Val_free(Val val) {
  /* printf("free(");
  Val_print(val);
  printf(")\n"); */
  switch (val.tp) {
  case STR_V:
    String_free(val.s);
    break;
  case LIST_V:
    List_free(val.l);
    break;
  case FUNC_V:
    Scope_free(val.f->closure);
    break;
  default:
    break;
  }
}

// Map

Map *Map_new() {
  Map *map = (Map *)malloc(sizeof(Map));
  map->children = (Map **)calloc(128, sizeof(Map *));
  map->is_end = false;
  return map;
}

void Map_free(Map *map) {
  assert(map);
  if (map->is_end)
    Val_free(map->v);
  for (size_t i = 0; i < 128; i++) {
    if (map->children[i])
      Map_free(map->children[i]);
  }
  free(map->children);
  free(map);
}

void Map_insert(Map *map, char *k, Val v) {
  assert(map && k);
  if (!*k) {
    if (map->is_end)
      Val_free(map->v);
    map->v = v;
    map->is_end = true;
    return;
  }
  if (!map->children[*k]) {
    map->children[*k] = Map_new();
  }
  Map_insert(map->children[*k], k + 1, v);
}

Val *Map_find(Map *map, char *k) {
  assert(map && k);
  // printf("%s\n", k);
  if (!*k) {
    if (map->is_end)
      return &map->v;
    else
      return NULL;
  }
  if (!map->children[*k])
    return NULL;
  return Map_find(map->children[*k], k + 1);
}

// Token

Token Token_new(TokenType tp) {
  Token new;
  new.tp = tp;
  return new;
}

Token Token_INT(long long i) {
  Token new = Token_new(INT_T);
  new.i = i;
  return new;
}

Token Token_STR(String *s) {
  assert(s);
  Token new = Token_new(STR_T);
  new.s = s;
  return new;
}

Token Token_SYM(String *s) {
  assert(s);
  Token new = Token_new(SYM_T);
  new.s = s;
  return new;
}

Token Token_SP(SPToken sp) {
  Token new = Token_new(SP_T);
  new.sp = sp;
  return new;
}

void Token_free(Token t) {
  switch (t.tp) {
  case STR_T:
  case SYM_T:
    String_free(t.s);
    break;
  default:
    break;
  }
}

// Lexer

Lexer *Lexer_new(String *code) {
  assert(code);
  Lexer *l = (Lexer *)malloc(sizeof(Lexer));
  l->code = code;
  l->cur = code->val;
  Lexer_next(l);
  return l;
}

void Lexer_free(Lexer *l) {
  assert(l);
  free(l->code);
  Token_free(l->token);
}

void Lexer_next(Lexer *l) {
  Lexer_skip(l);
  if (l->cur != l->code->val)
    Token_free(l->token);
  if (!*l->cur) {
    l->token.tp = EOF_T;
  } else if (*l->cur == '(') {
    l->token.tp = SP_T;
    l->token.sp = LPAREN_T;
    l->cur++;
  } else if (*l->cur == ')') {
    l->token.tp = SP_T;
    l->token.sp = RPAREN_T;
    l->cur++;
  } else if (isdigit(*l->cur)) {
    l->token.tp = INT_T;
    l->token.i = 0;
    while (*l->cur && isdigit(*l->cur)) {
      l->token.i *= 10;
      l->token.i += *l->cur++ - '0';
    }
  } else if (*l->cur == '"') {
    l->token.tp = STR_T;
    l->token.s = String_new("");
    l->cur++;
    while (*l->cur && *l->cur != '"') {
      if (*l->cur == '\\') {
        l->cur++;
        if (!*l->cur) {
          printf("Unexpected EOF.\n");
          exit(-1);
        } else if (*l->cur == 'r')
          String_append(l->token.s, '\r'), l->cur++;
        else if (*l->cur == 't')
          String_append(l->token.s, '\t'), l->cur++;
        else if (*l->cur == 'a')
          String_append(l->token.s, '\a'), l->cur++;
        else if (*l->cur == 'f')
          String_append(l->token.s, '\f'), l->cur++;
        else if (*l->cur == 'v')
          String_append(l->token.s, '\v'), l->cur++;
        else if (*l->cur == 'b')
          String_append(l->token.s, '\b'), l->cur++;
        else if (*l->cur == 'n')
          String_append(l->token.s, '\n'), l->cur++;
        else if (*l->cur == '\'')
          String_append(l->token.s, '\''), l->cur++;
        else if (*l->cur == '"')
          String_append(l->token.s, '"'), l->cur++;
        else if (*l->cur == '\\')
          String_append(l->token.s, '\\'), l->cur++;
        else if (*l->cur == 'x') {
          l->cur++;
          char res = 0;
          for (char i = 0; i < 2; i++) {
            res *= 16;
            if (!*l->cur) {
              printf("Unexpected EOF.\n");
              exit(-1);
            } else if ('0' <= *l->cur && *l->cur <= '9')
              res += *l->cur++ - '0';
            else if ('a' <= *l->cur && *l->cur <= 'f')
              res += *l->cur++ - 'a';
            else if ('A' <= *l->cur && *l->cur <= 'F')
              res += *l->cur++ - 'A';
            else {
              printf("Wrong escape sequence.\n");
              exit(-1);
            }
          }
          String_append(l->token.s, res);
        } else {
          printf("Wrong escape sequence\n");
          exit(-1);
        }
      } else {
        String_append(l->token.s, *l->cur++);
      }
    }
    if (!*l->cur) {
      printf("Unexpected EOF.\n");
      exit(-1);
    }
    l->cur++;
  } else {
    l->token.tp = SYM_T;
    l->token.s = String_new("");
    while (*l->cur && !contains(*l->cur, " \n\t;\"()")) {
      String_append(l->token.s, *l->cur++);
    }
  }
}

void Lexer_skip(Lexer *l) {
  assert(l);
  while (*l->cur && contains(*l->cur, " \n\t;")) {
    if (*l->cur == ';') {
      while (*l->cur && *l->cur != '\n')
        l->cur++;
    } else {
      l->cur++;
    }
  }
}

// AST

void AST_free(AST ast) {
  switch (ast.tp) {
  case SYM_AST:
  case STR_AST:
    String_free(ast.s);
    break;
  case LIST_AST:
    for (long long i = 0; i < ast.len; i++)
      AST_free(ast.l[i]);
    break;
  default:
    break;
  }
}

AST parse(Lexer *l) {
  assert(l);
  if (l->token.tp == EOF_T) {
    printf("Unexpected EOF.\n");
    exit(-1);
  } else if (l->token.tp == SP_T && l->token.sp == LPAREN_T) {
    Lexer_next(l);
    NewSeq(AST, list);
    while (l->token.tp != EOF_T &&
           !(l->token.tp == SP_T && l->token.sp == RPAREN_T)) {
      SeqAppend(AST, list, parse(l));
    }
    if (l->token.tp == EOF_T) {
      printf("Unexpected EOF.\n");
      exit(-1);
    }
    Lexer_next(l);
    AST res;
    res.tp = LIST_AST;
    res.len = list_size;
    res.l = list_val;
    return res;
  } else if (l->token.tp == INT_T) {
    AST res;
    res.tp = NUM_AST;
    res.i = l->token.i;
    Lexer_next(l);
    return res;
  } else if (l->token.tp == STR_T) {
    AST res;
    res.tp = STR_AST;
    res.s = String_copy(l->token.s);
    Lexer_next(l);
    return res;
  } else if (l->token.tp == SYM_T) {
    AST res;
    res.tp = SYM_AST;
    res.s = String_copy(l->token.s);
    Lexer_next(l);
    return res;
  } else {
    printf("Unexpected token.\n");
    exit(-1);
  }
}

// Scope

Scope *Scope_new(Scope *parent) {
  Scope *new = (Scope *)malloc(sizeof(Scope));
  if (parent)
    new->parent = Scope_pass(parent);
  else
    new->parent = NULL;
  new->rc = (size_t *)malloc(sizeof(size_t));
  *new->rc = 1;
  new->vars = Map_new();
  return new;
}

Scope *Scope_pass(Scope *base) {
  assert(base);
  (*base->rc)++;
  return base;
}

void Scope_free(Scope *scope) {
  assert(scope);
  (*scope->rc)--;
  if (!*scope->rc) {
    free(scope->rc);
    if (scope->parent)
      Scope_free(scope->parent);
    Map_free(scope->vars);
    free(scope);
  }
}

Val *Scope_find(Scope *scope, char *name) {
  assert(scope);
  Val *res = Map_find(scope->vars, name);
  if (res)
    return res;
  else if (scope->parent)
    return Scope_find(scope->parent, name);
  else {
    printf("Undefined variable '%s'.", name);
    exit(-1);
  }
}

void Scope_define(Scope *scope, char *name, Val val) {
  assert(scope);
  Map_insert(scope->vars, name, val);
}

// Others

bool Val_toBool(Val v) {
  switch (v.tp) {
  case NULL_V:
    return false;
  case INT_V:
    return v.i;
  case STR_V:
    return v.s->size;
  case LIST_V:
    return v.l->size;
  case FUNC_V:
    return true;
  case CFUNC_V:
    return true;
  case CSTMT_V:
    return true;
  }
}

void Val_print(Val v) {
  switch (v.tp) {
  case NULL_V:
    printf("null");
    break;
  case INT_V:
    printf("%lld", v.i);
    break;
  case STR_V:
    printf("%s", v.s->val);
    break;
  case LIST_V:
    printf("(");
    if (v.l->size) {
      Val_print(v.l->val[0]);
      for (long long i = 1; i < v.l->size; i++) {
        printf(" ");
        Val_print(v.l->val[i]);
      }
    }
    printf(")");
    break;
  case FUNC_V:
    printf("<Func>");
    break;
  case CFUNC_V:
    printf("<CFunc>");
    break;
  case CSTMT_V:
    printf("<CStmt>");
    break;
  default:
    printf("Unknown type '%d'.", v.tp);
    exit(-1);
  }
}

// Std CFunc & CStmt

Val cstmt_define(long long cnt, AST *args, Scope *scope) {
  assert(cnt >= 2);
  assert(args[0].tp == SYM_AST);
  Val val = eval(args[1], scope);
  Scope_define(scope, args[0].s->val, val);
  return Val_pass(val);
}

Val cstmt_set(long long cnt, AST *args, Scope *scope) {
  assert(cnt >= 2);
  assert(args[0].tp == SYM_AST);
  Val val = eval(args[1], scope);
  Val *var = Scope_find(scope, args[0].s->val);
  if (!var) {
    printf("Undefined variable '%s'.\n", args[0].s->val);
    exit(-1);
  }
  *var = val;
  return Val_pass(val);
}

Val cstmt_if(long long cnt, AST *args, Scope *scope) {
  assert(cnt == 3);
  if (Val_toBool(eval(args[0], scope))) {
    return eval(args[1], scope);
  } else {
    return eval(args[2], scope);
  }
}

Val cstmt_lambda(long long cnt, AST *args, Scope *scope) {
  assert(cnt > 1);
  Func *f = (Func *)malloc(sizeof(Func));
  f->body = args + 1;
  f->body_len = cnt - 1;
  f->closure = Scope_pass(scope);
  f->params = args[0];
  Val res;
  res.tp = FUNC_V;
  res.f = f;
  return res;
}

Val cfunc_print(long long cnt, Val *args) {
  assert(cnt);
  for (long long i = 0; i < cnt; i++) {
    Val_print(args[i]);
  }
  for (long long i = 0; i < cnt - 1; i++) {
    Val_free(args[i]);
  }
  return args[cnt - 1];
}

Val cfunc_println(long long cnt, Val *args) {
  assert(cnt);
  for (long long i = 0; i < cnt; i++) {
    Val_print(args[i]);
  }
  for (long long i = 0; i < cnt - 1; i++) {
    Val_free(args[i]);
  }
  printf("\n");
  return args[cnt - 1];
}

Val cfunc_add(long long cnt, Val *args) {
  assert(cnt);
  assert(args[0].tp == INT_V);
  long long res = args[0].i;
  for (long long i = 1; i < cnt; i++) {
    res += args[i].i;
  }
  return INT_Val(res);
}

Val cfunc_sub(long long cnt, Val *args) {
  assert(cnt);
  assert(args[0].tp == INT_V);
  if (cnt == 0) {
    return INT_Val(-args[0].i);
  } else {
    long long res = args[0].i;
    for (long long i = 1; i < cnt; i++) {
      res -= args[i].i;
    }
    return INT_Val(res);
  }
}

Val cfunc_mul(long long cnt, Val *args) {
  assert(cnt);
  assert(args[0].tp == INT_V);
  long long res = args[0].i;
  for (long long i = 1; i < cnt; i++) {
    res *= args[i].i;
  }
  return INT_Val(res);
}

Val cfunc_div(long long cnt, Val *args) {
  assert(cnt > 1);
  assert(args[0].tp == INT_V);
  long long res = args[0].i;
  for (long long i = 1; i < cnt; i++) {
    res /= args[i].i;
  }
  return INT_Val(res);
}

Val cfunc_mod(long long cnt, Val *args) {
  assert(cnt > 1);
  assert(args[0].tp == INT_V);
  long long res = args[0].i;
  for (long long i = 1; i < cnt; i++) {
    res %= args[i].i;
  }
  return INT_Val(res);
}

Val cstmt_eq(long long cnt, AST *args, Scope *scope) {
  assert(cnt);
  Val last = eval(args[0], scope);
  assert(last.tp == INT_V);
  for (long long i = 1; i < cnt; i++) {
    Val cur = eval(args[i], scope);
    assert(cur.tp == INT_V);
    if (cur.i != last.i)
      return INT_Val(false);
    last = cur;
  }
  return INT_Val(true);
}

Val cstmt_ne(long long cnt, AST *args, Scope *scope) {
  assert(cnt);
  Val last = eval(args[0], scope);
  assert(last.tp == INT_V);
  for (long long i = 1; i < cnt; i++) {
    Val cur = eval(args[i], scope);
    assert(cur.tp == INT_V);
    if (cur.i == last.i)
      return INT_Val(false);
    last = cur;
  }
  return INT_Val(true);
}

Val cstmt_gt(long long cnt, AST *args, Scope *scope) {
  assert(cnt);
  Val last = eval(args[0], scope);
  assert(last.tp == INT_V);
  for (long long i = 1; i < cnt; i++) {
    Val cur = eval(args[i], scope);
    assert(cur.tp == INT_V);
    if (cur.i >= last.i)
      return INT_Val(false);
    last = cur;
  }
  return INT_Val(true);
}

Val cstmt_lt(long long cnt, AST *args, Scope *scope) {
  assert(cnt);
  Val last = eval(args[0], scope);
  assert(last.tp == INT_V);
  for (long long i = 1; i < cnt; i++) {
    Val cur = eval(args[i], scope);
    assert(cur.tp == INT_V);
    if (cur.i <= last.i)
      return INT_Val(false);
    last = cur;
  }
  return INT_Val(true);
}

Val cstmt_ge(long long cnt, AST *args, Scope *scope) {
  assert(cnt);
  Val last = eval(args[0], scope);
  assert(last.tp == INT_V);
  for (long long i = 1; i < cnt; i++) {
    Val cur = eval(args[i], scope);
    assert(cur.tp == INT_V);
    if (cur.i > last.i)
      return INT_Val(false);
    last = cur;
  }
  return INT_Val(true);
}

Val cstmt_le(long long cnt, AST *args, Scope *scope) {
  assert(cnt);
  Val last = eval(args[0], scope);
  assert(last.tp == INT_V);
  for (long long i = 1; i < cnt; i++) {
    Val cur = eval(args[i], scope);
    assert(cur.tp == INT_V);
    if (cur.i < last.i)
      return INT_Val(false);
    last = cur;
  }
  return INT_Val(true);
}

Val cstmt_and(long long cnt, AST *args, Scope *scope) {
  assert(cnt);
  for (long long i = 0; i < cnt; i++) {
    Val cur = eval(args[i], scope);
    if (!Val_toBool(cur))
      return INT_Val(false);
    Val_free(cur);
  }
  return INT_Val(true);
}

Val cstmt_or(long long cnt, AST *args, Scope *scope) {
  assert(cnt);
  for (long long i = 0; i < cnt; i++) {
    Val cur = eval(args[i], scope);
    if (Val_toBool(cur))
      return INT_Val(true);
    Val_free(cur);
  }
  return INT_Val(false);
}

Val cfunc_strcat(long long cnt, Val *args) {
  assert(cnt);
  assert(args[0].tp == STR_V);
  String *res = args[0].s;
  for (long long i = 1; i < cnt; i++) {
    assert(args[i].tp == STR_V);
    String_extend(res, args[i].s);
    Val_free(args[i]);
  }
  return STR_Val(res);
}

Val cfunc_list(long long cnt, Val *args) {
  List *res = List_new();
  for (long long i = 0; i < cnt; i++)
    List_append(res, args[i]);
  return LIST_Val(res);
}

Val cstmt_begin(long long cnt, AST *args, Scope *scope) {
  Val res = NULL_Val();
  Scope *new_scope = Scope_new(scope);
  for (long long i = 0; i < cnt; i++) {
    Val_free(res);
    res = eval(args[i], new_scope);
  }
  Scope_free(new_scope);
  return res;
}

Val cstmt_while(long long cnt, AST *args, Scope *scope) {
  assert(cnt);
  Val res = NULL_Val();
  while (Val_toBool(eval(args[0], scope))) {
    Scope *new_scope = Scope_new(scope);
    for (long long i = 1; i < cnt; i++) {
      Val_free(res);
      res = eval(args[i], new_scope);
    }
    Scope_free(new_scope);
  }
  return res;
}

Val cfunc_set_nth(long long cnt, Val *args) {
  assert(cnt == 3);
  assert(args[0].tp == LIST_V);
  assert(args[1].tp == INT_V);
  assert(args[1].i < args[0].l->size);
  args[0].l->val[args[1].i] = args[2];
  return args[0];
}

Val cfunc_list_nth(long long cnt, Val *args) {
  assert(cnt == 2);
  assert(args[0].tp == LIST_V);
  assert(args[1].tp == INT_V);
  assert(args[1].i < args[0].l->size);
  return Val_pass(args[0].l->val[args[1].i]);
}

Val cfunc_list_append(long long cnt, Val *args) {
  assert(cnt == 2);
  assert(args[0].tp == LIST_V);
  List_append(args[0].l, args[1]);
  return Val_pass(args[0]);
}

// Eval

Val eval(AST ast, Scope *scope) {
  switch (ast.tp) {
  case NUM_AST:
    return INT_Val(ast.i);
  case STR_AST:
    return STR_Val(String_copy(ast.s));
  case SYM_AST: {
    Val *res = Scope_find(scope, ast.s->val);
    if (!res) {
      printf("Undefined variable '%s'.\n", ast.s->val);
      exit(-1);
    }
    return Val_pass(*res);
  }
  case LIST_AST: {
    assert(ast.len);
    Val func = eval(ast.l[0], scope);
    if (func.tp == CSTMT_V)
      return func.cs(ast.len - 1, ast.l + 1, scope);
    NewSeq(Val, args);
    for (long long i = 1; i < ast.len; i++) {
      SeqAppend(Val, args, eval(ast.l[i], scope));
    }
    if (func.tp == CFUNC_V) {
      Val res = func.cf(args_size, args_val);
      FreeSeq(args);
      return res;
    }
    if (func.tp == FUNC_V) {
      assert(func.f);
      Val res = NULL_Val();
      Scope *new_scope = Scope_new(scope);
      assert(func.f->params.len == args_size);
      for (long long i = 0; i < args_size; i++) {
        Scope_define(new_scope, func.f->params.l[i].s->val, args_val[i]);
      }
      for (long long i = 0; i < func.f->body_len; i++) {
        res = eval(func.f->body[i], new_scope);
      }
      FreeSeq(args);
      Scope_free(new_scope);
      return res;
    }
    printf("Expect a function.\n");
    exit(-1);
  }
  }
}

Val CFUNC_Val(CFunc cf) {
  Val v;
  v.tp = CFUNC_V;
  v.cf = cf;
  return v;
}

Val CSTMT_Val(CStmt cs) {
  Val v;
  v.tp = CSTMT_V;
  v.cs = cs;
  return v;
}

Scope *std_scope() {
  Scope *scope = Scope_new(NULL);
#define B_CF(sym, name) Scope_define(scope, sym, CFUNC_Val(cfunc_##name))
#define B_CS(sym, name) Scope_define(scope, sym, CSTMT_Val(cstmt_##name))
  B_CS("define", define);
  B_CS("set!", set);
  B_CS("if", if);
  B_CS("lambda", lambda);
  B_CF("print", print);
  B_CF("println", println);
  B_CF("+", add);
  B_CF("-", sub);
  B_CF("*", mul);
  B_CF("/", div);
  B_CF("%", mod);
  B_CS("=", eq);
  B_CS("!=", ne);
  B_CS(">", gt);
  B_CS("<", lt);
  B_CS(">=", ge);
  B_CS("<=", le);
  B_CS("and", and);
  B_CS("or", or);
  B_CF("strcat", strcat);
  B_CF("list", list);
  B_CS("begin", begin);
  B_CS("while", while);
  B_CF("set-nth!", set_nth);
  B_CF("list-nth", list_nth);
  B_CF("list-append", list_append);
#undef B_CF
#undef B_CS
  return scope;
}
