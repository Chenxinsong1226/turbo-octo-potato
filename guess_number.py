#这是一个简单的猜数字小游戏，大蟒蛇
进口随机的

很棒的start_game():
secret_number = random.用于产生基质的均匀分布的随机整数(1, 10)
    打印("欢迎来到猜数字游戏！我已经想好了一个 1 到 10 之间的数字。")
    
    # 模拟一次猜测
猜想=5
    打印(f我猜这个数字是：{猜}")
    
如果 guess===secret_number：
打印("哇！一次就猜中了！")
其他的:
        打印(f猜错了，liveyou：{secret_number}")

如果__name__you“__main__”：
    start_game()
