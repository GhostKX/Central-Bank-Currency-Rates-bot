# Central Bank Currency Exchange Rates Bot 🏦  

A **Python-based Telegram bot** that provides real-time exchange rates and currency conversion using data from the **Central Bank of Uzbekistan**. Users can check exchange rates and convert between **UZS (Uzbek Sum)** and major international currencies.  

Built using **PyTelegramBotAPI**, this bot offers a simple and interactive way to get currency exchange information.  

---

## Features  


### 📈 Exchange Rates  
- **Live Rates**: Fetches real-time exchange rates from the Central Bank of Uzbekistan  
- **Multiple Currencies**: Supports USD, EUR, RUB, GBP, and CHF  
- **Rate Changes**: Shows daily differences in exchange rates  
- **Well-Formatted Output**: Neatly structured messages with currency flags and values  


### 💸 Currency Conversion  
- **Convert UZS to Foreign Currency**  
- **Convert Foreign Currency to UZS**  
- **Uses Real-Time Exchange Rates** for accurate calculations  
- **Supports Decimal & Comma Formats** for numbers  


### 🤖 User-Friendly Interface  
- **Interactive Buttons** for smooth navigation  
- **Step-by-Step Conversion Process**  
- **Error Handling** to prevent incorrect inputs  
- **Back Navigation** to return to previous menus easily  

---

## 💱 Supported Currencies  
- 🇺🇸 **USD** (US Dollar)  
- 🇪🇺 **EUR** (Euro)  
- 🇷🇺 **RUB** (Russian Ruble)  
- 🇬🇧 **GBP** (British Pound)  
- 🇨🇭 **CHF** (Swiss Franc)  

---

## 🛠 Requirements  
- **Python 3.x**  
- **PyTelegramBotAPI** (for Telegram bot functionality)  
- **Requests** (for API calls)  
- **python-dotenv** (for managing environment variables)  

---

## 🚀 Installation  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/GhostKX/Central-Bank-Currency-Rates-bot.git
```

2. Install required dependencies
```bash
pip install -r requirements.txt
```

3. Configure the bot

- Create a .env file to store your Telegram API Key and OpenWeatherMap API Key
- Add your Telegram Bot Token:

```
API_KEY=your-telegram-bot-token
```

4. Navigate to the project directory
```bash
cd Central-Bank-Currency-Rates-bot
```

5. Run the bot
```bash
python PythonCentralBankRate_bot.py
```

---

## Usage

### Initial Setup
1. Start the bot with `/start`
2. Choose an option:
   - **📈 Currency Rate**: Get the latest exchange rates
   - **💸 Convert**: Convert currencies


### Exchange Rate Check
- Select "📈 Currency Rate"
- The bot will return exchange rates for supported currencies in a structured message
- Example output:
```
🏦 Currency Rates

📅 15 February 2025  
______________________________
🇺🇸   USD   13,003.95   +14.88    
🇪🇺   EUR   13,554.02   +79.16    
🇷🇺   RUB      143.20    +5.03     
🇬🇧   GBP   16,243.23   +74.44    
🇨🇭   CHF   14,323.11   +57.25    
______________________________

```


### Currency Conversion
1. Select "💸 Convert"
2. Choose the conversion type:
   - **UZS >>> Any**: Convert from Uzbek Sum
   - **ANY >>> UZS**: Convert to Uzbek Sum
3. Select target currency
4. Enter amount to convert
5. The bot will return the converted value



#### Example output
```
💸 Convert  

➡️ UZS >>> ANY  

💵 To USD  

💬 Enter amount in UZS: 1,300,395 

*********************************************
💵 USD: $ 100.00
*********************************************
______________________________________
Type in UZS (sum) amount 💬

🔹 Exchange Rate: 1 USD = 13,003.95 UZS  
🔹 Converted Amount: $100.00  
```

---

## Author

- Developed by **GhostKX**
- GitHub: **[GhostKX](https://github.com/GhostKX/Central-Bank-Currency-Rates-bot)**