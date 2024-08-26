import time

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait

from LocatorPage.LocatorsPage import AdminLocatorsPage, LoginLocatorsPage, AdminJobIconLocators, \
    AdminOrganisationIconLocators, AdminQualificationsIconLocators, AdminNationalitiesIconLocators, \
    AdminConfigurationIconLocators


class LoginActionsPage:
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)

    # To set up Login Page (Username,Password and SubmitButton)
    def enter_username(self, username):
        enter_username = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(LoginLocatorsPage.ENTER_USERNAME))
        enter_username.send_keys(username)
        time.sleep(5)

    def enter_password(self, password):
        enter_password = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(LoginLocatorsPage.ENTER_PASSWORD))
        enter_password.send_keys(password)
        time.sleep(5)

    def click_submit_button(self):
        click_submit_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(LoginLocatorsPage.CLICK_SUBMIT_BUTTON))
        click_submit_button.click()


class AdminActionsPage:
    def __init__(self, driver):
        self.driver = driver

    def click_admin_button(self):
        click_admin_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AdminLocatorsPage.CLICK_ADMIN_BUTTON))
        click_admin_button.click()
        time.sleep(2)

    def click_admin_user_mgt_dropdown(self):
        click_admin_user_mgt_dropdown = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AdminLocatorsPage.CLICK_ADMIN_USER_MGT_DROPDOWN))
        click_admin_user_mgt_dropdown.click()
        time.sleep(5)

    def click_admin_users(self):
        click_admin_users = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AdminLocatorsPage.CLICK_ADMIN_USERS))
        click_admin_users.click()
        time.sleep(5)


class AdminJobIconActions:
    def __init__(self, driver):
        self.driver = driver

    def click_admin_job_dropdown(self):
        click_admin_job_dropdown = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AdminJobIconLocators.CLICK_ADMIN_JOB_DROPDOWN))
        click_admin_job_dropdown.click()
        time.sleep(5)

    def click_job_job_titles(self):
        click_job_job_titles = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AdminJobIconLocators.CLICK_ADMIN_JOB_JOB_TITLES))
        click_job_job_titles.click()
        time.sleep(2)

    def click_admin_job_dropdown1(self):
        click_admin_job_dropdown = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AdminJobIconLocators.CLICK_ADMIN_JOB_DROPDOWN))
        click_admin_job_dropdown.click()
        time.sleep(5)

    def click_admin_job_pay_grades(self):
        click_admin_job_pay_grades = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AdminJobIconLocators.CLICK_ADMIN_JOB_PAY_GRADES))
        click_admin_job_pay_grades.click()
        time.sleep(2)

    def click_admin_job_dropdown2(self):
        click_admin_job_dropdown = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AdminJobIconLocators.CLICK_ADMIN_JOB_DROPDOWN))
        click_admin_job_dropdown.click()
        time.sleep(5)

    def click_admin_job_employ_status(self):
        click_admin_job_employ_status = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AdminJobIconLocators.CLICK_ADMIN_JOB_EMPLOY_STATUS))
        click_admin_job_employ_status.click()
        time.sleep(2)

    def click_admin_job_dropdown3(self):
        click_admin_job_dropdown = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AdminJobIconLocators.CLICK_ADMIN_JOB_DROPDOWN))
        click_admin_job_dropdown.click()
        time.sleep(5)

    def click_admin_job_job_categories(self):
        click_admin_job_job_categories = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AdminJobIconLocators.CLICK_ADMIN_JOB_JOB_CATEGORIES))
        click_admin_job_job_categories.click()
        time.sleep(2)

    def click_admin_job_dropdown4(self):
        click_admin_job_dropdown = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AdminJobIconLocators.CLICK_ADMIN_JOB_DROPDOWN))
        click_admin_job_dropdown.click()
        time.sleep(5)

    def click_admin_job_work_shift(self):
        click_admin_job_work_shift = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AdminJobIconLocators.CLICK_ADMIN_JOB_WORK_SHIFT))
        click_admin_job_work_shift.click()
        time.sleep(5)


