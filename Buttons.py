from telebot import types


def start_bot_buttons():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    show_rates = types.KeyboardButton('📈 Currency Rate')
    convert = types.KeyboardButton('💸 Convert')
    markup.row(show_rates, convert)
    return markup


def currency_convert_type():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    uzs_any = types.KeyboardButton('UZS >>> ANY')
    any_uzs = types.KeyboardButton('ANY >>> UZS')
    back = types.KeyboardButton('⬅️ Back')
    markup.row(uzs_any, any_uzs)
    markup.add(back)
    return markup


def uzs_to_any():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    to_dollar = types.KeyboardButton('💵 To USD')
    to_euro = types.KeyboardButton('💶 To EUR')
    to_rub = types.KeyboardButton('🪙 To RUB')
    to_pound = types.KeyboardButton('💷 To GBP')
    to_frank = types.KeyboardButton('💴 To CHF')
    back = types.KeyboardButton('⬅️ Back')
    markup.row(to_dollar, to_euro, to_rub)
    markup.row(to_pound, to_frank)
    markup.add(back)
    return markup


def any_to_uzs():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    to_dollar = types.KeyboardButton('💵 From USD')
    to_euro = types.KeyboardButton('💶 From EUR')
    to_rub = types.KeyboardButton('🪙 From RUB')
    to_pound = types.KeyboardButton('💷 From GBP')
    to_frank = types.KeyboardButton('💴 From CHF')
    back = types.KeyboardButton('⬅️ Back')
    markup.row(to_dollar, to_euro, to_rub)
    markup.row(to_pound, to_frank)
    markup.add(back)
    return markup


def cancel():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    cancel_button = types.KeyboardButton('❌ Cancel')
    markup.add(cancel_button)
    return markup
