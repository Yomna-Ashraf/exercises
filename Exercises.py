# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 18:25:42 2021

@author: win10
"""


list1 = ["beter","matt","beter",
         "matt","beter","harry",
         "beter","beter","matt",
         "beter", "harry","harry",
         "axel","matt","beter","harry",
         "beter","beter","matt","beter",
         "harry","beter","matt","beter", "harry"]
b = len(list1)
list3 = []
list2 = []
for i in list1:
    if i not in list2:
        list2.append(i)
for a in list2:
    y=list1.count(a)

    if (y/b) * 100 >= 5:
        list3.append(a)
print(list3)


num = int(input())

for i in range(num):
    str1 = input()

    for d in str1:
        if str1.index(d) % 2 == 0 :
            print(d ,end="")
    print(" ",end="")        
    for x  in str1:
        if str1.index(x) % 2 ==1:
            print(x ,end="")

    print()

