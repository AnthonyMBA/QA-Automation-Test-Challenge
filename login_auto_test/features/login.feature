Feature: Swag Labs Login
  As a user
  I want to login to saucedemo.com
  So that I can access and view product listings / inventory

  Scenario: Successful login with valid credentials
    Given I am on the saucedemo homepage
    When I enter valid credentials
    And I click on the login button
    Then I should be redirected to the inventory page

  Scenario: Failed login with invalid username
    Given I am on the saucedemo homepage
    When I enter invalid username
    And I click on the login button
    Then I should see an error message

  Scenario: Failed login with invalid password
    Given I am on the saucedemo homepage
    When I enter invalid password
    And I click on the login button
    Then I should see an error message
