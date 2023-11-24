import datetime as dt,os,random,smtplib
current = dt.datetime.now()
myEmail = "muthiahsivavelan2026@gmail.com"
password = "knuhubbiochxgtvk"
def getquote():
    with open(os.path.dirname(__file__)+'/quotes.txt',encoding="utf-8") as f:
        l = f.readlines()
    line = random.choice(l)
    return line
if(current.weekday()==3):
    msg = getquote()
    connection = smtplib.SMTP("smtp.gmail.com",port=587)
    connection.starttls()
    connection.login(myEmail,password=password)
    connection.sendmail(from_addr=myEmail,to_addrs="muthiahsvn@gmail.com",msg=f"Subject:Motivational quote\n\n{msg}".encode("utf8"))
    connection.close()
