# tuple_A = (1,2,3)
# print(tuple_A[0])

# (a,b) = (1,2)
# print(b)

# def call(func):
#     for i in range(10):
#         func()

# def hello():
#     print("안녕")

# call(hello)

# numbers = [1,2,3,4,5,6]
# print("::".join(map(str,numbers)))

numbers = list(range(1, 10+1))

print("# 홀수만 출력")
print(list(filter(lambda x: x % 2 == 1,numbers)))
print()

print("# 3이상, 7미만 출력")
print(list(filter(lambda x: 3 <= x < 7,numbers)))
print()

print("# 제곱해서 50미만 추출")
print(list(filter(lambda x: x**2 < 50,numbers)))