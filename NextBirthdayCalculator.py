# Accepts an integer called month. Returns the number of days in the
# month passed in.
def getDaysInMonth(month):
    if month == 2:
        return 28
    elif month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    else:
        return 31


# Accepts a String called message. Prompts user for a date.
# Returns a list representing the date.
def getInformation(message):
    print message, "(dd/mm/yyyy)"
    date = raw_input()
    date = date.split("/")
    for x in range(len(date)):
        date[x] = int(date[x])
    return date


# Accepts integers representing today's month, today's date, the user's birth
# month and the user's birth date. Returns the number of days until the user's
# next birthday.
def wrapAround(todayMonth, todayDate, birthdayMonth, birthdayDate):
    totalDays = getDaysInMonth(todayMonth) - todayDate
    while todayMonth + 1 <= 12:
        totalDays = totalDays + getDaysInMonth(todayMonth + 1)
        todayMonth = todayMonth + 1
    todayMonth = 0
    while birthdayMonth > todayMonth + 1:
        totalDays = totalDays + getDaysInMonth(todayMonth + 1)
        todayMonth = todayMonth + 1
    return totalDays + birthdayDate


# Accepts an integer that represents the number of days until the user's
# next birthday. Prints a message corresponding to the number of days.
def printMessage(totalDays):
    print " "
    if totalDays == 0:
        print "Happy Birthday!"
    elif totalDays == 1:
        print "Wow! Your birthday is tomorrow!"
    else:
        print "Your birthday is in", totalDays, "days!"


# Prompts the user, asking if he or she would like to calculate another birthday.
def playAgain():
    print "Would you like to calculate another birthday? (yes or no)"
    answer = raw_input()
    if answer.startswith("y"):
        play = True
    else:
        play = False
    print(" ")
    return play


def absoluteDayOfTheYear(today):
    todayMonth = today[0]
    todayDate = today[1]
    totalDays = todayDate
    while todayMonth - 1 > 0:
        totalDays = totalDays + getDaysInMonth(todayMonth - 1)
        todayMonth = todayMonth - 1
    return totalDays


# Prompts the user for today's date and their birthday and calculates the
# number of days until their next birthday.
print "This program will calculate the number of days until your next birthday"
play = True

while play == True:
    today = getInformation("What is today's date?")
    todayMonth = today[0]
    todayDate = today[1]
    birthday = getInformation("When is your birthday?")
    birthdayMonth = birthday[0]
    birthdayDate = birthday[1]

    totalDays = 0
    # print todayDate, todayMonth, birthdayDate, birthdayMonth
    if birthdayMonth == todayMonth:
        if todayDate < birthdayDate:
            totalDays = birthdayDate - todayDate
        elif todayDate > birthdayDate:
            totalDays = wrapAround(todayMonth, todayDate, birthdayMonth, birthdayDate)
        else:
            totalDays = 0
    elif birthdayMonth > todayMonth:
        totalDays = getDaysInMonth(todayMonth) - todayDate
        while birthdayMonth > todayMonth + 1:
            totalDays = totalDays + getDaysInMonth(todayMonth + 1)
            todayMonth = todayMonth + 1
        totalDays = totalDays + birthdayDate
    elif birthdayMonth < todayMonth:
        totalDays = wrapAround(todayMonth, todayDate, birthdayMonth, birthdayDate)

    absDayOfTheYear = absoluteDayOfTheYear(today)
    print today[0], "/", today[1], "is day number", absDayOfTheYear, "of 365"
    printMessage(totalDays)
    play = playAgain()



