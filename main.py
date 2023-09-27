from api_keys import stock, news, twilio_account_sid, TwilioAuthToken
import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

paramsstock = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": stock
}

r = requests.get(STOCK_ENDPOINT, paramsstock)
data = r.json()

data_list = [value for (key, value) in data["Time Series (Daily)"].items()]
yesterday_data = data_list[0]
yesterday_closing_price = float(yesterday_data["4. close"])
print(yesterday_closing_price)

#TODO 2. - Get the day before yesterday's closing stock price

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = float(day_before_yesterday_data["4. close"])
print(day_before_yesterday_closing_price)

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

print(format(abs(yesterday_closing_price - day_before_yesterday_closing_price), '.4f'))
difference = float(format(abs(yesterday_closing_price - day_before_yesterday_closing_price), '.4f'))

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

percentage_change = difference/yesterday_closing_price*100
print(percentage_change)
percentage_change = 6

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

if percentage_change > 5:
    print("Get News")


    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

paramsnews = {
    "qInTitle": COMPANY_NAME,
    "apiKey":news
}

if percentage_change > 5:
    response = requests.get(NEWS_ENDPOINT, paramsnews)
    data = response.json()
articles = data["articles"]

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation

if percentage_change > 5:
    three_articles = articles[:3]
    print(three_articles)
    print(len(three_articles))

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

if percentage_change > 5:
    formatted_articles = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]
    print(formatted_articles[0])

#TODO 9. - Send each article as a separate message via Twilio.

# auth_token = TwilioAuthToken
# account_sid = twilio_account_sid
# client = Client(account_sid, auth_token)
#
# text_message = ""
#
# for x in formatted_articles:
#     text_message += x
#     text_message += "\n"
# # print(text_message)
#
# message = client.messages.create(
#     from_="+18449161624",
#     body=text_message,
#     to="+14155900939"
# )
#
# print(message.sid)
# print(message.status)


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

