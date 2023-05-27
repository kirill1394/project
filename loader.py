from aiogram.dispatcher.filters.state import StatesGroup, State


class Start(StatesGroup):
    start_practice = State()
    start_vid = State()
    start_posledovatelnost = State()
