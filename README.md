# OSINT Universal Checker

## Что делает этот скрипт?

- Проверяет никнеймы в соцсетях: Telegram, VK, Instagram, Twitter(X), GitHub, Discord (только по ID).
- Проверяет номер телефона (советует куда смотреть, API не встроен).

## Как использовать?

1. Установи зависимости:
    ```
    pip install requests
    ```
2. Запусти:
    ```
    python main.py
    ```
3. Введи ник или номер телефона.

## Как расширить?

- Добавь свои сервисы в переменную `SOCIALS` в main.py.
- Для проверки телефона через API добавь KEY в config.py и доработай функцию check_phone.
