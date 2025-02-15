# Central Bank Currency Exchange Rates

import telebot
import Buttons
import requests
import datetime
from dotenv import load_dotenv
import os


# Load environment variables from .env file
load_dotenv()
API_KEY = str(os.getenv('API_KEY'))
bot = telebot.TeleBot(API_KEY)


# Command /start message handler to start the bot
@bot.message_handler(commands=['start'])
def start_bot(message):
    user_id = message.from_user.id
    bot.send_message(user_id, '✨Welcome to the Central Bank Currency Rate bot 🏦',
                     reply_markup=Buttons.start_bot_buttons())
    bot.register_next_step_handler(message, handling_user_choice)


all_currencies = []


# Handling user choice
def handling_user_choice(message):
    user_id = message.from_user.id
    if message.text == '📈 Currency Rate':
        url = 'https://cbu.uz/en/arkhiv-kursov-valyut/json/'
        bank_currency_data = requests.get(url)
        if bank_currency_data.status_code == 200:
            bank_currency_data = bank_currency_data.json()
            currencies_ids = [0, 1, 2, 3, 13]
            flag = ['🇺🇸', '🇪🇺', '🇷🇺', '🇬🇧', '🇨🇭']
            for n in currencies_ids:
                if n == 13:
                    flag_number = flag[4]
                else:
                    flag_number = flag[n]
                currency_code = bank_currency_data[n]['Ccy']
                currency_rate = bank_currency_data[n]['Rate']
                currency_diff = bank_currency_data[n]['Diff']
                if '-' in currency_diff:
                    all_currencies.append([flag_number, currency_code, currency_rate, currency_diff])
                else:
                    currency_diff = float(currency_diff)
                    all_currencies.append([flag_number, currency_code, currency_rate, f'+{currency_diff}'])

            message_to_the_user = ''
            for i in all_currencies:
                flag_country, currency_code, currency_rate, currency_diff = i
                if currency_code == 'RUB':
                    message_to_the_user += f'\n\n{flag_country:<10} {currency_code:<12} {currency_rate:<10} {currency_diff:<10}'
                else:
                    message_to_the_user += f'\n\n{flag_country:<10} {currency_code:<10} {currency_rate:<10} {currency_diff:<10}'

            today_date = datetime.date.today()
            formatted_date = today_date.strftime('%d of %B, %Y')
            bot.send_message(user_id, f'🏦 Currency Rates'
                                      f'\n\n{formatted_date}'
                                      f'\n{'_' * 30}'
                                      f'\n{message_to_the_user}'
                                      f'\n{'_' * 30}', reply_markup=Buttons.start_bot_buttons())
            all_currencies.clear()
            bot.register_next_step_handler(message, handling_user_choice)
        else:
            bot.send_message(user_id, '❌ Error. Could not retrieve data ❌'
                                      '\n\nPlease try again later 💬', reply_markup=Buttons.start_bot_buttons())
            bot.register_next_step_handler(message, start_bot)
    elif message.text == '💸 Convert':
        bot.send_message(user_id, 'Please choose convertion type 💬', reply_markup=Buttons.currency_convert_type())
        bot.register_next_step_handler(message, currency_convert_type)
    else:
        bot.send_message(user_id, '❌ Error ❌'
                                  '\n\n⬇️ Please use buttons below ⬇️', reply_markup=Buttons.start_bot_buttons())
        bot.register_next_step_handler(message, handling_user_choice)


def currency_convert_type(message):
    user_id = message.from_user.id
    if message.text == 'UZS >>> ANY':
        bot.send_message(user_id, '💰 Please choose currency type to convert to 💰',
                         reply_markup=Buttons.uzs_to_any())
        bot.register_next_step_handler(message, uzs_to_any_type)
    elif message.text == 'ANY >>> UZS':
        bot.send_message(user_id, '💰 Please choose currency type to convert to UZS 💰',
                         reply_markup=Buttons.any_to_uzs())
        bot.register_next_step_handler(message, any_type_to_uzs)
    elif message.text == '⬅️ Back':
        bot.send_message(user_id, '🔙Getting back',
                         reply_markup=Buttons.start_bot_buttons())
        bot.register_next_step_handler(message, handling_user_choice)
    else:
        bot.send_message(user_id, '❌ Error ❌'
                                  '\n\n⬇️ Please use buttons below ⬇️', reply_markup=Buttons.start_bot_buttons())
        bot.register_next_step_handler(message, currency_convert_type)


