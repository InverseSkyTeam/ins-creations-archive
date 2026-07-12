// include/k.h {
#pragma once

// include/kglobal.h {
#pragma once

namespace k {
namespace tokens {}  // namespace tokens
namespace lex {
namespace __test {}
}  // namespace lex
namespace ast {}        // namespace ast
namespace parse {}      // namespace parse
namespace interpret {}  // namespace interpret
namespace api {}
}  // namespace k

// }

// include/tokens.h {
#pragma once

#include <iostream>
#include <memory>
#include <string>
#include <vector>


namespace k::tokens {
enum class TokenType { Int, Float, String, Symbol, Operator };
class Token;
class IntToken;
class FloatToken;
class StringToken;
class SymbolToken;
class OperatorToken;

class Token {
 public:
  virtual ~Token() = default;
  TokenType getType() const { return type; }
  virtual std::string toString() = 0;

 protected:
  Token(TokenType tokenType) : type(tokenType) {}

 private:
  TokenType type;
};

class IntToken : public Token {
 public:
  IntToken(int value) : Token(TokenType::Int), value(value) {}
  virtual ~IntToken() = default;
  int getInt() const { return value; }
  void setInt(int v) { value = v; }

  std::string toString() { return "<IntToken:" + std::to_string(value) + ">"; }

 private:
  int value;
};
class FloatToken : public Token {
 public:
  FloatToken(double value) : Token(TokenType::Float), value(value) {}
  virtual ~FloatToken() = default;
  double getFloat() const { return value; }
  void setFloat(double v) { value = v; }
  std::string toString() {
    return "<FloatToken:" + std::to_string(value) + ">";
  }

 private:
  double value;
};

class StringToken : public Token {
 public:
  StringToken(std::string value) : Token(TokenType::String), value(value) {}
  virtual ~StringToken() = default;
  std::string getString() { return value; }
  void setString(std::string v) { value = v; }
  std::string toString() { return "<StringToken:\"" + value + "\">"; }

 private:
  std::string value;
};

class SymbolToken : public Token {
 public:
  SymbolToken(std::string op) : Token(TokenType::Symbol), op(op) {}
  virtual ~SymbolToken() = default;
  std::string getSymbol() const { return op; }
  void setSymbol(std::string v) { op = v; }
  std::string toString() { return "<SymbolToken:\"" + op + "\">"; }
  bool operator==(SymbolToken& t) { return t.op == op; }

 private:
  std::string op;
};

class OperatorToken : public Token {
 public:
  OperatorToken(std::string op) : Token(TokenType::Operator), op(op) {}
  virtual ~OperatorToken() = default;
  std::string getOperator() const { return op; }
  void setOperator(std::string v) { op = v; }
  std::string toString() { return "<OperatorToken:\"" + op + "\">"; }
  bool operator==(OperatorToken& t) { return t.op == op; }

 private:
  std::string op;
};

class TokenList {
 public:
  TokenList() {}
  //   TokenList(TokenList&) = delete;
  std::vector<std::shared_ptr<Token>>& getVector() { return pTokens; }
  std::shared_ptr<Token> get(std::size_t index) { return pTokens.at(index); }
  void push_back(std::shared_ptr<Token> pToken) { pTokens.push_back(pToken); }
  virtual ~TokenList() = default;

 private:
  std::vector<std::shared_ptr<Token>> pTokens;
};
using pTokenList = std::shared_ptr<TokenList>;
}  // namespace k::tokens
// }

// include/lexer.h {
#pragma once

#include <algorithm>
#include <cassert>
#include <cctype>
#include <memory>
#include <stdexcept>
#include <string>
#include <vector>


namespace k::lex {
class Lexer;
class Lexer {
 public:
  Lexer(const std::string& input)
      : input(input), vec(std::make_shared<tokens::TokenList>()) {
    currentIndex = 0;
    inputLength = input.size();
  }
  virtual ~Lexer() = default;

  [[noreturn]] void errorWhileLexing(const std::string& str = std::string{
                                         "Lexer Crashed:Unknown Error."}) {
    throw std::runtime_error(str);
  }

  bool validSymbol(char c) {
    return (!isspace(c)) && (!isblank(c)) && c != '(' && c != ')';
  }

  int toInt(std::string s) const { return std::stoi(s); }
  double toFloat(std::string s) const { return std::stod(s); }

