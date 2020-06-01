from twilio.rest import Client
import math, random

account_sid = 'AC72aa5e228e3b8871ed6d59f025006143'
auth_token = '[AuthToken]'
client = Client(account_sid, auth_token)

love_msg = ['I','L','O','V','E','Y','O','U']
def send_loves():
    for msg in love_msg:
        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body=msg,
            to='whatsapp:+919003533119'
        )

        print(message.sid)

# Flooding OTPs

# def generateOTP():
#     # Declare a digits variable
#     # which stores all digits
#     digits = "0123456789"
#     OTP = ""
#
#     # length of password can be chaged
#     # by changing value in range
#     for i in range(6):
#         OTP += digits[math.floor(random.random() * 10)]
#
#     return OTP


# count = random.randint(1, 10)
# print(count)

# def send_loves():
#     for i in range(count):
#         message = client.messages.create(
#             from_='whatsapp:+14155238886',
#             #body='Your Twilio code is 1238432',
#             body='Your OTP is '+generateOTP(),
#             to='whatsapp:+919003533119'
#         )
#
#         print(message.sid)