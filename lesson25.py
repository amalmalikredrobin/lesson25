# a = 4
# b = 5 
# c = 2

# print(((a**0.5 + (a+ b * b)**(1/3))  **  0.5) / (a + ( b/ (2 * c ** 0.5))))
# print(a + 1.7677669529663687)
# print(2.252180460284177 / 5.767766952966369)


# def sum(num):
#     if type (num) is int or type(num) is float:
#         digits = list(str(num))
#         sum = 0
#         for dgt in digits:
#             if dgt.isdigit():
#                 sum += int(dgt)
#         return sum
#     else:
#         return 'Error'

# print(sum(111))
# print(sum(-123))
# print(sum(12.3))
# print(sum(-345.6))
# print(sum('1121'))

def magic(*nums, k):
    sum = 0
    for num in nums:
        sum += num ** 2
    if sum % k == 0:
        return 'MAAAAAAAGIC'
    

magic(2,5,7, k=39)