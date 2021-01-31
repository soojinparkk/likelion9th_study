# 제어문 - 분기문
# if (조건) :

num = int(input("score 입력: "))

if (num >= 80) :
    print(num, "점 PASS")
elif (num >= 60) :
    print(num, "점 FAIL")
else :
    print(num, "점 RETRY")


str = input("동아리 이름: ")

if (str == "likelion") :
    print("YES")
else :
    print("NO")