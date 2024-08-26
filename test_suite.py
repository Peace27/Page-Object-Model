
import pytest
from selenium import webdriver

from ActionPage.ActionsPage import LoginActionsPage, AdminActionsPage, AdminJobIconActions, \
    AdminOrganisationIconActions, AdminQualificationsIconActions, AdminNationalitiesIconActions, \
    AdminCorporateBrandingIconActions, AdminConfigurationIconActions


@pytest.fixture(scope="module")
def driver_setup():
    driver = webdriver.Chrome()
    driver.implicitly_wait(20)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="module")
def login(driver_setup):
    driver = driver_setup
    login_page = LoginActionsPage(driver)  # call the login class
    login_page.open_url("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")  # call the url
    return login_page


def test_login_page_on_orange_HR_website(login):
    login.enter_username("Admin")
    login.enter_password("admin123")
    login.click_submit_button()


def test_admin_page_button(login):
    admin_page = AdminActionsPage(login.driver)
    admin_page.click_admin_button()
    admin_page.click_admin_user_mgt_dropdown()
    admin_page.click_admin_users()


def test_admin_page_job_dropdown(login):
    admin_page = AdminJobIconActions(login.driver)
    admin_page.click_admin_job_dropdown()
    admin_page.click_job_job_titles()
    admin_page.click_admin_job_dropdown1()
    admin_page.click_admin_job_pay_grades()
    admin_page.click_admin_job_dropdown2()
    admin_page.click_admin_job_employ_status()
    admin_page.click_admin_job_dropdown3()
    admin_page.click_admin_job_job_categories()
    admin_page.click_admin_job_dropdown4()
    admin_page.click_admin_job_work_shift()


def test_admin_page_organisation_dropdown(login):
    admin_page = AdminOrganisationIconActions(login.driver)
    admin_page.click_admin_0rg_dropdown()
    admin_page.click_admin_org_general_info()
    admin_page.click_admin_0rg_dropdown1()
    admin_page.click_admin_org_locations()
    admin_page.click_admin_0rg_dropdown2()
    admin_page.click_admin_org_structure()


def test_admin_page_qualification_dropdown(login):
    admin_page = AdminQualificationsIconActions(login.driver)
    admin_page.click_admin_qua_dropdown()
    admin_page.click_admin_qua_skills()
    admin_page.click_admin_qua_dropdown1()
    admin_page.click_admin_qua_education()
    admin_page.click_admin_qua_dropdown2()
    admin_page.click_admin_qua_licences()
    admin_page.click_admin_qua_dropdown3()
    admin_page.click_admin_qua_memberships()


def test_admin_page_nationalities(login):
    admin_page = AdminNationalitiesIconActions(login.driver)
    admin_page.click_admin_nationality()


def test_admin_page_corporate_branding(login):
    admin_page = AdminCorporateBrandingIconActions(login.driver)
    admin_page.click_admin_cor_branding()


def test_admin_page_configuration_dropdown(login):
    admin_page = AdminConfigurationIconActions(login.driver)
    admin_page.click_admin_configuration_dropdown()
    admin_page.click_admin_configuration_email_config()
    admin_page.click_admin_configuration_dropdown1()
    admin_page.click_admin_configuration_email_subscript()
    admin_page.click_admin_configuration_dropdown2()
    admin_page.click_admin_configuration_localization()
    admin_page.click_admin_configuration_dropdown3()
    admin_page.click_admin_configuration_lang_package()
    admin_page.click_admin_configuration_dropdown4()
    admin_page.click_admin_configuration_modules()
    admin_page.click_admin_configuration_dropdown5()
    admin_page.click_admin_configuration_social_media_aut()
    admin_page.click_admin_configuration_dropdown6()
    admin_page.click_admin_configuration_register_oat_client()
    admin_page.click_admin_configuration_dropdown7()
    admin_page.click_admin_configuration_ldap()
