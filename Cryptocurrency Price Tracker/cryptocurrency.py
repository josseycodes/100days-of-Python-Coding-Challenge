import requests
import matplotlib.pyplot as plt

def fetch_prices(coin_list):
    prices = {}
    for coin in coin_list:
        url = f'https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd'
        response = requests.get(url)
        data = response.json()
        prices[coin] = data[coin]['usd']
    return prices

def display_prices(prices):
    for coin, price in prices.items():
        print(f'{coin}: ${price:.2f}')

def plot_prices(prices):
    coins = list(prices.keys())
    values = list(prices.values())

    plt.figure(figsize=(10, 5))
    plt.bar(coins, values, color='skyblue')
    plt.xlabel('Cryptocurrency')
    plt.ylabel('Price (USD)')
    plt.title('Cryptocurrency Prices')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def main():
    coin_list = ['bitcoin', 'ethereum', 'ripple']  # Add more cryptocurrencies as needed
    prices = fetch_prices(coin_list)
    display_prices(prices)
    plot_prices(prices)

if __name__ == "__main__":
    main()
