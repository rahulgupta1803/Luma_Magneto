import time

from Pageobjects.login_page import Login
from Utilities.loggen import LogGenerator
from Utilities.xlutilis import RowCount, ReadData, WriteData


class Test_Login_ddt():
    fpath = 'D:\\credence\\Luma_Magneto_Pytest_Project\\excel file\\ddt excel.xlsx'
    log = LogGenerator.loggen()


    def test_logn_ddt(self,setup):
        self.driver = setup
        self.log.info ('Opening browser')
        self.lp = Login(self.driver)
        self.rl = RowCount(self.fpath, 'Sheet1')
        print(self.rl)
        list = []
        for x in range (2,self.rl+1):
            email = ReadData (self.fpath, 'Sheet1',x,2)
            password = ReadData(self.fpath,'Sheet1',x,3)
            exp_results = ReadData (self.fpath,"Sheet1",x, 4)
            self.lp.Click_Login()
            self.log.info('click on login')
            self.lp.Enter_Email(email)
            self.log.info('Enter Email')
            self.lp.Enter_pass(password)
            self.log.info('Enter Password')
            self.lp.Signin()
            self.log.info('click on sign in')

            time.sleep(3)
            if self.lp.Status()==True:

                WriteData (self.fpath, "Sheet1", x, 5, 'successful')
                self.log.info('write "successful" in column 5 in excel')
                self.driver.save_screenshot(f".//screenshots//login with {email}-{password} is successful.png")
                self.log.info(f'Take screenshot of login with {email}-{password}')
                if exp_results == 'successful':
                    WriteData (self.fpath,'Sheet1',x, 6, 'pass')
                    self.log.info('write "pass" in column 6 in excel')
                    list.append('pass')
                    self.log.info('append the list with pass')
                    self.lp.Logout()
                    self.log.info('click on logout')
                else:
                    WriteData(self.fpath, 'Sheet1', x, 6, 'fail')
                    self.log.info('write "fail" in column 6 in excel sheet')
                    list.append('fail')
                    self.log.info('append the list with fail')
                    self.lp.Logout()
                    self.log.info('click on logout')

            else:
                WriteData(self.fpath, "Sheet1", x, 5, 'unsuccessful')
                self.log.info('write "unsuccessful" in column 6 in excel sheet')
                self.driver.save_screenshot(f".//screenshots//login with {email}-{password} is unsuccessful.png")
                self.log.info(f'take screenshot of login with {email}-{password}')
                if exp_results == 'unsuccessful':
                    WriteData(self.fpath, "Sheet1", x, 6, 'pass')
                    self.log.info('write "pass" in column 6 in excel sheet')
                    list.append('pass')
                    self.log.info('Append list with pass')

                else:
                    WriteData(self.fpath, "Sheet1", x, 6, 'fail')
                    self.log.info('write "fail" in column 6 in excel sheet')
                    list.append('fail')
                    self.log.info('Append list with fail')
        if 'fail' in list:
            print('Test is failed')
            self.log.info('Test is failed')
            assert False
        else:
            print('Test is passed')
            self.log.info('Test is passed \n')
            assert True






# pytest -v -s --alluredir="D:\credence\Luma_Magneto_Pytest_Project\allure-results" "D:\credence\Luma_Magneto_Pytest_Project\Testcases\test_login_ddt.py" --browser chrome

# pytest -v -s --html=HTML_File/login_ddt.html "D:\credence\Luma_Magneto_Pytest_Project\Testcases\test_login_ddt.py" --browser chrome