def uzs_to_any_type(message):
    user_id = message.from_user.id
    if message.text == '💵 To USD':
        bot.send_message(user_id, 'Type in UZS (sum) amount 💬', reply_markup=Buttons.cancel())
        text = '💵 USD: $'
        number = 0
        bot.register_next_step_handler(message, to_handling, user_id, number, text)
    elif message.text == '💶 To EUR':
        bot.send_message(user_id, 'Type in UZS (sum) amount 💬', reply_markup=Buttons.cancel())
        text = '💶 EUR: €'
        number = 1
        bot.register_next_step_handler(message, to_handling, user_id, number, text)
    elif message.text == '🪙 To RUB':
        bot.send_message(user_id, 'Type in UZS (sum) amount 💬', reply_markup=Buttons.cancel())
        text = '🪙 RUB: ₽'
        number = 2
        bot.register_next_step_handler(message, to_handling, user_id, number, text)
    elif message.text == '💷 To GBP':
        bot.send_message(user_id, 'Type in UZS (sum) amount 💬', reply_markup=Buttons.cancel())
        text = '💷 GBP: £'
        number = 3
        bot.register_next_step_handler(message, to_handling, user_id, number, text)
    elif message.text == '💴 To CHF':
        bot.send_message(user_id, 'Type in UZS (sum) amount 💬', reply_markup=Buttons.cancel())
        text = '💴 CHF: ₣'
        number = 13
        bot.register_next_step_handler(message, to_handling, user_id, number, text)
    elif message.text == '⬅️ Back':
        bot.send_message(user_id, '🔙 Getting back', reply_markup=Buttons.currency_convert_type())
        bot.register_next_step_handler(message, currency_convert_type)
    else:
        bot.send_message(user_id, '❌ Error ❌'
                                  '\n\n⬇️ Please use buttons below ⬇️', reply_markup=Buttons.uzs_to_any())
        bot.register_next_step_handler(message, uzs_to_any_type)


def to_handling(message, user_id, number, text):
    if message.text == '❌ Cancel':
        bot.send_message(user_id, '💰 Please choose currency type to convert to 💰',
                         reply_markup=Buttons.uzs_to_any())
        bot.register_next_step_handler(message, uzs_to_any_type)
    else:
        user_message = message.text.strip().replace(' ', '')
        user_message = user_message.replace(',', '.')
        if user_message.count('.') > 1:
            bot.send_message(user_id, '❌ Error. Invalid number ❌'
                                      '\n\nPlease try again 💬', reply_markup=Buttons.cancel())
            bot.register_next_step_handler(message, to_handling, user_id, number, text)
            return

        try:
            uzs_number = float(user_message)
            url = requests.get('https://cbu.uz/en/arkhiv-kursov-valyut/json/')
            if url.status_code == 200:
                currency_data = url.json()
                usd_buy_rate = float(currency_data[number]['Rate'])
                usd_amount = uzs_number / usd_buy_rate
                bot.send_message(user_id, f'{'*' * 45}'
                                          f'\n\n{text} {usd_amount:.2f}'
                                          f'\n\n{'*' * 45}')
                bot.send_message(user_id, f'\n{'_' * 38}'
                                          '\n\nType in UZS (sum) amount 💬', reply_markup=Buttons.cancel())
                bot.register_next_step_handler(message, to_handling, user_id, number, text)
            else:
                bot.send_message(user_id, '❌ Error. Could not retrieve data ❌'
                                          '\n\nPlease try again later 💬', reply_markup=Buttons.uzs_to_any())
                bot.register_next_step_handler(message, uzs_to_any_type)
        except ValueError:
            bot.send_message(user_id, '❌ Error. Invalid number ❌'
                                      '\n\nPlease try again 💬', reply_markup=Buttons.cancel())
            bot.register_next_step_handler(message, to_handling, user_id, number, text)


