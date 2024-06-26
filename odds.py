import sys

def main():
    if len(sys.argv) != 3:
        print("Console input must have 2 arguments, an under and over value.")
        sys.exit()
    
    while True:
        try:
            under = abs(int(sys.argv[1]))
            over = abs(int(sys.argv[2]))
            break
        except ValueError:
            print("Invalid input type.")
            sys.exit()
    calculate_odds(under, over)
    
    
    
def calculate_odds(under, over):
    under_odds = under/(under+100)*100
    over_odds = over/(over+100)*100
    print(f"{round(under_odds, 2)}%, {round(over_odds, 2)}%")  
    

main()