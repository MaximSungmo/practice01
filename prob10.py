# 숫자를 입력 받아서 아래와 같은 실행결과가 나타나도록 코드를 완성하세요.
flag=True
while(flag):
    number = input('숫자를 입력하세요 :')
    result = 0
    if number.isdigit() :
        number = int(number)
        if number % 2 == 0:
            for i in range(0, number+1, 2):
                result = result + i
        else :
            for i in range(1, number+1, 2):
                result = result + i
        print('결과 값 : ', result)
    else :
        if number == 'exit':
            flag=False
            print('종료 되었습니다.')




