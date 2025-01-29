from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from config.i18n import i18n_middleware

_ = i18n_middleware.i18n.gettext

router = Router()


@router.message(Command("set_language"))
async def set_language_command(message: Message, state: FSMContext):
    await message.answer(
        _("Choose the language"),
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=_("Kazakh"), callback_data="set_language:kk")],
                [InlineKeyboardButton(text=_("Russian"), callback_data="set_language:ru")],
                [InlineKeyboardButton(text=_("English"), callback_data="set_language:en")],
            ]
        )
    )


@router.callback_query(F.data.startswith("set_language:"))
async def set_language_button_handler(callback: CallbackQuery, state: FSMContext):
    __, locale = callback.data.split(":")
    await i18n_middleware.set_locale(state, locale)
    with i18n_middleware.i18n.use_locale(locale):
        _ = i18n_middleware.i18n.gettext
        response_text = _("Language changed to {locale}").format(locale=locale)

    await callback.message.answer(response_text)
