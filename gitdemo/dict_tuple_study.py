num_dict={"first_one":1,"second_one":2}
num_dict["third_one"]=3 #向字典中添加新的键值对
num_dict.update({"fourth_one":4})
print(f"字典中的内容为:\n",num_dict)
num_max=num_dict["third_one"]
#print(num_max)
print(f"字典长度为",len(num_dict))

"""
content=input("请输入你要查询的内容:")
if content in num_dict:
    print("你查询的"+content+"内容为:"+str(num_dict[content]))
else:
    print("您的查询不存在!")
"""

#以下分别输出字典中的所有键，值，以及键值对
print("字典中的键为:")
for key in num_dict.keys():
    print(key)
print("字典中的值为:")
for value in num_dict.values():
    print(value)
print("字典中的所有键值对分别为:")
for key,value in num_dict.items():
    print(key,value)

#打印字典.items
#这是 把键值对以元组形式展示出来，方便遍历，不代表字典本体就是元组组成的列表。
print(num_dict.items())

del num_dict["third_one"]
print("删除第三个键值对后的字典为:",num_dict)

