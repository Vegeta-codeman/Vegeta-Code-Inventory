import random   #导入random模块，用于生成随机数

print("Welcome to the Number Guessing Game!")   #打印欢迎信息，提示用户进入数字猜测游戏
print("I'm thinking of a number between 1 and 100.")    #提示玩家,程序的游戏为1-100之间

number = random.randint(1, 100) #随机生成1到100之间的整数,作为答案
count = 0   #初始化计数器,记录玩家猜了多少次

while True: #无限循环,直到玩家猜对才通过break退出循环
    guess = input("Make a guess: ") #获取玩家输入,input返回的永远是字符串类型

    if not guess.isdigit(): #检查输入是否为全数字,如果不是
        print("Please enter a valid number.")   #提示玩家输入无效
        continue    #跳过本次循环,让玩家继续输入,不计次数

    guess = int(guess)  #输入合法化,把字符串专程整数,方便后面做大小比较
    count += 1  #有效猜测一次,计数器加1

    if guess < number:  #如果玩家猜的数字比答案小
        print("Too low.")   #提示太小了
    elif guess > number:    #如果玩家猜的数字比答案大
        print("Too high.")  #提示太大了
    else:   #如果以上两个选项都不是
        print(f"Congratulations! You've guessed the number {number} in {count} attempts.")  #打印恭喜信息,显示玩家猜对的数字和猜测次数
        break   #跳出while循环,结束游戏

    """
    语法	含义
    random.randint(a, b)	生成 a 到 b 之间的随机整数，包含两端
    input()	获取用户输入，返回值永远是字符串
    str.isdigit()	判断字符串是否只由数字组成，用于输入校验
    continue	跳过本次循环剩余代码，直接进入下一次循环
    break	直接跳出整个循环
    if / elif / else	多条件分支判断，从上到下依次检查，命中一个就不再往下判断
    """