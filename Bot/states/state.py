from aiogram.fsm.state import StatesGroup, State


class StateTemplate(StatesGroup):
    first_step = State()
    second_step = State()


