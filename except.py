# try:
#     print(3/0)
# except ZeroDivisionError:
#     print("an error occured")

def func(num):
    if num < 4:
        x = num/(num-3)
    
    print("value of x: ", x)

try:
    #func(3)
    func(5)

except ZeroDivisionError:
    print("ZeroDivisionError handled.")
except NameError:
    print("NameError handled")

