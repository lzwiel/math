import math

def calculator():
    print("欢迎使用科学计算器！")
    while True:
        print("\n请选择要进行的操作：")
        print("1. 加法")
        print("2. 减法")
        print("3. 乘法")
        print("4. 除法")
        print("5. 幂运算")
        print("6. 开方运算")
        print("7. 对数运算")
        print("8. 三角函数")
        print("9. 退出")
        
        choice = int(input("请输入对应的数字："))
        if choice == 1:
            num1 = float(input("请输入第一个数："))
            num2 = float(input("请输入第二个数："))
            result = num1 + num2
            print("结果为：", result)
        elif choice == 2:
            num1 = float(input("请输入第一个数："))
            num2 = float(input("请输入第二个数："))
            result = num1 - num2
            print("结果为：", result)
        elif choice == 3:
            num1 = float(input("请输入第一个数："))
            num2 = float(input("请输入第二个数："))
            result =num1 * num2
            print("结果为：", result)
        elif choice == 4:
            num1 = float(input("请输入第一个数："))
            num2 = float(input("请输入第二个数："))
            if num2 == 0:
                print("除数不能为0，请重新输入！")
            else:
                result = num1 / num2
                print("结果为：", result)
        elif choice == 5:
            num1 = float(input("请输入底数："))
            num2 = float(input("请输入指数："))
            result = math.pow(num1, num2)
            print("结果为：", result)
        elif choice == 6:
            num1 = float(input("请输入一个数："))
            if num1 < 0:
                print("负数不能开方，请重新输入！")
            else:
                result = math.sqrt(num1)
                print("结果为：", result)
        elif choice == 7:
            num1 = float(input("请输入底数："))
            num2 = float(input("请输入真数："))
            if num1 <= 0 or num1 == 1:
                print("底数必须大于0且不等于1，请重新输入！")
            elif num2 <= 0:
                print("真数必须大于0，请重新输入！")
            else:
                result = math.log(num2, num1)
                print("结果为：", result)
        elif choice == 8:
            print("请选择要计算的三角函数：")
            print("1. 正弦函数")
            print("2. 余弦函数")
            print("3. 正切函数")
            print("4. 反正弦函数")
            print("5. 反余弦函数")
            print("6. 反正切函数")
            
            trig_choice = int(input("请输入对应的数字："))
            if trig_choice == 1:
                angle = float(input("请输入角度（度）："))
                radian = math.radians(angle)
                result = math.sin(radian)
                print("结果为：", result)
            elif trig_choice == 2:
                angle = float(input("请输入角度（度）："))
                radian = math.radians(angle)
                result = math.cos(radian)
                print("结果为：", result)
            elif trig_choice == 3:
                angle = float(input("请输入角度（度）："))
                radian = math.radians(angle)
                result = math.tan(radian)
                print("结果为：", result)
            elif trig_choice == 4:
                value = float(input("请输入值（取值范围为[-1,1]）："))
                if value < -1 or value > 1:
                    print("值超出取值范围，请重新输入！")
                else:
                    radian = math.asin(value)
                    angle = math.degrees(radian)
                    print("结果为：", angle)
            elif trig_choice == 5:
                value = float(input("请输入值（取值范围为[-1,1]）："))
                if value < -1 or value > 1:
                    print("值超出取值范围，请重新输入！")
                else:
                    radian = math.acos(value)
                    angle = math.degrees(radian)
                    print("结果为：", angle)
            elif trig_choice == 6:
                value = float(input("请输入值："))
                radian = math.atan(value)
                angle = math.degrees(radian)
                print("结果为：", angle)
            else:
                print("无效的选择，请重新输入！")
        elif choice == 9:
            print("感谢使用科学计算器，再见！")
            break
        else:
            print("无效的选择，请重新输入！")
            
calculator()
这个科学计算器包括加法、减法、乘法、除法、幂运算、开方运算、对数运算、三角函数等多个选项，并对输入的数据进行了错误处理，确保了程序的稳定性和准确性。
