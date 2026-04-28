**OTP Generator using Python**
This project is an implementation of an OTP-based authentication system built using Python. It generates a random OTP and sends it to the user’s email using the SMTP library. The user is then prompted to enter the OTP for verification.

**Features:**

1.Random 4-digit OTP generation
2.Email sending using SMTP (Gmail server)
3.User input-based OTP verification
4.Simple and beginner-friendly implementation

**Technologies Used:**

1.Python
2.smtplib (for email sending)
3.random module



**to run successfully**
App Password is used to securely allow the Python application to send emails without exposing the main Gmail account password.


**Gmail App Password Setup**
1.Go to https://myaccount.google.com
 and sign in
2.Open Security
3.Enable 2-Step Verification
4.In Security, click App Passwords
5.Select:
App → Mail
Device → Windows Computer (or “Other”)
Click Generate
6.Copy the 16-character password

**👉 Use it in your code:**

password = "your_app_password_here"

**⚠️ Note:**

Do not use your normal Gmail password
Remove spaces from the app password


