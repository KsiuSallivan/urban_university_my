from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

api = "7733_my_token"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


# Группа состояний
class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


# Клавиатура
keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(KeyboardButton('Рассчитать'), KeyboardButton('Информация'), KeyboardButton('Купить'))

# Inline-клавиатура для расчёта
inline_keyboard_calculation = InlineKeyboardMarkup()
inline_keyboard_calculation.add(InlineKeyboardButton('Рассчитать норму калорий', callback_data='calories'))
inline_keyboard_calculation.add(InlineKeyboardButton('Формулы расчёта', callback_data='formulas'))

# Inline-клавиатура для продуктов
inline_keyboard_products = InlineKeyboardMarkup()
inline_keyboard_products.add(InlineKeyboardButton('Product1', callback_data='product_buying'),
                             InlineKeyboardButton('Product2', callback_data='product_buying'))
inline_keyboard_products.add(InlineKeyboardButton('Product3', callback_data='product_buying'),
                             InlineKeyboardButton('Product4', callback_data='product_buying'))


# Функция для старта
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer('Привет! Выберите действие:', reply_markup=keyboard)


# Функция для вывода Inline-меню
@dp.message_handler(text='Рассчитать')
async def main_menu(message: types.Message):
    await message.answer('Выберите опцию:', reply_markup=inline_keyboard_calculation)


# Функция для вывода формулы
@dp.callback_query_handler(text='formulas')
async def get_formulas(call: types.CallbackQuery):
    await call.message.answer('Формула Миффлина-Сан Жеора:\nБМР = 10 * вес + 6.25 * рост - 5 * возраст - 161')
    await call.answer()


# Функция для установки возраста
@dp.callback_query_handler(text='calories')
async def set_age(call: types.CallbackQuery):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()


# Функция для установки роста
@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()


# Функция для установки веса
@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()


# Функция для расчета и отправки калорий
@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    await state.update_data(weight=message.text)
    data = await state.get_data()

    # Упрощенная формула Миффлина - Сан Жеора для женщин
    bmr = 10 * float(data['weight']) + 6.25 * float(data['growth']) - 5 * float(data['age']) - 161
    await message.answer(f'Ваша норма калорий: {bmr:.2f} ккал')

    await state.finish()


# Message handler, который реагирует на текст "Купить" и вызывает функцию get_buying_list
@dp.message_handler(text='Купить')
async def get_buying_list(message: types.Message):
    for i in range(1, 5):
        await message.answer(f'Название: Product{i} | Описание: описание {i} | Цена: {i * 100}')
        # Отправка картинки к каждому продукту
        with open(f'product{i}.jpg', 'rb') as photo:
            await message.answer_photo(photo)
    await message.answer('Выберите продукт для покупки:', reply_markup=inline_keyboard_products)


# Callback handler, который реагирует на "product_buying" и вызывает функцию send_confirm_message
@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call: types.CallbackQuery):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
