import qrcode
import cv2
import os


def main(bot):
    @bot.message_handler(commands=["makeqr"])
    def trigger_makeqr(message):
        bot.send_message(message.chat.id, "Пришлите ссылку на сайт или текст:", )
        bot.register_next_step_handler(message, makeqr)

    @bot.message_handler(commands=["readqr"])
    def trigger_readqr(message):
        bot.send_message(message.chat.id, "Пришлите qr-код:")
        bot.register_next_step_handler(message, readqr)

    def readqr(message):
        users_readqr = message.photo[-1].file_id
        file_info = bot.get_file(users_readqr)
        download_file = bot.download_file(file_info.file_path)
        with open("image.jpg", 'wb') as new_file:
            new_file.write(download_file)
        img = cv2.imread("image.jpg")
        detector = cv2.QRCodeDetector()
        data = detector.detectAndDecode(img)
        os.remove('image.jpg')
        bot.send_message(message.chat.id, data)

    def makeqr(message):
        user_link = message.text
        userqr = qrcode.make(user_link)
        userqr.save("file.png")
        bot.send_document(message.chat.id, open("file.png", "rb"))
        os.remove("file.png")
