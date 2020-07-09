# hello = "test python"
# print(hello.title())
# print(hello.upper())
# print(hello.lower())
list = ["fff", "aaaa", "sdfsdf"]
print(list)
print(list.pop())
print(list)
list.append("ssss")
print(list)
list.insert(1, "sfs")
print(list)
if list.__contains__("sfsfs"):
    list.remove("sfsfs")
else:
    print("none")
list.sort()
print(list)
list.sort(reverse=True)
print(list)
list.reverse()
print(list)
print("list sorted")
print(sorted(list, reverse=True))
print(list)
print(sorted(list))
print(list)
print(len(list))
# message = input("tell me your word !")
# message = int(message)
# print(message > 10)
# while循环后面要加:
text = ""


def test():
    print(text)

age = "sdfs"
#可以用来判断是否为空串
if age:
    print("age is none")

while text != "exit":
    text = input("请输入退出")
    test()
    print("not quit")


