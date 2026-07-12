#include <iostream>
#include <string>
#include <algorithm>
#include <cctype>
#include <cmath>

// 声明函数原型
double expression(const std::string &str, size_t &pos);
double number(const std::string &str, size_t &pos);
double factor(const std::string &str, size_t &pos);
double term(const std::string &str, size_t &pos);

// 解析数字
double number(const std::string &str, size_t &pos) {
    double result = 0;
    while (pos < str.length() && std::isdigit(str[pos])) {
        result = result * 10 + (str[pos++] - '0');
    }
    return result;
}

// 解析括号和函数
double factor(const std::string &str, size_t &pos) {
    if (str[pos] == '(') {
        ++pos; // 跳过左括号
        double result = expression(str, pos);
        ++pos; // 跳过右括号
        return result;
    } else if (std::tolower(str[pos]) == 'm') {
        // 检测min或max函数
        std::string func = str.substr(pos, 3);
        std::transform(func.begin(), func.end(), func.begin(), ::tolower);
        pos += 3; // 跳过函数名
        ++pos; // 跳过左括号
        double a = expression(str, pos);
        ++pos; // 跳过逗号
        double b = expression(str, pos);
        ++pos; // 跳过右括号
        if (func == "max") {
            return std::max(a, b);
        } else if (func == "min") {
            return std::min(a, b);
        }
    }
    return number(str, pos);
}

// 解析乘除
double term(const std::string &str, size_t &pos) {
    double result = factor(str, pos);
    while (pos < str.length()) {
        if (str[pos] == '*') {
            ++pos;
            result *= factor(str, pos);
        } else if (str[pos] == '/') {
            ++pos;
            double divisor = factor(str, pos);
            if (divisor != 0) {
                result /= divisor;
            } else {
                throw std::runtime_error("Division by zero.");
            }
        } else {
            break;
        }
    }
    return result;
}

// 解析加减
double expression(const std::string &str, size_t &pos) {
    double result = term(str, pos);
    while (pos < str.length()) {
        if (str[pos] == '+') {
            ++pos;
            result += term(str, pos);
        } else if (str[pos] == '-') {
            ++pos;
            result -= term(str, pos);
        } else {
            break;
        }
    }
    return result;
}

int main() {
    std::string expr = "";
    std::cin >> expr;
    size_t pos = 0;
    try {
        double result = expression(expr, pos);
        std::cout << "Result: " << result << std::endl;
    } catch (const std::exception &e) {
        std::cerr << "Error: " << e.what() << std::endl;
    }
    return 0;
}