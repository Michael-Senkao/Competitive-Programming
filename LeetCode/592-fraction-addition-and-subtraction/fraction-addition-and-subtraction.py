class Solution:
    def fractionAddition(self, expression: str) -> str:
        def evaluate(n1, d1, n2, d2):
            num1,num2,denum1,denum2 = int(n1), int(n2), int(d1), int(d2)
            if denum1 == denum2:
                return (str(num1 + num2), str(denum1))
            return (str((num1*denum2) + (num2*denum1)), str(denum1*denum2))

        def findGCD(num1, num2):
            if num2 == 0:
                return num1
            return findGCD(num2, num1 % num2)

        start = 0
        n,d = 0,1

        if expression[0] != "-":
            expression = "+" + expression
    
        while start < len(expression):
            n2 = expression[start: start + 2]
            if expression[start + 2] != "/":
                n2 += expression[start + 2]
                start += 1
            d2 = expression[start + 3]
            if start + 4 < len(expression) and expression[start+4].isnumeric():
                d2 += expression[start + 4]
                start += 1
            n,d = evaluate(n, d, n2, d2)

            start += 4

        if n == "0":
            return "0/1"

        num = int(n)
        denum = int(d)
        gcd = findGCD(abs(num), denum)
        return str(num//gcd) + "/" + str(denum//gcd)
        