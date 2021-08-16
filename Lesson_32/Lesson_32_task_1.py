import requests


url = "https://ru.wikipedia.org/wiki/Стандарт_исключений_для_роботов"
resp = requests.get(url)
print(resp)