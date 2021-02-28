# Analysis
## **1. System Description**

The problem of sharing large amounts of contact information and social media affects many young and busy people the impact of which is a lot of time wasted by the error prone process of entering in large amounts of information manually. For all people who frequently share significant amounts of contact information QR MeNow is a QR code generating webapp that allows users to share contact information efficiently; unlike manually entering in your contact information every time, QR MeNow allows users to only input their information a single time then share a single QR code from then on. QR-MeNow is also a free service that can be used by anyone with lots of contact information, social media, and more. <br>

The **Homepage** can access the **Scanner** and **Secure Sign In** pages. The **Scanner** will open a camera so that a QR code can be scanned. The **Secure Sign In** will be a page that allows for a sign in with *username* and *password*. The **Secure Sign In** will take you to the **Account Handler** as well as the **Profile**. The **Account Handler** allows for the creation and change of a profile. The **Profile** page will have a *name*, *phone number*, *email*, and *other data* and can access the **QR Creator**. More data can be added with the **Profile Info** generic area. The **Profile Library** is the database where everyones *profiles* are stored in the *profile library*. The **QR Creator** will take the information from the **Profile** and create a *QR code*. The *QR code* is passed to the **QR Display**, which calls the **Temp Viewing Page** to display the QR's information. The **QR Creator** can also access the **QR Handler**, which allows for QR codes to be set for a limited number of *uses* or a limited amount of *time*. <br>

## __2. Model__
![](https://github.com/Oddant1/QR-MeNow/blob/main/documentation/assets/D3Model.JPG)


