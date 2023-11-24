import pandas,datetime as dt,smtplib,random, os
current = dt.datetime.now()
datadf = pandas.read_csv(os.path.dirname(__file__)+"/friendsList.csv")

myEmail = "muthiahsivavelan2026@gmail.com"
password = "knuhubbiochxgtvk"

n = random.randint(1,3)
with open(os.path.dirname(__file__)+f"/letterDir/letter{n}.txt") as f:
    data = f.read()
for index,row in datadf.iterrows():
    if(row.month==current.month and row.day==current.day):
        letterMsg = data.replace("[name]",row["name"])
        with smtplib.SMTP("smtp.gmail.com:587") as connection:
            connection.starttls()
            connection.login(myEmail,password=password)
            connection.sendmail(from_addr=myEmail,to_addrs=row.email,msg=f"Subject:Wishing you happy birthday\n\n{letterMsg}".encode("utf8"))