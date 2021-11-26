import requests
import json
from config import keys


class ConvertionException(Exception):  #исключение
    pass #пустой класс


class CryptoConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        if quote == base:
            raise ConvertionException(f'Невозможно перевести одинаковые валюты {base}.')  # исключение

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {quote}')  # исключение

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {base}')  # исключение

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не удалось обработать количество {amount}')  # исключение

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')  # f делвет денамической, а {keys[quote]} какую валюту хотим купить , и {keys[base]} сколько хотим купить
        total_base = json.loads(r.content)[keys[base]]

        return total_base
