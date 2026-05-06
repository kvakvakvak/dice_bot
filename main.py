import secrets
from vkbottle.bot import Bot, Message
import db

TOKEN = "vk1.a.-BTzntO46GkOubI4_KRgcvEL41LVqqoFWO19UtBTEOoRDtCyp1B9ZXhPI4gVG7ZeqJbJi-_BJ660LMkUo130Wa-6FPS_lmvtI-LZk74c5P3Pe9vD0egBeGH5TnBBk5hJDD99EyCBPrKbFR1zH3Fk0OybWeL8EYdEwHitDFLia9EP4BfqT_S5pHff_Hg3MXKaB8zxeyKqTrQKjLESABnGOQ"

db.init_db()
bot = Bot(token=TOKEN)


@bot.on.message()
async def handler(message: Message):
    text = (message.text or "").strip().lower()
    uid = message.from_id

    if text == "кинуть кубик":
        base = secrets.randbelow(101)
        if db.is_feathered(uid):
            result = min(base + 5, 100)
        else:
            result = base
        await message.answer(str(result))
        return

    if text == "надеть сорочье перышко":
        if db.is_feathered(uid):
            await message.answer("Сорочье перышко уже надето.")
        else:
            db.add_feather(uid)
            await message.answer("Сорочье перышко надето. Бросок кубика теперь +5.")
        return

    if text == "снять сорочье перышко":
        if not db.is_feathered(uid):
            await message.answer("Сорочьего перышка нет.")
        else:
            db.remove_feather(uid)
            await message.answer("Сорочье перышко снято.")
        return


if __name__ == "__main__":
    bot.run_forever()
