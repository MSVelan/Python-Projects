import requests, datetime, os,time
from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv()
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_APIKEY = os.environ.get("APIKEY_STOCK")
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
TWILIO_ENDPOINT = "https://api.twilio.com/2010-04-01"


    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

parameters = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK_NAME,
    "apikey": STOCK_APIKEY
}
#https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo


today = datetime.date.today()
s=str(today)
r = s.split("-")
r[-1] = format(int(r[-1])-2,'02d')
yesterday = "-".join(r)
r[-1] = format(int(r[-1])-1,'02d')
dayBeforeYesterday = "-".join(r)

response = requests.get(STOCK_ENDPOINT,params=parameters)
data = response.json()
yesterday_close = float(data["Time Series (Daily)"][yesterday]["4. close"])
dayBeforeYesterday_close = float(data["Time Series (Daily)"][dayBeforeYesterday]["4. close"])
print(yesterday_close, " ", dayBeforeYesterday_close)

#TODO 2. - Get the day before yesterday's closing stock price

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

percent = 0
diff = yesterday_close - dayBeforeYesterday_close
upDown = None
if(yesterday_close>dayBeforeYesterday_close):
    upDown = "🔺"
    percent = round((diff*100)/yesterday_close)
else:
    diff *= -1
    upDown = "🔻"
    percent = round((diff*100)/yesterday_close)

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

news_APIKEY = os.environ["news_APIKEY"]
news_parameters = {
    "qInTitle":COMPANY_NAME,
    "language":"en",
    "publishedAt":dayBeforeYesterday,
    "sortBy":"publishedAt",
    "apiKey": news_APIKEY
}


account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
twilioPhone = "+13613155229"

client = Client(account_sid, auth_token)


# percent = 6

if(percent>=3):
    res = requests.get(NEWS_ENDPOINT,params=news_parameters)
    newsData = res.json()
    articles = newsData["articles"][:3]

    formattedArticles = [f"{STOCK_NAME}: {upDown}{percent}%\nHeadline: {article['title']}\n Brief: {article['description']}" for article in articles]
    for article in formattedArticles:
        message = client.messages.create(
            body=article,
            from_="+13613155229",
            to="+918525021258"
        )
        print(message.body)

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

