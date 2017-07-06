# A game that prompts the user to guess a number and gives a hint after each
# guess. Prints statistics if the user does not want to play again.

import random

play = True
max = 1000 # set the max number that can be guessed
count = 0
guess = 0
sum = 0
totalGames = 0
best = 1000000

while play:
    if count == 0:
        answer = random.randint(1, max)
        totalGames = totalGames + 1
        print "I'm thinking of a number between 1 and", max, "..."
    count = count + 1
    print "Your guess? "
    guess = int(raw_input())
    if guess > answer:
        print "It's lower."
    elif guess < answer:
        print "It's higher."
    else:
        print "You got it right in", count, "guesses."
        sum = sum + count
        if count < best:
            best = count
        print "Play again? (yes/no)"
        again = raw_input()
        print " "
        if again.startswith("n"):
            play = False
        count = 0

print "Overall results:"
print "Total games      =", totalGames
print "Total guesses    =", sum
print "Avg guesses/game =", (float(sum) / totalGames)
print "Best game        =", best
