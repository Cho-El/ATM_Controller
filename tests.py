from unittest import TestCase, main
from api import atm_controller, valid_pin
from database import db

class Mytests(TestCase):
    '''
    'rule': ['xx-xx','xxx-xxx-xx','x-xx-x'] 기본 저장된 규칙
    '''
    def test_valid_pin(self):
        # 맞는 케이스
        _testcase = ['00-19', '00-13', '111-888-21','3-44-7']
        for i in _testcase:
            self.assertTrue(valid_pin(i,db.db['rule']))

        # 틀린 케이스 
        _testcase = ['fji-21', '2999-1-2','3','a12-fk2-11','4444','x2--']
        for i in _testcase:
            self.assertFalse(valid_pin(i,db.db['rule']))
        
    def test_atm_controller_show(self):

        # 맞는 케이스
        for k in db.db['pin'].keys():
            cont = atm_controller(k,db.db)
            self.assertTrue(cont.show_accounts())

        #틀린 케이스
        ks = ['000-111','00-4444','489-48']
        for k in ks:
            cont = atm_controller(k,db.db)
            self.assertFalse(cont.show_accounts())

if __name__ == '__main__':
    main()