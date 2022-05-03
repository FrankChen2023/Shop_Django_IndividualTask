from django.test import Client, TestCase
from django.urls import reverse

#Create your tests here.


class IndividualTaskTest(TestCase):

    # 01. Test the index page.
    def test_index_text(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Welcome to Amazing Shopping created by Frank Chen")

    # 02. Test the login page.
    def test_login_text(self):
        client = Client()
        response = client.get('/log_in/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "User Login Page")

    # 03. Test the registration page.
    def test_register_text(self):
        client = Client()
        response = client.get('/sign_up/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "User Registration")
    
    # 04. Test the log out page.
    def test_logout_text(self):
        client = Client()
        response = client.get('/log_out/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "You have logged out! You will return to home page automatically in 3 seconds.")

    # 05. Test the product search page.
    def test_product_search_text(self):
        client = Client()
        response = client.get('/product_search/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Product search")
    
    # 06. Test the basket add page.
    def test_basket_add_text(self):
        client = Client()
        response = client.get('/basket_add/' )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Please modify the details of your new basket:")
    
    # 07. Test the basket delete page.
    def test_basket_delete_text(self):
        client = Client()
        response = client.get('/basket_delete/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Basket delete")
        self.assertContains(response, "Username:")
    
    # 08. Test the basket detail page.
    def test_basket_detail_text(self):
        client = Client()
        response = client.get('/basket_detail/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Basket detail")
        self.assertContains(response, "Username:")
    

    # 09. Test the basket edit page.
    def test_basket_edit_text(self):
        client = Client()
        response = client.get('/basket_edit/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Basket detail edit")
        self.assertContains(response, "Please check and modify the basket details:")
        self.assertContains(response, "Click delete to remove this basket with all items in it.")

    # 10. Test the basket payment page.
    def test_basket_payment_text(self):
        client = Client()
        response = client.get('/basket_payment/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Basket payment")
        self.assertContains(response, "Please check your order:")
        self.assertContains(response, "Your account balance:")
    
    # 11. Test the customer balance page.
    def test_customer_balance_text(self):
        client = Client()
        response = client.get('/customer_balance/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Balance & Baskets")
        self.assertContains(response, "Your available balance:")
        self.assertContains(response, "Your have no current basket.")

    # 12. Test the item add page.
    def test_item_add_text(self):
        client = Client()
        response = client.get('/item_add/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Product list")
        self.assertContains(response, "Search:")
        self.assertContains(response, "Result: Click item name to pick your target into your basket!")

    # 13. Test the item delete page.
    def test_item_delete_text(self):
        client = Client()
        response = client.get('/item_delete/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Success! The item has been removed from your basket.")

    # 14. Test the item detail page.
    def test_item_detail_text(self):
        client = Client()
        response = client.get('/item_detail/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Item detail")

    # 15. Test the item edit page.
    def test_item_edit_text(self):
        client = Client()
        response = client.get('/item_edit/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Basket item edit")
        self.assertContains(response, "Please check your orders:")

    # 16. Test the admin console page.
    def test_admin_console_text(self):
        client = Client()
        response = client.get('/admin_console/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Admin Console")
        self.assertContains(response, "This is administrator console page, where allows you to check all tables.")
        self.assertContains(response, "*A accurate search function offered.")


        
        
