"""
driver.add_cookie({"name": "key", "value": "value"})
only specific keys are allowed

more keys:
expires,
max-age,
path ('/' to be accessible to all),
domain (http://www.example.ru/),
secure (https),
htttponly (doesn't allow access via API, xss => security),
samesite (xss attacks) (=None - no limits, =Lax - only safe http methods, =Strict or =SameSite - strict => cookies
cannot be sent to other websites),
"""


import time
from pprint import pprint
from selenium import webdriver

cookie_dict = {
'name': 'any_name_cookie',    # Любое имя для cookie
    'value': 'any_value_cookie',  # Любое значение для cookie
    'expiry': 2_000_000_000,      # Время жизни cookie в секундах
    'path': '/',                  # Директория на сервере дял которой будут доступны cookie
    'domain': 'parsinger.ru',     # Информация о домене и поддомене для которых доступны cookie
    'secure': True,  # or False   # Сигнал браузера о том что передать cookie только по защищённому HTTPS
    'httpOnly': True,  # or False # Ограничивает достук к cookie по средствам API
    'sameSite': 'Strict',  # or lax or none # Ограничение на передачу cookie между сайтами
}


with webdriver.Chrome() as webdriver:
    webdriver.get('https://parsinger.ru/methods/4/index.html')
    webdriver.add_cookie(cookie_dict)
    pprint(webdriver.get_cookies())
    time.sleep(120)