import random
import os,time,datetime
print("*"*10+"M106-dos**********")
time.sleep(0.5)
ship = "-------------------------------------------------------"
print("Please choose:1=Start M106-DOS Normally 2=Turn off.")
u = int(input())
print(ship)
if u == 1:
    space = "\ "
    sp="*"
    s=" "
    i = "a"
    ia = ' '
    data="""
    |---------------------------|
    |          M106DOS          |
    |       Version3.2.2B       |
    |---------------------------|
    """
    print(data)
    print("欢迎！Welcome!")
    time.sleep(2)
    print("             "*75)
    print(ia)
    if i == "A" or "a":
        time.sleep(0.8)
        i = "b"
        print(ship)
        if i == "A" or "a" or "b" or "B":
            time.sleep(0.1)
            print("C:> ")
            while 1 < 2:
                print(ship)
                i = input("\033[32m你可以输入'M106-dos'去查看关于M106-DOS的文件；\n'run'可以查看电脑里的选项。例如文件管理器，重置电脑等；\n'exit'可以结束进程并关闭M106DOS;\n'version'可以查看版本/升级")
                if i == "version":
                    print(ship)
                    print("版本：Version3.2.3，版本号：21CORI270300322B\n修复问题\n优化DOS(The 2nd Version of the 3.2.3th Generation's of M106DOS)")
                    print("Built on Old Technology 0.2.1010")
                elif i == "M106-dos":
                    print(ship)
                    for i in range(1,35):
                        print("C:>M106-dos>M106DosDoc"+ str(i) +".dll")
                        i += 1
                elif i == "exit":
                    break
                
                elif i == "run":
                    print(ship)
                    print("\033[33m运行窗口:")
                    time.sleep(0.2)
                    print(ship)
                    i = input("你可以输入'explorer'去浏览电脑里的文件，但不能删除、更改；\n'return'可以返回第一页\n  'off'可以关闭M106-DOS；\n'reset'可以修复你的M106-DOS并且重启M106-DOS；\n 你可以输入'all'去使用所有应用\n请选择:\033[0m")
                    if i == "explorer":
                        print(ship)
                        print("C:> ")
                        d = input("下一步:")
                        time.sleep(0.2)
                        print("C:>",d)
                        s = input("下一步:")
                        print("C:>",d,space,s)
                        f = input("下一步:")
                        print("C:>",d,space,s,space,f)
                        g = input("下一步:")
                        print("C:>",d,space,s,space,f,space,g)
                        a = input("下一步:")
                        print("C:>",d,space,s,space,f,space,g,space,a)
                    elif i == "return":
                        pass
                    elif i == "all":
                        print(ship)
                        n = int(input("1=计算器 2=计算练习机3=返回："))
                        if n == 1:
                            print(ship)
                            print("1=+、2=-、3=x、4=/")
                            i = input(":")
                            first = int(input("第一个数"))
                            second = int(input("第二个数"))
                            if i == "1":
                                print(first+second)
                            elif i == "2":
                                print(first-second)
                            elif i == "3":
                                print(first*second)
                            elif i == str(4):
                                print(first/second)
                        elif n == 3:
                            pass
                        else:
                            now = datetime.datetime.now()
                            current_time = now.strftime("\033[42m**********今天是%Y年%m月%d日**********\033[0m")
                            print(current_time)
                            print("\033[44m**********计算练习机(bsd，只包含整数计算)**********\033[0m")
                            print("\033[43m**********版本：V.1.1.09**********\033[0m")
                            old = input("请选择你的年龄段：1、1~3年级 2、4~6年级")
                            time1 = time.time()
                            score = 100
                            MyAnswer = 0
                            if old == "1":
                                time.sleep(1)
                                level1 = input("1、一年级 2、二年级 3、三年级")
                                if level1 == "1":
                                    time.sleep(0.5)
                                    do1 = input("1、加法 2、减法")
                                    if do1 == "1":
                                        time.sleep(0.5)
                                        times1 = int(input("请输入练习的题数："))
                                        for i in range(times1):
                                            everyS = (100/times1) // score
                                            plus01 = random.randint(1,15)
                                            plus02 = random.randint(1,15)
                                            print(plus01,"+",plus02,"=")
                                            MyAnswer = int(input("你的答案："))
                                            answer1 = plus01 + plus02
                                            if answer1 == MyAnswer:
                                                score += 0
                                            else:
                                                score -= everyS
                                    elif do1 == "2":
                                        time.sleep(0.5)
                                        times1 = int(input("请输入练习的题数："))
                                        for i in range(times1):
                                            everyS = (100/times1) // score
                                            plus03 = random.randint(5,15)
                                            plus04 = random.randint(1,5)
                                            print(plus03,"-",plus04,"=")
                                            MyAnswer = int(input("你的答案："))
                                            answer1 = plus03 - plus04
                                            if answer1 == MyAnswer:
                                                score += 0
                                            else:
                                                score -= everyS
                                elif level1 == "2":
                                    time.sleep(0.5)
                                    do1 = input("1、加法 2、减法 3、乘法 4、除法")
                                    if do1 == "1":
                                        time.sleep(0.5)
                                        times1 = int(input("请输入练习的题数："))
                                        for i in range(times1):
                                            everyS = (100/times1) // score
                                            plus01 = random.randint(1,50)
                                            plus02 = random.randint(1,50)
                                            print(plus01,"+",plus02,"=")
                                            MyAnswer = int(input("你的答案："))
                                            answer1 = plus01 + plus02
                                            if answer1 == MyAnswer:
                                                score += 0
                                            else:
                                                score -= everyS
                                    elif do1 == "2":
                                        time.sleep(0.5)
                                        times1 = int(input("请输入练习的题数："))
                                        for i in range(times1):
                                            everyS = (100/times1) // score1
                                            plus03 = random.randint(25,50)
                                            plus04 = random.randint(1,25)
                                            print(plus03,"-",plus04,"=")
                                            MyAnswer = int(input("你的答案："))
                                            answer1 = plus03 - plus04
                                            if answer1 == MyAnswer:
                                                score += 0
                                            else:
                                                score -= everyS
                                    elif do1 == "3":
                                        time.sleep(0.5)
                                        times1 = int(input("请输入练习的题数："))
                                        for i in range(times1):
                                            everyS = (100/times1) // score
                                            plus03 = random.randint(1,9)
                                            plus04 = random.randint(1,9)
                                            print(plus03,"×",plus04,"=")
                                            MyAnswer = int(input("你的答案："))
                                            answer1 = plus03 * plus04
                                            if answer1 == MyAnswer:
                                                score += 0
                                            else:
                                                score -= everyS
                                    else:
                                        time.sleep(0.5)
                                        times1 = int(input("请输入练习的题数："))
                                        for i in range(times1):
                                            everyS = (100/times1) // score
                                            plus03 = random.randint(1,85)
                                            plus04 = random.randint(1,8)
                                            print(plus03,"÷",plus04,"=(取整)")
                                            MyAnswer = int(input("你的答案："))
                                            answer1 = plus03 % plus04
                                            if answer1 == MyAnswer:
                                                score += 0
                                            else:
                                                score -= everyS
                                elif level1 == "3":
                                    time.sleep(0.5)
                                    do1 = input("1、加法 2、减法 3、乘法 4、除法")
                                    if do1 == "1":
                                        time.sleep(0.5)
                                        times1 = int(input("请输入练习的题数："))
                                        for i in range(times1):
                                            everyS = (100/times1) // score
                                            plus01 = random.randint(1,1000)
                                            plus02 = random.randint(1,1500)
                                            print(plus01,"+",plus02,"=")
                                            MyAnswer = int(input("你的答案："))
                                            answer1 = plus01 + plus02
                                            if answer1 == MyAnswer:
                                                score += 0
                                            else:
                                                score -= everyS
                                    elif do1 == "2":
                                        time.sleep(0.5)
                                        times1 = int(input("请输入练习的题数："))
                                        for i in range(times1):
                                            everyS = (100/times1) // score
                                            plus03 = random.randint(750,1500)
                                            plus04 = random.randint(1,750)
                                            print(plus03,"-",plus04,"=")
                                            MyAnswer = int(input("你的答案："))
                                            answer1 = plus03 - plus04
                                            if answer1 == MyAnswer:
                                                score += 0
                                            else:
                                                score -= everyS
                                    elif do1 == "3":
                                        time.sleep(0.5)
                                        times1 = int(input("请输入练习的题数："))
                                        for i in range(times1):
                                            everyS = (100/times1) // score
                                            plus03 = random.randint(1,50)
                                            plus04 = random.randint(1,100)
                                            print(plus03,"×",plus04,"=")
                                            MyAnswer = int(input("你的答案："))
                                            answer1 = plus03 * plus04
                                            if answer1 == MyAnswer:
                                                score += 0
                                            else:
                                                score -= everyS
                                    else:
                                        time.sleep(0.5)
                                        times1 = int(input("请输入练习的题数："))
                                        for i in range(times1):
                                            everyS = (100/times1) // score
                                            plus03 = random.randint(1,1000)
                                            plus04 = random.randint(1,9)
                                            print(plus03,"÷",plus04,"=(取整)")
                                            MyAnswer = int(input("你的答案："))
                                            answer1 = plus03 % plus04
                                            if answer1 == MyAnswer:
                                                score += 0
                                            else:
                                                score -= everyS   
                            else:
                                time.sleep(1)
                                level1 = input("1、四年级 2、五年级 3、六年级")
                                if level1 == "1":
                                    time.sleep(0.5)
                                    do1 = input("1、加法 2、减法 3、乘法 4、除法")
                                    if do1 == "1":
                                        time.sleep(0.5)
                                        times1 = int(input("请输入练习的题数："))
                                        for i in range(times1):
                                            everyS = (100/times1) // score
                                            plus01 = random.randint(1,10000)
                                            plus02 = random.randint(1,15000)
                                            print(plus01,"+",plus02,"=")
                                            MyAnswer = int(input("你的答案："))
                                            answer1 = plus01 + plus02
                                            if answer1 == MyAnswer:
                                                score += 0
                                            else:
                                                score -= everyS
                                    elif do1 == "2":
                                        time.sleep(0.5)
                                        times1 = int(input("请输入练习的题数："))
                                        for i in range(times1):
                                            everyS = (100/times1) // score
                                            plus03 = random.randint(5000,15000)
                                            plus04 = random.randint(1,5000)
                                            print(plus03,"-",plus04,"=")
                                            MyAnswer = int(input("你的答案："))
                                            answer1 = plus03 - plus04
                                            if answer1 == MyAnswer:
                                                score += 0
                                            else:
                                                score -= everyS
                                    elif do1 == "3":
                                        time.sleep(0.5)
                                        times1 = int(input("请输入练习的题数："))
                                        for i in range(times1):
                                            everyS = (100/times1) // score
                                            plus03 = random.randint(10000,15000)
                                            plus04 = random.randint(1,10000)
                                            print(plus03,"×",plus04,"=")
                                            MyAnswer = int(input("你的答案："))
                                            answer1 = plus03 * plus04
                                            if answer1 == MyAnswer:
                                                score += 0
                                            else:
                                                score -= everyS
                                    else:
                                        time.sleep(0.5)
                                        times1 = int(input("请输入练习的题数："))
                                        for i in range(times1):
                                            everyS = (100/times1) // score
                                            plus03 = random.randint(10000,15000)
                                            plus04 = random.randint(1,75)
                                            print(plus03,"÷",plus04,"=(取整)")
                                            MyAnswer = int(input("你的答案："))
                                            answer1 = plus03 % plus04
                                            if answer1 == MyAnswer:
                                                score += 0
                                            else:
                                                score -= everyS
                                elif level1 == "2":
                                    time.sleep(0.5)
                                    do1 = input("1、加法 2、减法 3、乘法 4、除法")
                                    if do1 == "1":
                                        time.sleep(0.5)
                                        times1 = int(input("请输入练习的题数："))
                                        for i in range(times1):
                                            everyS = (100/times1) // score
                                            plus01 = random.randint(150000,100000)
                                            plus02 = random.randint(1,150000)
                                            print(plus01,"+",plus02,"=")
                                            MyAnswer = int(input("你的答案："))
                                            answer1 = plus01 + plus02
                                            if answer1 == MyAnswer:
                                                score += 0
                                            else:
                                                score -= everyS
                                    elif do1 == "2":
                                        time.sleep(0.5)
                                        times1 = int(input("请输入练习的题数："))
                                        for i in range(times1):
                                            everyS = (100/times1) // score
                                            plus03 = random.randint(15000,100000)
                                            plus04 = random.randint(5000,15000)
                                            print(plus03,"-",plus04,"=")
                                            MyAnswer = int(input("你的答案："))
                                            answer1 = plus03 - plus04
                                            if answer1 == MyAnswer:
                                                score += 0
                                            else:
                                                score -= everyS
                                    elif do1 == "3":
                                        time.sleep(0.5)
                                        times1 = int(input("请输入练习的题数："))
                                        for i in range(times1):
                                            everyS = (100/times1) // score
                                            plus03 = random.randint(15000,100000)
                                            plus04 = random.randint(1500,15000)
                                            print(plus03,"×",plus04,"=")
                                            MyAnswer = int(input("你的答案："))
                                            answer1 = plus03 * plus04
                                            if answer1 == MyAnswer:
                                                score += 0
                                            else:
                                                score -= everyS
                                    elif do1 == "4":
                                        time.sleep(0.5)
                                        times1 = int(input("请输入练习的题数："))
                                        for i in range(times1):
                                            everyS = (100/times1) // score
                                            plus03 = random.randint(15000,100000)
                                            plus04 = random.randint(150,15000)
                                            print(plus03,"-",plus04,"=")
                                            MyAnswer = int(input("你的答案："))
                                            answer1 = plus03 - plus04
                                            if answer1 == MyAnswer:
                                                score += 0
                                            else:
                                                score -= everyS
                                elif level1 == "3":
                                    time.sleep(0.5)
                                    do1 = input("1、加法 2、减法 3、乘法 4、除法")
                                    if do1 == "1":
                                        time.sleep(0.5)
                                        times1 = int(input("请输入练习的题数："))
                                        for i in range(times1):
                                            everyS = (100/times1) // score
                                            plus01 = random.randint(1500000,1000000)
                                            plus02 = random.randint(1,1500000)
                                            print(plus01,"+",plus02,"=")
                                            MyAnswer = int(input("你的答案："))
                                            answer1 = plus01 + plus02
                                            if answer1 == MyAnswer:
                                                score += 0
                                            else:
                                                score -= everyS
                                    elif do1 == "2":
                                        time.sleep(0.5)
                                        times1 = int(input("请输入练习的题数："))
                                        for i in range(times1):
                                            everyS = (100/times1) // score
                                            plus03 = random.randint(150000,1000000)
                                            plus04 = random.randint(50000,150000)
                                            print(plus03,"-",plus04,"=")
                                            MyAnswer = int(input("你的答案："))
                                            answer1 = plus03 - plus04
                                            if answer1 == MyAnswer:
                                                score += 0
                                            else:
                                                score -= everyS
                                    elif do1 == "3":
                                        time.sleep(0.5)
                                        times1 = int(input("请输入练习的题数："))
                                        for i in range(times1):
                                            everyS = (100/times1) // score
                                            plus03 = random.randint(150000,1000000)
                                            plus04 = random.randint(15000,150000)
                                            print(plus03,"×",plus04,"=")
                                            MyAnswer = int(input("你的答案："))
                                            answer1 = plus03 * plus04
                                            if answer1 == MyAnswer:
                                                score += 0
                                            else:
                                                score -= everyS
                                    elif do1 == "4":
                                        time.sleep(0.5)
                                        times1 = int(input("请输入练习的题数："))
                                        for i in range(times1):
                                            everyS = (100/times1) // score
                                            plus03 = random.randint(150000,1000000)
                                            plus04 = random.randint(1500,150000)
                                            print(plus03,"-",plus04,"=")
                                            MyAnswer = int(input("你的答案："))
                                            answer1 = plus03 - plus04
                                            if answer1 == MyAnswer:
                                                score += 0
                                            else:
                                                score -= everyS
                            time2 = time.time()
                            time = time2 - time1
                            everyT = time % times1
                            print("\033[41m本次练习你用了：",time,"秒。\033[41m")
                            #print("本次练习平均每道题你用了：",everyT,"秒。")#
                            print("你的成绩是：",score,"分。\033[0m")
                            if time < 60 and everyT < 10 and score == 100:
                                print("\033[41m优秀！\033[0m")
                            elif score >= 60:
                                print("及格")
                            else:
                                print('加油！')
                    elif i == "off":
                        break 
                    elif i == "reset":
                        pass
else:
    print()
