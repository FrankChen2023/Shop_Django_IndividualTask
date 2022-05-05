Feature: Test new member can be added into the registered group.
    Scenario: The registration page can register new members, and those account could visit more contents.
        Given I navigate to the registration page
        When I click on the sign up botton
        Then I should redirect to login page
        Then I should be able to login the account
        Then I add new row to User and customer tables