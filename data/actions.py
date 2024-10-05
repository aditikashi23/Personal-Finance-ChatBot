from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import requests

class ActionTrackExpense(Action):
    def name(self):
        return "action_track_expense"

    def run(self, dispatcher, tracker, domain):
        entities = tracker.latest_message['entities']
        amount = None
        category = None

        for entity in entities:
            if entity['entity'] == 'amount':
                amount = entity['value']
            if entity['entity'] == 'category':
                category = entity['value']
        
        if amount and category:
            dispatcher.utter_message(text=f"Tracked {amount} for {category} successfully!")
        else:
            dispatcher.utter_message(text="I couldn't track the expense. Please provide more details.")
        
        return []

class ActionSetBudget(Action):
    def name(self):
        return "action_set_budget"

    def run(self, dispatcher, tracker, domain):
        entities = tracker.latest_message['entities']
        amount = None
        category = None

        for entity in entities:
            if entity['entity'] == 'amount':
                amount = entity['value']
            if entity['entity'] == 'category':
                category = entity['value']
        
        # Here you can save the budget to a database or file
        if amount and category:
            dispatcher.utter_message(text=f"Budget of {amount} set for {category}.")
        else:
            dispatcher.utter_message(text="I couldn't set the budget. Please try again.")
        
        return []

class ActionCheckCurrency(Action):
    def name(self):
        return "action_check_currency"

    def run(self, dispatcher, tracker, domain):
        # Assume the user asks for "convert X USD to EUR"
        base_currency = "USD"
        target_currency = "EUR"
        amount = 100 

        # Make API call to get conversion rate
        api_key = "3d5b0a42a1144636a5f26da51d6e8884"
        url = f"https://openexchangerates.org/api/latest.json?app_id={api_key}"
        response = requests.get(url).json()
        conversion_rate = response['rates'][target_currency]

        converted_amount = amount * conversion_rate
        dispatcher.utter_message(
            text=f"{amount} {base_currency} is {converted_amount:.2f} {target_currency}."
        )
        return []

class ActionCheckStockPrice(Action):
    def name(self):
        return "action_check_stock_price"

    def run(self, dispatcher, tracker, domain):
        stock_symbol = "AAPL"

        # Make API call to get stock price
        api_key = "Y9MBYQ2HTAQQIW7F"
        url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={stock_symbol}&interval=5min&apikey={api_key}"
        response = requests.get(url).json()
        latest_price = response['Time Series (5min)'][list(response['Time Series (5min)'])[0]]['1. open']

        dispatcher.utter_message(
            text=f"The latest price for {stock_symbol} is {latest_price} USD."
        )
        return []
