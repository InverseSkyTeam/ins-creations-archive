#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <ctype.h>

typedef enum {
    Number, Binary,
} ASTType;

typedef enum {
    Add = '+', Sub = '-', Mul = '*', Div = '/',
    LParen = '(', RParen = ')',
} Operator;

typedef struct AST {
    ASTType type;
    union {
        int number;
        struct {
            Operator op;
            struct AST *left, *right;
        } binary;
    };
} AST;

AST* newNumberAST(int number) {
    AST* res = (AST*)malloc(sizeof(AST));
    res->type = Number;
    res->number = number;
    return res;
}

AST* newBinaryAST(Operator op, AST *left, AST *right) {
    AST* res = (AST*)malloc(sizeof(AST));
    res->type = Binary;
    res->binary.op = op;
    res->binary.left = left;
    res->binary.right = right;
    return res;
}

void destroyAST(AST* ast) {
    switch (ast->type) {
    case Binary: destroyAST(ast->binary.left); destroyAST(ast->binary.right); break;
    }
    free(ast);
}

typedef enum {
    Oper, Value,
} TokenType;

typedef struct {
    TokenType type;
    union {
        Operator op;
        int value;
    };
} Token;

Token newOperToken(Operator op) {
    Token res;
    res.type = Oper;
    res.op = op;
    return res;
}

Token newValueToken(int value) {
    Token res;
    res.type = Value;
    res.value = value;
    return res;
}

typedef struct {
    Token *items;
    size_t size, max_size;
} TokenList;

TokenList* newTokenList() {
    TokenList *res = (TokenList*)malloc(sizeof(TokenList));
    res->items = (Token*)malloc(sizeof(Token) * 8);
    res->size = 0;
    res->max_size = 8;
    return res;
}

void TokenListPush(TokenList *token_list, Token token) {
    if (token_list->size == token_list->max_size) {
        token_list->max_size *= 2;
        realloc(token_list->items, sizeof(Token) * token_list->max_size);
    }
    token_list->items[token_list->size++] = token;
}

void destroyTokenList(TokenList *token_list) {
    free(token_list->items);
    free(token_list);
}

TokenList *tokenize(char* code) {
    size_t pos = 0;
    TokenList* res = newTokenList();

    while (code[pos]) {
        while (code[pos] && (code[pos] == ' ' || code[pos] == '\n' || code[pos] == '\t'))
            pos++;
        if (!code[pos])
            break;
        else if (isdigit(code[pos])) {
            int num = code[pos++] - '0';
            while (code[pos] && isdigit(code[pos])) {
                num *= 10;
                num += code[pos++] - '0';
            }
            TokenListPush(res, newValueToken(num));
        }
        else if (code[pos] == '+' || code[pos] == '-' || code[pos] == '*' || code[pos] == '/' || code[pos] == '(' || code[pos] == ')')
            TokenListPush(res, newOperToken((Operator)code[pos++]));
        else {
            printf("Error!\n");
            exit(-1);
        }
    }

    return res;
}

typedef struct {
    TokenList* tokens;
    size_t pos;
    Token current_token;
} Parser;

Parser* newParser(TokenList* tokens) {
    Parser* res = (Parser*)malloc(sizeof(Parser));
    res->tokens = tokens;
    res->pos = 0;
    res->current_token = tokens->items[0];
    return res;
}

Token ParserNext(Parser* parser) {
    parser->current_token = parser->tokens->items[++parser->pos];
    return parser->tokens->items[parser->pos - 1];
}

void destroyParser(Parser* parser) {
    destroyTokenList(parser->tokens);
    free(parser);
}

AST* parse_term(Parser* parser);
AST* parse_unit(Parser* parser);

AST* parse_expr(Parser* parser) {
    AST* res = parse_term(parser);
    while (parser->current_token.type == Oper && (parser->current_token.op == Add || parser->current_token.op == Sub)) {
        Operator op = ParserNext(parser).op;
        res = newBinaryAST(op, res, parse_term(parser));
    }
    return res;
}

AST* parse_term(Parser* parser) {
    AST* res = parse_unit(parser);
    while (parser->current_token.type == Oper && (parser->current_token.op == Mul || parser->current_token.op == Div)) {
        Operator op = ParserNext(parser).op;
        res = newBinaryAST(op, res, parse_unit(parser));
    }
    return res;
}

AST* parse_unit(Parser* parser) {
    if (parser->current_token.type == Value)
        return newNumberAST(ParserNext(parser).value);
    else if (parser->current_token.value == LParen) {
        ParserNext(parser);
        AST* res = parse_expr(parser);
        if (parser->current_token.type != Oper || parser->current_token.op != RParen)
            exit(-1);
        ParserNext(parser);
        return res;
    }
    else
        exit(-1);
}

int eval(AST* ast) {
    switch (ast->type) {
    case Number:
        return ast->number;
    case Binary: {
        int left = eval(ast->binary.left), right = eval(ast->binary.right);
        switch (ast->binary.op) {
        case Add:
            return left + right;
        case Sub:
            return left - right;
        case Mul:
            return left * right;
        case Div:
            return left / right;
        }
    }
    }
    exit(-1);
}

char code[1024 * 1024];

int main(int argc, char const *argv[])
{
    gets(code);
    TokenList* tokens = tokenize(code);
    Parser* parser = newParser(tokens);
    AST* ast = parse_expr(parser);
    printf("%d\n", eval(ast));
    destroyParser(parser);
    destroyAST(ast);
    return 0;
}
