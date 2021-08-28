#----- Import Offices ----- #

import os
import telebot
import requests 
import sys
from telebot import types
telebot.logger.setLevel(__import__('logging').DEBUG)

#----- Import Offices ----- #


#----- Config ----- #
token = "1979813752:AAHso7IuJsV7Z9BI_QGtMMrUQpY1BP9hocU" # توكن بوتك
sudo_user = "or_33" # يوزرك بدون @
bot = telebot.TeleBot(token)
we = "أهلا عزيزي يجب عليك الاشتراك في قناة البوت \n قناة البوت :" #m رسالة الاشتراك الاجباري
url = "https://s.instgramblack.tk/in.php?User={}".format(sudo_user)
response = requests.get(url).json()
sudo_id = response['Info']['id']
#----- Config ----- #


#----- Open File ----- #
file = open("fcm.txt", 'r')
pr = file.readline()

file = open("admin.txt", 'r')
admin_user = file.readline()
#----- Open File ----- #


#----- Function Area ----- #
def id_ls(id):
    result = False
    file = open("users.txt", 'r')
    for line in file:
        if line.strip()==id:
            result = True
    file.close()
    return result

def bk(message):
    bk = open('users.txt', 'rb')
    bot.send_document(message.chat.id, bk)
    
def brod(message):
    mes = message.text
    f = open("users.txt","r")
    for idu in f:
        bot.send_message(idu, text="{}".format(mes))

def brod_fr(message:str):
    mes = message.text
    mei = message.id
    f = open("users.txt","r")
    for idu in f:
        bot.forward_message(idu, str(sudo_id), mei)

def show_admin(message):
    oo = open('admin.txt', "r")
    bot.send_document(message.chat.id, oo)
    
def delete_admin(message):
    me = message.text
    with open("admin.txt", "r") as f:
        lines = f.readlines()
    with open("admin.txt", "w") as f:
        for line in lines:
            if line.strip("\n") != "{}".format(me):
                f.write(line)
    bot.send_message(message.chat.id, "تم تنزيل @{} بنجاح".format(me))

def fcm(message):
    mes = message.text
    f = open("fcm.txt", 'a')
    f.write("{}\n".format(mes))
    f.close()
    bot.send_message(message.chat.id, "تم وضع {}@ قناه لشتراك اجباري".format(mes))

def admin_add(message):
    mes = message.text
    f = open("admin.txt", 'a')
    f.write("{}\n".format(mes))
    f.close()
    bot.send_message(message.chat.id, "تم رفع @{} ادمن في البوت بنجاح .".format(mes))
#----- Function Area ----- #


#----- Start Bot ----- #
@bot.message_handler(commands=['start'])
def any_msg(message:str):
    idd = message.from_user.id
    if message.chat.type == 'private':
        idu = message.from_user.id
        us = str(message.chat.first_name)
        f = open("users.txt", 'a')
        if(not id_ls(str(idu))):
            f.write("{}\n".format(idu))
            f.close()
    sub = f'https://api.telegram.org/bot{token}/getChatMember?chat_id=@{pr}&user_id={idd}'
    req = requests.get(sub)
    if idd == admin_user or sudo_user or 'member' in req.text or 'creator' in  req.text or 'administrator' in  req.text:
        bot.send_message(message.chat.id, 'أهلا بك عزيزي في بوت اشتراك اجباري . \n يمكنك اضافة البوت في المجموعه . \n و استخدامه عن طريق امر ( تفعيل البوت) .') # رسالة ستارت حقت البوت
    else:
        bot.send_message(message.chat.id, f'{we} @{pr}')

