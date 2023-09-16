import os
import json
try:
    from pyrogram import Client, filters
except:
    try:
        print('pyrogram kuruluyor...')
        os.system('sudo pip3 install pyrogram')
        from pyrogram import Client, emoji, filters
    except:
        print('pip yokmuş. önce onu kuralım :D')
        print('pip kuruluyor...')
        os.system('sudo apt install python3-pip')
        print('pyrogram kuruluyor..')
        os.system('sudo pip3 install pyrogram')
        print('kurulum tamamlandı')
        from pyrogram import Client, filters
import config
import random
bot = Client('slapbot',api_hash = config.api_hash, api_id = config.api_id, bot_token=config.slapbottoken)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

agıza_terlik = ["CgACAgQAAxkBAAIBNGT4r5L-S9lYuAqDoH8jJIw3M9XOAAK0AgAC0fBMUSzABFbFXlqkHgQ",
                "CgACAgQAAxkBAAIBYWT4x7fju4Cadg3y0cXniqYzwteOAAI-AwACR_8EU-GC5hBU3CdTHgQ"]
enseye_saplak_gif = ["CgACAgIAAxkBAAIBLGT4qcONoVCBGO64pS8gEvH6tJ3JAAKDAQAC0YPQSEI6WuAwYGhSHgQ",
                     "CgACAgQAAxkBAAIBXGT4xzNiLWUaI-IcGDMTgUwq3CXEAALyAgAChw0MUwRes_x6xeiwHgQ"]

slapMessage = [
    "{}, {}'nin üzerine benzin döktü ve ateşe verdi! 🔥",
    "{}, {}'nin kafasını balık dolu kovaya soktu! 🐠",
    "{}, {}'nin yüzüne pasta fırlattı! 🎂",
    "{}, {}'nin yüzüne bir fincan kahve döktü! ☕️",
    "{}, {}'nin yüzüne 150 $ fırlattı! 💴",
    "{}, {}'nin yüzüne bir demlik çay döktü! 🫖",
    "{}, {}'nin yüzüne bir bardak su döktü! 🚰",
    "{}, {} için aldığı hediyeyi parçaladı! 🎁",
    "{}, {}'nin yüzüne 200 $ fırlattı! 🤑",
    "{}, {}'nin yüzüne bir şişe kola döktü! 🍾",
    "{}, {}'nin üzerine tüplü TV fırlattı! 📺",
    "{}, {}'nin kalbini kırdı! 💔",
    "{}, {}'ye çiçek verdi 💐",
    "{}, {}'nin yanağından öptü 😘",
    "{}, {}'nin internetinin kablosunu kopardı 😈",
    "{}, {}'nin proje ödevini yırttı! 😳",
    "{}, {}'nin camına taş attı! 🪨",
    "{}, {}'nin ağzına tuvalet terliği ile vurdu 🩴",
    "{}, {}'nin kafasına pofuduk terlik fırlattı 😁",
    "{}, {}'nin kafasını arı kovanına soktu 🐝",
    "{}, {}'nin burnuna leblebi tıkadı 😁",
    "{}, {}'nin dişini kırdı 🦷",
    "{}, {}'nin arabasının lastiğini patlattı 🛞",
    "{}, {}'nin ciğerini çıkarıp kedilere verdi 🐈",
    "{}, {}'nin kolunu cimcirdi 😝",
    "{}, {}'nin saçlarına sakız yapıştırdı 😧",
    "{}, {}'yi Satürn'e kaçırdı 🪐",
    "{}, {}'nin saçlarına yıldız taktı 🌟",
    "{}, {}'yi Everest'in tepesinden aşağıya attı 🏔",
    "{}, {}'ye kız kulesinde çay ısmarladı 🍵",
    "{}, {}'yi valse davet etti 💃🕺",
    "{}, {}'nin kafasını su dolu kovaya daldırdı 😁",
    "{}, {}'nin çayına bisküvi bandırdı 🍪",
    "{}, {}'ni duş alırken kombiyi kapattı 😶‍🌫️",
    "{}, {}'ya kendisini çekemiyor diye anten aldı 📡",
    "{}, {}'nin fırın küreğiyle ağzına vurdu 😐",
    "{}, {}'nin akşam yemeği yerine kafasının etini yedi 😮‍💨",
    "{}, {}'e dengesizsin diyip terazi aldı ⚖️",
    "{}, {}'ya sayısalcıyım seni bir güzel çarparım dedi ✖️",
    "{}, {}'yi yanlışlıkla gruptan banladı 🙀",
    "{}, {}'nin doğum gününü kutlarken pastaya kafasını soktu 🎂",
    "{}, {}'nin ensesine şaplak attı 👀",
    "{}, {}'nin kafasını kuma gömdü 😔",
    "{}, {}'nin komple vücudunu kuma gömdü 😃"
    
]
ban_stickers = ["CgACAgQAAxkBAAIBQGT4taKQVmzbr9NB4du06OxWoVfiAAI2AwACoN4EU0FC1C_2rOhoHgQ",
                "CgACAgQAAxkBAAIBQmT4tbg96Snq1WGMpbr_iV1kSCyRAAIZAwACoUQFU4Y5Wg6FfVrfHgQ",
                "CgACAgQAAxkBAAIBRGT4tcIfXFnPv-Dwievx6m9LQiMtAAL1AgAC77oMUyjIEn-aHKIQHgQ",
                "CgACAgQAAxkBAAIBRmT4tclkkbhW-vcecRmN52AHJAxdAAIKAwACKm0NU7HAIW0RQ9qBHgQ",
                "CgACAgQAAxkBAAIBSGT4tc6NZJ2dtlMKT_27KmmluNH7AAIZAwACoUQFU4Y5Wg6FfVrfHgQ",
                "CgACAgQAAxkBAAIBSmT4tdPflTcZwgvVPZGE79ISO4XPAAI0AwACn8UEU87vRmQWq6GXHgQ",
                "CgACAgQAAxkBAAIBTGT4teAUH_5iHopTU4qVFXnfIBj0AAINAwAC_9QFUyVhmM0pnuOzHgQ",
                "CgACAgQAAxkBAAIBTmT4tffpEY4qeBDAAgqsryrkyNmIAAIEAwACEywMU0iAi25BhjS2HgQ"]

