Feature: Emag Favorites feature

      Background:
      Given home: I am a user on emag.ro Home page
      When home: I search after "biscuiti"

       @favorites1
       Scenario Outline: Test the favorites list is complete
         When products: I add product to favorites list by "<product_name>"
         When products: I click on favorites icon
         Then products: I verify that I am on favorites page
         Then favorites: I verify that the favorites list is complete by "<product_name>"

       Examples:
         |product_name                                               |
         |Biscuiti cu ciocolata si fulgi de cocos Bounty Cookies, 180g|
#         |Biscuiti cu ciocolata si caramel Mars Cookies, 162g         |

       @favorites2
       Scenario Outline: Test list has one element less, after I delete one element
             When favorites: I delete one product by "{product_name}"
             Then favorites: I see one element less in the list

             Examples:
             |product_name |
             |Biscuiti cu ciocolata si fulgi de cocos Bounty Cookies, 180g|
             |Biscuiti cu ciocolata si caramel Mars Cookies, 162g         |
