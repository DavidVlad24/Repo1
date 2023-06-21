from behave import *

@Given("Home_page: I am on home page")
def step_impl(context):
    context.Home_Page.navigate_to_checkbox()

@When("Home_page: I click on checkbox")
def step_impl(context):
    context.Home_Page.click_on_checkbox()

@Then("Home_page: I verify if i am on checkbox page")
def step_impl(context):
    context.Home_Page.check_url_checkbox()


@Given("Home_page: I am on home page 1")
def step_impl(context):
    context.Home_Page.navigate_to_form_auth()

@When("Home_page: I click on Form Authentication")
def step_impl(context):
    context.Home_Page.click_on_form_auth()

@Then("Home_page: I verify if i am on Form Authentication page")
def step_impl(context):
    context.Home_Page.check_url_form_auth()


@Given("Home_page: I am on home page 2")
def step_impl(context):
    context.Home_Page.navigate_to_add_remove_elements()

@When("Home_page: I click on Add/Remove Elements")
def step_impl(context):
    context.Home_Page.click_on_add_remove_elements()

@Then("Home_page: I verify if i am on Add/Remove Elements page")
def step_impl(context):
    context.Home_Page.check_url_add_remove_elements()


