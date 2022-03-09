# if __name__ == '__main__':
#     n = int(input())
    
#     li = []
#     for i in range(n):
#         li.append(i**2)
    
#     print(*li,sep='\n')

def is_leap(year):
    leap = False
    
    # Write your logic here
    if year % 4 == 0 and (year % 100 == 0 and year % 400 == 0):
        return True 
    else:
        return leap

year = int(input())
print(is_leap(year))