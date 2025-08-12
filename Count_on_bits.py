class BitwiseOperations:
    @staticmethod
    def CountOnBits(number):
        result = 0
        if not isinstance(number,int):
            return "Please enter integer number"
        while number != 0: 
            if number & 1 == 1:
                result += 1
            number = number >> 1
        return result
    

if __name__ == "__main__":
    input_number = int(input("Please enter your number : "))
    count_no_of_on_bits = BitwiseOperations.CountOnBits(input_number)
    print(count_no_of_on_bits)
