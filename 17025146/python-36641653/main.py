_print = {
    "name":"print",
    "effect":"输出"
}
_input = {
    "name":"input",
    "effect":"输入"
}
_cout = {
    "name":"cout",
    "effect":"输出"
}
_cin = {
    "name":"cin",
    "effect":"输入"
}
pyfun = {
    "print":"_print",
    "input":"_input"
}
cfun = {
    "cout":"_cout",
    "cin":"_cin"
}
lang = {
    "python":"pyfun",
    "cpp":"cfun"
}
name = "python"
fname = "input"
languge = eval(lang[name])
fun = eval(languge[fname])
print(fun["name"],fun["effect"])