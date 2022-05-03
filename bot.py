import telebot
import qr
import weather
import translater
import welcomes
import shorterlinks

common_bot = telebot.TeleBot('5397870921:AAFOwpwYHFlOMNymfBIRt_ueQSpZmP0OXV8')
weather.main(common_bot, 'be0dd655bec4b0c470430cc0f02d4683')
qr.main(common_bot)
welcomes.main(common_bot)
shorterlinks.main(common_bot)
translater.main(common_bot)

common_bot.polling(True)
