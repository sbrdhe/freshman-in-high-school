import random

rn = random.randrange(1,101,1)
print(rn)
num = int(input("숫자를 입력해주세요 : "))

if num == rn:
    print("같은 숫자 입니다.")
else:
    print("다른 숫자입니다")
