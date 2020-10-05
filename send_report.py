import sys, csv, smtplib, ssl

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465 # With TLS
USERNAME = "naveen.p.bvm@gmail.com"
PASSWORD = "9719@Np835629"

context = ssl.create_default_context()

server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)

try:
    server.ehlo() # Can be omitted
    server.starttls(context=context) # Secure the connection
    server.ehlo() # Can be omitted
    server.login(USERNAME, PASSWORD)
    # TODO: Send email here
    server.sendmail("eportal@scindia.edu", "naveen.panwar27@gmail.com", "Hello Test Mail")
except Exception as e:
    # Print any error messages to stdout
    print(e)
finally:
    server.quit() 
