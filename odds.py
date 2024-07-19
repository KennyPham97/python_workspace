import sys

def main():
    if len(sys.argv) != 3:
        sys.exit("Console input must have 2 arguments, an under and over value.")
    
    while True:
        try:
            under = abs(int(sys.argv[1]))
            over = abs(int(sys.argv[2]))
            break
        except ValueError:
            sys.exit("Invalid input type.")
    calculate_odds(under, over)
    
    
    
def calculate_odds(under, over):
    under_odds = under/(under+100)*100
    over_odds = over/(over+100)*100
    print(f"{round(under_odds, 2)}%, {round(over_odds, 2)}%")  
    

main()