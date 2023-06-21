from behave import *


@Given('login_auth: I am a user on login page 1')
def step_impl(context):
    context.login_page_auth.navigate_to_form_auth()


@When('login_auth: I fill in my username with "{u_username}"')
def step_impl(context, u_username):
    context.login_page_auth.set_username(u_username)


@When('login_auth: I fill in my password with "{p_password}"')
def step_impl(context, p_password):
    context.login_page_auth.set_password(p_password)


@When('login_auth: Click login button 1')
def step_impl(context):
    context.login_page_auth.click_login_button()


@Then('login_auth: I verify the invalid login username message "{msg1}"')
def step_impl(context, msg1):
    context.login_page_auth.verify_invalid_username_message(msg1)


@Then('login_auth: I verify the invalid login password message "{msg2}"')
def step_impl(context, msg2):
    context.login_page_auth.verify_invalid_password_message(msg2)

@Then('login_auth: Verify login message "{msg3}"')
def step_impl(context, msg3):
    context.login_page_auth.success_login_message(msg3)

@Then('login_auth: I click on log out buttton')
def step_impl(context):
    context.login_page_auth.click_logout_button()

@Then('login_auth: We check the log out message "{msg4}"')
def step_impl(context, msg4):
    context.login_page_auth.logout_message(msg4)
