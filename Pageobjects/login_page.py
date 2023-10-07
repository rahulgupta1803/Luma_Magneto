from selenium.webdriver.common.by import By


class Login():
    click_login_LINK_TEXT =(By.LINK_TEXT,'Sign In')
    text_email_ID=(By.ID,'email')
    text_password_ID = (By.ID, 'pass')
    click_signin_XPATH = (By.XPATH,"//fieldset[@class='fieldset login']//span[contains(text(),'Sign In')]")
    status_CSS = (By.CSS_SELECTOR,"div[class='panel header'] span[class='logged-in']")
    click_menu_XPATH = (By.XPATH,'/html/body/div[2]/header/div[1]/div/ul/li[2]/span/button')
    click_signout_XPATH = (By.XPATH,"//div[@aria-hidden='false']//a[normalize-space()='Sign Out']")

    def __init__(self,driver):
        self.driver = driver

    def Click_Login(self):
        self.driver.find_element(*Login.click_login_LINK_TEXT).click()

    def Enter_Email(self, email):
        self.driver.find_element(*Login.text_email_ID).send_keys(email)

    def Enter_pass(self, password):
        self.driver.find_element(*Login.text_password_ID).send_keys(password)

    def Signin(self):
        self.driver.find_element(*Login.click_signin_XPATH).click()

    def Status(self):
        try:
            c = self.driver.find_element(*Login.status_CSS).text
            print(c)
            return True
        except:
            return False


    def Logout(self):
        self.driver.find_element(*Login.click_menu_XPATH).click()
        self.driver.find_element(*Login.click_signout_XPATH).click()








