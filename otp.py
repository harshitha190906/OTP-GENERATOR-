import smtplib
import random

# Generate OTP
otp = random.randint(1000, 9999)

# Email details
sender = "harshithabantrothu7@gmail.com"
receiver = input("Enter receiver email: ")

# Email message
message = f"Subject: OTP Verification\n\nYour OTP is: {otp}"

try:
    # Connect to Gmail SMTP server
    server = smtplib.SMTP("smtp.gmail.com", 587, timeout=10)
    server.starttls()

    # Login using App Password
    password = "sfgn hzqu syca cfgz"
    server.login(sender, password)

    # Send email
    server.sendmail(sender, receiver, message)
    server.quit()

    print("OTP sent successfully!")

except Exception as e:
    print("Error sending email:", e)
    exit()

# OTP Verification
try:
    user_otp = int(input("Enter the OTP you received: "))

    if user_otp == otp:
        print("Verified successfully!")
    else:
        print("Invalid OTP. Login denied.")

except ValueError:
    print("Please enter a valid numeric OTP.")
