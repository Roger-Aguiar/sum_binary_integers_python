# Name:         Roger Silva Santos Aguiar
# Function:     This application gets 2 integer numbers, converts both to binary and sums the two integers.
# Initial date: July 1, 2020
# Last update:  July 1, 2020

class SumBinaryIntegers:
    def __init__(self, firstNumber, secondNumber):
        self.firstNumber = firstNumber
        self.secondNumber = secondNumber

    def returnSumIntegers(self):
        return self.firstNumber + self.secondNumber

    def returnBinarySum(self):
        binaryNumber1 = ""
        binaryNumber2 = ""
        firstBinaryNumber = SumBinaryIntegers.convertIntegersToBinary(self.firstNumber)
        secondBinaryNumber = SumBinaryIntegers.convertIntegersToBinary(self.secondNumber)

        for bit in firstBinaryNumber:
            binaryNumber1 = binaryNumber1 + str(bit)

        for bit in secondBinaryNumber:
            binaryNumber2 = binaryNumber2 + str(bit)

        print("{} in binary is {} " .format(self.firstNumber, binaryNumber1))
        print("{} in binary is {} " .format(self.secondNumber, binaryNumber2))

    def convertIntegersToBinary(decimalNumber):
        binaryNumber = []

        while decimalNumber != 1:
            remainder = decimalNumber % 2
            decimalNumber = int(decimalNumber / 2)
            binaryNumber.append(remainder)

        binaryNumber.append(decimalNumber)

        binaryNumber.reverse()
        return binaryNumber

if __name__ == '__main__':
    firstNumber = int(input("Enter the first number: "))
    secondNumber = int(input("Enter the second number: "))

    sumIntegers = SumBinaryIntegers(firstNumber, secondNumber)
    sum = sumIntegers.returnSumIntegers()
    binarySum = sumIntegers.returnBinarySum()

    # print("{} + {} = {}" .format(firstNumber, secondNumber, sum))