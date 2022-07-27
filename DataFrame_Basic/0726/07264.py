# #함수 연습문제
# 주민번호를 입력하면 유효한지 유효하지 않은지 bool값으로 반환하는 함수를 정의하고 함수를 실행시켜서 결과를 출력하시오
# /*
#  * 사용자로부터 주민번호 입력 받음 : 000000-0000000 (문자열로 읽어들임)
# 		-을 제외시키고 한문자 한문자를 정수로 변환해서 int[] 에 저장 (배열의 크기는 13)
# 		주민번호 체크 :
# 		주민번호 앞에서부터 12자리의 각 자리의 수에 가중치 
# 		{ 2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5 }를 곱합니다.
# 		곱한수를 모두 더하여 총합을 구합니다.		 
# 		총합을 11로 나눈 나머지를 구합니다.
# 		그 나머지를 11에서 뺀 결과가 CHECK DIGIT 입니다.
# 		뺀 결과가 2자리수인 경우에는 2자리수를 10으로 나눈 나머지가 CHECK DIGIT가 됩니다.
# 		CHECK DIGIT의 값이 입력 숫자 스트링의 13번째 숫자와 같으면 "CORRECT", 다르면 "INCORRECT"를 출력합니다.
# 		HINT> (11-나머지)%10 또는 (11-total%11)%10
#  */

# test_int = input().split('-')
# test_jumin = [int(i) for i in test_int[0]] + [int(i) for i in test_int[1]]

# for i in range(len(test_jumin) - 1):
#     test_jumin[i] *= (2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5)[i]

# CHECK_DIGIT = 11 - ((sum(test_jumin) - test_jumin[12]) % 11)

# if CHECK_DIGIT // 10 > 0:
#     CHECK_DIGIT = CHECK_DIGIT % 10

# if CHECK_DIGIT == test_jumin[12]:
#     print("CORRECT")
# else:
#     print("INCORRECT")

# #CodeExcercise 
# 같은 숫자가 나올 때까지 주사위 6개를 동시에 무한 반복해서 던진다.
# 같은 숫자가 나올 때까지 몇 번 던졌는지, 1부터 6까지 연속된 숫자는 몇 번 나왔는지 출력하는  프로그램 코드를 작성하시오
# [Sample Run]  
# 6개 주사위가 모두 동일한 숫자가 나옴 --> 2 2 2 2 2 2
# 6개가 동일한 숫자가 나올 때까지 주사위를 던진 횟수 --> 10652
# 6개가  동일한 숫자가 나올 때까지 1 ~6의 연속번호가 나온 횟수 --> 172

import random

dice = [random.randint(1, 6) for i in range(6)]
list = []
count = 0 # 던진 횟수
serial = 0 # 각자 다른 주사위 수가 나왔을 경우

while True:
    if dice[0] != dice[1] != dice[2] != dice[3] != dice[4] != dice[5]:
        serial += 1
    if dice[0] == dice[1] == dice[2] == dice[3] == dice[4] == dice[5]:
        list.append(dice)
        break
    else:
        count += 1
        dice = [random.randint(1, 6) for i in range(6)]
print(list, count, serial)