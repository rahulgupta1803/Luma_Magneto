import time

from Pageobjects.amount_verification_page import Amount_Verification
from Pageobjects.login_page import Login
from Pageobjects.product_page import Product
from Utilities.ReadConfig import ReadConfig


class Test_Amount_Verification():
    email = ReadConfig.getUserEmail()
    password  = ReadConfig.getUserPassword()


    def test_amount_verification(self,setup):
        self.driver = setup
        self.lp = Login(self.driver)
        self.pp = Product(self.driver)
        self.avp = Amount_Verification(self.driver)
        self.lp.Click_Login()
        self.lp.Enter_Email(self.email)
        self.lp.Enter_pass(self.password)
        self.lp.Signin()
        self.pp.jacket_section()
        self.pp.Fitness_Jacket_size()
        self.pp.Fitness_Jacket_colour()
        self.pp.Fitness_Jacket_add_cart()
        self.pp.Wind_Jacket_Size()
        self.pp.Wind_Jacket_colour()
        self.pp.Wind_Jacket_add_cart()
        self.pp.CLick_Add_Cart()
        self.pp.Edit_Add_Cart()
        self.pp.Qauntity_Fitness_Jacket(5)
        self.pp.Qauntity_Wind_Jacket(4)
        self.pp.Update_Shopping_Cart()

        amount_list =[]
        time.sleep(10)

        al= self.avp.Length_Amount()
        print('amount length:', al)
        for y in range(1,al+1):
            time.sleep(3)
            b=self.avp.diff_Amount(y)
            d=b.replace("$","")
            amount_list.append(d)

        time.sleep(2)
        h=self.avp.Total_Amount()
        k = h.replace("$","")
        amount_list.append(k)
        print('amount_list',amount_list)
        subtotal=float(amount_list[0])
        print('subtotal:',subtotal)
        g = amount_list[1]
        discount = float(g.replace("-",""))
        print('discount', discount)
        shipping_rate = float(amount_list[2])
        print('shipping_rate',shipping_rate)
        my_total = subtotal-discount+shipping_rate
        print('my_total',my_total)

        site_total = round(float(amount_list[3]),1)
        print('site total', site_total)
        if my_total == site_total:
            print("total is correct")
        else:
            print('Total is wrong')









