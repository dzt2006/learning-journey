# import random
#
# num = random.randint(1,100)
#
#
# class Car:
#     '''汽车类'''
#     pass        # pass表示占位，空语句，暂时不写内容
#
# car1 = Car()
# print(car1)


# class Car:
#     def start(self):
#         print("self", self)
#     def run(self):
#         print("汽车在行使")
#
# car1 = Car()
# car1.start()
# car1.run()
# print("Car1", car1)
#
# car2 = Car()
# car2.start()
# car2.run()
# print("Car2", car2)

# class Car:
#     wheel_count = 4
#     def start(self):
#         print("self", self)
#     def run(self):
#         print(f"{self.color} 的 {self.brand} 启动了！")
#
# car1 = Car()
# car1.color = "红色"
# car1.brand = "保时捷"
# print(car1.run())



# class Car:
#     wheel_count = 4
#     # 创建对象的时候会自动调用
#     def __init__(self):
#         print("我是__init__方法")
#         self.color = "红色"
#         self.brand = "保时捷"
#     def start(self):
#         print(f"{self.color} 的 {self.brand} 启动了！")
#
# car1 = Car()
# car1.start()



class Car:
    # 销毁对象时自动执行(就是后面代码没有用到这个类了，就会执行)
    def __del__(self):
        print(f"{self.brand} 被销毁了")

car1 = Car()





