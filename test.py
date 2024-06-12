# def main():
#     x = get_int("What's x? ")
#     print(f"x is {x}")

# def get_int(prompt):
#     while True:
#         try:
#             x = int(input(prompt))
#             return x
#         except ValueError:
#             print("Not an integer.")
            
# main()


team = [
    "kenny",
    "chris",
    "vlad",
    "andrew",
    "mark",
    "celida",
]
def main():
    while True:
        answer = input("Who's on the Trinoor Solution Dev Team? ").lower()
        if validate_person(answer):
            break
        else:
            print("Incorrect, try again")
            pass
    
def validate_person(answer):
    if answer in team:
        print("Correct!")
        return True
    
    
    


main()