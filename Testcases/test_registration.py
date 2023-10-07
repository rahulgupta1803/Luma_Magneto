import time

from Pageobjects.create_account_page import Create_Account
from Utilities.ReadConfig import ReadConfig
from Utilities.loggen import LogGenerator


class Test_Registration():
    log=LogGenerator().loggen()
    user_mail = ReadConfig.getUserEmail()
    user_password = ReadConfig.getUserPassword()

    def test_registration(self,setup):
        self.driver=setup
        self.log.info("open Browser")
        self.cap = Create_Account(self.driver)
        self.cap.Click_Create_Account()
        self.log.info("Click on create Account")
        self.cap.Enter_First_Name('Rahul')
        self.log.info("Enter first_name")
        self.cap.Enter_Last_Name('Gupta')
        self.log.info("Enter last_name")
        self.cap.Enter_Emailid(self.user_mail)
        self.log.info("Enter email id")
        self.cap.Enter_Password(self.user_password)
        self.log.info("Enter Password")
        self.cap.Enter_Confirm_Password(self.user_password)
        self.log.info("Enter confirm_password")
        self.cap.Click_Create_Button()
        self.log.info("Click create account")
        time.sleep(2)
        if self.cap.Status()==True:
            time.sleep(1)
            self.driver.save_screenshot(".//screenshots//reg_successful.png")
            self.log.info("taking screenshot")
            time.sleep(1)
            print(self.cap.Print_Succ_Mess())
            self.log.info("print successful_message")
            self.cap.LogOut()
            self.log.info("click logout\n")
            assert True
        else:
            time.sleep(1)
            self.driver.save_screenshot(".//screenshots//reg_failed.png")
            self.log.info("taking screenshot")
            time.sleep(2)
            print(self.cap.Print_Fail_Mess())
            self.log.info("print failed_message\n")
            assert False


# pytest -v -s "D:\credence\Luma_Magneto_Pytest_Project\Testcases\test_registration.py" --browser chrome