class AdminOrganisationIconActions:
    def __init__(self, driver):
        self.driver = driver

    def click_admin_0rg_dropdown(self):
        click_admin_0rg_dropdown = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AdminOrganisationIconLocators.CLICK_ADMIN_ORG_DROPDOWN))
        click_admin_0rg_dropdown.click()
        time.sleep(5)

    def click_admin_org_general_info(self):
        click_admin_org_general_info = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AdminOrganisationIconLocators.CLICK_ADMIN_ORG_GENERAL_INFO))
        click_admin_org_general_info.click()
        time.sleep(2)

    def click_admin_0rg_dropdown1(self):
        click_admin_0rg_dropdown = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AdminOrganisationIconLocators.CLICK_ADMIN_ORG_DROPDOWN))
        click_admin_0rg_dropdown.click()
        time.sleep(5)

    def click_admin_org_locations(self):
        click_admin_org_locations = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AdminOrganisationIconLocators.CLICK_ADMIN_ORG_LOCATIONS))
        click_admin_org_locations.click()
        time.sleep(2)

    def click_admin_0rg_dropdown2(self):
        click_admin_0rg_dropdown = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AdminOrganisationIconLocators.CLICK_ADMIN_ORG_DROPDOWN))
        click_admin_0rg_dropdown.click()
        time.sleep(5)

    def click_admin_org_structure(self):
        click_admin_org_structure = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AdminOrganisationIconLocators.CLICK_ADMIN_ORG_STRUCTURE))
        click_admin_org_structure.click()
        time.sleep(5)


class AdminQualificationsIconActions:
    def __init__(self, driver):
        self.driver = driver

    def click_admin_qua_dropdown(self):
        click_admin_qua_dropdown = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AdminQualificationsIconLocators.CLICK_ADMIN_QUA_DROPDOWN))
        click_admin_qua_dropdown.click()
        time.sleep(5)

    def click_admin_qua_skills(self):
        click_admin_qua_skills = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AdminQualificationsIconLocators.CLICK_ADMIN_QUA_SKILLS))
        click_admin_qua_skills.click()
        time.sleep(2)

    def click_admin_qua_dropdown1(self):
        click_admin_qua_dropdown1 = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AdminQualificationsIconLocators.CLICK_ADMIN_QUA_DROPDOWN))
        click_admin_qua_dropdown1.click()
        time.sleep(5)

    def click_admin_qua_education(self):
        click_admin_qua_education = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AdminQualificationsIconLocators.CLICK_ADMIN_QUA_EDUCATION))
        click_admin_qua_education.click()
        time.sleep(2)

    def click_admin_qua_dropdown2(self):
        click_admin_qua_dropdown2 = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AdminQualificationsIconLocators.CLICK_ADMIN_QUA_DROPDOWN))
        click_admin_qua_dropdown2.click()
        time.sleep(5)

    def click_admin_qua_licences(self):
        click_admin_qua_licences = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AdminQualificationsIconLocators.CLICK_ADMIN_QUA_LICENSES))
        click_admin_qua_licences.click()
        time.sleep(2)

    def click_admin_qua_dropdown3(self):
        click_admin_qua_dropdown3 = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AdminQualificationsIconLocators.CLICK_ADMIN_QUA_DROPDOWN))
        click_admin_qua_dropdown3.click()
        time.sleep(5)

    def click_admin_qua_memberships(self):
        click_admin_qua_memberships = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AdminQualificationsIconLocators.CLICK_ADMIN_QUA_MEMBERSHIPS))
        click_admin_qua_memberships.click()
        time.sleep(5)


class AdminNationalitiesIconActions:
    def __init__(self, driver):
        self.driver = driver

    def click_admin_nationality(self):
        click_admin_nationality = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AdminNationalitiesIconLocators.CLICK_ADMIN_NATIONALITY))
        click_admin_nationality.click()
        time.sleep(5)


class AdminCorporateBrandingIconActions:
    def __init__(self, driver):
        self.driver = driver

    def click_admin_cor_branding(self):
        click_admin_cor_branding = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AdminCorporateBrandingIconLocators.CLICK_ADMIN_COR_BRANDING))
        click_admin_cor_branding.click()
        time.sleep(5)


