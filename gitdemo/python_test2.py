user_age=input("请输入您的年龄:")
print(user_age)
weight=input(f"请输入您的体重(单位:kg):")
height=input(f"请输入您的身高(单位:M):")
BMI=int(weight)/(float(height)**2)#BMI计算公式
print(f"您的BMI指数为:",BMI)
if BMI<18.5:
    print("您的体重偏瘦!")
elif 18.5<BMI<=24.9:
    print("您的体重正常!")
elif BMI>=25 and BMI<=30:
    print("您的体重偏胖!")
else:
    print("您的体重过胖!")
