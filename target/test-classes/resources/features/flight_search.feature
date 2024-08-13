Feature: Flight search on Despegar
  As a user
  I want to search for flights
  So that I can find the best travel options

  Scenario: Search for flights from Bogotá to Santa Marta
    Given I am on the Despegar homepage
    When I enter the origin "Bogotá, Bogotá D.C., Colombia"
    And I enter the destination "San"
    And I select the travel dates
    And I click on the search button
    Then I should see the search results
