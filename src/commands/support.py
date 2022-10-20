from src.objs import *

#: Support menu
@bot.message_handler(commands=['support'])
def support(message, userLanguage=None):
    userLanguage = userLanguage or dbSql.getSetting(message.chat.id, 'language')

    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text=language['joinChannelBtn'][userLanguage], url='https://t.me/the_seeker_s_cave'))
    markup.add(telebot.types.InlineKeyboardButton(text=language['shareWithFriendsBtn'][userLanguage], url=f"https://t.me/share/url?url=t.me/TSSC_Torrent_Robot&text={language['shareText'][userLanguage]}"), telebot.types.InlineKeyboardButton(text=language['joinDiscussionBtn'][userLanguage], url='https://t.me/Master_Torrenz_s_Cave'))
    markup.add(telebot.types.InlineKeyboardButton(text=language['subscribeChannelBtn'][userLanguage], url='https://www.youtube.com/channel/UCs2B-CslcZ0sTH6Tesp_-Kg'), telebot.types.InlineKeyboardButton(text=language['followGithubBtn'][userLanguage], url='https://theseekerscave.wixsite.com/seekerscave'))
    markup.add(telebot.types.InlineKeyboardButton(text=language['donateBtn'][userLanguage], url=f"https://www.paypal.com/donate/?hosted_button_id=VDL539XYV4A66"))
    
    bot.send_message(message.chat.id, language['support'][userLanguage].format(language['supportBtn'][userLanguage]), reply_markup=markup, disable_web_page_preview=True)
