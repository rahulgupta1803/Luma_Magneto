from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Create_Account():
    click_create_account_LINK_TEXT = (By.LINK_TEXT,'Create an Account')
    text_first_name_ID=(By.ID,'firstname')
    text_last_name_ID = (By.ID, 'lastname')
    text_email_ID = (By.ID, 'email_address')
    text_password_ID = (By.ID, 'password')
    text_confirm_password_ID = (By.ID, 'password-confirmation')
    click_create_account_button_XPATH = (By.XPATH,'//*[@id="form-validate"]/div/div[1]/button/span')
    status_XPATH = (By.XPATH,'//*[@id="maincontent"]/div[2]/div[1]/div[3]/div[2]/div/div[2]/a[2]')
    click_menu_XPATH = (By.XPATH,'/html/body/div[2]/header/div[1]/div/ul/li[2]/span/button')
    click_logout_XPATH = (By.XPATH,'/html/body/div[2]/header/div[1]/div/ul/li[2]/div/ul/li[3]/a')
    text_print_succ_mess_XPATH=(By.XPATH, "/html[1]/body[1]/div[2]/main[1]/div[1]/div[2]/div[1]/div[1]/div[1]")
    text_print_failed_mess_XPATH =(By.XPATH,"/html[1]/body[1]/div[2]/main[1]/div[2]/div[2]/div[1]/div[1]/div[1]")


    def __init__(self,driver):
        self.driver=driver

    def Click_Create_Account(self):
        self.driver.find_element(*Create_Account.click_create_account_LINK_TEXT).click()

    def Enter_First_Name(self,firstname):
        self.driver.find_element(*Create_Account.text_first_name_ID).send_keys(firstname)

    def Enter_Last_Name(self, lastname):
        self.driver.find_element(*Create_Account.text_last_name_ID).send_keys(lastname)

    def Enter_Emailid(self,email_id):
        self.driver.find_element(*Create_Account.text_email_ID).send_keys(email_id)

    def Enter_Password(self, password):
        self.driver.find_element(*Create_Account.text_password_ID).send_keys(password)

    def Enter_Confirm_Password(self, conf_password):
        self.driver.find_element(*Create_Account.text_confirm_password_ID).send_keys(conf_password)

    def Click_Create_Button(self):
        self.driver.find_element(*Create_Account.click_create_account_button_XPATH).click()

    def LogOut(self):
        self.driver.find_element(*Create_Account.click_menu_XPATH).click()
        self.driver.find_element(*Create_Account.click_logout_XPATH).click()

    def Print_Succ_Mess(self):
        c = self.driver.find_element(*Create_Account.text_print_succ_mess_XPATH).text
        return c
    def Print_Fail_Mess(self):
        d = self.driver.find_element(*Create_Account.text_print_failed_mess_XPATH).text
        return d

    def Status(self):
        try:
            self.driver.find_element(*Create_Account.status_XPATH)
            return True
        except:
            return False



    