string = "text"
print(string, string[0], type(string))

integer = 15
print(integer, type(integer))

decimal, complEx = 23.7, 1+3j
print(decimal, type(decimal))
print(complEx, type(complEx))

fruit = ["apple", "banana", "pear"]
print(fruit, type(fruit))

veg = ("tomato", "potato", "cucumber")
print(veg, type(veg))

x = range(7)
print(x, type(x))

dictionary = {"plane" : "Flugzeug", "page" : 15, "line" : 22}
print(dictionary, type(dictionary))

syrup = {"hazelnut", "chocolate", "lavender"}
print(syrup, type(syrup))

icecream_flavours = frozenset({"vanilla", "chocolate", "mint", "caramel"})
print(icecream_flavours, type(icecream_flavours))

fact = True
print(fact, type(fact))

empty = None
print(empty, type(empty))

bt = b"Hello"
print(bt, type(bt))

btarr = bytearray(5)
print(btarr, type(btarr))

mem = memoryview(bytes(5))
print(mem, type(mem))