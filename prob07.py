# 키보드에서 5개의 정수를 입력 받아 리스트에 저장하고 평균을 구하는 프로그램을 작성하시오
a=[]
for i in range(0, 5):
    a.append(int(input('>')))
sum_list = 0
count = 0
for i in a :
    sum_list = sum_list + i
    count = count + 1

print('평균 :', sum_list/count)
