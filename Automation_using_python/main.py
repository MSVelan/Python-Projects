# import smtplib

# myEmail = "muthiahsivavelan2026@gmail.com"
# password = "knuhubbiochxgtvk"
# with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
#     connection.starttls()
#     connection.login(myEmail,password=password)
#     connection.sendmail(from_addr=myEmail,to_addrs="muthiah2026@yahoo.com", msg="Subject:Hello\n\nThis is body of the email.")

import datetime as dt

current = dt.datetime.now()
print(type(current)) #datetime
year = current.year
dayOfTheWeek = current.weekday()
print(dayOfTheWeek)
print(year)

dateOfBirth = dt.datetime(year=2003,month=7,day=26)
print(dateOfBirth)