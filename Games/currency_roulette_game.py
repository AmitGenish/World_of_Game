import random
import requests


def fetch_exchange_rate(from_currency, to_currency, amount):
    url = "https://currency-conversion-and-exchange-rates.p.rapidapi.com/convert"
    querystring = {"from": from_currency, "to": to_currency, "amount": str(amount)}
    headers = {
        "X-RapidAPI-Key": "ec817cac05msh837b531f1abbf31p185c56jsn8f8f3ce0b194",
        "X-RapidAPI-Host": "currency-conversion-and-exchange-rates.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        data = response.json()
        return data['result']
    else:
        return None


def get_money_interval(difficulty, usd_amount):
    ils_amount = fetch_exchange_rate("USD", "ILS", usd_amount)
    if ils_amount is not None:
        return [ils_amount - (5 * difficulty), ils_amount + (5 * difficulty)]
    else:
        print("Error fetching the exchange rate.")
        return [0, 0]


def get_guess_from_user(usd_amount):
    return float(input(f"Guess the value in ILS for ${usd_amount}: "))


def compare_results(interval, user_guess):
    return interval[0] <= user_guess <= interval[1]


def play(difficulty):
    usd_amount = random.randint(1, 100)
    interval = get_money_interval(difficulty, usd_amount)
    if interval == [0, 0]:
        print("Cannot proceed without the exchange rate.")
        return False
    user_guess = get_guess_from_user(usd_amount)
    result = compare_results(interval, user_guess)
    print("\nYou won!" if result else "\nYou lost!\n\nI would accept any answer within the range of", interval)
    return result
