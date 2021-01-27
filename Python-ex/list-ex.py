# 리스트 내장함수

li = [0, 1, "like", 3, "lion", 0]
li2 = [8, 6, 0, 3, 5]

# 1. 리스트 길이
# : len(리스트 변수)

print(len(li))

# 2. 리스트 원소 오름차순 정렬 -> 리스트 반환X
# : 리스트 변수.sort()

li2.sort()
print(li2)

# 3. 리스트 내 특정 원소의 인덱스 찾기
# : 리스트 변수.index(특정 원소)

print(li.index(1))

# 4. 리스트 내 특정 원소 등장 횟수
# : 리스트 변수.count(특정 원소)

print(li.count('like'))