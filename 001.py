def sum_everything(a, b):
    if a == int(a) and b == int(b):
        return a + b
    elif a == str(a) and b == str(b):
        return a + b
    elif a == list(a) and b == list(b):
        return a + b
    elif a == int(a) and b == str(b):
        b = len(b)
        print(a + str(b))
    elif a == str(a) and b == int(b):
        print(a + str(b))
    elif a == list(a) or b == list(b):
        if a == list(a):
            return a.append(b)
        elif b == list(b):
            b = str(b)
            return a + b


print(sum_everything(1, 2))
print(sum_everything("1", 100))
# print(sum_everything(1, "test"))
print(sum_everything([], 100))
# print(sum_everything("1", []))