# **ATM_Controller**

알로카토스 백엔드 과제

---

# 실행 방법

---

[main.py](http://main.py)파일에서 실행 후 쉘창에 입력하여 사용

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/3909aeb2-1108-4ff6-82e9-e19534fcff56/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/774e2bfc-704d-4945-a134-06c1e539016c/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/acb5bd8c-fe9b-409d-b487-646277123595/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/301120c9-b2d2-498b-9495-4ddd4f4e5452/Untitled.png)

# DB 조건 및 기본 데이터 추가

---

[database.py](http://database.py) 파일의 db class 딕셔너리 형태로 되어 있다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/520f6b4c-b6eb-408f-a647-8b2da505aabf/Untitled.png)

데이터 추가를 원할 시 이곳에 추가

# 데이터 테스트

---

[tests.py](http://test.py) 파일에서 실행

False와 True를 반환하는 pin을 검증하는 valid_pin함수와 atm_controller의 pin번호와 연관된 계정이 있는지를 확인하는 show_accounts()함수를 테스트 해보았다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b8b8177b-de6a-4b5d-b7ae-f6aa841b4b03/Untitled.png)
