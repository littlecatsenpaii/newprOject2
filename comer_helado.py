print("With this program you can determinate your choose about ice cream")
comerhelado_input = input("Do you want to eat ice cream? (Yes / No )").upper()

if comerhelado_input == "YES":
    comerhelado = True
elif comerhelado_input == "NO":
    comerhelado = False
else:
    print("Yo only can choose Yes or No, so your answer is No")
    comerhelado = False

tenerdinero_input = input("Do you have money to eat ice cream? (Yes / No)").upper()
if tenerdinero_input == "YES":
    tenerdinero = True
elif tenerdinero_input == "NO":
    tenerdinero = False
else:
    print("Yo only can choose Yes or No, so your answer is No")
    tenerdinero = False

tia_input = input("Your aunt is there? (Yes / No)").upper()
if tia_input == "YES":
    tia = True
elif tia_input == "NO":
    tia = False
else:
    print("Yo only can choose Yes or No, so your answer is No")
    tia = False

comerhelado = comerhelado_input == "YES"
tenerdinero = tenerdinero_input == "YES"
tia = tia_input == "YES"
presupuesto = tenerdinero or tia

if comerhelado or presupuesto:
    print("Eat an ice cream")
else:
    print("Don't eat ice cream")
