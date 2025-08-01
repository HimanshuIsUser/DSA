class BitCalculationEvenOrOdd:
    def __init__(self):
        pass

    @staticmethod
    def is_even(number):
        if isinstance(number,int):
            if number & 1 == 0:
                return True
            else:
                return False
        else:
            raise ValueError("Input must be an integer")


if __name__ == "__main__":
   print(BitCalculationEvenOrOdd.is_even(int(input("Plese enter a number to check wheather its a even or odd : "))))