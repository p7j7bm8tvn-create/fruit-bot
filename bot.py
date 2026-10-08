import asyncio
import json
import os
from aiogram import Bot, Dispatcher, F, types
from aiogram.types import InlineKeyboardButton, WebAppInfo, InlineKeyboardMarkup

# Токен и ссылка (пока оставим здесь, позже спрячем)
TOKEN = "8585323352:AAGmJHJ64aEznWPZr9diCKR0dRoeIbs9VfQ"
WEBAPP_URL = "https://p7j7bm8tvn-create.github.io/fruit-shop/"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(F.text == "/start")
async def start(msg: types.Message):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🛒 Открыть магазин", web_app=WebAppInfo(url=WEBAPP_URL))]
    ])
    await msg.answer("Добро пожаловать в магазин Фрукты и Овощи! Нажмите кнопку ниже, чтобы открыть каталог:", reply_markup=kb)

@dp.message(F.web_app_data)
async def handle_order(msg: types.Message):
    try:
        data = json.loads(msg.web_app_data.data)
        items_text = "\n".join([f"• {i['name']} — {i['volume']} г — {i['price']} ₽" for i in data['items']])
        text = f"✅ *Ваш заказ принят!*\n\n{items_text}\n\n💰 *Итого: {data['total']} ₽*\n\nСпасибо за заказ! Мы свяжемся с вами для уточнения доставки."
        await msg.answer(text, parse_mode="Markdown")
    except Exception as e:
        await msg.answer("Произошла ошибка при обработке заказа. Попробуйте снова.")

async def main():
    print("Бот запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
