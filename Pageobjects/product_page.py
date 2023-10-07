import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class Product():
    click_fitness_jacket_size_XPATH = (By.XPATH,"//div[@class='swatch-opt-430']//div[@id='option-label-size-143-item-169']")
    click_fitness_jacket_colour_XPATH = (By.XPATH,"//div[@class='swatch-opt-430']//div[@id='option-label-color-93-item-56']")
    click_fitness_jacket_add_to_cart_XPATH = (By.XPATH,"//li[1]//div[1]//div[1]//div[3]//div[1]//div[1]//form[1]//button[1]//span[1]")
    click_wind_jacket_size_XPATH = (By.XPATH,"//div[@class='swatch-opt-414']//div[@id='option-label-size-143-item-168']")
    click_wind_jacket_colour_XPATH = (By. XPATH,"//div[@class='swatch-opt-414']//div[@id='option-label-color-93-item-53']")
    click_wind_jacket_add_to_cart_XPATH = (By.XPATH,"//li[2]//div[1]//div[1]//div[4]//div[1]//div[1]//form[1]//button[1]//span[1]")
    click_add_cart_XPATH = (By.XPATH,"/html[1]/body[1]/div[2]/header[1]/div[2]/div[1]/a[1]")
    click_view_edit_cart_XPATH = (By.XPATH,"//span[normalize-space()='View and Edit Cart']")
    fitness_jacket_quantity_XPATH = (By.XPATH,"/html[1]/body[1]/div[2]/main[1]/div[3]/div[1]/div[2]/form[1]/div[1]/table[1]/tbody[1]/tr[1]/td[3]/div[1]/div[1]/label[1]/input[1]")
    wind_jacket_quantity_XPATH = (By.XPATH, "/html[1]/body[1]/div[2]/main[1]/div[3]/div[1]/div[2]/form[1]/div[1]/table[1]/tbody[2]/tr[1]/td[3]/div[1]/div[1]/label[1]/input[1]")
    click_update_shopping_cart_XPATH = (By.XPATH,"//span[normalize-space()='Update Shopping Cart']")
    click_proceed_to_checkout_XPATH = (By.XPATH,"//span[normalize-space()='Proceed to Checkout']")
    text_company_name_XPATH = (By.XPATH,"/html[1]/body[1]/div[2]/main[1]/div[2]/div[1]/div[2]/div[4]/ol[1]/li[1]/div[2]/form[1]/div[1]/div[3]/div[1]/input[1]")
    text_street_address_XPATH = (By.XPATH, "/html[1]/body[1]/div[2]/main[1]/div[2]/div[1]/div[2]/div[4]/ol[1]/li[1]/div[2]/form[1]/div[1]/fieldset[1]/div[1]/div[1]/div[1]/input[1]")
    text_city_XPATH = (By.XPATH, "/html[1]/body[1]/div[2]/main[1]/div[2]/div[1]/div[2]/div[4]/ol[1]/li[1]/div[2]/form[1]/div[1]/div[4]/div[1]/input[1]")
    select_state_XPATH = (By.XPATH,"/html[1]/body[1]/div[2]/main[1]/div[2]/div[1]/div[2]/div[4]/ol[1]/li[1]/div[2]/form[1]/div[1]/div[5]/div[1]/select[1]")
    text_zip_XPATH = (By.XPATH, "/html[1]/body[1]/div[2]/main[1]/div[2]/div[1]/div[2]/div[4]/ol[1]/li[1]/div[2]/form[1]/div[1]/div[7]/div[1]/input[1]")
    select_country_XPATH = (By.XPATH, "/html[1]/body[1]/div[2]/main[1]/div[2]/div[1]/div[2]/div[4]/ol[1]/li[1]/div[2]/form[1]/div[1]/div[8]/div[1]/select[1]")
    text_phone_XPATH = (By.XPATH, "/html[1]/body[1]/div[2]/main[1]/div[2]/div[1]/div[2]/div[4]/ol[1]/li[1]/div[2]/form[1]/div[1]/div[9]/div[1]/input[1]")
    click_shipping_method_CSS=(By.CSS_SELECTOR,"input[value='flatrate_flatrate']")
    click_next_XPATH = (By.XPATH,"//span[normalize-space()='Next']")
    click_placed_order_XPATH = (By.XPATH,"/html[1]/body[1]/div[3]/main[1]/div[2]/div[1]/div[2]/div[4]/ol[1]/li[3]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[4]/div[1]/button[1]")
    print_thanks_message_XPATH = (By.XPATH,"//span[@class='base']")
    print_order_no_XPATH = (By.XPATH,"//div[@class='page-wrapper']//p[1]")
    click_menu_XPATH = (By.XPATH, '/html/body/div[2]/header/div[1]/div/ul/li[2]/span/button')
    click_signout_XPATH = (By.XPATH, "//div[@aria-hidden='false']//a[normalize-space()='Sign Out']")
    click_new_address_CSS = (By.CSS_SELECTOR,".action.action-show-popup")
    click_unsave_address_CSS = (By.CSS_SELECTOR,"#shipping-save-in-address-book")
    click_ship_here_CSS = (By.CSS_SELECTOR,"button[class='action primary action-save-address'] span")
