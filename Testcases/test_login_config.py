import time

from Pageobjects.login_page import Login
from Utilities.ReadConfig import ReadConfig


class Test_Login_Config():
    email = ReadConfig.getUserEmail()
    password = ReadConfig.getUserPassword()

    def test_login_config(self,setup):
        self.driver = setup
        self.lp = Login(self.driver)
        self.lp.Click_Login()
        self.lp.Enter_Email(self.email)
        self.lp.Enter_pass(self.password)
        self.lp.Signin()
        time.sleep(2)
        if self.lp.Status()==True:
            self.driver.save_screenshot(".//screenshots//success_login_config.png")
            self.lp.Logout()
            assert True

        else:
            self.driver.save_screenshot(".//screenshots//Failed_login_config.png")
            assert False

        # pytest -v -s --browser chrome "D:\credence\Luma_Magneto_Pytest_Project\Testcases\test_login_config.py"