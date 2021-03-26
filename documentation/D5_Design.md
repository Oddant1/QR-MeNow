# Cs 386 D5 QR-MeNow


## 1. Description
The problem of sharing large amounts of contact information and social media affects many young and busy people the impact of which is a lot of time wasted by the error prone process of entering in large amounts of information manually. For all people who frequently share significant amounts of contact information QR MeNow is a QR code generating webapp that allows users to share contact information efficiently; unlike manually entering in your contact information every time, QR MeNow allows users to only input their information a single time then share a single QR code from then on. QR-MeNow is also a free service that can be used by anyone with lots of contact information, social media, and more.

## 2. Architecture 
![](https://github.com/Oddant1/QR-MeNow/blob/main/documentation/assets/D5ArchitectureDiagram.JPG)

The server and the app are our two primary modules. The server stores the user data in a database, and it stores the QR codes themselves on disk. The server also executes the code that actually generates QR codes. This allows the server to have access to and manage all data. The application provides a user interface to enter data into the database, generate QR codes, and view QR codes. The user has access to the application, but their interaction with the server is strictly limited to adding to their database and selecting data to generate a QR code with.

## 3. Class Diagram
![](https://github.com/Oddant1/QR-MeNow/blob/main/documentation/assets/D5ClassDiagram.JPG)

## 4. Sequence diagram
![](https://github.com/Oddant1/QR-MeNow/blob/main/documentation/assets/D5SequenceDiagram.jpg)

Use Case: Create QR code
Actor: Sender
Description: A sender creates a QR code to share contact information.
Preconditions: The sender has contact information registered.
Postconditions: The sender has a QR code they can share.
1. The sender accesses the system.
2. The sender selects create QR code.
3. The sender configures the QR code.
4. The sender confirms creation of the QR code.
5. The system generates a QR code matching their specification.
6. The QR code is stored in the system for later retrieval.

Alternative Flow:
1. If at any point the sender chooses to cancel their choices are thrown out, and no QR code is generated.

## 5. Design Patterns
### Creational: Singleton
We use what is effectively a singleton for our QR code list. It is a Python list of QRCode objects that we use as a piece of global state. We can add items to it in one function and remove items in another. All other pieces of code only view the state. This isn't specifically a singleton because it isn't a class we control that we can _only_ create one instance of. Once we start implementing more functionality, we will wrap it in a singleton described below. Right now wrapping it in a class would be overkill.

![](https://github.com/Oddant1/QR-MeNow/blob/main/documentation/assets/Singleton.png)

This is the current implementation. As stated above, it is not yet wrapped in a singleton because a list provides all the functionality we need so far.
https://github.com/Oddant1/QR-MeNow/blob/e073a94d8d68122c28b344ae68e87812352d1999/host-server.py#L15

### Structural: Facade
Our QRCode class stores metadata that we pass off to the qrcode generation code provided by the Flask library. Currently it only stores the text that will go into the generated QR code. In the future we plan on using it to store additional metadata about the code such as the amount of time the code will remain valid for. It acts as a facade for the Flask QR code implementation.

![](https://github.com/Oddant1/QR-MeNow/blob/main/documentation/assets/Facade.png)

This is the current implementation of the QRCode class. Currently it contains only the queryString.
https://github.com/Oddant1/QR-MeNow/blob/main/QRCode.py

## 6. Design Principles

Single-Reponsibility Principle: Our host-server class conntains opperations specific to the hosted webapp. our userProfile class houses opperations specific to opperations on userprofiles

Open-Closed Priciple: Our class extends the qrcode python library by creating a wrapper object which contains metadata information such as the number of remaining uses of a qr code. This is done with modify.

Liskov subsistituion prinicple: Our program does not make signifigent use of the subclasses and thus does not make signifigent use of this principle.

Interface segregation principle: None of our objects are relient on methods they do not use in order to maintain high cohesion and low coupling.

Dependency inversion principle: When interacting with user profile low level interaction is never done directly but is mediated through the user_profile_handler class which allows for refactoring underlying code without breaking functionality with the rest of the program.