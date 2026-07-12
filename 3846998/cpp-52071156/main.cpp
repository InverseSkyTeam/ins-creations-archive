/*
极不完善的Lisp，甚至可以称为Lisp语法的C（没有GC）
使用动态作用域（懒得给作用域写自动释放）、、、
无类型（真正的无，运行时根本不能知道一个值的类型）
上帝的编程语言？不，只有上帝能用的编程语言！（
*/
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

#define ERROR(msg)                                                             \
  {                                                                            \
    printf msg;                                                                \
    exit(-1);                                                                  \
  }

char *str_clone(char *base) {
  char *str = (char *)malloc(sizeof(char) * (strlen(base) + 1));
  strcpy(str, base);
  return str;
}

char *str_nclone(char *base, size_t n) {
  char *str = (char *)malloc(sizeof(char) * (n + 1));
  memcpy(str, base, n);
  str[n] = '\0';
  return str;
}

typedef struct Func Func;

typedef union Val {
  long long i;
  char *s;
  union Val *p;
  Func *f;
} Val;

typedef enum ExprType {
  INT_E,
  STR_E,
  SYM_E,
  LIST_E,
} ExprType;

typedef struct Expr Expr;
typedef struct Scope Scope;

typedef Val (*cfunc_t)(long long, Val *);
typedef Val (*cstmt_t)(long long, Expr *, Scope *);

typedef struct Expr {
  ExprType tp;
  union {
    long long i;
    char *s;
    struct Expr *p;
  };
  long long len;
} Expr;

typedef enum FuncType {
  FUNC_T,
  CFUNC_T,
  CSTMT_T,
} FuncType;

typedef struct func_t {
  char **params;
  Expr *body;
  long long len;
} func_t;

typedef struct Func {
  FuncType tp;
  union {
    cfunc_t cf;
    cstmt_t cs;
    func_t f;
  };
} Func;

typedef struct Map {
  struct Map **children;
  bool is_t;
  Val val;
} Map;

Map Map_new() {
  Map m;
  m.children = (Map **)calloc(128, sizeof(Map *));
  m.is_t = false;
  return m;
}

void Map_free(Map m) {
  for (int i = 0; i < 128; i++) {
    if (m.children[i])
      Map_free(*m.children[i]);
  }
  free(m.children);
}

void Map_insert(Map *m, char *k, Val v) {
  if (*k == 0) {
    m->is_t = true;
    m->val = v;
  } else {
    if (!m->children[*k]) {
      m->children[*k] = (Map *)malloc(sizeof(Map));
      *m->children[*k] = Map_new();
    }
    Map_insert(m->children[*k], k + 1, v);
  }
}

Val *Map_find(Map *m, char *k) {
  if (*k == 0) {
    if (m->is_t)
      return &m->val;
    else
      return NULL;
  } else if (m->children[*k])
    return Map_find(m->children[*k], k + 1);
  else
    return NULL;
}

typedef enum TokenType {
  EOF_TK,
  INT_TK,
  STR_TK,
  SYM_TK,
  SP_TK,
} TokenType;

typedef struct Token {
  TokenType tp;
  union {
    long long i;
    char *s;
  };
} Token;

typedef struct Lexer {
  char *cur;
  Token t;
} Lexer;

bool contains(char ch, char *base) {
  for (char *i = base; *i; i++)
    if (*i == ch)
      return true;
  return false;
}

void Lexer_next(Lexer *l) {
  while (*l->cur && contains(*l->cur, " \n\t;")) {
    if (*l->cur == ';') {
      while (*l->cur && *l->cur != '\n')
        l->cur++;
    } else
      l->cur++;
  }

  Token tk;
  if (!*l->cur) {
    tk.tp = EOF_TK;
  } else if (isdigit(*l->cur)) {
    long long num = 0;
    while (isdigit(*l->cur)) {
      num *= 10;
      num += *l->cur++ - '0';
    }
    tk.tp = INT_TK;
    tk.i = num;
  } else if (contains(*l->cur, "()")) {
    tk.tp = SP_TK;
    tk.i = *l->cur++;
  } else {
    NewSeq(char, id);
    while (*l->cur && !contains(*l->cur, " \n\t;()")) {
      SeqAppend(char, id, *l->cur++);
    }
    SeqAppend(char, id, 0);
    tk.tp = SYM_TK;
    tk.s = id_val;
  }
  l->t = tk;
}

