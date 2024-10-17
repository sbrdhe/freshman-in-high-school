# def  factorial(n):
#     output=1
#     for i in range(1,n+1):
#         output *= i

#     return output


# print(factorial(5))

def factorial(n):
    if n == 0:
        return 1
    
    else :
        return n * factorial(n-1)

print(factorial(5))