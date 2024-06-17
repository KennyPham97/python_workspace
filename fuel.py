#prompt user for a fraction formatted as x/y
#x,y are both integers and output is a percentage rounded to the nearest integer
#print E if 1% or less remains, print F if 99% or more remains
#if x,y are not ints, or x is greater than y, prompt user again. 
#catch exceptions like ValueError or ZeroDivisionError.

def main():
    while True:
        try:
            x,y = input("Fraction: ").split("/")
            if int(x) <= int(y):
                convert_to_percentage(x,y)
                break
        except (ValueError,ZeroDivisionError):
            continue

def convert_to_percentage(x,y):
    percentage = int(x)/int(y)*100
    if percentage >=99:
        print("F")
    elif percentage <= 1:
        print("E")
    else:
        print(round(percentage),"%",sep="")
    
main()