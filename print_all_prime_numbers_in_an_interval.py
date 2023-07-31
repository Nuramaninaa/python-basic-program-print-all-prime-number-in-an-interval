#python program to check prime number between interval

low_value = int(input("Enter the low number : "))
upper_value = int(input("Enter the upper number : "))

print ("The Prime Numbers in the range are: ")
for number in range (low_value, upper_value + 1):
  if number > 1:
     for i in range(2, number):
       if  (number % i)  == 0 :
             break

     else:
        print (number)
    