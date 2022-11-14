import asyncio
from time import sleep

from pyrogram import Client

from config import api_id, api_hash, tel

# TARGET = -1001782512258
# TARGET = 'yana_cinema'
# TARGET = 'indi_pitera'
CHATS = ['piter_indi', 'indi_pitera']


def get_title(self):
    name = str(self.ref).split('/')[0]
    from pyrogram import Client
    app = Client("my_account", api_id=6274889, api_hash='677311382dd96bd3ee187d35f6eba853', phone_number='+79924250282')
    title = []
    print(name)

    async def main():
        async with app:
            data = await app.get_chat(name)
            title.append(data.title)

    app.run(main())
    print(title[0])
    return title[0]
