"""
Create Phone Number
https://www.codewars.com/kata/525f50e3b73515a6db000b83/train/python
args: list of 10 integers -> ex.[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
return: string of numbers in the form of phone number -> ex."(123) 456-7890"
"""

def create_phone_number(n):
    conv2str = "".join(list(map(str, n)))
    return "({0}) {1}-{2}".format(conv2str[:3], conv2str[3:6], conv2str[6:])

# print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))