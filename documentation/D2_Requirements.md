# Requirements
## 1. Positioning
___
### 1.1 Problem Statement
The problem of sharing large amounts of contact information and social media affects many young and busy
people the impact of which is a lot of time wasted by the error prone process of entering in large amounts of
information manually.
### 1.2 Product Position Statement
For all people who frequently share significant amounts of contact information QR MeNow is a QR code
generating webapp that allows users to share contact information efficiently; unlike manually entering
in your contact information every time, QR MeNow allows users to only input their information a single
time then share a single QR code from then on.
### 1.3 Value Proposition and Consumer Segment
**Value Proposition:** QR-MeNow is a free service that allows people with a lot of contact information to
share their information more quickly and accurately than ever before. <br>
**Consumer Segment:** People who frequently share large amounts of contact information and social media.
## 2. Stakeholders
___
1. __People who frequently share large amounts of contact information__: <br>
   This is the primary demographic we are targeting with our product. These people could get a large amount of
   use out of our product because it can cut down drastically on the amount of time they need to spend entering
   their contact information.

2. __Mobile users__: <br>
   Ideally we will have an app to allow mobile users to easily access our service, but we will be starting with
   a website with an app as a stretch goal.

2. __Developers__: <br>
   The developers have a stake in the product because they are putting their time and effort into creating it.
## 3. Functional Requirements (features)
___
1. Enter contact information
2. Generate QR code
3. Share QR code
4. Limit time QR code is active for
5. Limit number of uses QR code is active for
6. Specify which contact information a QR code shares
7. Access through webapp
8. Access through downloaded Android app
9. Register an account
10. Notify a user when their QR code is used
## 4. Non-functional Requirements
___
1. Usability - 8 out of 10 testers are able to register contact information, create a QR code, set parameters
   for the QR code, and share the QR code without help or advice not available from QR MeNow itself.
2. Readability - 8 out of 10 people with relevant programming experience (other than original QR MeNow devs)
   are satisfied with the readability of the code.