  void readString() {
    assert(currentChar() == '"');
    bool validEndOfString = false;
    advanceIndex();
    std::vector<char> charBuffer;
    while (currentIndex < inputLength) {
      if (currentChar() == '"') {
        validEndOfString = true;
        break;
      } else if (currentChar() == '\\' && hasNext()) {
        char escapeChar = advanceIndexAndGet();
        if (escapeChar == 'n') {
          charBuffer.push_back('\n');
        } else if (escapeChar == 't') {
          charBuffer.push_back('\t');
        } else if (escapeChar == '\\') {
          charBuffer.push_back('\\');
        } else {
          charBuffer.push_back('\\');
          charBuffer.push_back(escapeChar);
        }
      } else {
        charBuffer.push_back(currentChar());
      }
      advanceIndex();
    }
    if (validEndOfString) {
      std::string result{charBuffer.begin(), charBuffer.end()};
      vec->push_back(
          std::make_shared<tokens::StringToken>(tokens::StringToken{result}));
    } else {
      errorWhileLexing("Invalid End Of String.");
    }
  }
  void readNumber() {
    assert(isdigit(currentChar()));
    std::vector<char> charBuffer;
    bool isFloat = false;
    while (!(isspace(currentChar()) || isblank(currentChar()) ||
             currentChar() == '(' || currentChar() == ')')) {
      if (currentChar() == '.') isFloat = true;
      if ((!isdigit(currentChar())) && currentChar() != '.')
        errorWhileLexing("Unexpected Number Literals.");
      charBuffer.push_back(currentChar());
      advanceIndex();
    }
    currentIndex--;
    if (isFloat) {
      vec->push_back(std::make_shared<tokens::FloatToken>(tokens::FloatToken(
          toFloat(std::string{charBuffer.begin(), charBuffer.end()}))));
    } else {
      vec->push_back(std::make_shared<tokens::IntToken>(tokens::IntToken(
          toInt(std::string{charBuffer.begin(), charBuffer.end()}))));
    }
  }
  void readSymbol() {
    std::vector<char> charBuffer;
    if (!validSymbol(currentChar())) {
      errorWhileLexing("Invalid Token.");
    }
    charBuffer.push_back(currentChar());
    advanceIndex();
    while (currentIndex < inputLength) {
      if (validSymbol(currentChar()))
        charBuffer.push_back(currentChar());
      else {
        currentIndex--;
        break;
      }
      advanceIndex();
    }
    vec->push_back(std::make_shared<tokens::SymbolToken>(tokens::SymbolToken(
        std::string{charBuffer.begin(), charBuffer.end()})));
  }

  bool hasNext() const { return currentIndex < inputLength - 1; }
  void advanceIndex(unsigned step = 1) { currentIndex += step; }
  char currentChar(unsigned offset = 0) const {
    return input.at(currentIndex + offset);
  }
  char advanceIndexAndGet(unsigned step = 1) {
    advanceIndex(step);
    return currentChar();
  }

  void skipWhiteSpace() {
    while (isspace(currentChar()) || isblank(currentChar())) advanceIndex();
  }

  std::shared_ptr<tokens::TokenList> lex() {
    while (currentIndex < inputLength) {
      skipWhiteSpace();
      if (currentChar() == '(') {
        vec->push_back(std::make_shared<tokens::OperatorToken>(
            tokens::OperatorToken("(")));
      } else if (currentChar() == ')') {
        vec->push_back(std::make_shared<tokens::OperatorToken>(
            tokens::OperatorToken(")")));
      } else if (currentChar() == '"') {
        readString();
      } else if (isdigit(currentChar())) {
        readNumber();
      } else {
        readSymbol();
      }
      advanceIndex();
    }
    return vec;
  }

 private:
  unsigned int currentIndex;
  std::size_t inputLength;
  std::string input;

  tokens::pTokenList vec;
};
}  // namespace k::lex

namespace k::lex::__test {
inline auto Test_main() -> int {
  k::lex::Lexer lexer{"(define(add a b)(+ 1 2.2)) (define a \"hello world!\")"};
  auto pl = lexer.lex();
  auto& l = *pl;
  for (auto i = l.getVector().begin(); i != l.getVector().end(); i++) {
    auto& v = **i;
    std::cout << v.toString() << std::endl;
  }
  return 0;
}
}  // namespace k::lex::__test
// }

// 尚未实现..
// #include "ast.h"
// #include "parser.h"
// #include "interpreter.h"

// }

auto main() -> int { return k::lex::__test::Test_main(); }