Lexer Lexer_new(char *code) {
  Lexer new;
  new.cur = code;
  Lexer_next(&new);
  return new;
}

Expr parse(Lexer *l) {
  // puts(l->cur);
  Expr res;
  if (l->t.tp == EOF_TK) {
    printf("Unexpected EOF.\n");
    exit(-1);
  } else if (l->t.tp == SP_TK && l->t.i == '(') {
    Lexer_next(l);
    NewSeq(Expr, list);
    long long len = 0;
    while (l->t.tp != EOF_TK && !(l->t.tp == SP_TK && l->t.i == ')')) {
      SeqAppend(Expr, list, parse(l));
      len++;
    }
    if (l->t.tp == EOF_TK) {
      printf("Unexpected EOF.\n");
      exit(-1);
    }
    Lexer_next(l);
    res.tp = LIST_E;
    res.p = list_val;
    res.len = len;
  } else if (l->t.tp == INT_TK) {
    res.tp = INT_E;
    res.i = l->t.i;
    Lexer_next(l);
  } else if (l->t.tp == SYM_TK) {
    res.tp = SYM_E;
    res.s = l->t.s;
    Lexer_next(l);
  } else {
    printf("Unexpected token.\n");
    exit(-1);
  }
  return res;
}

typedef struct Scope {
  Map var;
  struct Scope *parent;
} Scope;

Scope *Scope_new(Scope *parent) {
  Scope *new = (Scope *)malloc(sizeof(Scope));
  new->var = Map_new();
  new->parent = parent;
  return new;
}

void Scope_free(Scope *scope) {
  Map_free(scope->var);
  free(scope);
}

Val *Scope_find(Scope *scope, char *k) {
  Val *v = Map_find(&scope->var, k);
  if (v)
    return v;
  else if (scope->parent)
    return Scope_find(scope->parent, k);
  else
    return NULL;
}

void Scope_define(Scope *scope, char *k, Val v) {
  Map_insert(&scope->var, k, v);
}

Val eval(Expr e, Scope *scope);

Val _cstmt_begin(long long cnt, Expr *body, Scope *scope) {
  Scope *new_scope = Scope_new(scope);
  Val res;
  res.i = 0;
  for (long long i = 0; i < cnt; i++) {
    res = eval(body[i], new_scope);
  }
  Scope_free(new_scope);
  return res;
}

Val _cstmt_define(long long cnt, Expr *args, Scope *scope) {
  assert(cnt >= 2);
  Expr name = args[0];
  assert(name.tp == SYM_E);
  Val val = eval(args[1], scope);
  Scope_define(scope, name.s, val);
  return val;
}

Val _cstmt_lambda(long long cnt, Expr *args, Scope *scope) {
  assert(cnt >= 1);
  NewSeq(char *, params);
  assert(args[0].tp == LIST_E);
  for (long long i = 0; i < args[0].len; i++) {
    assert(args[0].p[i].tp == SYM_E);
    SeqAppend(char *, params, args[0].p[i].s);
  }
  SeqAppend(char *, params, NULL);
  Val res;
  res.f = (Func *)malloc(sizeof(Func));
  res.f->tp = FUNC_T;
  res.f->f = (func_t){params_val, args + 1, cnt - 1};
  return res;
}

Val _cstmt_if(long long cnt, Expr *args, Scope *scope) {
  assert(cnt == 3);
  long long cond = eval(args[0], scope).i;
  // printf("%lld\n", cond);
  if (cond) {
    return eval(args[1], scope);
  } else {
    return eval(args[2], scope);
  }
}

Val _cfunc_print_i(long long cnt, Val *args) {
  assert(cnt == 1);
  printf("%lld", args->i);
  Val res = *args;
  free(args);
  return res;
}

