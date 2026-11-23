import asyncio
import requests
#from aiogram import Bot, Dispatcher, executor, types

# bot = Bot(token="fwkerjfkds")
# dp = Dispatcher(bot)

URL = "https://catalog.onliner.by/sdapi/catalog.api/search/dram"
PARAMS = {"group": 0, "group_limit": 0, "limit": 30, "dramkit[0]": "ddr4dimm", "dramkit[1]": "ddr4sodimm", "dramkit[operation]": "union"}

data = requests.get(URL, params=PARAMS).json() 

items = []
for product in data['products']:
    gb = product['description_list'][0]
    gb = gb.replace(" ГБ", "")
    items.append({"name":product['html_url'], "price": product['prices']['price_min']['amount'], "gb": gb, "desc": {product['description_list'][0]}})

items.sort(key=lambda item: float(item['price']))

prices = []
for item in items:
    prices.append({"url": item['name'], 'price': (float(item['price'])/float(item['gb'])), "desc": item['desc']})


prices.sort(key=lambda item: float(item['price']))

for price in prices:
    print(f"url:{price['url']} Стоимость за гб: {price['price']} GB total: {price['desc']}")

# @dp.message_handler(commands=["start"])
# async def start_message(message: types.Message):
#     while True:
#         text = "" 
#         for item in prices:
             #text += f"url:{item['url']} Стоимость за гб: {item['price']}\n\n"

#         await message.reply(text)
#         await asyncio.sleep(3600*24)


# if __name__ == "__main__":
#     executor.start_polling(dp, skip_updates=True)