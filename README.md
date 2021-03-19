  # QR-MeNow
  CS386 Software Engineering Project

  QR MeNow is a QR code generating webapp that allows users to share contact information efficiently; unlike manually entering in your contact information every time, QR MeNow allows users to only input their information a single time then share a single QR code from then on. QR-MeNow is also a free selfhostable service that can be used by anyone with lots of contact information, social media, and more.



  # Setting up

  Clone this repo with 
  
  '''git clone https://github.com/Oddant1/QR-MeNow
  
  

  Run the create_db.py to create the initial database
  
 ''' python3 create_db.py

  Run the host-server.py to start a local copy of the service on localhost using port 5000

 ''' python3 host-server.py
 
 Now connect to the server with a web browser.

  # How to use

  There are two main ways to use this product one time uses and account based uses

  ## One Time Use QR codes

  1. Select the Generate a new qrcode option
  2. Enter in your contact information you wish to share.
  3. Have the person you want to share the qr code with scan the code

  ## Account based QR codes

  Account based qr codes have the benefit of allow you to save contact information
  and generate new codes with a limited subset of that information.

  The steps for account use are the following

  1. Register an account under the "Create an Account" section
  2. Login to your account.
  3. Three add/update your contact information to your account.
  4. select the information you want to include in a qrcode
  5. generate a new code

Obviously returning users can skip steps 1 and 3 most of the time.


