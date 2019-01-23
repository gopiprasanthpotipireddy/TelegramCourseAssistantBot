from pprint import pprint
import requests

bot_token = "636526358:AAFICNoJFF5FHxyQbnrPDuUA2smCeiqYxaA"
test_url = "https://80b55509.ngrok.io/{}".format(bot_token)

#test_url = "https://gopiprasanth.pythonanywhere.com/{}".format(bot_token)
def get_url(method):
    return "https://api.telegram.org/bot{}/{}".format(bot_token,method)

d={}
d['url']=test_url
r = requests.get(get_url("setWebhook"), data=d)
r = requests.get(get_url("getWebhookInfo"))
#data={}
#data['chat_id']=118410660
#data['text']='hi iam bot friend'
#r = requests.post(get_url("sendMessage"), data=data)
pprint(r.status_code)
pprint(r.json())    