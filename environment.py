from browser import Browser
from pages.Home_Page import HomePage
from pages.login_page_auth import LoginPage



def before_all(context):
    context.browser = Browser()
    context.Home_Page = HomePage()
    context.login_page_auth = LoginPage()



def after_all(context):
    context.browser.close()
