while True:
    try:
        x = int(input("What's x? "))
        print(f"x is {x}")
        break
    except ValueError:
        print("x is not an integer")
        continue

# x = int(input("What's x? "))
# print(f"x is {x}")