Val _cfunc_newline(long long cnt, Val *args) {
  assert(cnt == 0);
  printf("\n");
  free(args);
  Val res;
  return res;
}

Val _cfunc_add(long long cnt, Val *args) {
  assert(cnt >= 1);
  long long res = args[0].i;
  for (long long i = 1; i < cnt; i++)
    res += args[i].i;
  Val r;
  r.i = res;
  free(args);
  return r;
}

Val _cfunc_sub(long long cnt, Val *args) {
  assert(cnt >= 1);
  Val r;
  if (cnt > 1) {
    long long res = args[0].i;
    for (long long i = 1; i < cnt; i++)
      res -= args[i].i;
    r.i = res;
  } else {
    r.i = -args[0].i;
  }
  free(args);
  return r;
}

Val _cfunc_mul(long long cnt, Val *args) {
  assert(cnt >= 1);
  long long res = args[0].i;
  for (long long i = 1; i < cnt; i++)
    res *= args[i].i;
  Val r;
  r.i = res;
  free(args);
  return r;
}

Val _cfunc_div(long long cnt, Val *args) {
  assert(cnt == 2);
  Val res;
  res.i = args[0].i / args[1].i;
  return res;
}

Val _cfunc_mod(long long cnt, Val *args) {
  assert(cnt == 2);
  Val res;
  res.i = args[0].i % args[1].i;
  return res;
}

Val _cstmt_eq(long long cnt, Expr *args, Scope *scope) {
  assert(cnt >= 1);
  Val res;
  long long first = eval(args[0], scope).i;
  for (long long i = 1; i < cnt; i++)
    if (!(eval(args[i], scope).i == first)) {
      res.i = 0;
      return res;
    }
  res.i = 1;
  return res;
}

Val _cstmt_ne(long long cnt, Expr *args, Scope *scope) {
  assert(cnt >= 1);
  Val res;
  long long first = eval(args[0], scope).i;
  for (long long i = 1; i < cnt; i++)
    if (!(eval(args[i], scope).i != first)) {
      res.i = 0;
      return res;
    }
  res.i = 1;
  return res;
}

Val _cstmt_gt(long long cnt, Expr *args, Scope *scope) {
  assert(cnt >= 1);
  Val res;
  long long first = eval(args[0], scope).i;
  for (long long i = 1; i < cnt; i++) {
    long long v = eval(args[i], scope).i;
    if (!(first > v)) {
      res.i = 0;
      return res;
    }
    first = v;
  }
  res.i = 1;
  return res;
}

Val _cstmt_lt(long long cnt, Expr *args, Scope *scope) {
  assert(cnt >= 1);
  Val res;
  long long first = eval(args[0], scope).i;
  for (long long i = 1; i < cnt; i++) {
    long long v = eval(args[i], scope).i;
    if (!(first < v)) {
      res.i = 0;
      return res;
    }
    first = v;
  }
  res.i = 1;
  return res;
}

Val _cstmt_ge(long long cnt, Expr *args, Scope *scope) {
  assert(cnt >= 1);
  Val res;
  long long first = eval(args[0], scope).i;
  for (long long i = 1; i < cnt; i++) {
    long long v = eval(args[i], scope).i;
    if (!(first >= v)) {
      res.i = 0;
      return res;
    }
    first = v;
  }
  res.i = 1;
  return res;
}

Val _cstmt_le(long long cnt, Expr *args, Scope *scope) {
  assert(cnt >= 1);
  Val res;
  long long first = eval(args[0], scope).i;
  for (long long i = 1; i < cnt; i++) {
    long long v = eval(args[i], scope).i;
    if (!(first <= v)) {
      res.i = 0;
      return res;
    }
    first = v;
  }
  res.i = 1;
  return res;
}

Val _cstmt_and(long long cnt, Expr *args, Scope *scope) {
  assert(cnt >= 1);
  Val res;
  for (long long i = 0; i < cnt; i++) {
    if (!eval(args[i], scope).i) {
      res.i = 0;
      return res;
    }
  }
  res.i = 1;
  return res;
}

