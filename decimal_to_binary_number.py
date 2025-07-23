class DecimalToBinaryConverter:
  def __init__(self):
    pass
  
  def decimal_to_binary(self,decimal):
    if not isinstance(decimal,int):
      raise TypeError("Incorrect type of decimal value")

    input_value = decimal
    list_of_reminder = []
    while input_value != 1:
      input_value,reminder = divmod(input_value,2)
      list_of_reminder.append(reminder)
    list_of_reminder.append(1)
    return list_of_reminder
      
      
  def main(self):
    user_input = input("Please inter your decimal value : ")
    if user_input and isinstance(user_input,str):
      user_input = int(user_input)
    
    decimal_value = self.decimal_to_binary(user_input)
    decimal_value.reverse()
    return print(decimal_value)
  
  
  
if __name__ == '__main__':
  initialize_class = DecimalToBinaryConverter()
  initialize_class.main()