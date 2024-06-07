def superDigit(n, k):
    # Write your code here
    def super_digits(num):
        if num > 9:
            return super_digits(num % 10 + super_digits(num//10))
        return num
    
    initial_sum = 0
    for digit in n:
        initial_sum += int(digit)
        
    n = super_digits(initial_sum)
    k = super_digits(k)
    return super_digits(n*k)
