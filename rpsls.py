#程序目标：实现运行rpsls游戏
#作者：杨熙

#转换
def name_to_number(name):
    if name == "石头":
        number = 0
    elif name == "史波克":
        number = 1
    elif name == "布":
        number = 2
    elif name == "蜥蜴":
        number = 3
    elif name=="剪刀":
        number = 4
    return number
#转换
def number_to_name(number):
    if number == 0:
        name = "石头"
    elif number == 1:
        name = "史波克"
    elif number == 2:
        name = "布"
    elif number == 3:
        name = "蜥蜴"
    else:
        name = "剪刀"
    return name
print("欢迎使用RPSLS游戏")
print("----------------")
plyer_choice=input("请输入您的选择:")
print("--------")
import sys
while plyer_choice!="石头":
    print("Error: No Correct Name")
    sys.exit(0)
plyer_number=name_to_number(plyer_choice)
import random
computer_number=random.randrange(0, 5)
computer_choice=number_to_name(computer_number)
print("你的选择为"+plyer_choice)
print("计算机的选择为"+computer_choice)
#游戏规则
x=(plyer_number-computer_number)%5
if x==1 or x==2:
    print("你赢了!")
elif x==3 or x==4:
    print("机器赢了!")
else:
    print("你和计算机出的一样")
