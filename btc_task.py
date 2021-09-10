#Import the libraries
from bs4 import BeautifulSoup
import requests
import time
import smtplib
import ssl
from email.mime.text import MIMEText as MT
from email.mime.multipart import MIMEMultipart as MM

#Create a function to get the price of a cryptocurrency
def get_crypto_price(coin):
  #Get the URL
  url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=100&page=1&sparkline=false"+coin+"+price"
#Make a request to the website
  HTML = requests.get(url)
#Parse the HTML
  soup = BeautifulSoup(HTML.text, 'html.parser')
#Find the current price
  text = soup.find("div", attrs={'class':'BNeawe iBp4i AP7Wnd'}).text
#Return the text
  return text

#Store the email addresses for the receiver, and the sender and store the senders password
receiver = '<RECEIVER_EMAIL_ADDRESS>'
sender = '<SENDER_EMAIL_ADDRESS>'
sender_password = '<SENDER_PASSWORD>'

#Create a function to send emails
def send_email(sender, receiver, sender_password, text_price):
  #Create a MIMEMutltipart Object
  msg = MM()
  msg['Subject'] = "New Crypto Price Alert !"
  msg['From']= sender
  msg['To']= receiver
#Create the HTML for the message
  HTML = """
    <html>
      <body>
        <h1>New Crypto Price Alert !</h1> 
        <h2>"""+text_price+"""
        </h2>
      </body>
    </html>
    """