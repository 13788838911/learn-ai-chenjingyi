#list可变序列，有序，元素可重复
#str不可变序列，有序，字符可重复
#dict可变映射无序
#1.
# nums=list(map(int,input().split()))
# print(sorted(nums))

# num=nums
# num.sort()
# print(num)

#2.
# for i in range (1,10):
#     for j in range(1,i+1):
#         print(f"{i}*{j}={i*j} ",end="")
#     print()
    

#3.
# str1=str(input())
# a=str1.find("ol")
# if (a!=-1):
#     str1=str1.replace("ol","fzu")
# print(str1[::-1])

#4.
# lst=input().split()
# new=list()
# for element in lst:
#     if(element.isdigit()):
#         num=int(element)
#         new.append(num)
# print(sorted(new))

# lst=input().split()
# for element in lst[:]:
#     if not element.isdigit():
#         lst.remove(element)
# print(sorted(lst))

#5.
# d=dict()
# while(1):
#     num = int(input())
#     if num==0:
#         break
#     name = input()
#     d[num] = name

# for n in list(d.keys()):
#     if n % 2 == 0:
#         d.pop(n)

# print(d)

# def count(lst,str1):
#     cnt=0
#     for num in lst:
#         if num==str1:
#             cnt+=1
#     return cnt

# string=input().split()
# d=dict()
# for element in string:
#     n=count(string,element)
#     k=element
#     d[k]=n
# print(d)


