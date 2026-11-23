import asyncio
import requests
from aiogram import Bot, Dispatcher, executor, types

bot = Bot(token="fwkerjfkds")
dp = Dispatcher(bot)

URL = "https://catalog.onliner.by/sdapi/catalog.api/search/dram"
PARAMS = {"group": 0, "group_limit": 0, "limit": 30, "dramkit[0]": "ddr4dimm", "dramkit[1]": "ddr4sodimm", "dramkit[operation]": "union"}

data = requests.get(URL, params=PARAMS).json() 

items = []
for product in data['products']:
    items.append({"name":product['url'], "price": product['prices']['price_min']['amount']})

items.sort(key=lambda item: float(item['price']))

for item in items:
    print(item)

'''
@dp.message_handler(commands=["start"])
async def start_message(message: types.Message):
    while True:
        text = "" 
        for item in items:
            text += item

        await message.reply(text)
        await asyncio.sleep(3600*24)'''


# if __name__ == "__main__":
#     executor.start_polling(dp, skip_updates=True)