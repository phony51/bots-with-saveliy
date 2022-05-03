import pyshorteners


def main(bot):
    @bot.message_handler(commands=["shortlink"])
    def trigger_shortlink(message):
        bot.send_message(message.chat.id, "Введите ссылку, которую хотите сократить:")
        bot.register_next_step_handler(message, shortlink)

    def shortlink(message):
        link = message.text
        s = pyshorteners.Shortener()
        bot.send_message(message.chat.id, s.tinyurl.short(link))
