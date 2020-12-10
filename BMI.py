class BMI:
    def __init__(self,name,age,weight,height):
        self.name = name
        self.age = int(age)
        self.weight = int(weight)
        self.height = float(height)
        self.BMI = float(self.weight/(self.height*self.height))
    def say(self):
        print("{n}的BMI是{p}".format(n=self.name,p=self.weight/(self.height*self.height)))
        if self.BMI <18.5:
            print("偏瘦")
        elif self.BMI <24:
            print("正常")
        elif self.BMI <30:
            print("偏胖")
        else :
            print("肥胖")
    def the_age(self):
            print("{n}".format(n=self.name), "的年龄是：{n}".format(n=self.age))

    def the_weight(self):
            print("{n}".format(n=self.name), "的体重是：{n}".format(n=self.weight))

    def the_height(self):
            print("{n}".format(n=self.name), "的身高是：{n}".format(n=self.height))
zhangsan = BMI("zhangsan", "20", 73,1.73)
zhangsan.say()
zhangsan.the_age()
zhangsan.the_weight()
zhangsan.the_height()
