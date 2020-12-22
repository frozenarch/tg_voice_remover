from pyrogram import Client, filters
from pyrogram.types import Message

app = Client(':memory:', device_model='HUY')


@app.on_message(filters.voice & filters.private)
def on_voice(_: Client, message: Message):
    message.delete()
    message.reply_text('__Карыстальнік абмежаваў войсаблядства__')


if __name__ == '__main__':
    app.run()
