from selenium.webdriver.common.by import By


class DemoPage:
    def __init__(self, driver):
        self.driver = driver

    header_logo = (By.XPATH, "//img[@title='Provet Cloud']")
    header_tl = (By.XPATH, "//h1[normalize-space()='Request a demo']")
    header_pr = (By.XPATH, "//p[contains(text(),'Fill in your contact information and we will conta')]")
    first_name_txt = (By.XPATH, "//input[@id='firstname-026d3da1-3ad3-4492-9470-1d4274bcae4c_6261']")
    last_name_txt = (By.XPATH, "//input[@id='lastname-026d3da1-3ad3-4492-9470-1d4274bcae4c_6261']")
    clinic_name_txt = (By.XPATH, "//input[@id='company-026d3da1-3ad3-4492-9470-1d4274bcae4c_6261']")
    email_txt = (By.XPATH, "//input[@id='email-026d3da1-3ad3-4492-9470-1d4274bcae4c_6261']")
    phone_number_txt = (By.XPATH, "//input[@id='phone-026d3da1-3ad3-4492-9470-1d4274bcae4c_6261']")
    job_title_txt = (By.XPATH, "//input[@id='jobtitle-026d3da1-3ad3-4492-9470-1d4274bcae4c_6261']")
    country_dd = (By.XPATH, "//select[@id='country__dropdown_-026d3da1-3ad3-4492-9470-1d4274bcae4c_6261']")
    submit_btn = (By.XPATH, "//form[@id='hsForm_026d3da1-3ad3-4492-9470-1d4274bcae4c_6261']//input[@value='Submit']")
    accept_btn = (By.XPATH, "//*[@id='hs-eu-decline-button']")
    decline_btn = (By.XPATH, "//*[@id='hs-eu-decline-button']")
    footer_logo = (By.XPATH, "//p[normalize-space()='© Provet Cloud 2023.']")
    submit_chk = (By.XPATH, "//input[@id='LEGAL_CONSENT.subscription_type_6801572-026d3da1-3ad3-4492-9470-1d4274bcae4c_6261']")
    privacy_link = (By.XPATH, "//a[normalize-space()='Privacy Notice.']")
    first_name_val_msg = (By.XPATH, "//div[@class='hs_firstname hs-firstname hs-fieldtype-text field hs-form-field']//label[@class='hs-error-msg hs-main-font-element'][normalize-space()='Please complete this required field.']")
    last_name_val_msg = (By.XPATH, "//div[@class='hs_lastname hs-lastname hs-fieldtype-text field hs-form-field']//label[@class='hs-error-msg hs-main-font-element'][normalize-space()='Please complete this required field.']")
    clinic_name_val_msg = (By.XPATH, "//div[@class='hs_company hs-company hs-fieldtype-text field hs-form-field']//label[@class='hs-error-msg hs-main-font-element'][normalize-space()='Please complete this required field.']")
    email_val_msg = (By.XPATH, "//div[@class='hs_email hs-email hs-fieldtype-text field hs-form-field']//label[@class='hs-error-msg hs-main-font-element'][normalize-space()='Please complete this required field.']")
    email_validity = (By.XPATH, "//label[normalize-space()='Email must be formatted correctly.']")
    phone_number_val_msg = (By.XPATH, "//div[@class='hs_phone hs-phone hs-fieldtype-text field hs-form-field']//label[@class='hs-error-msg hs-main-font-element'][normalize-space()='Please complete this required field.']")
    phone_number_validity = (By.XPATH, "//label[normalize-space()='Must contain only numbers, +()-. and x.']")
    country_val_msg = (By.XPATH, "//label[normalize-space()='Please select an option from the dropdown menu.']")
    submit_chk_val_msg = (By.XPATH, "//div[@class='hs_LEGAL_CONSENT.subscription_type_6801572 hs-LEGAL_CONSENT.subscription_type_6801572 hs-fieldtype-booleancheckbox field hs-form-field']//label[@class='hs-error-msg hs-main-font-element'][normalize-space()='Please complete this required field.']")
    all_fields_val_msg = (By.XPATH, "//label[normalize-space()='Please complete all required fields.']")
    success = (By.XPATH, "//h1[contains(text(),'Thank you for contacting us.')]")

    def header(self):
        return self.driver.find_element(*DemoPage.header_logo)

    def header_title(self):
        return self.driver.find_element(*DemoPage.header_tl)

    def header_para(self):
        return self.driver.find_element(*DemoPage.header_pr)

    def first_name(self):
        return self.driver.find_element(*DemoPage.first_name_txt)

    def last_name(self):
        return self.driver.find_element(*DemoPage.last_name_txt)

    def clinic_name(self):
        return self.driver.find_element(*DemoPage.clinic_name_txt)

    def email(self):
        return self.driver.find_element(*DemoPage.email_txt)

    def phone_number(self):
        return self.driver.find_element(*DemoPage.phone_number_txt)

    def job_title(self):
        return self.driver.find_element(*DemoPage.job_title_txt)

    def country(self):
        return self.driver.find_element(*DemoPage.country_dd)

    def submit(self):
        return self.driver.find_element(*DemoPage.submit_btn)

    def submit_chk_box(self):
        return self.driver.find_element(*DemoPage.submit_chk)

    def accept(self):
        return self.driver.find_element(*DemoPage.accept_btn)

    def decline(self):
        return self.driver.find_element(*DemoPage.decline_btn)

    def footer(self):
        return self.driver.find_element(*DemoPage.footer_logo)

    def privacy_notice_link(self):
        return self.driver.find_element(*DemoPage.privacy_link)

    def first_name_validation(self):
        return self.driver.find_element(*DemoPage.first_name_val_msg)

    def last_name_validation(self):
        return self.driver.find_element(*DemoPage.last_name_val_msg)

    def clinic_name_validation(self):
        return self.driver.find_element(*DemoPage.clinic_name_val_msg)

    def email_validation(self):
        return self.driver.find_element(*DemoPage.email_val_msg)

    def email_validity_check(self):
        return self.driver.find_element(*DemoPage.email_validity)

    def phone_number_validation(self):
        return self.driver.find_element(*DemoPage.phone_number_val_msg)

    def phone_number_validity_check(self):
        return self.driver.find_element(*DemoPage.phone_number_validity)

    def country_validation(self):
        return self.driver.find_element(*DemoPage.country_val_msg)

    def submit_chk_validation(self):
        return self.driver.find_element(*DemoPage.submit_chk_val_msg)

    def all_fields_validation(self):
        return self.driver.find_element(*DemoPage.all_fields_val_msg)

    def success_message(self):
        return self.driver.find_element(*DemoPage.success)
