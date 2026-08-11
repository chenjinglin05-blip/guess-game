import random

name = input("你叫什么名字？")
print(f"你好，{name}，我们来玩猜数字游戏!")

secret = random.randint(1,100)
print(f"我已经想好了一个1到100之间的数字")

count = 0

while True:
    guess = int(input("你猜是几？"))
    count = count+1

    if guess == secret:
        print(f"🎉 恭喜你猜对了！你一共猜了 {count} 次")
        break
    elif guess > secret:
        print("📈 猜大了，再小一点")
    else:
        print("📉 猜小了，再大一点")

