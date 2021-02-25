import unittest

from collections import namedtuple
from decimal import Decimal
from sqlalchemy.orm.session import Session as OrmSession

from exanho.core.common import Error
import exanho.orm.domain as domain

from exanho.purchbot.utils import accounts as util
from exanho.purchbot.model.account import *

from .config import db_url

SingleTestCase = namedtuple('SingleTestCase', ['initial_data', 'expected'])

class TestAccountManager(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        d = domain.Domain(db_url)
        domain.Sessional.domain = d
        cls.session = domain.Sessional.domain.Session

    def setUp(self):
        self.session:OrmSession = self.__class__.session

    def tearDown(self):
        self.session.rollback()

    @classmethod
    def tearDownClass(cls):
        cls.session.close()

    def test_get_account_name(self):

        test_set = [
            SingleTestCase(initial_data=(BalAccCode.C901, None, None), expected='901'),
            SingleTestCase(initial_data=(BalAccCode.C107, 1, None), expected='1070000000001'),
            SingleTestCase(initial_data=(BalAccCode.C301, 987, 555), expected='30100000009870000000555'),
            SingleTestCase(initial_data=(BalAccCode.C102, None, 555), expected=AssertionError)
        ]

        self.inner_test_get_account_name(test_set)
        
    def inner_test_get_account_name(self, test_set:list):
        for single_test_case in test_set:
            if type(single_test_case.expected) == type and issubclass(single_test_case.expected, Exception):
                with self.assertRaises(single_test_case.expected):
                    self.assertEqual(
                        util.get_account_name(*single_test_case.initial_data),
                        single_test_case.expected,
                        f'for case: {single_test_case.initial_data}'
                    )
            else:
                self.assertEqual(
                    util.get_account_name(*single_test_case.initial_data),
                    single_test_case.expected,
                    f'for case: {single_test_case.initial_data}'
                )

    def test_get_account(self):
        expected_bal_code = BalAccCode.C101
        expected_analitic1 = 999999
        expected_analitic2 = 888888
        expected_desc = 'account desc 555'

        expected_account_name = util.get_account_name(expected_bal_code, expected_analitic1, expected_analitic2)
        actual_acc_acount = self.session.query(AccAccount).filter(AccAccount.account == expected_account_name).one_or_none()
        self.assertIsNone(actual_acc_acount)

        actual_acc_acount = util.get_account(self.session, expected_bal_code, expected_analitic1, expected_analitic2, desc=expected_desc)
        self.assertIsNotNone(actual_acc_acount)
        self.assertEqual(actual_acc_acount.account, expected_account_name)
        self.assertEqual(actual_acc_acount.balance_code, expected_bal_code)
        self.assertEqual(actual_acc_acount.analitic1, expected_analitic1)
        self.assertEqual(actual_acc_acount.analitic2, expected_analitic2)
        self.assertEqual(actual_acc_acount.desc, expected_desc)

        actual_acc_acount = None
        actual_acc_acount = self.session.query(AccAccount).filter(AccAccount.account == expected_account_name).one_or_none()
        self.assertIsNotNone(actual_acc_acount)

    def test_get_remain(self):
        acc_acount = util.get_account(self.session, BalAccCode.C101, 777777, 666666)

        actual_remain = self.session.query(AccRemain).filter(AccRemain.account_id == acc_acount.id).one_or_none()
        self.assertIsNone(actual_remain)

        actual_remain = util.get_remain(self.session, acc_acount)
        self.assertIsNotNone(actual_remain)
        self.assertEqual(actual_remain.account, acc_acount)
        self.assertEqual(actual_remain.dt, Decimal('0'))
        self.assertEqual(actual_remain.cr, Decimal('0'))
        self.assertIsNone(actual_remain.last_payment_id)

        actual_remain = None

        actual_remain = self.session.query(AccRemain).filter(AccRemain.account_id == acc_acount.id).one_or_none()
        self.assertIsNotNone(actual_remain)

    def test_get_remain_amount(self):
        acc_acount = util.get_account(self.session, BalAccCode.C331)

        actual_remain_amount = util.get_remain_amount(self.session, acc_acount)
        self.assertEqual(actual_remain_amount, Decimal('0'))

        acc_remain = util.get_remain(self.session, acc_acount)
        acc_remain.dt = Decimal('200')
        acc_remain.cr = Decimal('175')

        actual_remain_amount = util.get_remain_amount(self.session, acc_acount)
        self.assertEqual(actual_remain_amount, Decimal('25'))

    def test_make_payment(self):
        dt_account1 = util.get_account(self.session, BalAccCode.C107, 444444, 333333)
        cr_account = util.get_account(self.session, BalAccCode.C907)

        with self.assertRaises(Error):
            util.make_payment(self.session, dt_account1, cr_account, Decimal('-1'))

        with self.assertRaises(Error):
            util.make_payment(self.session, dt_account1, cr_account, Decimal('100'))

        actual_record1 = util.make_payment(self.session, dt_account1, cr_account, Decimal('100'), True)
        self.assertEqual(actual_record1.dt, dt_account1.id)
        self.assertEqual(actual_record1.cr, cr_account.id)
        self.assertEqual(actual_record1.amount, Decimal('100'))

        self.assertEqual(util.get_remain_amount(self.session, dt_account1), Decimal('100'))
        self.assertEqual(util.get_remain(self.session, dt_account1).updated_by, actual_record1.id)
        self.assertEqual(util.get_remain_amount(self.session, cr_account), Decimal('-100'))
        self.assertEqual(util.get_remain(self.session, cr_account).updated_by, actual_record1.id)

        actual_record2 = util.make_payment(self.session, dt_account1, cr_account, Decimal('75'), True)
        self.assertEqual(actual_record2.dt, dt_account1.id)
        self.assertEqual(actual_record2.cr, cr_account.id)
        self.assertEqual(actual_record2.amount, Decimal('75'))

        self.assertEqual(util.get_remain_amount(self.session, dt_account1), Decimal('175'))
        self.assertEqual(util.get_remain(self.session, dt_account1).updated_by, actual_record2.id)
        self.assertEqual(util.get_remain_amount(self.session, cr_account), Decimal('-175'))
        self.assertEqual(util.get_remain(self.session, cr_account).updated_by, actual_record2.id)

        dt_account2 = util.get_account(self.session, BalAccCode.C107, 222222, 111111)

        actual_record3 = util.make_payment(self.session, dt_account2, cr_account, Decimal('125'), True)
        self.assertEqual(actual_record3.dt, dt_account2.id)
        self.assertEqual(actual_record3.cr, cr_account.id)
        self.assertEqual(actual_record3.amount, Decimal('125'))

        self.assertEqual(util.get_remain_amount(self.session, dt_account1), Decimal('175'))
        self.assertEqual(util.get_remain(self.session, dt_account1).updated_by, actual_record2.id)
        self.assertEqual(util.get_remain_amount(self.session, dt_account2), Decimal('125'))
        self.assertEqual(util.get_remain(self.session, dt_account2).updated_by, actual_record3.id)
        self.assertEqual(util.get_remain_amount(self.session, cr_account), Decimal('-300'))
        self.assertEqual(util.get_remain(self.session, cr_account).updated_by, actual_record3.id)

        dt_account3 = util.get_account(self.session, BalAccCode.C107)

        actual_record4 = util.make_payment(self.session, dt_account3, dt_account2, Decimal('49.5'))
        self.assertEqual(actual_record4.dt, dt_account3.id)
        self.assertEqual(actual_record4.cr, dt_account2.id)
        self.assertEqual(actual_record4.amount, Decimal('49.5'))

        self.assertEqual(util.get_remain_amount(self.session, dt_account1), Decimal('175'))
        self.assertEqual(util.get_remain(self.session, dt_account1).updated_by, actual_record2.id)
        self.assertEqual(util.get_remain_amount(self.session, dt_account2), Decimal('75.5'))
        self.assertEqual(util.get_remain(self.session, dt_account2).updated_by, actual_record4.id)
        self.assertEqual(util.get_remain_amount(self.session, dt_account3), Decimal('49.5'))
        self.assertEqual(util.get_remain(self.session, dt_account3).updated_by, actual_record4.id)
        self.assertEqual(util.get_remain_amount(self.session, cr_account), Decimal('-300'))
        self.assertEqual(util.get_remain(self.session, cr_account).updated_by, actual_record3.id)

        actual_record5 = util.make_payment(self.session, cr_account, dt_account3, Decimal('49.5'))
        self.assertEqual(actual_record5.dt, cr_account.id)
        self.assertEqual(actual_record5.cr, dt_account3.id)
        self.assertEqual(actual_record5.amount, Decimal('49.5'))

        self.assertEqual(util.get_remain_amount(self.session, dt_account1), Decimal('175'))
        self.assertEqual(util.get_remain(self.session, dt_account1).updated_by, actual_record2.id)
        self.assertEqual(util.get_remain_amount(self.session, dt_account2), Decimal('75.5'))
        self.assertEqual(util.get_remain(self.session, dt_account2).updated_by, actual_record4.id)
        self.assertEqual(util.get_remain_amount(self.session, dt_account3), Decimal('0'))
        self.assertEqual(util.get_remain(self.session, dt_account3).updated_by, actual_record5.id)
        self.assertEqual(util.get_remain_amount(self.session, cr_account), Decimal('-250.5'))
        self.assertEqual(util.get_remain(self.session, cr_account).updated_by, actual_record5.id)