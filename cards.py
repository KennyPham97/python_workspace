import random

cards = ["ash blossom", 
         "neo space connector",
         "imperm",
         "gearfried",
         "noble arms museum",
         "durendal",
         "joyeuse",
         "renaud",
         "ogier",
         "oliver",
         "ricci"
         ]

def main():
    print(random.sample(cards, k=2))

if __name__ == "__main__":
    main()
    
    
#random.choice selects random with replacement
#random.sample selects random without replacement.