beyin_yeme = ["CgACAgQAAxkBAAIBUmT4t5z5KtN_ZKVK44Ho2hi8RxQpAALYAgACeH4MU8BdEKjqGlZeHgQ",
]
              #"CgACAgQAAxkBAAIBVGT4t6BHlWT8d0NnbJp9CzjfYbzRAAISAwACEwkFU-91LuBLmC9aHgQ",
              #"CgACAgQAAxkBAAIBVmT4t6s9odzDqIGIAsn_yvsc9XCvAAImAwACujcNUwqeE5_UbwdlHgQ"

gif_dict = {
    "{}, {}'nin ensesine şaplak attı 👀":random.choice(enseye_saplak_gif),
    "{}, {}'nin ağzına tuvalet terliği ile vurdu 🩴":random.choice(agıza_terlik),
    "{}, {}'nin komple vücudunu kuma gömdü 😃":"CgACAgQAAxkBAAIBPGT4tHyg0dzzHwX52f9t0T4EFhtmAAIJAwAChQUNU5pzyUqNSf9PHgQ",
    "{}, {}'nin doğum gününü kutlarken pastaya kafasını soktu 🎂":"CgACAgQAAxkBAAIBPmT4tUKjfyJzBygiSzewufiXBTJWAAL2AgACkmwMUywX37HDNHi4HgQ",
    "{}, {}'yi yanlışlıkla gruptan banladı 🙀":random.choice(ban_stickers),
    "{}, {}'ya sayısalcıyım seni bir güzel çarparım dedi ✖️":"CgACAgQAAxkBAAIBUGT4txLTzfhunPVgVpXF86Xo_GVJAAIqAwACHg0tU4Qaj0LrcMCUHgQ",
    "{}, {}'nin akşam yemeği yerine kafasının etini yedi 😮‍💨":random.choice(beyin_yeme),
    "{}, {}'nin üzerine benzin döktü ve ateşe verdi! 🔥":"CgACAgQAAxkBAAIBZ2T4yfEWml8KgVeYVkAvJbEGOG-vAALmAgACWpoMU4p1OtrtVm2NHgQ",
    "{}, {}'nin kafasını balık dolu kovaya soktu! 🐠":"CgACAgQAAxkBAAIBaWT4y3CCcIxrtdMfa6d69i5ZR9XlAAIKAwACtxI0U5wjGRIuHDWEHgQ",
    "{}, {}'nin yüzüne pasta fırlattı! 🎂":"CgACAgQAAxkBAAIBa2T4zAKIVhJqn5MKuyaHINDcQnLQAAIfBAACFyr8UnvScme2KqPbHgQ",
}


