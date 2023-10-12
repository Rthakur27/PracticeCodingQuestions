def rev_number(number):
    if 999 < number < 10000:
        rev_num = 0
        original_num = number

        while number > 0:
            digit = number % 10
            rev_num = rev_num * 10 + digit
            number //= 10

        return rev_num, rev_num == original_num
    else:
        return None, False

num = int(input("Enter a four-digit number: "))

rev_num, is_palindrome = rev_number(num)

if rev_num is not None:
    print(f"Original Number: {num}")
    print(f"Reversed Number: {rev_num}")
    if is_palindrome:
        print("The number is a palindrome.")
    else:
        print("The number is not a palindrome.")
else:
    print("Please enter a valid four-digit number.")
