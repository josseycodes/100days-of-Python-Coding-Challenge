import requests
import json
import matplotlib.pyplot as plt
import pandas as pd

# Alpha Vantage API Key (replace with your own)
ALPHA_VANTAGE_API_KEY = 'YOUR_API_KEY'

def get_stock_price(symbol):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=1min&apikey={ALPHA_VANTAGE_API_KEY}'
    response = requests.get(url)
    data = response.json()
    latest_data = data['Time Series (1min)']
    latest_timestamp = max(latest_data.keys())
    latest_price = latest_data[latest_timestamp]['1. open']
    return float(latest_price)

def calculate_portfolio_value(portfolio):
    total_value = 0
    for stock, quantity in portfolio.items():
        price = get_stock_price(stock)
        total_value += price * quantity
    return total_value

def visualize_portfolio_performance(portfolio, portfolio_history):
    df = pd.DataFrame(portfolio_history, columns=['Date', 'Portfolio Value'])
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df['Portfolio Value'], label='Portfolio Value', color='blue')
    plt.title('Portfolio Performance')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    portfolio = {
        'AAPL': 10,
        'GOOGL': 5,
        'TSLA': 8,
    }
    
    portfolio_history = []
    
    while True:
        choice = input("Enter 'P' to see portfolio value, 'S' to analyze individual stocks, 'V' to visualize performance, or 'Q' to quit: ")
        
        if choice == 'P':
            portfolio_value = calculate_portfolio_value(portfolio)
            print(f'Current portfolio value: ${portfolio_value:.2f}')
            portfolio_history.append([pd.Timestamp.now(), portfolio_value])
        
        elif choice == 'S':
            stock_symbol = input('Enter the stock symbol: ')
            stock_quantity = portfolio.get(stock_symbol, 0)
            if stock_quantity > 0:
                stock_price = get_stock_price(stock_symbol)
                stock_value = stock_price * stock_quantity
                print(f'{stock_symbol} - Quantity: {stock_quantity}, Current Price: ${stock_price:.2f}, Total Value: ${stock_value:.2f}')
            else:
                print(f'You do not own {stock_symbol} in your portfolio.')
        
        elif choice == 'V':
            visualize_portfolio_performance(portfolio, portfolio_history)
        
        elif choice == 'Q':
            break
        
        else:
            print('Invalid choice. Please try again.')

if __name__ == '__main__':
    main() 
