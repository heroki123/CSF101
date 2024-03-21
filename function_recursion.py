def sum_of_digits(n):
    if n < 10:         #if n is a single-digit or less than 10 , return n
        return n
    
    else:              #recursive case: calculate the sum od digits
        last_digit = n % 10       #Get the last digits of n
        remaining_digits = n // 10      #get the remaining digits by integer divide

        return last_digit + sum_of_digits(remaining_digits)

print(sum_of_digits(123))