class AdminConfigurationIconActions:
    def __init__(self, driver):
        self.driver = driver

    def click_admin_configuration_dropdown(self):
        click_admin_configuration_dropdown = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AdminConfigurationIconLocators.CLICK_ADMIN_CONFIGURATION_DROPDOWN))
        click_admin_configuration_dropdown.click()
        time.sleep(2)

    def click_admin_configuration_email_config(self):
        click_admin_configuration_email_config = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AdminConfigurationIconLocators.CLICK_ADMIN_CONFIGURATION_EMAIL_CONFIG))
        click_admin_configuration_email_config.click()
        time.sleep(5)

    def click_admin_configuration_dropdown1(self):
        click_admin_configuration_dropdown1 = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AdminConfigurationIconLocators.CLICK_ADMIN_CONFIGURATION_DROPDOWN))
        click_admin_configuration_dropdown1.click()
        time.sleep(2)

    def click_admin_configuration_email_subscript(self):
        click_admin_configuration_email_subscript = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AdminConfigurationIconLocators.CLICK_ADMIN_CONFIGURATION_EMAIL_SUBSCRIPT))
        click_admin_configuration_email_subscript.click()
        time.sleep(5)

    def click_admin_configuration_dropdown2(self):
        click_admin_configuration_dropdown2 = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AdminConfigurationIconLocators.CLICK_ADMIN_CONFIGURATION_DROPDOWN))
        click_admin_configuration_dropdown2.click()
        time.sleep(5)

    def click_admin_configuration_localization(self):
        click_admin_configuration_localization = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AdminConfigurationIconLocators.CLICK_ADMIN_CONFIGURATION_LOCALIZATION))
        click_admin_configuration_localization.click()
        time.sleep(5)

    def click_admin_configuration_dropdown3(self):
        click_admin_configuration_dropdown3 = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AdminConfigurationIconLocators.CLICK_ADMIN_CONFIGURATION_DROPDOWN))
        click_admin_configuration_dropdown3.click()
        time.sleep(5)

    def click_admin_configuration_lang_package(self):
        click_admin_configuration_lang_package = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AdminConfigurationIconLocators.CLICK_ADMIN_CONFIGURATION_LANG_PACKAGE))
        click_admin_configuration_lang_package.click()
        time.sleep(2)

    def click_admin_configuration_dropdown4(self):
        click_admin_configuration_dropdown4 = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AdminConfigurationIconLocators.CLICK_ADMIN_CONFIGURATION_DROPDOWN))
        click_admin_configuration_dropdown4.click()
        time.sleep(5)

    def click_admin_configuration_modules(self):
        click_admin_configuration_modules = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AdminConfigurationIconLocators.CLICK_ADMIN_CONFIGURATION_MODULES))
        click_admin_configuration_modules.click()
        time.sleep(2)

    def click_admin_configuration_dropdown5(self):
        click_admin_configuration_dropdown5 = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AdminConfigurationIconLocators.CLICK_ADMIN_CONFIGURATION_DROPDOWN))
        click_admin_configuration_dropdown5.click()
        time.sleep(5)

    def click_admin_configuration_social_media_aut(self):
        click_admin_configuration_social_media_aut = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AdminConfigurationIconLocators.CLICK_ADMIN_CONFIGURATION_SOCIAL_MEDIA_AUT))
        click_admin_configuration_social_media_aut.click()
        time.sleep(2)

    def click_admin_configuration_dropdown6(self):
        click_admin_configuration_dropdown6 = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AdminConfigurationIconLocators.CLICK_ADMIN_CONFIGURATION_DROPDOWN))
        click_admin_configuration_dropdown6.click()
        time.sleep(5)

    def click_admin_configuration_register_oat_client(self):
        click_admin_configuration_register_oat_client = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                AdminConfigurationIconLocators.CLICK_ADMIN_CONFIGURATION_REGISTER_OAT_CLIENT))
        click_admin_configuration_register_oat_client.click()
        time.sleep(2)

    def click_admin_configuration_dropdown7(self):
        click_admin_configuration_dropdown7 = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AdminConfigurationIconLocators.CLICK_ADMIN_CONFIGURATION_DROPDOWN))
        click_admin_configuration_dropdown7.click()
        time.sleep(5)

    def click_admin_configuration_ldap(self):
        click_admin_configuration_ldap = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AdminConfigurationIconLocators.CLICK_ADMIN_CONFIGURATION_LDAP))
        click_admin_configuration_ldap.click()
        time.sleep(5)
