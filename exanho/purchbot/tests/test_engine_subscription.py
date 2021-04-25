import datetime
import unittest

from collections import namedtuple
from decimal import Decimal
from sqlalchemy.orm.session import Session as OrmSession

from exanho.core.common import Error
import exanho.orm.domain as domain

from exanho.purchbot.utils import subscription as sub_eng
from exanho.purchbot.model import Client, ProductKind, Product, OrderStatus, Order, EventSubscription

from .config import db_url

SingleTestCase = namedtuple('SingleTestCase', ['initial_data', 'expected'])

class TestSubscriptionEngine(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        d = domain.Domain(db_url)
        domain.Sessional.domain = d
        cls.session = domain.Sessional.domain.Session
        cls.client = Client()
        cls.product = Product(
            kind = ProductKind.SUBSCRIPTION,
            code = 'Prdt',
            name = 'sub product'
        )
        cls.order1 = Order(
            status = OrderStatus.DURING,
            client = cls.client,
            product = cls.product,
            amount = 5.0
        )
        cls.order2 = Order(
            status = OrderStatus.DURING,
            client = cls.client,
            product = cls.product,
            amount = 5.0
        )
        cls.session.add_all([cls.order1, cls.order2])

    def setUp(self):
        self.session:OrmSession = self.__class__.session
        self.order1 = self.__class__.order1

    def tearDown(self):
        self.session.rollback()

    @classmethod
    def tearDownClass(cls):
        cls.session.close()

    def test_find_and_deactivate(self):
        sub1 = EventSubscription(
            last_date = datetime.date.today() - datetime.timedelta(days=1),
            order = self.order1,
            active = True
        )
        sub2 = EventSubscription(
            last_date = datetime.date.today(),
            order = self.order2,
            active = True
        )
        self.session.add_all([sub1, sub2])
        self.session.flush()

        self.assertTrue(sub1.active)
        self.assertTrue(sub2.active)
        
        sub_eng.find_and_deactivate(self.session, datetime.date.today() - datetime.timedelta(days=1))
        self.session.refresh(sub1)
        self.session.refresh(sub2)

        self.assertTrue(sub1.active)
        self.assertTrue(sub2.active)
        
        sub_eng.find_and_deactivate(self.session)
        self.session.refresh(sub1)
        self.session.refresh(sub2)

        self.assertFalse(sub1.active)
        self.assertTrue(sub2.active)