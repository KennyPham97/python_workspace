def main():
    fruit = input("Item: ").lower()
    kcal = get_calories(fruit)

    if kcal:
        print("Calories:",kcal)
    return None

def get_calories(fruit):
    fruits = {
        "apple": 130,
        "banana": 110,
        "strawberries": 50,
        "cantaloupe": 50,
        "grapes": 90,
        "orange": 80,
        "peach": 60,
        "avocado": 50,
        "sweet cherries": 100,
        "kiwifruit": 90,
        "pear": 100,
        "watermelon": 80
        }

    if fruit in fruits:
        kcal = fruits[fruit]
        return kcal

main()


#Can use a for loop for line 25.
# for f in fruits:
#     if f == fruit:
#         kcal = fruits[f]
#         return kcal

#can use else statement in line 7.