Val _cstmt_or(long long cnt, Expr *args, Scope *scope) {
  assert(cnt >= 1);
  Val res;
  for (long long i = 0; i < cnt; i++) {
    if (eval(args[i], scope).i != 0) {
      res.i = 1;
      return res;
    }
  }
  res.i = 0;
  return res;
}

Val _cfunc_malloc(long long cnt, Val *args) {
  assert(cnt == 1);
  Val *res = malloc(args[0].i);
  Val r;
  r.p = res;
  free(args);
  return r;
}

Val _cfunc_free(long long cnt, Val *args) {
  assert(cnt == 1);
  free(args[0].p);
  Val r;
  r.i = 1;
  free(args);
  return r;
}

Val _cfunc_free_func(long long cnt, Val *args) {
  assert(cnt == 1);
  func_t f = args[0].f->f;
  free(f.params);
  Val r;
  r.i = 1;
  free(args);
  return r;
}

Val _cfunc_list(long long cnt, Val *args) {
  Val new;
  new.p = args;
  return new;
}

Val _cfunc_nth(long long cnt, Val *args) {
  assert(cnt == 2);
  Val res = args[0].p[args[1].i];
  return res;
}

Val _cstmt_set_f(long long cnt, Expr *args, Scope *scope) {
  assert(cnt == 2);
  Expr name = args[0];
  assert(name.tp == SYM_E);
  Val v = eval(args[1], scope);
  *Scope_find(scope, name.s) = v;
  return v;
}

Val _cfunc_set_nth_f(long long cnt, Val *args) {
  assert(cnt == 3);
  args[0].p[args[1].i] = args[2];
  return args[2];
}

Val _cstmt_while(long long cnt, Expr *args, Scope *scope) {
  assert(cnt >= 1);
  Val res;
  res.i = 0;
  Scope *new_scope = Scope_new(scope);
  while (eval(args[0], scope).i) {
    for (long long i = 1; i < cnt; i++) {
      res = eval(args[i], new_scope);
    }
  }
  Scope_free(new_scope);
  return res;
}

Val new_cfunc(cfunc_t cf) {
  Val res;
  res.f = (Func *)malloc(sizeof(Func));
  res.f->tp = CFUNC_T;
  res.f->cf = cf;
  return res;
}

Val new_cstmt(cstmt_t cs) {
  Val res;
  res.f = (Func *)malloc(sizeof(Func));
  res.f->tp = CSTMT_T;
  res.f->cs = cs;
  return res;
}

Scope *std_scope() {
  Scope *scope = Scope_new(NULL);
  Scope_define(scope, "begin", new_cstmt(&_cstmt_begin));
  Scope_define(scope, "define", new_cstmt(&_cstmt_define));
  Scope_define(scope, "lambda", new_cstmt(&_cstmt_lambda));
  Scope_define(scope, "if", new_cstmt(&_cstmt_if));
  Scope_define(scope, "print_i", new_cfunc(&_cfunc_print_i));
  Scope_define(scope, "newline", new_cfunc(&_cfunc_newline));
  Scope_define(scope, "+", new_cfunc(&_cfunc_add));
  Scope_define(scope, "-", new_cfunc(&_cfunc_sub));
  Scope_define(scope, "*", new_cfunc(&_cfunc_mul));
  Scope_define(scope, "/", new_cfunc(&_cfunc_div));
  Scope_define(scope, "%", new_cfunc(&_cfunc_mod));
  Scope_define(scope, "=", new_cstmt(&_cstmt_eq));
  Scope_define(scope, "!=", new_cstmt(&_cstmt_ne));
  Scope_define(scope, ">", new_cstmt(&_cstmt_gt));
  Scope_define(scope, "<", new_cstmt(&_cstmt_lt));
  Scope_define(scope, ">=", new_cstmt(&_cstmt_ge));
  Scope_define(scope, "<=", new_cstmt(&_cstmt_le));
  Scope_define(scope, "and", new_cstmt(&_cstmt_and));
  Scope_define(scope, "or", new_cstmt(&_cstmt_or));
  Scope_define(scope, "malloc", new_cfunc(&_cfunc_malloc));
  Scope_define(scope, "free", new_cfunc(&_cfunc_free));
  Scope_define(scope, "free_func", new_cfunc(&_cfunc_free_func));
  Scope_define(scope, "list", new_cfunc(&_cfunc_list));
  Scope_define(scope, "nth", new_cfunc(&_cfunc_nth));
  Scope_define(scope, "set!", new_cstmt(&_cstmt_set_f));
  Scope_define(scope, "set-nth!", new_cfunc(&_cfunc_set_nth_f));
  Scope_define(scope, "while", new_cstmt(&_cstmt_while));
  return scope;
}

