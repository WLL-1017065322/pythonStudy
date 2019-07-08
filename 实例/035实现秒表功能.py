import time

print("回车开始，ctrl+c结束：")

while True:
    try:
        input()
        start_time = time.time()
        print("开始")
        while True:
            print("计时：",round(time.time()-start_time),"秒",end="\r")#回车
            time.sleep(0.001)
            # round()
            # 方法返回浮点数x的四舍五入值。

    except KeyboardInterrupt:
        print("结束")
        end_time = time.time()
        print("总共的时间：",round(end_time-start_time,2),"secs")
        break



##有问题