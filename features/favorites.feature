Feature: Emag Favorites feature

      Background:
      Given home: I am a user on emag.ro Home page
      When home: I search after "biscuiti"

       @favorites1
       Scenario Outline: Test the favorites list is complete
         When products: I add product to favorites list by "<product_name1>"
         When products: I add product to favorites list by "<product_name2>"
         When products: I click on favorites icon
         Then products: I verify that I am on favorites page
         And favorites: I verify that the favorites list is complete by "<product_name1>"
         And favorites: I verify that the favorites list is complete by "<product_name2>"

       Examples:
         |product_name1                                               |product_name2                                   |
         |Biscuiti cu ciocolata si fulgi de cocos Bounty Cookies, 180g|Jeleuri cu aroma de fructe Haribo Goldbaren,360g|


       @favorites2
       Scenario Outline: Test that after I delete an element by name from favorites,it isn't displayed anymore
         When products: I add product to favorites list by "<product_name1>"
         When products: I add product to favorites list by "<product_name2>"
         When products: I click on favorites icon
         Then products: I verify that I am on favorites page
         When favorites: I delete one product by "<product_name1>"
         Then favorites: I do not see the "<product_name1>" anymore
         When favorites: I delete one product by "<product_name2>"
         Then favorites: I do not see the "<product_name2>" anymore


       Examples:
         |product_name1                                               |product_name2                                   |
         |Biscuiti cu ciocolata si fulgi de cocos Bounty Cookies, 180g|Jeleuri cu aroma de fructe Haribo Goldbaren,360g|



