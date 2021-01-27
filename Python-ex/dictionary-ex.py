# 딕셔너리 내장함수

paris = {"fruit": "apple", "number": "5"}

# 하나의 ket-value 쌍을 추가하는 방법
# : 딕셔너리 변수[key] = value

paris["animal"] = "tiger"
print(paris)

# 특정 key-value 삭제하는 방법
# : del 딕셔너리 변수[key]
# 리스트, 튜플에서도 사용됨

del paris["number"]
print(paris)

# key로 value를 얻는 방법
# : 딕셔너리 변수.get(key)

print(paris.get("fruit"))