dontslapme = [
    "Yahu beni niye tokatlamaya çalışıyorsun 🥺",
    "😳😳",
    "Bunu yapmayacağım 😊",
    ":Dsfgasd?",
    "Kendimi tokatlattırmayacağım. 😑"
]
dontslapown = [
    "Sahibimi tokatlayamam :/",
    "Bunu çok istiyorum ama yapamam 😔",
    "Şaka yapıyor olmalısın :D",
    "Keşke mümkün olsa..."
]


#jsonda keyler int olamaz
#slaplanan puanı eklenecek

@bot.on_message(filters.command('start')&filters.private)
async def start(bot, message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    start_message = f"""
Merhaba {message.from_user.first_name}!
Ben gruplarda eğlenceli vakit geçirebilmeni sağlayacak bir slap botuyum.
"""
    keyboard = InlineKeyboardMarkup([[InlineKeyboardButton('Beni Grubuna Ekle💫', url=f"https://t.me/{config.slapbotusername}?startgroup=a"), InlineKeyboardButton('Yapımcı 🧑‍💻', user_id=config.slapbotowner)]])
    await bot.send_message(user_id, start_message, reply_markup=keyboard)
    await bot.send_message(config.slapbotowner, f"Kullanıcı: {message.from_user.first_name}\nid:<code>{message.from_user.id}</code>")



@bot.on_message(filters.command('slap'))
async def slap(bot, message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    reply_to_message = message.reply_to_message
    if message.reply_to_message != None:
        try:
            reply_from_user_id = reply_to_message.from_user.id
        except:
            return await message.reply("Grup geçmişi kapalıysa daha önceki mesajları göremem :/")
        if user_id == reply_from_user_id:
            kendini_tokatlama = ['Kendini tokatlamamalısın 🥹', 'Bunu yapmana müsaade edemem :(']
            return await message.reply(random.choice(kendini_tokatlama))
        if reply_from_user_id == config.slapbotid:
            return await message.reply(random.choice(dontslapme))
        if reply_from_user_id == config.slapbotowner:
            return await message.reply(random.choice(dontslapown))
        reply_from_user_name = reply_to_message.from_user.first_name
        random_slapMessage = random.choice(slapMessage)
        await bot.send_message(chat_id, random_slapMessage.format(f"<a href='tg://user?id={user_id}'>{first_name}</a>", f"<a href='tg://user?id={reply_from_user_id}'>{reply_from_user_name}</a>"))
        if random_slapMessage in gif_dict.keys():
            await bot.send_animation(chat_id, gif_dict[random_slapMessage])
        #db islemleri
        with open('db.json', 'r') as f:
            data = json.load(f)
        #slaplanan
        try:
            slaplanan = data["users"][str(reply_from_user_id)]
            tokatlanma_puanı = slaplanan['puan'][2] + 1
            puan = slaplanan['puan'][0] + 1
            tokat_puani = slaplanan['puan'][1]
            slaplanan.update({"puan":[puan, tokat_puani, tokatlanma_puanı]})
            with open('db.json', 'w') as f:
                json.dump(data, f, indent=4)
            
        except KeyError as e:
            tokatladı = 0
            tokatlandı = 1
            data["users"].update({reply_from_user_id:{"isim" : str(reply_from_user_name), "puan" : [tokatladı + tokatlandı, tokatladı, tokatlandı]}})
            with open('db.json', 'w') as f:
                json.dump(data, f, indent=4)
        
        #slaplayan
        try:
            user_info = data['users'][str(user_id)]
            if user_info['puan'][1] == 0:
                #ilk kez slaplıyor ama daha önce slaplanmış
                tokatladı = 1
                tokatlandı = user_info['puan'][2]
                user_info.update({ "puan" : [tokatladı + tokatlandı, tokatladı, tokatlandı]})
                with open('db.json', 'w') as f:
                    json.dump(data, f, indent=4)
            else:
                #daha önce kullanmış
                puan = user_info['puan'][0]
                puan = puan + 1
                tokatladı = user_info['puan'][1] + 1
                tokatlandı = user_info['puan'][2] 
                user_info.update({"isim" : str(first_name), "puan" : [puan, tokatladı, tokatlandı]})
                with open('db.json', 'w') as f:
                    json.dump(data, f, indent=4)
            if user_info['puan'][1] == 100:
                await message.reply('Tebrikler! Yüz kez birilerini tokatlamışsınız 😝')
            
        except KeyError as e:

            #ilk kez slaplıyor ve daha önce de hiç slaplanmamış
            tokatladı = 1
            tokatlandı = 0
            data["users"].update({user_id:{"isim" : str(first_name), "puan" : [tokatladı + tokatlandı, tokatladı, tokatlandı]}})
            with open('db.json', 'w') as f:
                json.dump(data, f, indent=4)
        
    elif len(message.command) == 2:
        slaplanan = message.command[1]
        random_slapMessage = random.choice(slapMessage)
        await bot.send_message(chat_id, random_slapMessage.format(f"<a href='tg://user?id={user_id}'>{first_name}</a>", slaplanan))
        if random_slapMessage in gif_dict.keys():
            await bot.send_animation(chat_id, gif_dict[random_slapMessage])
    else:
        await message.reply('Bana slaplamam gereken birisini göstermelisin 🥹')

@bot.on_message(filters.private&filters.animation)
async def animation(bot, message):
    chat_id = message.chat.id
    await bot.send_message(chat_id, f"{message.animation.file_id}")

def get_puan(element):
    return element['puan']

#skor tablosu
@bot.on_message(filters.command(['s[kc]or', 's[kc]orlar', 's[ıi]ralama', 'topslap']))
async def skor(bot, message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    with open('db.json', 'r') as f:
        data = json.load(f)
    if len(message.command) == 1 and message.reply_to_message == None:
        tablo = "" 
        ilk_20_id = list()
        if len(list(data['users'].keys())) < 20:
            ilk_20_id = list(data['users'].keys())[:]
        else:
            ilk_20_id = list(data['users'].keys())[20]
        isim_puan_list = []
        for i in ilk_20_id:
            isim = data['users'][str(i)]['isim']
            puan = data['users'][str(i)]['puan'][0]
            isim_puan_list.append({"isim":isim, "puan":puan})
        isim_puan_list.sort(key=get_puan, reverse=True)
        for i in enumerate(isim_puan_list):
            sira, eleman = i
            sira = sira + 1
            tablo += f"{sira}.{eleman['isim']} ⇻ {eleman['puan']}\n"
        await message.reply(tablo)
    elif message.reply_to_message != None:
        try:
            reply_user_id = message.reply_to_message.from_user.id
            replyUserInfo = data['users'][str(reply_user_id)]
            isim = replyUserInfo['isim']
            atis = replyUserInfo['puan'][1]
            alis = replyUserInfo['puan'][2]
            await message.reply(f"<b>⬥Kullanıcı: </b>{isim}\n<b>⬥Attığı tokat sayısı: </b>{atis}\n<b>⬥Yediği tokat sayısı: </b>{alis}\n<b>⬥Toplam puan: </b>{atis+alis}")
        except KeyError:
            await message.reply('Böyle bir kullanıcı bulunmuyor!')

#yeni grup
@bot.on_chat_member_updated()
async def new_chat(bot, message):
    with open('db.json', 'r') as f:
        data = json.load(f)
    chat_id = message.chat.id 
    chat_title = message.chat.title
    if "'" in chat_title:
        chat_title = chat_title.replace("'", "") 
    grup_username = message.chat.username
    if str(chat_id) in data['groups']:
        return
    else:
        link = ""
        if grup_username != None:
            link = f"t.me/{grup_username}"
        await bot.send_message(config.slapbotowner, f"Yeni grup:<a href='{link}'>{chat_title}</a> (<code>{chat_id}</code>)-Total:{str(len(data['groups']))}", disable_web_page_preview=True)
        data['groups'].update({chat_id:{"group_name":chat_title, "group_username":grup_username}})
        with open('db.json', 'w') as f:
            json.dump(data, f, indent=4)



import asyncio
async def reset_at(hard_reset = False):
    try:
        bot.terminate()
    except Exception as e:
        print('hata')
        asyncio.ensure_future(bot.stop())
        with open("tambunoktadahatavarpanpaaaa.txt", "w") as wwww:
            wwww.write(str(e))
    await asyncio.sleep(.5)
    if not hard_reset:
        os.system('sudo nohup python3 slapbot.py &')
    await asyncio.sleep(.5)

    if hard_reset:
        os.system('sudo bash /etc/rc.local')
    os.kill(os.getpid(), 9)

@bot.on_message(filters.command('res')& filters.regex('/res')&filters.private)
async def resres(bot, message):
    text = ''
    text = message.text.replace('/res ', '')
    if text == 'hard':
        await message.reply('hard reset atılıyor...')
        await reset_at(hard_reset=True)
    else:
        await message.reply('reset atılıyor...')
        await reset_at()
print("slapbot runnig")
bot.run()