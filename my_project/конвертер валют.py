import requests

class Currency_convertor:

    # Храним коэф. конверсии
    rates = {}
    def __init__(self, url):
        data = requests.get(url).json()
        self.rates = data["rates"]

    
    # Умножение между суммой и коэф. конверсии
    def convert(self, from_currency, to_currency, amount):
        initial_amount = amount
        if from_currency != 'EUR' :
            amount = amount / self.rates[from_currency]


    # Ставим ограничение в 2 знака после запятой
        amount = round(amount * self.rates[to_currency], 2)
        print(f'{initial_amount} {from_currency} = {amount} {to_currency}')

 

if __name__ == "__main__":
    # YOUR_ACCESS_KEY нужно получить на fixer.io
    url = str.__add__('https://api.apilayer.com/fixer/latest?apikey=', 'RuWsrUZjPM7zGedT8HlVb7qnq02RYPZx')
    c = Currency_convertor(url)
    from_country = input("From Country: ")
    to_country = input("TO Country: ")
    amount = int(input("Amount: "))

    c.convert(from_country, to_country, amount)