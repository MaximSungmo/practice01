# 주어진 리스트 데이터를 이용하여 3의 배수의 개수와 배수의 합을 구하여 출력형태와 같이 출력하세요.

given_list = [ 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]

count = 0
sum_list = 0
for i in given_list:
    if i % 3 == 0 :
        count = count + 1
        sum_list = sum_list + i

print('주어진 리스트에서 3의 배수의 개수 =>', count)
print('주어진 리스트에서 3의 배수의 합 =>', sum_list)