# Cs 386 D7 QR-MeNow

## 1. Description
The problem of sharing large amounts of contact information and social media affects many young and busy people, the impact of which is a lot of time wasted by the error prone process of entering in large amounts of information manually. For all people who frequently share significant amounts of contact information QR MeNow is a QR code generating webapp that allows users to share contact information efficiently; unlike manually entering in your contact information every time, QR MeNow allows users to only input their information a single time then share a single QR code from then on. QR-MeNow is also a free service that can be used by anyone with lots of contact information, social media, and more.
* https://github.com/Oddant1/QR-MeNow
* https://trello.com/b/PbDwMMN3/cs386-group-project-qr-menow
* https://trello.com/b/pkVT1xEm/issue-tracker
## 2. Verification (tests)

### 2.1 Unit test - Robert

2.1.1 - Test Framework: pytest
2.1.2 - https://github.com/Oddant1/QR-MeNow/tree/main/documentation/tests/unit
2.1.3 - Also mock object https://github.com/Oddant1/QR-MeNow/blob/main/documentation/tests/unit/testDatabaseOps.py
2.1.4 - ![](https://github.com/Oddant1/QR-MeNow/blob/main/documentation/assets/D7_UnitTests.png)

### 2.2 Integration test - Jakob

2.2.1 - Test Framework: pytest
2.2.2 - https://github.com/Oddant1/QR-MeNow/tree/main/documentation/tests/Integration
2.2.3 - Test for Account Creation - https://github.com/Oddant1/QR-MeNow/tree/main/documentation/tests/Integration/testAccountCreation.py - This test goes over the entire process of creating an account, and makes sure that the database is being created and storing info correctly.
2.2.4 - ![](https://github.com/Oddant1/QR-MeNow/blob/main/documentation/assets/cs386IntegrationTests.JPG)

### 2.3 Acceptance - Kyler

2.3.1 - Test Framework: Selenium
2.3.2 - https://github.com/Oddant1/QR-MeNow/tree/main/documentation/tests/acceptence
2.3.3 - https://github.com/Oddant1/QR-MeNow/blob/main/documentation/tests/acceptence/selenium-qr-me-now-test.side
2.3.4 - https://github.com/Oddant1/QR-MeNow/blob/main/documentation/assets/acceptence-demo.mp4

## 3. Validation (user evaluation) 


## Interview 1 Aiden
How would you describe the homepage of our app? 

I would describe it as minimal but in a good way, it’s easy to navigate and find where my information is. 

On a scale of 1 to 10, how would you rate the layout of our application? 

I would give it a 7, It would be nice to see everything fit to gether a little better. 

On the same scale, how likely would you use the system in its current state?

7 again, it seems nice and convenient


## Interview 2 Shane 
How would you describe the homepage of our app?

I would describe it as smooth and fluent. The page has a nice flow to it. 

On a scale of 1 to 10, how would you rate the layout of our application? 

9, I really like how easy it is to add your information and that if I am not logged in I will get redirected to be logged in. 

On the same scale, how likely would you use the system in its current state?

9 If this system stays up I will definitely use this to share my information with coworkers. 

## Interview 3 Sara
How would you describe the homepage of our app? 

Visually pleasing, I like the choice of colors and text fonts. 

On a scale of 1 to 10, how would you rate the layout of our application? 

6 I think this is a good start to something useful but seems a little clunky with the navigation. 

On the same scale, how likely would you use the system in its current state?

5, I find that it’s easier for me to just add my information manually to someone’s phone, but it would be nice to just post this outside my office window.

## Results
Overall I would say that our results proved that we were successful in proving that we create the product we set out to from the start. We do have some feedback on what we could do to make this product better for the future. Overall the 3 people that were interviewed seemed to like the product. 

## Reflections:
What worked well in this project was the accounting system and user data. Having everyone’s data stored in a data base allowed us to make sure that a user can only have access to their own information. Along with the accounting system, the user validation system worked flawlessly, you would have to create an account and log in before you could add your information and view it. What we could have done better is having an option for the user to locally store their qr codes on their device other than just taking a screenshot. Another thing that could have been improved on is the general layout of the site. 

