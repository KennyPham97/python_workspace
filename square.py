def main():
    height = int(input("What's the height? "))
    square_outline(height)

def square_outline(n):
    for i in range(n):
        if 0 < i < n-1:
            print("#"," "*(n-2),"#")
        else:
            print("# " * n)

main()
        