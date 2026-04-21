#给定一个十进制整数 n，请将其转换为对应的二进制表示，并输出
"""num_list=[]
n=int(input("请输入一个十进制数:"))#输入十进制数
if n==0:
    print(0)
else:
 while n>0:#保证n>0就条件足够，若此种情况会导致最后一位二进制数被遗漏
   num_1=n//2#求的十进制除于2后的整数
   num_list.append(n%2)
   n=num_1
 num_length=len(num_list)
 for i in range(num_length-1,-1,-1):
    print(num_list[i],end='')#print()语句中，默认为print(i,end='\n')
    print()
"""
#给定一个二进制整数（由若干个 0 和 1 组成的字符串），请将其转换为对应的十进制整数并输出。
nums=input().strip()
length=len(nums)
total=0
num_length=length
for i in range(length):
   num=int(nums[i])*(2**(num_length-1))
   total+=num
   num_length-=1
print(total)








