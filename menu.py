# Name:         Roger Silva Santos Aguiar
# Function:     This application makes the sum between two binary numbers,
#               the user enters two integer numbers, the application converts both to
#               binary and makes the sum in binary.
# Initial date: July 2, 2020
# Last update:  July 2, 2020

#Required modules
import sum_binary_integers

class Menu:
    def menu(self):
        print("This application makes the sum between two binary numbers. \nYou will enter two integers, and the "
              "application will convert \nboth to binary and makes the sum in binary.")

        print("\n**************************************************Menu**************************************************\n")
        print("1 - Sum binary numbers")
        print("2 - Exit")
        print("\n********************************************************************************************************\n")

    def getValues(self):
        firstNumber = int(input("\nEnter the first number: "))
        secondNumber = int(input("Enter the second number: "))

        sumIntegers = sum_binary_integers.SumBinaryIntegers(firstNumber, secondNumber)
        sumIntegers.makeBinarySum()


if __name__ == '__main__':
    runMenu = Menu()
    runMenu.menu()

    option = int(input("Please, choose an option: "))

    while option == 1:
        runMenu.getValues()
        runMenu.menu()
        option = int(input("Please, choose an option: "))

    if option == 2:
        print("End program.")