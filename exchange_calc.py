from bs4 import BeautifulSoup
import requests

def currency(input_currency, output_currency, amount):
    url = f"https://www.x-rates.com/calculator/?from={input_currency}&to={output_currency}&amount={amount}"
    content = requests.get(url).text
    soup = BeautifulSoup(content, 'html.parser')
    currency = soup.find('span', class_ = "ccOutputRslt").get_text()
    print(currency)

if __name__ == '__main__':
    currency('EUR', 'INR', '10')

