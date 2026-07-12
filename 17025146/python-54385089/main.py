from lex import Lex

generator = Lex()

@generator.pattern('".*"')
def string(text):
    print("String:", text)
generator.compile()
generator.lex('"success"')