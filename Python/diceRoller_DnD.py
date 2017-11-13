#DnD Dice Roller

## Import needed functions
import random
## Dice roller for attacks and skill checks
def roll (x, s, m): #Input: x = number of dice, s = number of sides on dice, m = plus/minus modifier
    total = 0 + m
    count = 0
    while count < x:
        total = total + random.randint(1, s)
        count = count + 1
    return total
## Rolls a d6
def d6():
    return random.randint(1,6)
## Finds the lowest number in an array and removes it
def dropLow (a):
    if len(a) < 2: #Arrays with one entry have nothing removed
        return a
    else:
        a.remove(min(a))
        return a
## Generates an array of random rolls to use for character starting stats
def statArray():
    finArr = []
    z = 0
    while z < 7: #roll seven...
        diceArr = []
        x = 0
        while x < 4: #...sets of 4d6...
            diceArr.append(d6())
            x += 1
        diceRem = dropLow(diceArr) #...and drop lowest number...
        dSum = 0
        for d in diceRem:
            dSum += d #...then total the dice sum....
        finArr.append(dSum)
        z += 1
    return (dropLow(finArr)) #...and drop the lowest sum
