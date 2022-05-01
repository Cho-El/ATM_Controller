def valid_pin(pin_num, rules):

    pin_num_l = list(pin_num.split('-')) # -을 빼고 나눠서 리스트로 삽입
    # -을 제외한 문자들이 모두 숫자로 이루어져 있는지 확인
    for string in pin_num_l: # 숫자가 아닌경우 result를 false로 반환
        if string.isdigit():
            continue
        else:
            return False #
            
    
    # -를 기준으로 나눈 구간의 갯수가 같은지 확인
    for rule in rules:
        if len(rule) != len(pin_num): # 길이가 서로 다르다면
            continue
        rule_l = list(rule.split('-'))
        
        for string in zip(pin_num_l, rule_l):
            if len(string[0]) != len(string[1]): # 길이가 다른게 존재하다면 해당 string과는 형식이 다름 다음거 순회
                break
        else: # 다 돌았는데 break문이 없었다면 해당 pin과 같은 형식을 찾음
            result = True # 길이가 다른 것이 없다면 유효하므로 True
            break

    else: # 규칙들을 다 확인해 보았는데 True가 나오지 않았었다면 result = False
        result = False
    
    return result


class atm_controller():
    def __init__(self, pin_num: str, db: dict):
        self.pin_num = pin_num
        self.db = db

    def show_accounts(self) -> bool:
        if self.pin_num in self.db['pin']:
            accounts = ' '.join(self.db['pin'][self.pin_num].keys())
            print(f'연결된 계정은 : {accounts} 입니다.')
            return True
        else:
            return False

    def get_balance(self, account) -> 'balance':
        return self.db['pin'][self.pin_num][account]

    def deposit(self, account) -> 'balance': # 입금
        money = int(input('얼마를 입금하시겠습니까? '))
        self.db['pin'][self.pin_num][account] += money
        return self.db['pin'][self.pin_num][account]

    def withdrawal(self,account) -> 'balance': # 출금
        money = int(input('얼마를 출금하시겠습니까? '))
        self.db['pin'][self.pin_num][account] -= money
        return self.db['pin'][self.pin_num][account]

    @staticmethod
    def selected_account() -> 'User_account': # 계정 선택
        select_ac = input('잔고를 확인하실 계정을 입력해주세요 : ')
        return select_ac