# -----------If address open in popup window----------------------
    text_company_name_popup_XPATH = (By.XPATH, "/html[1]/body[1]/div[3]/aside[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[3]/div[1]/input[1]")
    text_street_address_popup_XPATH = (By.XPATH, "/html[1]/body[1]/div[3]/aside[2]/div[2]/div[1]/div[1]/form[1]/div[1]/fieldset[1]/div[1]/div[1]/div[1]/input[1]")
    text_city_popup_XPATH = (By.XPATH, "/html[1]/body[1]/div[3]/aside[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[4]/div[1]/input[1]")
    select_state_popup_XPATH = (By.XPATH, "/html[1]/body[1]/div[3]/aside[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[5]/div[1]/select[1]")
    text_zip_popup_XPATH = (By.XPATH, "/html[1]/body[1]/div[3]/aside[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[7]/div[1]/input[1]")
    select_country_popup_XPATH = (By.XPATH, "/html[1]/body[1]/div[3]/aside[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[8]/div[1]/select[1]")
    text_phone_popup_XPATH = (By.XPATH, "/html[1]/body[1]/div[3]/aside[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[9]/div[1]/input[1]")


    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver,40)



    def jacket_section(self):
        a=ActionChains(self.driver)
        m = self.driver.find_element(By.XPATH,"//a[@id='ui-id-5']//span[@class='ui-menu-icon ui-icon ui-icon-carat-1-e']")
        a.move_to_element(m).perform()
        n=self.driver.find_element(By.XPATH,"//a[@id='ui-id-17']//span[contains(text(),'Tops')]")
        a.move_to_element(n).perform()
        p=self.driver.find_element(By.XPATH,"//a[@id='ui-id-19']//span[contains(text(),'Jackets')]")
        a.move_to_element(p).click().perform()

    def Fitness_Jacket_size(self):
        self.wait.until(EC.visibility_of_element_located(self.click_fitness_jacket_size_XPATH)).click()

    def Fitness_Jacket_colour(self):
        self.wait.until(EC.visibility_of_element_located(self.click_fitness_jacket_colour_XPATH)).click()

    def Fitness_Jacket_add_cart(self):
        self.wait.until(EC.visibility_of_element_located(self.click_fitness_jacket_add_to_cart_XPATH)).click()

    def Wind_Jacket_Size(self):
        self.wait.until(EC.visibility_of_element_located(self.click_wind_jacket_size_XPATH)).click()

    def Wind_Jacket_colour(self):
        self.wait.until(EC.visibility_of_element_located(self.click_wind_jacket_colour_XPATH)).click()

    def Wind_Jacket_add_cart(self):
        self.wait.until(EC.visibility_of_element_located(self.click_wind_jacket_add_to_cart_XPATH)).click()

    def CLick_Add_Cart(self):
        self.wait.until(EC.visibility_of_element_located(self.click_add_cart_XPATH)).click()

    def Edit_Add_Cart(self):
        self.wait.until(EC.visibility_of_element_located(self.click_view_edit_cart_XPATH)).click()

    def Qauntity_Fitness_Jacket(self,a):
        self.wait.until(EC.visibility_of_element_located(self.fitness_jacket_quantity_XPATH)).clear()
        self.wait.until(EC.visibility_of_element_located(self.fitness_jacket_quantity_XPATH)).send_keys(a)

    def Qauntity_Wind_Jacket(self, b):
        self.wait.until(EC.visibility_of_element_located(self.wind_jacket_quantity_XPATH)).clear()
        self.wait.until(EC.visibility_of_element_located(self.wind_jacket_quantity_XPATH)).send_keys(b)

    def Update_Shopping_Cart(self):
        self.wait.until(EC.visibility_of_element_located(self.click_update_shopping_cart_XPATH)).click()

    def Proceed_Checkout(self):
        self.wait.until(EC.visibility_of_element_located(self.click_proceed_to_checkout_XPATH)).click()

    def Enter_Company_name(self, name):
        self.wait.until(EC.visibility_of_element_located(self.text_company_name_XPATH)).send_keys(name)

    def Enter_Street_Address(self,address):
        self.wait.until(EC.visibility_of_element_located(self.text_street_address_XPATH)).send_keys(address)

    def Enter_City(self,city):
        self.wait.until(EC.visibility_of_element_located(self.text_city_XPATH)).send_keys(city)

    def Select_State(self,x):
        state = Select(self.wait.until(EC.visibility_of_element_located(self.select_state_XPATH)))
        state.select_by_visible_text(x)

    def Select_Country(self,y):
        country = Select(self.wait.until(EC.visibility_of_element_located(self.select_country_XPATH)))
        country.select_by_visible_text(y)

    def Enter_Zip(self,zip):
        self.wait.until(EC.visibility_of_element_located(self.text_zip_XPATH)).send_keys(zip)

    def Enter_Phone(self,phone):
        self.wait.until(EC.visibility_of_element_located(self.text_phone_XPATH)).send_keys(phone)

    def Shipping_method(self):
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

        self.wait.until(EC.visibility_of_element_located(self.click_shipping_method_CSS)).click()

    def Click_Next(self):
        self.wait.until(EC.visibility_of_element_located(self.click_next_XPATH)).click()

    def Place_order(self):
        element = self.wait.until(EC.visibility_of_element_located(self.click_placed_order_XPATH))
        self.driver.execute_script("arguments[0].click();",element)


    def status(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.print_thanks_message_XPATH))
            return True
        except:
            return False

    def Message(self):
        print(self.wait.until(EC.visibility_of_element_located(self.print_thanks_message_XPATH)).text)

    def Order_number(self):
        print(self.wait.until(EC.visibility_of_element_located(self.print_order_no_XPATH)).text)

    def Click_Menu(self):
        self.wait.until(EC.visibility_of_element_located(self.click_menu_XPATH)).click()

    def Click_SignOut(self):
        self.wait.until(EC.visibility_of_element_located(self.click_signout_XPATH)).click()

    def New_Adress_status(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.click_new_address_CSS))
            return True
        except:
            return False

    def New_Adress(self):
        self.wait.until(EC.visibility_of_element_located(self.click_new_address_CSS)).click()

    def Unsave_Address(self):
        self.wait.until(EC.visibility_of_element_located(self.click_unsave_address_CSS)).click()


    def Ship_Here(self):
        self.wait.until(EC.visibility_of_element_located(self.click_ship_here_CSS)).click()



    def Enter_Company_name_popup(self,name):
        self.wait.until(EC.visibility_of_element_located(self.text_company_name_popup_XPATH)).send_keys(name)

    def Enter_Street_Address_popup(self,address):
        self.wait.until(EC.visibility_of_element_located(self.text_street_address_popup_XPATH)).send_keys(address)

    def Enter_City_popup(self,city):
        self.wait.until(EC.visibility_of_element_located(self.text_city_popup_XPATH)).send_keys(city)

    def Select_State_popup(self,x):
        state = Select(self.wait.until(EC.visibility_of_element_located(self.select_state_popup_XPATH)))
        state.select_by_visible_text(x)

    def Select_Country_popup(self,y):
        country = Select(self.wait.until(EC.visibility_of_element_located(self.select_country_popup_XPATH)))
        country.select_by_visible_text(y)

    def Enter_Zip_popup(self,zip):
        self.wait.until(EC.visibility_of_element_located(self.text_zip_popup_XPATH)).send_keys(zip)

    def Enter_Phone_popup(self,phone):
        self.wait.until(EC.visibility_of_element_located(self.text_phone_popup_XPATH)).send_keys(phone)





