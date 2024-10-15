from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests

# Custom Action to Track Expenses
class ActionTrackExpense(Action):
    def name(self) -> str:
        return "action_set_budget"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict):
        amount = tracker.get_slot("amount")
        category = tracker.get_slot("category")
        
        if amount and category:
            # Logic to track the expense (e.g., save to a database)
            dispatcher.utter_message(text=f"Expense of {amount} dollars added for {category}.")
        else:
            dispatcher.utter_message(text="Please provide both the amount and the category for your expense.")
        
        return []

# Custom Action to Check Stock Price
class ActionCheckStockPrice(Action):
    def name(self) -> str:
        return "action_check_stock_price"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict):
        stock_symbol = tracker.get_slot("stock_symbol")
        
        if stock_symbol:
            api_key = "Y9MBYQ2HTAQQIW7F"
            url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={stock_symbol}&interval=5min&apikey={api_key}"
            response = requests.get(url).json()
            latest_price = response['Time Series (5min)'][list(response['Time Series (5min)'])[0]]['1. open']
            
            if response.status_code == 200:
                dispatcher.utter_message(text=f"The current stock price of {stock_symbol} is {latest_price} USD.")
            else:
                dispatcher.utter_message(text=f"Sorry, I couldn't retrieve the stock price for {stock_symbol}.")
        else:
            dispatcher.utter_message(text="Please provide a stock symbol, like AAPL or TSLA.")
        
        return []

# Custom Action to Check Exchange Rate
class ActionCheckExchangeRate(Action):
    def name(self) -> str:
        return "action_check_currency"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict):
        amount = tracker.get_slot("amount")
        currency_from = tracker.get_slot("currency_from")
        currency_to = tracker.get_slot("currency_to")
        
        if currency_from and currency_to:
            # Example exchange rate API (you would replace this with a real API)
            api_key = "3d5b0a42a1144636a5f26da51d6e8884"
            url = f"https://openexchangerates.org/api/latest.json?app_id={api_key}"
            response = requests.get(url).json()
            conversion_rate = response['rates'][currency_from]
            
            if response.status_code == 200:
                data = response.json()
                if amount:
                    converted_amount = amount * conversion_rate
                    dispatcher.utter_message(text=f"{amount} {currency_from} is equal to {converted_amount} {currency_to}.")
                else:
                    dispatcher.utter_message(text=f"The exchange rate from {currency_from} to {currency_to} is {conversion_rate}.")
            else:
                dispatcher.utter_message(text=f"Sorry, I couldn't retrieve the exchange rate for {currency_from} to {currency_to}.")
        else:
            dispatcher.utter_message(text="Please provide the currencies you want to convert.")
        
        return []

    

