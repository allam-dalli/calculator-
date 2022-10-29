from re import findall
from os import system
def myEval(expression: str) -> float:
    num = "(\d+\.\d+|\d+)"
    for vl  in findall(f"{num}\^{num}", expression):
        a, b = map(float, vl)
        vl = "^".join(vl)
        expression = expression.replace(vl, str(a**b))
    for vl in findall(f"{num}\*{num}", expression):
        a, b = map(float, vl)
        vl = "*".join(vl)
        expression = expression.replace(vl, str(a * b))
    for vl in findall(f"{num}\/{num}", expression):
        a, b = map(float, vl)
        vl = "/".join(vl)
        expression = expression.replace(vl, str(a / b))
    for vl in findall(f"{num}\+{num}", expression):
        a, b = map(float, vl)
        vl = "+".join(vl)
        expression = expression.replace(vl, str(a + b))
    for vl in findall(f"{num}\-{num}", expression):
        a, b = map(float, vl)
        vl = "-".join(vl)
        expression = expression.replace(vl, str(a - b))
    for vl in findall("\(.+\)", expression):
        r_vl = myEval(vl[1:-1])
        expression = expression.replace(vl, str(r_vl))
    if len(findall(num, expression)) != 1:
        expression = str(myEval(expression))
    return float(expression)
nopi = input ("enter the evaluation please  :  ")
m = myEval(nopi)
print (m)
system ('pause')