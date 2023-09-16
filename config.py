import json

with open("config.json","r") as f:
    config = json.loads(f.read())

slapbottoken = config.get("token")
slapbotadmins = config.get("slapbotadmins", None)

#bota start verenler bu idye log olarak gelecek
slapbotowner = config.get("slapbotowner", None)

slapbotid = config.get("slapbotid", None)

#beni grubuna ekle butonu için gerekli
slapbotusername = config.get("slapbotusername", "slapci_bot")

#ilk yetkilendirme için gerekli
api_hash = ""
api_id = int()