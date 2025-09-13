import re
print(re.match(r"(^\d{15}$)|(^\d{17}([0-9]|x)$)",input("输入身份证号："))!=None)