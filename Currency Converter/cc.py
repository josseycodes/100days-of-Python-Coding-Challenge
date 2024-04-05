import requests

def get_exchange_rate(base_currency, target_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    response = requests.get(url)
    data = response.json()
    exchange_rate = data['rates'][target_currency]
    return exchange_rate

def convert_currency(amount, from_currency, to_currency):
    exchange_rate = get_exchange_rate(from_currency, to_currency)
    converted_amount = amount * exchange_rate
    return converted_amount

def main():
    amount = float(input("Enter the amount: "))
    from_currency = input("From which currency (3-letter currency code): ").upper()
    to_currency = input("To which currency (3-letter currency code): ").upper()

    converted_amount = convert_currency(amount, from_currency, to_currency)
    print(f"{amount} {from_currency} is equal to {converted_amount} {to_currency}")

if __name__ == "__main__":
    main()
