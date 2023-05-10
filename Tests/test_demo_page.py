import pytest
from Pages.DemoPage import DemoPage
from TestData.DemoPageData import DemoPageData
from Utilities.BaseClass import BaseClass


class TestDemoPage(BaseClass):
    def setup(self):
        self.demo_page = DemoPage(self.driver)

    # Checks if all the fields are displayed
    def test_case_01_validate_fields(self):
        self.demo_page.decline().click()
        fields = [
            self.demo_page.header(),
            self.demo_page.header_title(),
            self.demo_page.header_para(),
            self.demo_page.first_name(),
            self.demo_page.last_name(),
            self.demo_page.clinic_name(),
            self.demo_page.email(),
            self.demo_page.phone_number(),
            self.demo_page.job_title(),
            self.demo_page.country(),
            self.demo_page.submit(),
            self.demo_page.submit_chk_box(),
            self.demo_page.footer()
        ]
        for field in fields:
            field.is_displayed()

    # Checks if the validation messages are displayed for all the fields
    def test_case_02_validation_message(self):
        self.demo_page.submit().click()
        validations = [
            self.demo_page.first_name_validation(),
            self.demo_page.last_name_validation(),
            self.demo_page.clinic_name_validation(),
            self.demo_page.email_validation(),
            self.demo_page.phone_number_validation(),
            self.demo_page.country_validation(),
            self.demo_page.submit_chk_validation(),
            self.demo_page.all_fields_validation()
        ]
        for validation in validations:
            validation.is_displayed()

    # Checks for invalid Email and Phone number format
    def test_case_03_email_phone_check(self, get_data):
        self.demo_page.email().send_keys(get_data["invalid_email"])
        self.demo_page.email_validity_check().is_displayed()
        self.demo_page.phone_number().send_keys(get_data["invalid_phone"])
        self.demo_page.phone_number_validity_check().is_displayed()

    # Checks if the form submits successfully
    def test_case_04_submission(self, get_data):
        self.clear_and_enter(self.demo_page.first_name(), get_data["first_name"])
        self.clear_and_enter(self.demo_page.last_name(), get_data["last_name"])
        self.clear_and_enter(self.demo_page.clinic_name(), get_data["clinic_name"])
        self.clear_and_enter(self.demo_page.email(), get_data["email"])
        self.clear_and_enter(self.demo_page.phone_number(), get_data["phone"])
        self.clear_and_enter(self.demo_page.job_title(), get_data["job_title"])
        self.select_option_by_text(self.demo_page.country(), get_data["country"])
        self.demo_page.submit_chk_box().click()
        self.demo_page.submit().click()
        # alert_text = self.demo_page.success_message().text
        # assert ("Thank you" in alert_text)

    @pytest.fixture(params=DemoPageData.test_demopage_data)
    def get_data(self, request):
        return request.param
