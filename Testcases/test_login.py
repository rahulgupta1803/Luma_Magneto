import time

from Pageobjects.login_page import Login


class Test_Login():


    def test_login(self,setup):
        self.driver=setup
        self.lp = Login(self.driver)
        self.lp.Click_Login()
        self.lp.Enter_Email('rahuls@xesta.com')
        self.lp.Enter_pass('Rahul1234..')
        self.lp.Signin()
        time.sleep(2)
        if self.lp.Status()==True:
            self.driver.save_screenshot(".//screenshots//success_login.png")
            self.lp.Logout()
            assert True

        else:
            self.driver.save_screenshot(".//screenshots//Failed_login.png")
            assert False


# pytest -v -s --browser chrome "D:\credence\Luma_Magneto_Pytest_Project\Testcases\test_login.py"

