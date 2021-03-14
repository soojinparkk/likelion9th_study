import random

mem_name = list(input('whole name:').split())           # 팀원 이름
num = len(mem_name)                                     # 팀원 전체 숫자 (운영진 제외)
manage_name = ['a', 'b', 'c', 'd']                      # 운영진 이름
team_num = len(manage_name)                             # 운영진 수
check = num // team_num + 1

for i in range(team_num):
    temp = []
    
    if (i == num % team_num):
        check -= 1

    while (len(temp) < check):
        student = random.choice(mem_name)

        if student not in temp:
            temp.append(student)
            mem_name.remove(student)

    print(manage_name.pop(random.randint(0, len(manage_name) - 1)), '팀: ',temp)