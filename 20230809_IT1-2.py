# def print_n_times(value,n):
#     for i in range(n):
#         print(value)

# value = input("값 : ")
# n = int(input("값 :  "))

# print_n_times(value,n)

# def print_n_times(n, *values):
#     for i in range(n):
#         for value in values:
#             print(value)
#         print(" ")
# printoutput = output * valu
# etu
# return outputt"안녕","하세요","
# 
#   굿나잇")

# def print_n_times(value,n=2):
#     for i in range(n):
#         print(value)

# print_n_times("ㅎㅇ")

# while True:
#     print(".",end="")

# def test(a,b=10,c=100):
#     print(a+b+c)

# test(10,c=300)

# def return_test():
#     print("A")
#     return
#     print("B")

# return_test()

def mul(*values):
   output = 1
   for value in values:
      output = output * value
      
   return output
print(mul(5, 7, 9, 10)) 