3. Performance - Receives at least all Bs from https://www.webpagetest.org/
4. Reliability - Will ensure that 9 out of 10 users can access their QR codes at any given time.
5. Speed - 8 out of 10 users are satisfied with the speed of the service.
## 5. MVP
___
Our minimum viable product needs to allow a user to access our service through a webapp. The user will need to be
able to register contact information or social media account information that is stored for later retrieval. They
will then need to be able to generate a QR code that, when scanned, takes the scanner to a page displaying all of
the user's contact information. This QR code needs to persist for later retrieval by the user. We can validate these
features by having anyone (a potential end-user, or one of the devs) access the website, input some contact
information, generate a QR code, then scan that QR code with an external device and ensure that it brings them to a
page containing the registered contact information.
## 6. Use Cases
___
### 6.1 Use Case Diagram
![](https://github.com/Oddant1/QR-MeNow/blob/D2/documentation/assets/D2UseCase.png)
### 6.2 Use case descriptions and interface sketch
__Use Case 1:__ Add contact information <br>
__Actor:__ Sender <br>
__Description:__ The sender adds their contact information to the system. <br>
__Preconditions:__ The sender has an account. <br>
__Postconditions:__ The sender's contact information is in the system. <br>
__Main Flow:__ <br>
1. The sender accesses the system.
2. The sender selects add contact information.
2. The sender adds contact information to the system.
4. The sender saves their contact information
5. The contact information is added to the system <br>

__Alternative Flow:__ <br>
- If at any time the sender chooses to cancel, their contact information is thrown out
  and not stored in the system.
![](https://github.com/Oddant1/QR-MeNow/blob/D2/documentation/assets/D2UseCase1.png)

__Use Case 2:__ Update contact information <br>
__Actor:__ Sender <br>
__Description:__ The sender updates existing contact information <br>
__Preconditions:__ The sender has contact information in the system <br>
__Postconditions:__ The sender's existing contact information has been updated. <br>
__Main Flow:__ <br>
1. The sender accesses the system.
2. The sender selects edit contact information.
3. The sender selects the piece of contact information they would like to edit.
4. The sender enters their new contact information in place of the old.
6. The sender saves their new contact information.
7. The system replaces the sender's old contact information with the new. <br>

__Alternative Flow:__
- If at any point the sender chooses to cancel the operation the system retains their old
  contact information.
![](https://github.com/Oddant1/QR-MeNow/blob/D2/documentation/assets/D2UseCase2.png)

__Use Case 3:__ Create QR code <br>
__Actor:__ Sender <br>
__Description:__ A sender creates a QR code to share contact information. <br>
__Preconditions:__ The sender has contact information registered. <br>
__Postconditions:__ The sender has a QR code they can share. <br>
1. The sender accesses the system.
2. The sender selects create QR code.
3. The sender configures the QR code.
4. The sender confirms creation of the QR code.
5. The system generates a QR code matching their specification.
6. The QR code is stored in the system for later retrieval <br>

__Alternative Flow:__
- If at any point the sender chooses to cancel their choices are thrown out, and no QR code is
  generated.
![](https://github.com/Oddant1/QR-MeNow/blob/D2/documentation/assets/D2UseCase3.png)

__Use Case 4:__ Scan QR code <br>
__Actor:__ Receiver <br>
__Description:__ A receiver scans a QR code generated by a sending user. <br>
__Preconditions:__ Their is an existing QR code to be scanned. <br>
__Postconditions:__ The receiver has access to the information that QR code was configured to share. <br>
1. The receiver scans an existing QR code.
2. The system validates that the QR code is still active.
3. The system displays the contact information the QR code was configured to display to the receiver. <br>

__Alternative Flow:__ <br>
- 2a1. The system determines that the QR code scanned is no longer valid.
- 2a2. The system informs the receiver that the scanned QR code is no longer valid.
- 2b1. If the QR code has a limited number of uses, the system subtracts one from the remaining uses.
![](https://github.com/Oddant1/QR-MeNow/blob/D2/documentation/assets/D2UseCase4.png)

__Use Case 5:__ Revoke QR code <br>
__Actor:__ Sender <br>
__Description:__ A sender revokes an existing QR code. <br>
__Preconditions:__ The sender has at least one existing active QR code. <br>
__Postconditions:__ The chosen QR code is rendered invaid. <br>
1. The sender accesses the system.
2. The sender selects an existing QR code.
3. The sender chooses to delete that QR code.
4. The sender confirms deleting the QR code.
5. The system invalidates the QR code.
6. All future scans of the QR code say it is no longer valid. <br>

__Alternative Flow:__
- If at any point the sender chooses to cancel their QR code remains valid.
![](https://github.com/Oddant1/QR-MeNow/blob/D2/documentation/assets/D2UseCase5.png)

__Use Case 6:__ Pause QR code <br>
__Actor:__ Sender <br>
__Description:__ A sender renders an existing QR code temporarily invalid. <br>
__Preconditions:__ The sender has at least one existing active QR code registered. <br>
__Postconditions:__ The chosen QR code is temporarily invalid. <br>
1. The sender accesses the system.
2. The sender selects an existing QR code.
3. The sender chooses to pause that QR code.
5. The sender confirms pausing the QR code.
6. The system invalidates the QR code until resumed.
7. All scans of the QR code while it is paused say the QR code is not currently valid. <br>

__Alternative Flow:__
- If at any point the sender chooses to cancel their QR code remains valid.
![](https://github.com/Oddant1/QR-MeNow/blob/D2/documentation/assets/D2UseCase6.png)

## 7. User Stories
___
__User Story 1:__ As a user, I would like to be able to pause a QR code without permanently
  disabling it, so I can keep using it later if I choose to. __Priority: 5 Est. Hours: 1__ <br><br>
__User Story 2:__ As a user whose contact information has changed, I would like to be able to edit existing
  registered contact information, so I don't need to keep creating new entries when my contact informaiton
  changes. __Priority: 3 Est. Hours: 3__ <br><br>
__User Story 3:__ As a mobile user, I would like for the site to be designed with mobile use in mind, so it is
  easily accessible via phone. __Priority: 1 Est. Hours: 5__ <br><br>
__User Story 4:__ As a mobile user, I would ideally like an app, so I can avoid the need to use the website
 __Priority: 12 Est. Hours: 55__ <br><br>
__User Story 5:__ As a user, I would like to be able to be notified when someone uses one of my QR codes, so I
  can keep track of who is getting my contact information. __Priority: 11 Est. Hours: 30__ <br><br>
__User Story 6:__ As a user, I would like the UI to be simple, so I can easily navigate the service.
  __Priority: 2 Est. Hours: 5__ <br><br>
__User Story 7:__ As a mobile user, I would like to be able to configure the service to never notify me at
  all, so the service isn't adding to the notification spam on my phone. __Priority: 10 Est. Hours: 1__ <br><br>
__User Story 8:__ As a user, I would like to be able to configure a QR code to only share certain contact
  information, so I can tailor my QR codes to different uses. __Priority: 4 Est. Hours: 5__ <br><br>
__User Story 9:__ As a user, I would like to be able to configure a QR code to only last a certain amount of
  time, so if I'm at an event I can share my information with people at the event and not have to worry about
  deleting the QR code manually afterwards. __Priority: 6 Est. Hours: 4__ <br><br>
__User Story 10:__ As a user, I would like to be able to configure a QR code to only have a limited number of
  uses, so if I'm only trying to share it with a certain number of specific people I can share it with them and
  not have to worry about deleting the QR code manually afterwards. __Priority: 7 Est. Hours: 10__ <br><br>
__User Story 11:__ As a user, I would like to be able to share QR codes externally, so I can set them on my social
  media or personal website. __Priority: 8 Est. Hours: 3__ <br><br>
__User Story 12:__ As a user, I would like to be able to create an arbitrary number of QR codes, so I can have
  different codes configured for different situations. __Priority: 9 Est. Hours: 10__ <br>
## 8. Issue Tracker
___
https://trello.com/b/pkVT1xEm/issue-tracker </br>
![](https://github.com/Oddant1/QR-MeNow/blob/D2/documentation/assets/D2Trello.png)