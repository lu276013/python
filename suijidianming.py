file=open(r'C:\Users\Administrator\Desktop\xingming.csv','r')
lines=file.readlines()
students={}
for line in lines:
    tmp_list=line.split(',')
    xuehao = tmp_list[0]
    xingming = tmp_list[1]
    students[xuehao]=xingming
print(students)
import random
#random.sample([1,2,3,4],2)
#students.keys()
num=int(input("输入你要抽取的人数："))
xuehao_list = random.sample(students.keys(),num)
xuehao_list
for xuehao in xuehao_list:
    print(students[xuehao])