Automated tests for the request form located at https://www.provet.cloud/request-demo?hsCtaTracking=a3ea9906-246e-43f6-8ae9-d4aec8d67b08%7C5fc25f4f-8d28-4224-8de3-66ec41604683

Automated using Selenium with Python as the binding language.

Developed the framework using Page object model approach.

Brief explanation of each directories -

Pages: Includes the webpages that are automated. As one form was automated, there is one Python file in it in which all the locators are defined.

Report: HTML reports that are generated through pytest.  

TestData: The sample data that is used to enter into the fields in the Request form webpage.

Tests: Test cases related to the request form webpage.

Utilities: Utility files.

Note: Form submission was not validated due to recaptcha.
