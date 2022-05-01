# **ATM_Controller**

알로카토스 백엔드 과제

---

# 실행 방법

---

[main.py](http://main.py)파일에서 실행 후 쉘창에 입력하여 사용

```powershell
검증을 위한 Rule을 정의하고 싶으시면 1,
핀 번호를 입력하시려면 0,
pin번호를 입력해주세요 : 00-11
연결된 계정은 : syz yzw xyu 입니다.
syz 's Balance: 40

입금을 원하시면 1, 출금을 원하시면 0, 둘다 원하지 않으시면 -1를 입력해주세요 : 0     
얼마를 출금하시겠습니까? 10
남은 잔고는 : 30
```

# DB 조건 및 기본 데이터 추가

---

[database.py](http://database.py) 파일의 db class 딕셔너리 형태로 되어 있다.

```jsx
class db:
    db = {
        'rule': ['xx-xx','xxx-xxx-xx','x-xx-x'], # 검증을 위한 규칙
        'pin': {
            '00-11' : {
                'syz':40,
                'yzw':80,
                'xyu':90
            },
            '00-112-33' : {
                'abc':50,
                'def':80,
                'ghi':50
            },
            '00-111-22' : {
                'sdz':40,
                'yww':50,
                'xzu':90
            },
            '00-11-2' : {
                'sdz':20,
                'yww':30,
                'xzu':40
            }
        }
    }
```

데이터 추가를 원할 시 이곳에 추가

# 데이터 테스트

---

[tests.py](http://test.py) 파일에서 실행

False와 True를 반환하는 pin을 검증하는 valid_pin함수와 atm_controller의 pin번호와 연관된 계정이 있는지를 확인하는 show_accounts()함수를 테스트 해보았다.

```powershell
연결된 계정은 : syz yzw xyu 입니다.
연결된 계정은 : abc def ghi 입니다.
연결된 계정은 : sdz yww xzu 입니다.
연결된 계정은 : sdz yww xzu 입니다.
..
----------------------------------------------------------------------
Ran 2 tests in 0.001s

OK
```
