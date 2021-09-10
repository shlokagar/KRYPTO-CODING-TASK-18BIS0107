# KRYPTO-CODING-TASK-18BIS0107
used flask,celery for btc task
used Python3 in Sublime Text IDE
Create a function to send the alert def send_alert(): last_price = -1; 
#Create an infinite loop to continuously send/show the price while True: #Choose the cryptocurrency/coin coin = 'bitcoin' 
#Get the price of the cryptocurrency price = get_crypto_price(coin)  if last_price == 33,000: print(coin.capitalize()+' price: ', price) price_text = coin.capitalize()+' is '+price send_email(sender, receiver, sender_password, price_text) last_price = price time.sleep(3)

#Send the alert finally send_alert()
