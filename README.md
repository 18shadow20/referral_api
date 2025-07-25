## Установка и запуск

1. Клонируйте репозиторий:

```bash
git clone https://github.com/18shadow20/referral_api
cd Hummer_system
```
2. Создайте и активируйте виртуальное окружение:

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```
3. Установите зависимости:
```bash
pip install -r requirements.txt
```
4. Настройте базу данных в settings.py.
5. Выполните миграции:
```bash
python manage.py migrate
```
6. Запустите сервер:
```bash
python manage.py runserver
```
API
1. Отправка номера телефона (получение кода)
POST /auth/phone/

Тело запроса:
```json
{
  "phone_number": "+375291111111"
}
```
2. Проверка кода авторизации
POST /auth/verify/
Тело запроса:
```json
{
  "phone_number": "+3751111111",
  "auth_verify": "1234"
}
```
3. Получение профиля пользователя
GET /profile/

Параметры:
```json
{
  "phone_number": "+375291111111"
}
```
4. Активация реферального кода
POST /profile/

Тело запроса:
```json
{
  "phone_number": "+375291111111",
  "referral_code": "rgd8g4"
}
```
Postman коллекция
Для удобства работы с API приложена коллекция Postman:
Api.postman_collection.json
