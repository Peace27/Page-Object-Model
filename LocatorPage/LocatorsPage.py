from selenium.webdriver.common.by import By


class LoginLocatorsPage:
    ENTER_USERNAME = (By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input")
    ENTER_PASSWORD = (By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input")
    CLICK_SUBMIT_BUTTON = (By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')


class AdminLocatorsPage:
    CLICK_ADMIN_BUTTON = (By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a")
    CLICK_ADMIN_USER_MGT_DROPDOWN = (By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[1]")
    CLICK_ADMIN_USERS = (By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul/li/a")


class AdminJobIconLocators:
    CLICK_ADMIN_JOB_DROPDOWN = (By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]/span")
    CLICK_ADMIN_JOB_JOB_TITLES = (By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[1]/a")
    CLICK_ADMIN_JOB_PAY_GRADES = (By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[2]/a")
    CLICK_ADMIN_JOB_EMPLOY_STATUS = (By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[3]")
    CLICK_ADMIN_JOB_JOB_CATEGORIES = (By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[4]/a")
    CLICK_ADMIN_JOB_WORK_SHIFT = (By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[5]")


class AdminOrganisationIconLocators:
    CLICK_ADMIN_ORG_DROPDOWN = (By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[3]/span")
    CLICK_ADMIN_ORG_GENERAL_INFO = (By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[3]/ul/li[1]")
    CLICK_ADMIN_ORG_LOCATIONS = (By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[3]/ul/li[2]/a")
    CLICK_ADMIN_ORG_STRUCTURE = (By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[3]/ul/li[3]")


class AdminQualificationsIconLocators:
    CLICK_ADMIN_QUA_DROPDOWN = (By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[4]/span")
    CLICK_ADMIN_QUA_SKILLS = (By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[4]/ul/li[1]")
    CLICK_ADMIN_QUA_EDUCATION = (By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[4]/ul/li[2]")
    CLICK_ADMIN_QUA_LICENSES = (By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[4]/ul/li[3]")
    CLICK_ADMIN_QUA_MEMBERSHIPS = (By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[4]/ul/li[5]/a")


class AdminNationalitiesIconLocators:
    CLICK_ADMIN_NATIONALITY = (By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[5]/a")


class AdminCorporateBrandingIconLocators:
    CLICK_ADMIN_COR_BRANDING = (By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[6]")


class AdminConfigurationIconLocators:
    CLICK_ADMIN_CONFIGURATION_DROPDOWN = (By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[7]/span")
    CLICK_ADMIN_CONFIGURATION_EMAIL_CONFIG = (By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[7]/ul/li[1]")
    CLICK_ADMIN_CONFIGURATION_EMAIL_SUBSCRIPT = (By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[7]/ul/li[2]/a")
    CLICK_ADMIN_CONFIGURATION_LOCALIZATION = (By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[7]/ul/li[3]/a")
    CLICK_ADMIN_CONFIGURATION_LANG_PACKAGE = (By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[7]/ul/li[4]/a")
    CLICK_ADMIN_CONFIGURATION_MODULES = (By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[7]/ul/li[5]/a")
    CLICK_ADMIN_CONFIGURATION_SOCIAL_MEDIA_AUT = (By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[7]/ul/li[6]/a")
    CLICK_ADMIN_CONFIGURATION_REGISTER_OAT_CLIENT = (By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[7]/ul/li[7]/a")
    CLICK_ADMIN_CONFIGURATION_LDAP = (By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[7]/ul/li[8]/a")
