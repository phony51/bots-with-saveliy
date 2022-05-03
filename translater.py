import googletrans


def main(bot):
    @bot.message_handler(commands=["translate_from_en"])
    def to_en_trigger(message):
        bot.send_message(message.chat.id, "*Введите слово/предложение на английском:*", parse_mode="Markdown")
        bot.register_next_step_handler(message, to_en)

    def to_en(message):
        translator_en = googletrans.Translator()
        translate_en = translator_en.translate(message.text, src='en', dest='ru')
        bot.send_message(message.chat.id, translate_en.text)

    @bot.message_handler(commands=["translate_from_ru"])
    def to_ru_trigger(message):
        bot.send_message(message.chat.id, "*Введите слово/предложение на русском:*", parse_mode="Markdown")
        bot.register_next_step_handler(message, to_ru)

    def to_ru(message):
        translator_ru = googletrans.Translator()
        translate_ru = translator_ru.translate(message.text, src='ru')
        bot.send_message(message.chat.id, translate_ru.text)
