# user_input_a = input("정수 입력> ")

# if user_input_a.isdigit():

#     number_input_a = int(user_input_a)

#     print("원의 반지름:", number_input_a)
#     print("원의 둘레:", 2 * 3.14 * number_input_a)
#     print("원의 넓이:", 3.14 * number_input_a * number_input_a)
# else:
#     print("정수를 입력하지 않았습니다")

# try:

#     number_input_a = int(input("정수 입력> "))
    
#     print("원의 반지름:", number_input_a)
#     print("원의 둘레:", 2 * 3.14 * number_input_a)
#     print("원의 넓이:", 3.14 * number_input_a * number_input_a)
# except:
#     print("무언가 잘못되었습니다")

list_input_a = ["82","273","15","문자","57"]

list_number = []
for item in list_input_a:

    try:
        float(item)
        list_number.append(item)
    except:
        pass

print("{} 내부에 있는 숫자는".format(list_input_a))
print("{}입니다.".format(list_number))

