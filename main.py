import requests
import re

SOCIALS = {
    "Telegram": "https://t.me/{}",
    "VK": "https://vk.com/{}",
    "Instagram": "https://instagram.com/{}",
    "Twitter": "https://twitter.com/{}",
    "GitHub": "https://github.com/{}",
    "Discord": "https://discord.com/users/{}",  # Только по Discord ID!
}

def check_social(username):
    results = {}
    for name, url in SOCIALS.items():
        if name == "Discord" and not username.isdigit():
            results[name] = "Discord ищет только по ID, а не по нику!"
            continue
        link = url.format(username)
        try:
            resp = requests.get(link, timeout=5)
            if resp.status_code == 200:
                results[name] = f"✅ Найден: {link}"
            elif resp.status_code == 404:
                results[name] = "❌ Нет такого профиля"
            else:
                results[name] = f"⚠️ Статус: {resp.status_code}"
        except Exception as e:
            results[name] = f"Ошибка: {e}"
    return results

def check_phone(phone):
    # Только базовая обработка, без API!
    phone = re.sub(r'\D', '', phone)
    if len(phone) < 10:
        return "Номер слишком короткий"
    msg = (
        f"Телефон: +{phone}\n"
        "Для подробного поиска используй сервисы: getcontact, numverify, Truecaller (нужен API-ключ)\n"
        "Либо пробей вручную на сайтах типа avito, olx, youla, whatsapp web и т.д."
    )
    return msg

def main():
    target = input("Введи ник (username) или телефон: ").strip()
    if target.isdigit() or re.match(r'^\+?\d+$', target):
        print(check_phone(target))
    else:
        results = check_social(target)
        print("=== OSINT результаты ===")
        for site, res in results.items():
            print(f"{site}: {res}")

if __name__ == "__main__":
    main()
