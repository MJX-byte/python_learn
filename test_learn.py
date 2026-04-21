word="请输入你想输入3个数字:"
print(word)
nums=[]
for i in range(3):
    num=input(f"please enter the {i}st number:")
    nums.append(num)
print(f"all of the num are:",nums)