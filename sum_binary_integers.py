# Name:         Roger Silva Santos Aguiar
# Function:     This application gets 2 integer numbers, converts both to binary and sums the two integers.
# Initial date: July 1, 2020
# Last update:  July 2, 2020

class SumBinaryIntegers:
    def __init__(self, firstNumber, secondNumber):
        self.firstNumber = firstNumber
        self.secondNumber = secondNumber

    def returnSumIntegers(self):
        return self.firstNumber + self.secondNumber

    def makeBinarySum(self):
        firstBinaryNumber = SumBinaryIntegers.convertIntegersToBinary(self.firstNumber)
        secondBinaryNumber = SumBinaryIntegers.convertIntegersToBinary(self.secondNumber)
        binaryNumberSum = SumBinaryIntegers.sumBinaryNumbers(self, firstBinaryNumber, secondBinaryNumber)

        SumBinaryIntegers.displayBinaryNumbers(self, firstBinaryNumber, secondBinaryNumber, binaryNumberSum)

    def sumBinaryNumbers(self, firstBinaryNumber, secondBinaryNumber):
        bits = 0
        remainingBit = 0
        binaryNumberResult = []
        remainingBits = 0

        if len(firstBinaryNumber) < len(secondBinaryNumber):
            remaining = len(secondBinaryNumber) - len(firstBinaryNumber)

            while remainingBits < remaining:
                firstBinaryNumber.append(0)
                remainingBits = remainingBits + 1
        elif len(secondBinaryNumber) < len(firstBinaryNumber):
            remaining = len(firstBinaryNumber) - len(secondBinaryNumber)

            while remainingBits < remaining:
                secondBinaryNumber.append(0)
                remainingBits = remainingBits + 1

        while bits < len(firstBinaryNumber):
            if(firstBinaryNumber[bits] == 0 and secondBinaryNumber[bits] == 0 and remainingBit == 0):
                binaryNumberResult.append(0)
            elif (firstBinaryNumber[bits] == 0 and secondBinaryNumber[bits] == 1 and remainingBit == 0):
                binaryNumberResult.append(1)
            elif (firstBinaryNumber[bits] == 1 and secondBinaryNumber[bits] == 0 and remainingBit == 0):
                binaryNumberResult.append(1)
            elif (firstBinaryNumber[bits] == 1 and secondBinaryNumber[bits] == 1 and remainingBit == 0):
                binaryNumberResult.append(0)
                remainingBit = 1
            elif (firstBinaryNumber[bits] == 0 and secondBinaryNumber[bits] == 0 and remainingBit == 1):
                binaryNumberResult.append(1)
                remainingBit = 0
            elif (firstBinaryNumber[bits] == 0 and secondBinaryNumber[bits] == 1 and remainingBit == 1):
                binaryNumberResult.append(0)
                remainingBit = 1
            elif (firstBinaryNumber[bits] == 1 and secondBinaryNumber[bits] == 0 and remainingBit == 1):
                binaryNumberResult.append(0)
                remainingBit = 1
            elif (firstBinaryNumber[bits] == 1 and secondBinaryNumber[bits] == 1 and remainingBit == 1):
                binaryNumberResult.append(1)
                remainingBit = 1

            bits = bits + 1

        if remainingBit == 1:
            binaryNumberResult.append(remainingBit)

        return binaryNumberResult

    def displayBinaryNumbers(self, firstBinaryNumber, secondBinaryNumber, binaryNumberSum):
        binaryNumber1 = ""
        binaryNumber2 = ""
        binaryNumberResult = ""

        firstBinaryNumber.reverse()
        secondBinaryNumber.reverse()
        binaryNumberSum.reverse()

        for bit in firstBinaryNumber:
            binaryNumber1 = binaryNumber1 + str(bit)

        for bit in secondBinaryNumber:
            binaryNumber2 = binaryNumber2 + str(bit)

        for bit in binaryNumberSum:
            binaryNumberResult = binaryNumberResult + str(bit)

        sum = self.firstNumber + self.secondNumber

        print("\n**************************************************Results**************************************************\n")

        print("{} in binary is {} " .format(self.firstNumber, binaryNumber1))
        print("{} in binary is {} " .format(self.secondNumber, binaryNumber2))
        print("{} in binary is {} ".format(sum, binaryNumberResult))

        print("The sum of {} + {} = {}" .format(binaryNumber1, binaryNumber2, binaryNumberResult))

        print("\n***********************************************************************************************************\n")

    def convertIntegersToBinary(decimalNumber):
        binaryNumber = []

        while decimalNumber != 1:
            remainder = decimalNumber % 2
            decimalNumber = int(decimalNumber / 2)
            binaryNumber.append(remainder)

        binaryNumber.append(decimalNumber)

        return binaryNumber

if __name__ == '__main__':
    firstNumber = int(input("Enter the first number: "))
    secondNumber = int(input("Enter the second number: "))
    sumIntegers = SumBinaryIntegers(firstNumber, secondNumber)
    binarySum = sumIntegers.makeBinarySum()