@bot.message_handler(commands=['admin'])
def any_msg(message:str):
    if message.from_user.username in sudo_user or admin_user:
        file = open('users.txt', 'r')
        li = len(file.readlines())
        file.close()
        file = open('admin.txt', 'r')
        ad = len(file.readlines())
        file.close()
        admin_keyboard = types.InlineKeyboardMarkup()
        brod = types.InlineKeyboardButton(text='أذاعه .', callback_data='brod')
        # brod_pin = types.InlineKeyboardButton(text='أذاعه بالتثبيت .', callback_data='brod')
        brod_fr = types.InlineKeyboardButton(text='أذاعه بلتوجيه .', callback_data='brod_fr')
        bk = types.InlineKeyboardButton(text='نسخه احتياطيه .', callback_data='bk')
        sub = types.InlineKeyboardButton(text=f'عدد المشتركين : {li} .', callback_data='sub')
        del_admin = types.InlineKeyboardButton(text='تنزيل ادمن .', callback_data='delete_all_admin')
        add_admin = types.InlineKeyboardButton(text='اضف ادمن .', callback_data='add_admin')
        admin_list = types.InlineKeyboardButton(text=f'عدد الادمنيه : {ad} .', callback_data='add')
        admin_show = types.InlineKeyboardButton(text=f'قائمة الادمنيه .', callback_data='show_admins')
        fc = types.InlineKeyboardButton(text=f'تعيين قناة اشتراك اجباري .', callback_data='fcc')
        admin_keyboard.row_width = 2
        admin_keyboard.add(brod,brod_fr,bk,sub,fc,add_admin,del_admin,admin_list,admin_show)
        markup_help = types.InlineKeyboardMarkup()
        bot.send_message(message.chat.id, 'أهلا عزيزي الادمن . \n يمكنك التحكم عن طريق كيبورد اسفل و شكرا .', reply_markup=admin_keyboard)
#----- Start Bot ----- #


#----- Start InLine ----- #
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == 'brod':
                mesgg = bot.send_message(call.message.chat.id, text='*ارسل لي نص الاذاعه :*', parse_mode='markdown')
                bot.register_next_step_handler(mesgg, brod)

        # if call.data == 'brod_pin':
        #         mesgg = bot.send_message(call.message.chat.id, text='*ارسل لي نص الاذاعه :*', parse_mode='markdown')
        #         bot.register_next_step_handler(mesgg, brod)

        if call.data == 'brod_fr':
            mesgg = bot.send_message(call.message.chat.id, text='*قم بتوجيه رساله لكي اقوم في اذاعاتها : *', parse_mode='markdown')
            bot.register_next_step_handler(mesgg, brod_fr)

        if call.data == 'bk':
            bk(call.message)

    if call.from_user.username in sudo_user:    
        if call.data == 'fcc':
            mesg = bot.send_message(call.message.chat.id, text='*ارسل يوزر قناة الاشتراك الاجباري :*', parse_mode='markdown')
            bot.register_next_step_handler(mesg, fcm)
    else:
        bot.send_message(call.message.chat.id, "عذرأ الامر يخص المطور الاساسي فقط .")

    if call.from_user.username in sudo_user:  
        if call.data == 'delete_all_admin':
                mesgg = bot.send_message(call.message.chat.id, text='*حسنا ارسل لي يوزر الادمن : *', parse_mode='markdown')
                bot.register_next_step_handler(mesgg, delete_admin)
    else:
        bot.send_message(call.message.chat.id, "عذرأ الامر يخص المطور الاساسي فقط .")

    if call.from_user.username in sudo_user:    
        if call.data == 'add_admin':
                mesgg = bot.send_message(call.message.chat.id, text='*حسنا ارسل لي يوزر الادمن بدون @ :*', parse_mode='markdown')
                bot.register_next_step_handler(mesgg, admin_add)
    else:
        bot.send_message(call.message.chat.id, "عذرأ الامر يخص المطور الاساسي فقط .")

    if call.from_user.username in sudo_user:    
        if call.data == 'show_admins':
            show_admin(call.message)
    else:
        bot.send_message(call.message.chat.id, "عذرأ الامر يخص المطور الاساسي فقط .")
#----- Start InLine ----- #

#----- File Run ----- #
bot.polling(none_stop=True)
#----- File Run ----- #
