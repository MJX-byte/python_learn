# # grade=int(input("请输入你的期末成绩:"))
# # if grade>=60:
# #     final="OK"
# # else:
# #     final="BAD"
# # print(final)

# ###列表知识点学习:
# first="TV"
# shopping_list=["computer",first]
# shopping_list.append("food")
# print(f"起初存在的物品:",shopping_list)
# shopping_list.remove(first)
# print(f"移除之后的物品:",shopping_list)
num_list=[1,9,6,5,-2,-8]
num_first=num_list[0]
num_max=max(num_list)
num_min=min(num_list)
num_sorted=sorted(num_list)
print(num_max)
print(num_min)
print(num_sorted)
num_list.remove(num_list[0])
#num_list=str(num_list)
# num_list=num_list[::-1]
# print(num_list)
print(f"移除列表第一个元素后的列表为:",num_list)
num_list.insert(0,num_list[0])
#num_list.insert(0,num_first)
print(num_list)
num_list.append({1:"你好"})
print(num_list)
num_list1=num_list.copy()
print(f"两个列表位于的内存地址分别为:","num_list的地址:",id(num_list)," num_list1的地址:",id(num_list1))
#print("\n")
num_total=num_list.count(num_list[0])
print("列表中第一个元素的数量为:",num_total)
print("列表中元素1的个数为:",num_list.count(1))
num_list.clear()
print(num_list)
