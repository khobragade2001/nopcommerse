import pytest

class Test_ecommerse:

    def test_registraction_page(self):
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.select import Select
        import time

        d = webdriver.Chrome()
        d.maximize_window()
        x = By.XPATH

        ## go to url
        d.get("https://demo.nopcommerce.com/login")
        ## click on register
        d.find_element(x, "//button[normalize-space()='Register']").click()
        time.sleep(2)
        ### click on male button
        d.find_element(x, "//label[@for='gender-male']").click()
        ### enter first name
        d.find_element(x, "//input[@id='FirstName']").send_keys("ashish")
        ### enter last name
        d.find_element(x, "//input[@id='LastName']").send_keys("khobragade")

        #### enter drop down day
        aa1 = Select(d.find_element(x, "//select[@name='DateOfBirthDay']"))
        aa1.select_by_index(5)

        ### enter drop down months
        aa1 = Select(d.find_element(x, "//select[@name='DateOfBirthMonth']"))
        aa1.select_by_index(4)

        ### enter drop down year
        aa1 = Select(d.find_element(x, "//select[@name='DateOfBirthYear']"))
        aa1.select_by_index(82)

        ### enter mail id
        d.find_element(x, "//input[@id='Email']").send_keys("khobragade3030@gmail.com")
        ### enter pass
        d.find_element(x, "//input[@id='Password']").send_keys("Ashish@004")
        ### enter conform pass
        d.find_element(x, "//input[@id='ConfirmPassword']").send_keys("Ashish@004")
        ### click on register button
        d.find_element(x, "//button[@id='register-button']").click()
        time.sleep(2)
        d.close()

    @pytest.mark.skip
    def test_multiplication_001(self):
        a = 30
        s = 35
        mul = a*s
        print('multiplication of numbers is :', + str(mul))
        if mul == 1050:
            assert True
        else:
            assert False



class Test_commerse:

    def test_login(self):
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.select import Select
        import time

        d = webdriver.Chrome()
        d.maximize_window()
        x = By.XPATH

        ## go to url
        d.get("https://demo.nopcommerce.com/login")
        ## mail id
        d.find_element(x, "//input[@id='Email']").send_keys("khobragade3030@gmail.com")
        ## pass
        d.find_element(x, "//input[@id='Password']").send_keys("Ashish@004")
        ## login button
        d.find_element(x, "//button[normalize-space()='Log in']").click()
        time.sleep(5)

        ### add mac laptop
        d.find_element(x, "//div[@class='item-grid']//div[2]//div[1]//div[2]//div[3]//div[2]//button[1]").click()
        time.sleep(2)
        d.find_element(x, "//button[@id='add-to-cart-button-4']").click()
        ## goto home button
        d.find_element(x, "//span[contains(text(),'Home')]").click()
        time.sleep(3)

        ### add pc
        d.find_element(x, "//div[@class='page-body']//div[1]//div[1]//div[2]//div[3]//div[2]//button[1]").click()
        time.sleep(2)
        ##  ram drop down
        aa1 = Select(d.find_element(x, "//select[@id='product_attribute_2']"))
        aa1.select_by_index(3)
        time.sleep(2)
        ### click ssd
        d.find_element(x, "//input[@id='product_attribute_3_7']").click()
        ### aad to card pc
        d.find_element(x, "//button[@id='add-to-cart-button-1']").click()
        time.sleep(5)
        ## goto home button
        d.find_element(x, "//span[contains(text(),'Home')]").click()
        time.sleep(5)

        ### add electronics
        d.find_element(x, "//ul[@class='top-menu notmobile']//a[normalize-space()='Electronics']").click()
        time.sleep(2)
        ## sell phone folder
        d.find_element(x,
                       "//a[@title='Show products in category Cell phones'][normalize-space()='Cell phones']").click()
        time.sleep(2)
        ### nokia lumia
        d.find_element(x, "//div[@class='center-2']//div[3]//div[1]//div[2]//div[3]//div[2]//button[1]").click()
        time.sleep(5)
        # # ## goto home button
        # d.find_element(x, "//a[@title='Home']").click()
        # time.sleep(3)

        #####@@@@@@@@@@@ cheackout process
        ## go to shoping cart
        d.find_element(x, "//span[@class='cart-label']").click()
        time.sleep(3)
        ### go to agree button and clock
        d.find_element(x, "//input[@id='termsofservice']").click()
        time.sleep(2)
        ### cheackout button
        d.find_element(x, "//button[@id='checkout']").click()
        time.sleep(5)

        #############@@@@@@@@@ billing add
        aa1 = Select(d.find_element(x, "//select[@id='BillingNewAddress_CountryId']"))
        aa1.select_by_index(100)
        time.sleep(2)
        ## select city
        d.find_element(x, "//input[@id='BillingNewAddress_City']").send_keys("yavatmal")
        ### select add
        d.find_element(x, "//input[@id='BillingNewAddress_Address1']").send_keys("panchaashil nagar amravati road")
        ### con add
        d.find_element(x, "//input[@id='BillingNewAddress_Address2']").send_keys("lohara Yavatmal maharashtra")
        ### zip code
        d.find_element(x, "//input[@id='BillingNewAddress_ZipPostalCode']").send_keys("445001")
        ### phone no
        d.find_element(x, "//input[@id='BillingNewAddress_PhoneNumber']").send_keys("9673040564")
        #### click on continue button
        d.find_element(x, "//button[@onclick='Billing.save()']").click()
        time.sleep(3)
        #### shiping method continue button click
        d.find_element(x, "//button[@class='button-1 shipping-method-next-step-button']").click()
        time.sleep(3)
        ###payment method  continue button
        d.find_element(x, "//button[@class='button-1 payment-method-next-step-button']").click()
        time.sleep(3)
        ## click conti
        d.find_element(x, "//button[@class='button-1 payment-info-next-step-button']").click()
        time.sleep(3)
        #####final conform
        d.find_element(x, "//button[normalize-space()='Confirm']").click()
        time.sleep(5)

        ### click order detail
        d.find_element(x, "//a[normalize-space()='Click here for order details.']").click()
        time.sleep(3)
        ###click on download pdf
        d.find_element(x, "//a[@class='button-2 pdf-invoice-button']").click()
        time.sleep(5)
        d.close()

