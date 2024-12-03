import random
NUM_DICE_TO_ROLL=5
SEED= 2183
count=10

def roll_dice(num_rolls):
    """Returns a list of diced values"""
    dice_values=[]
    for i in range(num_rolls):
        dice_value=random.randint(1,6)
        dice_values.append(dice_value)
    return dice_values

def most_repeats(dice_values):
    """Returns the highest number of repeated values in the dice roll list."""
    counts = {}
    for value in dice_values:
        if value in counts:
            counts[value] += 1
        else:
            counts[value] = 1
    return max(counts.values(), default=0)

def main():
    random.seed(SEED)
    try_again ='Y'

    while try_again=='Y':
        dice_roll=roll_dice(NUM_DICE_TO_ROLL)
        repeat_val=most_repeats(dice_roll)

        print(f'Your roll of {dice_roll} contains {repeat_val} of a kind')
        print()
        try_again=input("Do you want to roll again (Y/N)?" )
        print("helloooooo")

if __name__ == "__main__":
    main()
