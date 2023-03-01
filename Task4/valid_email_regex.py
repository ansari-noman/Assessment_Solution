import re

valid_email_regex = r"^(?=.{1,256}$)[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$"


email = "example123@gmail.com"
if re.match(valid_email_regex, email):
    print("Valid email address!")
else:
    print("Invalid email address.")
