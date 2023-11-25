import time

from selenium.webdriver.common.by import By

from Pageobjects.login_page import Login
from Testcases.conftest import getuserdata


class Test_Parameter():

    def test_param(self,setup,getuserdata):
        self.driver = setup
        self.lp=Login(self.driver)
        self.lp.Click_Login()
        self.lp.Enter_Email(getuserdata[0])
        self.lp.Enter_pass(getuserdata[1])
        self.lp.Signin()

        time.sleep(3)
        if self.lp.Status()==True:

            self.driver.save_screenshot(f".//screenshots//successful login with param data {getuserdata[0]}, {getuserdata[1]}.png")
            assert True
        else:

            self.driver.save_screenshot(f".//screenshots//unsuccessful login with param data {getuserdata[0]}, {getuserdata[1]}.png")
            assert False



# pytest -v -s "D:\credence\Luma_Magneto_Pytest_Project\Testcases\test_login_paramater.py" --browser chrome