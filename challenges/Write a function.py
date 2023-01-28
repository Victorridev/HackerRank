

# def is_leap(year):
    
#     if ((year / 4 and year % 4 == 0) is True) and ((year / 100 and year % 100 == 0) is False) or ((year / 400 and year % 400 == 0) is True):
#         return True
#     else:
#         return False
        
# year = int(input())
# print(is_leap(year))



def is_leap(n):
    if n % 400 == 0:
        return True
    if n % 100 == 0:
        return False
    if n % 4 == 0:
        return True
    return False

print(is_leap(int(input())))