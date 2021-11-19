import telebot
import requests
from telebot import types
import os
#-commands_Bot-#
tok_kabos ="2103635412:AAHXnaM8ejDvX1XfRQ4k171IfdwejAJ2IsY"
bot = telebot.TeleBot(tok_kabos)
@bot.message_handler(commands = ["start"])
def kabos(message):
	c = message.chat.id
	f = message.chat.first_name
	u = message.from_user.username
	bot.reply_to(message,text=f"""*✹ - اهلا بـك فـي البوت الاول والغــي عـن نوعـه ❤️‍🔥🤖 .
✹ - اسمـــك {f} ⚜ .
✹ - ايـديك {c} ⚜  .
✹ - يــوزرك @{u} ⚜ .
✹ - مطــور البـوت : @NnKoNn 👨‍💻♥️ .
– – – – – – – – – – – – – – – – – – – – – – – –  
✹ - كـومـبو اسـيا سيـل ( رقم:رقم ) ، ارسـل /Asia 🏷 .
✹ - كـومـبو زين كاش ( رقم:رقم ) ، ارسـل /Zain 🏷 .
✹ - كـومـبو كورك ( رقم:رقم ) ، ارسـل /Korek 🏷 .
✹ - كـومـبو ايميلات لعدة دومينات ( ايميل فقط ) ، ارسـل /Email 🏷 .
✹ - كـومـبو فيزات ، ارسـل /Visa 🏷 .
– – – – – – – – – – – – – – – – – – – – – – – – 
✹ - استـمتــعو ❤️‍🔥📰 .*""",parse_mode="markdown")
@bot.message_handler(commands = ["Asia"])
def kabos(message):
    r = requests.get(f"https://tzzzzava.xyz/Apis/kabos/numbers.php?num=Asiacell")
    try:
        os.remove(f"{message.chat.id}.txt")
    except:
        pass
    open(f"AsIa.txt","a+").write(r.text)
    bot.send_document(message.chat.id,open(f"AsIa.txt","rb"),caption="* - تـم صنع كومبو اسيا سيل ✅*",parse_mode="markdown")
@bot.message_handler(commands = ["Zain"])
def kabos(message):
    r = requests.get(f"https://tzzzzava.xyz/Apis/kabos/numbers.php?num=zain")
    try:
        os.remove(f"{message.chat.id}.txt")
    except:
        pass
    open(f"ZaIn.txt","a+").write(r.text)
    bot.send_document(message.chat.id,open(f"ZaIn.txt","rb"),caption="*- تـم صنع كومبو زين (اثير)✅*",parse_mode="markdown")
@bot.message_handler(commands = ["Email"])
def kabos(message):
    r = requests.get(f"https://tzzzzava.xyz/Apis/kabos/combo-email.php")
    try:
        os.remove(f"{message.chat.id}.txt")
    except:
        pass
    open(f"EmailAll.txt","a+").write(r.text)
    bot.send_document(message.chat.id,open(f"EmailAll.txt","rb"),caption=" *- تـم صنع كومبو ايميلات ✅*",parse_mode="markdown")
@bot.message_handler(commands = ["Korek"])
def kabos(message):
    r = requests.get(f"https://tzzzzava.xyz/Apis/kabos/numbers.php?num=korek")
    try:
        os.remove(f"{message.chat.id}.txt")
    except:
        pass
    open(f"KoRek.txt","a+").write(r.text)
    bot.send_document(message.chat.id,open(f"KoRek.txt","rb"),caption="* - تـم صنع كومبو كورك ✅*",parse_mode="markdown")
@bot.message_handler(commands = ["Visa"])
def kabos(message):
    r = requests.get(f"https://tzzzzava.xyz/Apis/kabos/visamake.php")
    try:
        os.remove(f"{message.chat.id}.txt")
    except:
        pass
    open(f"VisAC.txt","a+").write(r.text)
    bot.send_document(message.chat.id,open(f"VisAC.txt","rb"),caption="* - تـم صنع كومبو فيزات ✅*",parse_mode="markdown")
bot.polling(True,timeout=4034)