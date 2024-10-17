# def fact(n): #함수명 fact / 입력값 n
#     # 0을 곱하면 답은 0 = 출력되지 않아야함
#     if n == 0:
#         return 1
#     else:
#         return n * fact(n-1) # 5! = 5x4x3x2x1
    
# print(fact(5))//

# counter = 0

# def fibo(n):
#     print("fibo{}".format(n))
#     global counter
#     counter+=1
#     if n == 1:
#         return 1
#     if n == 2:
#         return 1
#     else:
#         return fibo(n-1) + fibo(n-2)
# fibo(10)
# print("------------------------")
# print("fibo count is {}.".format(counter))

def flatten(data):
    out = []
    for item in data:
        if type(item) == list:
            out = out + flatten(item)
        else:
            out.append(item)
    return out



example = [[1,2,3], [4,[5,6],7,[8,9]]]
print("원본:",example)
print("변환:", flatten(example))