Val eval(Expr e, Scope *scope) {
  if (e.tp == INT_E) {
    Val res;
    res.i = e.i;
    return res;
  } else if (e.tp == SYM_E) {
    Val *res = Scope_find(scope, e.s);
    if (!res) {
      printf("Undefined variable '%s'.\n", e.s);
      exit(-1);
    }
    return *res;
  } else if (e.tp == LIST_E) {
    if (!e.len) {
      printf("Wrong function call.\n");
      exit(-1);
    }
    Func func = *eval(e.p[0], scope).f;
    if (func.tp == CFUNC_T) {
      NewSeq(Val, args);
      for (long long i = 1; i < e.len; i++) {
        SeqAppend(Val, args, eval(e.p[i], scope));
      }
      Val res = (*func.cf)(e.len - 1, args_val);
      return res;
    } else if (func.tp == CSTMT_T) {
      return (*func.cs)(e.len - 1, e.p + 1, scope);
    } else {
      NewSeq(Val, args);
      for (long long i = 1; i < e.len; i++) {
        SeqAppend(Val, args, eval(e.p[i], scope));
      }
      Scope *new_scope = Scope_new(scope);
      for (char **i = func.f.params; *i; i++) {
        Scope_define(new_scope, *i, args_val[i - func.f.params]);
      }
      Val res;
      res.i = 0;
      for (long long i = 0; i < func.f.len; i++) {
        res = eval(func.f.body[i], new_scope);
      }
      Scope_free(new_scope);
      FreeSeq(args);
      return res;
    }
  } else {
    exit(-2);
  }
}

int main(int argc, char const *argv[]) {
  Scope *scope = std_scope();
  FILE *f = fopen("test4.lisp", "r");
  NewSeq(char, code);
  while (!feof(f)) {
    SeqAppend(char, code, fgetc(f));
  }
  code_val[code_size - 1] = 0;
  fclose(f);
  Lexer l = Lexer_new(code_val);
  Expr e = parse(&l);
  eval(e, scope);
  Scope_free(scope);
  FreeSeq(code);
  return 0;
}

/*
(begin (define fn (lambda (a) (print_i a) (newline) 0)) (fn (fn 1)))

(begin (define a 10) (define b 20) (print_i (+ a b)) (newline))

(begin
 (define fn (lambda (a)
              (print_i a)
              (newline)
              (if (- a 10)
              (fn (+ a 1))
              0)))
 (fn 1)
 (free_func fn))

(begin
  (define print_i_nl (lambda (a)
                       (print_i a)
                       (newline)))
  (print_i_nl (* 1 2 3 4 5))
  (print_i_nl (and 0 1))
  (print_i_nl (or 0 1))
  (free_func print_i_nl))

(begin
  (define fac (lambda (a)
                (if (= a 0)
                  1
                  (* (fac (- a 1)) a))))
  (print_i (fac 10))
  (newline)
  (free_func fac))

(begin
  (define i 0)
  (while (< i 10)
         (set! i (+ i 1))
         (print_i i)
         (newline)))

(begin
  (define print_il
    (lambda (l, len)
      (define i 0)
      (while (< i len)
             (print_i (nth l i))
             (set! i (+ i 1)))
      (newline)))
  (define l (list 1 1 3))
  (print_il l 3)
  (set-nth! l 1 2)
  (print_il l 3)
  (free_func print_il)
  (free l))
*/