def any_type_to_uzs(message):
    user_id = message.from_user.id
    if message.text == '💵 From USD':
        bot.send_message(user_id, 'Type in USD (dollar) amount 💬', reply_markup=Buttons.cancel())
        text = 'USD (dollar)'
        number = 0
        bot.register_next_step_handler(message, from_handling, user_id, number, text)
    elif message.text == '💶 From EUR':
        bot.send_message(user_id, 'Type in EUR (euro) amount 💬', reply_markup=Buttons.cancel())
        text = 'EUR (euro)'
        number = 1
        bot.register_next_step_handler(message, from_handling, user_id, number, text)
    elif message.text == '🪙 From RUB':
        bot.send_message(user_id, 'Type in RUB (ruble) amount 💬', reply_markup=Buttons.cancel())
        text = 'RUB (ruble)'
        number = 2
        bot.register_next_step_handler(message, from_handling, user_id, number, text)
    elif message.text == '💷 From GBP':
        bot.send_message(user_id, 'Type in GBP (pound) amount 💬', reply_markup=Buttons.cancel())
        text = 'GBP (pound)'
        number = 3
        bot.register_next_step_handler(message, from_handling, user_id, number, text)
    elif message.text == '💴 From CHF':
        bot.send_message(user_id, 'Type in CHF (frank) amount 💬', reply_markup= Buttons.cancel())
        text = 'CHF (frank)'
        number = 4
        bot.register_next_step_handler(message, from_handling, user_id, number, text)
    elif message.text == '⬅️ Back':
        bot.send_message(user_id, '🔙 Getting back', reply_markup=Buttons.currency_convert_type())
        bot.register_next_step_handler(message, currency_convert_type)
    else:
        bot.send_message(user_id, '❌ Error ❌'
                                  '\n\n⬇️ Please use buttons below ⬇️', reply_markup=Buttons.uzs_to_any())
        bot.register_next_step_handler(message, uzs_to_any_type)


def from_handling(message, user_id, number, text):
    if message.text == '❌ Cancel':
        bot.send_message(user_id, '💰 Please choose currency type to convert to UZS (sum) 💰',
                         reply_markup=Buttons.any_to_uzs())
        bot.register_next_step_handler(message, any_type_to_uzs)
    else:
        user_message = message.text.strip().replace(' ', '')
        user_message = user_message.replace(',', '.')
        if user_message.count('.') > 1:
            bot.send_message(user_id, '❌ Error. Invalid number ❌'
                                      '\n\nPlease try again 💬', reply_markup=Buttons.cancel())
            bot.register_next_step_handler(message, from_handling, user_id, number, text)
            return

        try:
            currency_number = float(user_message)
            url = requests.get('https://cbu.uz/en/arkhiv-kursov-valyut/json/')
            if url.status_code == 200:
                currency_data = url.json()
                usd_sell_rate = float(currency_data[number]['Rate'])
                uzs_amount = currency_number * usd_sell_rate
                uzs_amount = f"{uzs_amount:,.0f}".replace(',', ' ')
                bot.send_message(user_id, f'{'*' * 45}'
                                          f'\n\n🏦 UZS:  {uzs_amount} sums'
                                          f'\n\n{'*' * 45}')
                bot.send_message(user_id, f'\n{'_' * 38}'
                                          f'\n\nType in {text} amount 💬', reply_markup=Buttons.cancel())
                bot.register_next_step_handler(message, from_handling, user_id, number, text)
            else:
                bot.send_message(user_id, '❌ Error. Could not retrieve data ❌'
                                          '\n\nPlease try again later 💬', reply_markup=Buttons.any_to_uzs())
                bot.register_next_step_handler(message, any_type_to_uzs)
        except ValueError:
            bot.send_message(user_id, '❌ Error. Invalid number ❌'
                                      '\n\nPlease try again 💬', reply_markup=Buttons.cancel())
            bot.register_next_step_handler(message, from_handling, user_id, number, text)


# Running the bot infinitely
bot.polling(non_stop=True)
