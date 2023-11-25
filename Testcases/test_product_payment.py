import time

from Pageobjects.login_page import Login
from Pageobjects.product_page import Product
from Utilities.ReadConfig import ReadConfig
from Utilities.loggen import LogGenerator


class Test_product_payment():
    user_email = ReadConfig.getUserEmail()
    user_password = ReadConfig.getUserPassword()
    log = LogGenerator.loggen()

    def test_product(self, setup):
        self.driver = setup
        self.log.info('Open the browser')
        self.lp = Login(self.driver)
        self.lp.Click_Login()
        self.log.info('Click login')
        self.pp = Product(self.driver)
        self.lp.Enter_Email(self.user_email)
        self.log.info('Enter Email')
        self.lp.Enter_pass(self.user_password)
        self.log.info('Enter Password')
        self.lp.Signin()
        self.log.info('Click Signin')

        self.pp.jacket_section()
        self.log.info('Enter in Jacket Section')

        self.pp.Fitness_Jacket_size()
        self.log.info('Select Fitness Jacket size')

        self.pp.Fitness_Jacket_colour()
        self.log.info('Select Fitness Jacket Color')

        self.pp.Fitness_Jacket_add_cart()
        self.log.info('Add Fitness Jacket to Cart')

        self.pp.Wind_Jacket_Size()
        self.log.info('Select Wind Jacket size')

        self.pp.Wind_Jacket_colour()
        self.log.info('Select Wind Jacket color')

        self.pp.Wind_Jacket_add_cart()
        self.log.info('Add Wind Jacket to Cart')
        time.sleep(2)
        self.pp.CLick_Add_Cart()
        self.log.info('Click add to cart')

        self.pp.Edit_Add_Cart()
        self.log.info('Click on Edit cart')

        self.pp.Qauntity_Fitness_Jacket(5)
        self.log.info('Change quantity of Fitness Jacket')

        self.pp.Qauntity_Wind_Jacket(4)
        self.log.info('Change quantity of wind Jacket size')

        self.pp.Update_Shopping_Cart()
        self.log.info('Click on Update shopping cart')
        time.sleep(3)
        self.pp.Proceed_Checkout()
        self.log.info('Click on Proceed checkout')

        if self.pp.New_Adress_status()==False:
            self.pp.Enter_Company_name('home')
            self.log.info('Enter company name')

            self.pp.Enter_Street_Address('HD-169, Kabir Nagar')
            self.log.info('Enter Street Address')

            self.pp.Enter_City('Raipur')
            self.log.info('Enter City')

            self.pp.Select_Country('India')
            self.log.info('Enter Country')

            self.pp.Select_State('Chhattisgarh')
            self.log.info('Enter State')

            self.pp.Enter_Zip('492099')
            self.log.info('Enter Zip')

            self.pp.Enter_Phone('9549652147')
            self.log.info('Enter Phone number')

        else:
            time.sleep(2)
            self.pp.New_Adress()
            self.log.info('Click on New address')

            self.pp.Enter_Company_name_popup('home')
            self.log.info('Enter company name')

            self.pp.Enter_Street_Address_popup('HD-169, Kabir Nagar')
            self.log.info('Enter Street Address')

            self.pp.Enter_City_popup('Raipur')
            self.log.info('Enter City')

            self.pp.Select_Country_popup('India')
            self.log.info('Enter Country')

            self.pp.Select_State_popup('Chhattisgarh')
            self.log.info('Enter State')

            self.pp.Enter_Zip_popup('492099')
            self.log.info('Enter Zip')

            self.pp.Enter_Phone_popup('9549652147')
            self.log.info('Enter Phone number')

            self.pp.Unsave_Address()
            self.log.info('Uncheck save address')

            self.pp.Ship_Here()
            self.log.info('Click on Ship Here')
        time.sleep(5)
        self.pp.Shipping_method()
        self.log.info('Click on  Shipping method')

        self.pp.Click_Next()
        self.log.info('Click on next')

        self.pp.Place_order()
        self.log.info('Click on Place Order')


        if self.pp.status()==True:
            print("Order is Confirmed")
            self.pp.Message()
            self.log.info('Print confirmation message')

            self.pp.Order_number()
            self.log.info('Print Order number')

            self.pp.Click_Menu()
            self.log.info('Click on menu')

            self.pp.Click_SignOut()
            self.log.info('Click on Signout')
            assert True
        else:
            print('Order is not confirmed')
            self.log.info('Order is failed')
            self.pp.Click_Menu()
            self.log.info('Click on menu')

            self.pp.Click_SignOut()
            self.log.info('Click on Signout')
            assert False



# pytest -v -s "D:\credence\Luma_Magneto_Pytest_Project\Testcases\test_product_payment.py" --browser chrome










