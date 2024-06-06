#minimum of 2 characters, max of 6
#must start with at least 2 letters
#numbers cannot be used in the middle of a plate, must be at the end and first number cannot be 0
#no periods, spaces, or punctuation marks allowed.

# def main():
#     plate = input("Plate: ")
#     if is_valid(plate) and number_check(plate):
#         print("Valid")
#     else:
#         print("Invalid")

# def is_valid(s):
#     if 2 <= len(s) <= 6 and s[0:2].isalpha() and s.isalnum():
#         return True

# def number_check(s):
#     for i in range(len(s)):
#         if s[i].isdigit():
#             index = s.index(s[i])
#             if s[index:].isdigit() and s[i] != '0':
#                 return True
#             else:
#                 return False
#     return True
# main()

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if 2 <= len(s) <= 6 and s[0:2].isalpha() and s.isalnum():
        for char in s:
            if char.isdigit():
                index = s.index(char)
                if s[index:].isdigit() and int(char) != 0:
                    return True
                else:
                    return False

        return True

main()

# def main():
#     plate = input("Plate: ")
#     if is_valid(plate):
#         print("Valid")
#     else:
#         print("Invalid")

# def is_valid(s):
#     if 1 < len(s) < 7 and s[0:2].isalpha() and s.isalnum():
#         for i in range(len(s)):
#             if s[i].isdigit():
#                 index = s.index(s[i])
#                 if s[index:].isdigit() and int(s[i]) != 0:
#                     return True
#                 else:
#                     return False
#         return True
                    
# main()