from selenium.webdriver.common.by import By


class Amount_Verification():
    Order_total_XPATH = (By.XPATH,'/html[1]/body[1]/div[2]/main[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[4]/th[1]')
    Total_amount_XPATH = (By.XPATH,'//*[@id="cart-totals"]/div/table/tbody/tr[4]/td/strong/span')





    def __init__(self, driver):
        self.driver = driver

    def length_distribution(self):
        m = len(self.driver.find_elements(By.XPATH, "/html[1]/body[1]/div[2]/main[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr/th[1]"))
        return m


    def Sub_Disc_Shipping(self,a):
        m =self.driver.find_element(By.XPATH,'//*[@id="cart-totals"]/div/table/tbody/tr['+str(a)+']/th').text
        return m

    def Length_Amount(self):
        m = len(self.driver.find_elements(By.XPATH,'//*[@id="cart-totals"]/div/table/tbody/tr/td/span'))
        return m

    def diff_Amount(self,a):
        m = self.driver.find_element(By.XPATH,'//*[@id="cart-totals"]/div/table/tbody/tr['+str(a)+']/td/span').text
        return m

    def Order_Total(self):
        m = self.driver.find_element(*Amount_Verification.Order_total_XPATH).text
        return m

    def Total_Amount(self):
        m = self.driver.find_element(*Amount_Verification.Total_amount_XPATH).text
        return m