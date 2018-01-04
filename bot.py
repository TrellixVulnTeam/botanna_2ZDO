import requests  
import datetime
#адрес бота
url = "https://api.telegram.org/bot507226896:AAGT_fsEO1milOkqbNp-VolQDJ0tGjaPvD4/"



def lastUpdate(data):  
    results = data['result']
    total_updates = len(results) - 1
    return results[total_updates]
    
def getChatID(update):  
    chatID = update['message']['chat']['id']
    return chatID
    
def sendResp(chat, text):  
    settings = {'chat_id': chat, 'text': text}
    response = requests.post(url + 'sendMessage', data=settings)
    return response



def getUpdatesJson(request):  
    settings = {'timeout': 100, 'offset': None}
    response = requests.get(request + 'getUpdates', data=settings)
    return response.json()
    

def main():  
    chatID = getChatID(lastUpdate(getUpdatesJson(url)))
    sendResp(chatID, 'Ваше сообщение')
    updateID = lastUpdate(getUpdatesJson(url))['update_id']
    while True:
        if updateID == lastUpdate(getUpdatesJson(url))['update_id']:
           sendResp(getChatID(lastUpdate(getUpdatesJson(url))), 'проба')
           updateID += 1
    sleep(1)       




if __name__ == '__main__':  
    main()
    
