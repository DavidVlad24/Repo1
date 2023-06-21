Feature: Check home page, login page and secure page functionality

  Scenario: Check checkbox link functionality
    Given Home_page: I am on home page
    When Home_page: I click on checkbox
    Then Home_page: I verify if i am on checkbox page

Scenario: Check Form Authentication link functionality
    Given Home_page: I am on home page 1
    When Home_page: I click on Form Authentication
    Then Home_page: I verify if i am on Form Authentication page

  Scenario: Check Add/Remove Elements link functionality
    Given Home_page: I am on home page 2
    When Home_page: I click on Add/Remove Elements
    Then Home_page: I verify if i am on Add/Remove Elements page

Scenario: I fill in username and password
  Given login_auth: I am a user on login page 1
  When login_auth: I fill in my username with "username"
  When login_auth: I fill in my password with "password"
  When login_auth: Click login button 1
  Then login_auth: I verify the invalid login username message "Your username is invalid!"
  Then login_auth: I verify the invalid login password message "Your password is invalid!"
  Then login_auth: Verify login message "You logged into a secure area!"
  Then login_auth: I click on log out buttton
  Then login_auth: We check the log out message "You logged out of the secure area!"


Scenario Outline: Check various pass and usernames
      Given login_auth: I am a user on login page 1
      When login_auth: I fill in my username with "<username>"
      When login_auth: I fill in my password with "<password>"
      When login_auth: Click login button 1
      Then login_auth: I verify the invalid login username message "<expected_error>!"
      Then login_auth: I verify the invalid login password message "<expected_error>"
      Then login_auth: Verify login message "<expected_notification>"
      Then login_auth: I click on log out buttton
      Then login_auth: We check the log out message "You logged out of the secure area!"

  Examples:
        | username     | password           |  expected_error            |     expected_notification      |
        | Username1    | Password1          | Your username is invalid!  |            None                |
        | None         |  None              | Your username is invalid!  |            None                |
        | tomsmith     |Password2           | Your password is invalid!  |            None                |
        | Username1    |SuperSecretPassword!| Your username is invalid!  |            None                |
        | tomsmith     |SuperSecretPassword!|            None            | You logged into a secure area! |