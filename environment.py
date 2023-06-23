from browser import Browser
from pages.Login_Page import LoginPage
from pages.SignUp_Page import SignUpUp
from pages.base_page import PageUrl
from pages.Sign_Up_page import SignUp


def before_all(context):
    context.browser = Browser()
    context.Login_Page = LoginPage()
    context.SignUp_Page = SignUpUp()
    context.base_page = PageUrl()
    context.Sign_Up = SignUp()


def after_all(context):
    context.browser.close()
