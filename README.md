# Personal Finance Chatbot

## Overview

The **Personal Finance Chatbot** is an interactive virtual assistant built using **Rasa**, designed to help users manage their finances by tracking expenses, setting budgets, and checking currency exchange rates and stock prices. The chatbot uses Rasa, REST APIs, and some Python.

### Features

- **Track Expenses**: Users can log their daily expenses by specifying the amount and category.
- **Set Budgets**: Users can establish budgets for various categories to manage their spending effectively.
- **Currency Conversion**: Users can inquire about real-time currency exchange rates and convert amounts between different currencies.
- **Stock Price Inquiry**: Users can check the latest stock prices for various stocks by specifying the stock symbol.

## Getting Started

Follow these steps to set up and run the Personal Finance Chatbot locally:

### Prerequisites

- Python 3.7 or later
- Rasa installed (you can install it using pip)

### Installation Steps

1. **Clone the Repository**
2. **Install Rasa**
3. **Run** rasa train
4. **Run** rasa run actions in another terminal
5. **Run** rasa shell --model "model_path"

#### Current Progress
- 10/05: Files are complete. Chatbot is running, but working on resolving action.py endpoint errors
- 10/15: Updated code to better respond to prompts and fix endpoint errors. Accurate responses for budget setting, but some API connection errors need to be resolved.



