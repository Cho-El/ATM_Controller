import sys
from database import db
from models import Pin_Rule
from api import atm_controller, valid_pin
if __name__ == '__main__':
    Cash_bin = db # db연동
    while True:
        # 하실 일이 무엇인지 확인
        want_to_do = int(input('검증을 위한 Rule을 정의하고 싶으시면 1,\n핀 번호를 입력하시려면 0, \n끝내시려면 -1을 입력해주세요 : '))
        
        # 프로그램 종료
        if want_to_do == -1:
            break

        # 검증을 위한 Rule 입력
        elif want_to_do == 1:
            input_rule = input('x와 -로만 이루어진 Rule를 입력해주세요 ex) xx-xx : \n')
            Cash_bin.db['rule'].append(input_rule) # db에 저장
            print(Cash_bin.db['rule'])

        # 핀 번호 입력하기
        elif want_to_do == 0:
            input_pin = input('pin번호를 입력해주세요 : ')
            
            if valid_pin(input_pin,Cash_bin.db['rule']): # pin이 유효한 경우 다음 단계로
                account = atm_controller(input_pin,Cash_bin.db)
                if account.show_accounts(): # db에 존재하는 경우 계정
                    selected = account.selected_account() # 계정 선택
                    print("%s 's Balance: %s \n" % (selected, account.get_balance(selected)))
                    check = int(input('입금을 원하시면 1, 출금을 원하시면 0, 둘다 원하지 않으시면 -1를 입력해주세요 : '))
                    if check == 1:
                        print('남은 잔고는 :', account.deposit(selected))
                    elif check == 0:
                        print('남은 잔고는 :', account.withdrawal(selected))


                else: # db에 존재하지 않는 경우
                    print('해당 핀번호가 존재하지 않습니다.\n')
            else:
                print('핀번호가 올바르지 않습니다.\n')
        else:
            print('잘못된 입력입니다. 다시 입력해주세요.\n')