def add(num1, num2):
    """Returns num1 plus num2."""
    return num1 + num2


def sub(num1, num2):
    """returns num1 - num2."""
    return num1 - num2


def mul(num1, num2):
    """returns num1 * num2."""
    return num1 * num2


def div(num1, num2):
    """returns num1 / num2."""
    try:
        return num1 / num2
    except ZeroDivisionError:
        print("Handled div by zero. Return zero")
        return 0


def runOperation(operation, num1, num2):
    if (operation == 1):
        print(add(num1, num2))
    elif (operation == 2):
        print(sub(num1, num2))
    elif (operation == 3):
        print(mul(num1, num2))
    elif (operation == 4):
        print(div(num1, num2))
    else:
        print("I don't understand")


def anotherCalculation(morecalc):
    if (morecalc == "y"):
        main()
    else:
        print("Bye")
        return


def main():
    validInput = False
    while not validInput:

        try:
            num1 = int(raw_input("What is number 1?"))
            num2 = int(raw_input("What is number 2?"))
            operation = int(raw_input("What do you want to do? 1)add, 2)subtract, 3)multiply, 4)divide"))
            validInput = True
            runOperation(operation, num1, num2)
        except ValueError:
            print("Invalid input. Try again")
        except:
            print("Unknown error")

    reRun = False
    while not reRun:

        try:
            morecalc = (raw_input("Another calculation?('y' for yes)"))
            anotherCalculation(morecalc)
            reRun = True
        except:
            return


main()
