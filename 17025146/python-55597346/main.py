import generator
import highlighting # 是的，为了彰显仪式感我连我两年前随手写的代码高亮输出都整合进来了

with open("grammar.txt", "r", encoding="utf-8") as f:
    rules = f.read()
with open("action.py", "r", encoding="utf-8") as f:
    action = f.read()

gene = generator.Rule(rules)
lex_code = gene.generate_lexer()
parse_code = gene.generate_parser(action)

code = lex_code + "\n" + parse_code

with open("parser.py", "w", encoding="utf-8") as f:
    f.write(lex_code)
    f.write("\n")
    f.write(parse_code)

highlighting.newprint(code)
