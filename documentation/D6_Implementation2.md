# Cs 386 D6 QR-MeNow

## 1. Introduction
The problem of sharing large amounts of contact information and social media affects many young and busy people the impact of which is a lot of time wasted by the error prone process of entering in large amounts of information manually. For all people who frequently share significant amounts of contact information QR MeNow is a QR code generating webapp that allows users to share contact information efficiently; unlike manually entering in your contact information every time, QR MeNow allows users to only input their information a single time then share a single QR code from then on. QR-MeNow is also a free service that can be used by anyone with lots of contact information, social media, and more.
* https://github.com/Oddant1/QR-MeNow
* https://trello.com/b/PbDwMMN3/cs386-group-project-qr-menow
* https://trello.com/b/pkVT1xEm/issue-tracker
## 2. Implemented requirements 
Implemented in current release:
* Usernames and passwords
    * https://trello.com/c/xD8KD6N5/27-account-tie-to-profiles
    * Implemented by Gavin Nelson https://github.com/Oddant1/QR-MeNow/pull/36
    * Approved by Robert Bednarek
    * ![](https://github.com/Oddant1/QR-MeNow/blob/main/documentation/assets/D6UsernamePassword.png)


* Refactor code for style guide
    * https://trello.com/c/FcpaDPvr
    * Implemented by Kyler Carling https://github.com/Oddant1/QR-MeNow/pull/30
    * Approved by Robert Bednarek

* Seperation of database functionality.
    * https://trello.com/c/QZwOQIa7
    * Implemented by Kyler Carling https://github.com/Oddant1/QR-MeNow/pull/31
    * Approved by Robert Bednarek

* Session authentication
    * https://trello.com/c/0l6JpXau/36-session-auth
    * Implemented by Gavin Nelson
    https://github.com/Oddant1/QR-MeNow/pull/36
    https://github.com/Oddant1/QR-MeNow/pull/38
    * Require user to be logged in to account to access profile
    * Approved by Joshua Melo

* Profile System 
    * https://trello.com/c/xD8KD6N5/27-account-tie-to-profiles
    * Implemented by Gavin Nelson https://github.com/Oddant1/QR-MeNow/pull/36
                    * https://github.com/Oddant1/QR-MeNow/pull/38
    * Only able to view/control own card
    * Approved by Robert Bednarek

* Refactor CSS and HTML
    * https://trello.com/c/LNQZZB1G
    * Implemented by Anthony Simard https://github.com/Oddant1/QR-MeNow/pull/37
    * Approved by Robert Bednarek

## 3. Demo
https://youtu.be/zWHvANhrzjA

## 4. Code quality

To improve code quality, we agreed on a standardized style guide which increased readabillity and clarified code functionality. For example we use camelCase on our file names and snake_case on of method names. Initially we also only marginally commented our code however since the codebase starting getting larger commenting became much more important. 

## 5. Lessons learned

We learned that standardizing a development environment and code style as early as possible would have been a good idea. We had some issues related to different coding styles and some issues related to misconfigured environments. It also would have been ideal for everyone to A: have GitHub experience going into this project and B: not have a million other things on their plate. 
