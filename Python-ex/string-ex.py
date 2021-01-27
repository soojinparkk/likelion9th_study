# 문자열 내장함수

str = "likelion study"

# 1. 문자열 길이
# : len(문자열 변수)

print(len(str))

# 2. 문자열 내 특정 문자의 등장 횟수
# : 문자열 변수.count(특정 문자)

print(str.count('l'))

# 3. 문자열을 특정 기준으로 나누기
# : 문자열 변수.split()
# 값을 넣지 않을 경우 공백 문자로 간주

print(str.split('l'))

# 4. 특정 문자의 인덱스 찾기
# : 문자열 변수.find(문자) or index(문자)
# 찾고자 하는 문자가 없을 경우 차이가 있음

print(str.find('q'))    # -1 출력
print(str.index('q'))   # error