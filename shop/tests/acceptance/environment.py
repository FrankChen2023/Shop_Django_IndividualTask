import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SampleDemo.settings')
django.setup()

from behave import fixture, use_fixture
from django.contrib.auth.models import User
from django.test.runner import DiscoverRunner
from django.test.testcases import LiveServerTestCase
from shop.models import Customer, Product, Basket, Basket_Detail


class BaseTestCase(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        User.objects.create_superuser(username='admin001', password='qwer1234', email='123@123.com')

        User.objects.create(username='Frank.C', password='123', email='123@123.com', is_staff=False)
        Product.objects.create(name="Apple", type="Food", amonut="99", price="1.99")
        super(BaseTestCase, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        User.objects.filter().delete()
        super(BaseTestCase, cls).tearDownClass()


@fixture
def django_test_case(context):
    context.test_case = BaseTestCase
    context.test_case.setUpClass()
    yield
    context.test_case.tearDownClass()
    context.selenium.quit()
    del context.test_case


def before_all(context):
    django.setup()
    context.test_runner = DiscoverRunner()
    context.test_runner.setup_test_environment()
    context.old_db_config = context.test_runner.setup_databases()
    yield
    context.test_runner.teardown_databases(context.old_db_config)
    context.test_runner.teardown_test_environment()


def before_scenario(context, scenario):
    use_fixture(django_test_case, context)
