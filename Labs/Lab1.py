import itertools

print("Hello World")
def func(a, b):
    bool = True
    if a > 0 and b > 0 and a%b == 0:
        return bool
    elif a%b != 0:
        bool = False;
        return bool
    if a < 0 or b < 0:
        return Exception("Error")


print(func(4,2))

def func1(a, b):
    array = []
    if a < b and b - a >1:
        for x in range(a+1, b):
            array.append(x)
        return array
    else:
      return Exception("NoSimpleDigits")


print(func1(1,3))

output_array=[]
input_array = ['a', ['c', 1, 3], ['f', 7, [4, '4']], [{'lalala': 111}]]

def func2(spysok):
    for i in range(0, len(spysok)):
        if(isinstance(spysok[i], list)):
            func2(spysok[i])
        else:
            output_array.append(spysok[i])

func2(input_array)

print(output_array)




