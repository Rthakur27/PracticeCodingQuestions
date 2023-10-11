num = int(input("Enter a three-digit number: "))

if 100 <= num <= 999:
    d1 = num / 100 
    d2 = (num / 10) % 10 
    d3 = num % 10 

    d_sum = d1 + d2 + d3

    print("The sum of the digits is:", d_sum)
else:
    print("Please enter a valid three-digit number.")
