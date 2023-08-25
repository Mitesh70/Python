def reverse_number(num):
    rev = 0
    original_num = num
    
    while num > 0:
        digit = num % 10
        rev = (rev * 10) + digit
        num = num // 10
    
    return rev, rev == original_num

num = int(input("Enter a number: "))
reversed_num, is_palindrome = reverse_number(num)

print(f"Reverse of {num} is {reversed_num}")
if is_palindrome:
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")
