# class BankAccount:
#     def __init__(self, name, balamce):
#         self.name = name                # 公开属性
#         self.__balamce = balamce        # 私有属性
#
#     def check_balamce(self):
#         print(f"{self.name}   余额 {self.__balamce}")
#
# account = BankAccount("dzt", 147258)
#
# account.check_balamce()
#
#
# # 尝试访问私有属性会报错
# # print(account.__balamce)
#
#
# # 强制访问私有属性（不推荐）
# print(account._BankAccount__balamce)



# 父类的父类     生物 (所有生物的共性)
# class livingThing():
#     feature = "有生命"
#
#     def breathe(self):
#         print("有呼吸")
#
#
#
# # 父类，动物
# class Animal(livingThing):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def eat(self):
#         print(f"{self.name} 在吃东西")
#
#     def sleep(self):
#         print(f"{self.name} 在睡觉")
#
#
# # 子类， 狗类 继承动物类
# class Dog(Animal):
#     def bark(self):
#         print("小狗哇哇叫")
#
#
# dog1 = Dog("旺财",2)
#
# # 继承了父类的公有属性
# print(dog1.name)
#
# dog1.eat()
# dog1.bark()
#
# # 访问间接继承自父类的属性和方法
# print(dog1.feature)
# dog1.breathe()




# class Amimal:
#     def make_sound(self):
#         print("动物发出声音")
#
# class Cat(Amimal):
#     # def make_sound(self):
#     #     print("喵喵喵")
#
#     def make_sound(self):
#         super().make_sound()
#         print("喵喵喵")
#
# # animal = Amimal()
# # animal.make_sound()
#
#
# cat = Cat()
# cat.make_sound()



# # 父类 1：手表类
# class Watch:
#     def show_time(self):
#         print(f"当前时间：15:00")
#
# # 父类 2：健康设备类
# class HeathDevice:
#     def check_heart_rate(self):
#         print(f"心率检测：75次/秒")
#
#
# #子类：只能手表类，继承两成父类
# class SmartWatch(Watch, HeathDevice):
#     pass
#
# smartWatch = SmartWatch()
# smartWatch.show_time()
# smartWatch.check_heart_rate()


class Phone:
    def take_photo(self):
        print("手机拍照：普通画质")

class Camera:
    def take_photo(self):
        print("相机拍照：高清画质")

class CameraPhone(Phone, Camera):
    # def take_photo(self):
    #     print("手机拍照：普通画质")
    #     print("相机拍照：高清画质")

    pass


# 优先执行最前参数的父类
cp = CameraPhone()
cp.take_photo()
Camera.take_photo(cp)









