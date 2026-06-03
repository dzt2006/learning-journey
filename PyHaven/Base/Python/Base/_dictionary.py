info = {
    "name": "dzt",
    "python": 98
}

print(info, type(info))

print(info["python"])

# print(info["语文"]) # 找不到直接报错
print(info.get("语文")) # 一般使用这个
print(info.get("语文","键名不存在"))

# 键名不存在直接添加新的键名
info["age"] = 20

# 键名存在直接修改
info["python"] = 99

# 先找然后删除
info.pop("age")

# 删除不存在的键就会报错
# info.pop("语文")
info.pop("语文", "bucunzai ") #这样就不会报错

# 全部清除
# info.clear()

print(info.keys())
print(info.values())
print(info.items())  # 拿出的每一对都是一对元组






