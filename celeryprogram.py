rom flask import Flask
from flask_celery import make_celery

app= Flask(__name__)
app.config['CELEBY_BROKER_URL']='celery/python-script/go-script'
app.config['CELEBY_BACKEND'] ='celery/python-script/go-script'

celery =make_celery(app)
@app.route('/process/<name>')
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


@celery.task()
def send_alert():
  last_price = -1;
  #Create an infinite loop to continuously send/show the price 
  while True:
    #Choose the cryptocurrency/coin
    coin = 'bitcoin'
    #Get the price of the cryptocurrency
    price = get_crypto_price(coin)
    #Check if the price has changed
    if last_price= 33,000:
      print(coin.capitalize()+' price: ', price)
      price_text = coin.capitalize()+' is '+price
      send_email(sender, receiver, sender_password, price_text)
      last_price = price #Update the last price
      time.sleep(3)

if __name__=='__nain__':
    app.run(debug=True)