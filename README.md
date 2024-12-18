# Электронная Сеть

Этот проект реализует веб-приложение для управления сетью электронных товаров, 
включающей фабрики, розничные сети и отдельных предпринимателей. Приложение 
предоставляет API для управления сетью, поставщиками, товарами и долгами, а 
также административную панель для управления данными.

## Используемые технологии

- Python 3.8+
- Django 3+
- Django Rest Framework (DRF) 3.10+
- PostgreSQL 10+
- JWT-аутентификация для безопасности API
- Django Filters для фильтрации API

## Инструкции по настройке

### 1. Клонируйте репозиторий

git clone https://github.com/Konovalexx/Electronic.git
cd Electronic

2. Создайте и активируйте виртуальное окружение
python3 -m venv venv
source venv/bin/activate  # На Windows используйте `venv\Scripts\activate`
3. Установите зависимости
pip install -r requirements.txt
4. Настройте базу данных PostgreSQL
Убедитесь, что PostgreSQL установлен и работает. Создайте базу данных с
названием torg (или любым другим на ваш выбор) и укажите данные для подключения
в файле settings.py
CREATE DATABASE torg;
5. Примените миграции
python manage.py migrate
6. Создайте суперпользователя для административной панели
python manage.py createsuperuser
7. Запустите сервер разработки
python manage.py runserver

8. Доступ к приложению
Административная панель: http://127.0.0.1:8000/admin/
Документация API (если нужно): http://127.0.0.1:8000/api/
Регистрация нового пользователя: http://127.0.0.1:8000/api/users/register/
Защищённый доступ (доступен только авторизованным пользователям): http://127.0.0.1:8000/api/users/protected/
Функции
Административная панель: Управление поставщиками, товарами и узлами сети, а 
также действия по очистке долгов.
API эндпоинты:
Поставщики: GET, POST, PUT, DELETE для работы с данными поставщиков.
Товары: GET, POST, PUT, DELETE для работы с данными товаров.
Узлы сети: GET, POST, PUT, DELETE для управления узлами сети, включая CRUD-операции и действия по очистке долгов.
JWT-аутентификация: Безопасный доступ к API через JWT токены.
Фильтрация: Фильтры для поиска узлов сети по городу, стране и уровню.
Пример использования API
Получить всех поставщиков
GET /api/suppliers/
Создать нового поставщика

POST /api/suppliers/
Content-Type: application/json
{
    "name": "Название Поставщика",
    "email": "supplier@example.com",
    "country": "Страна",
    "city": "Город",
    "street": "Улица",
    "house_number": "123",
    "debt": "100.50"
}
Получить все узлы сети (с возможностью фильтрации)

GET /api/networknodes/?country=Страна&city=Город
Очистить долги для выбранных узлов сети

POST /api/networknodes/clear-debt/
Content-Type: application/json
{
    "ids": [1, 2, 3]
}
Функции административной панели
Детали узлов сети: Показаны ссылки на поставщика, товары, сумму долга и другие
детали.
Действие очистки долга: Очистка долгов для выбранных узлов сети прямо из 
административной панели.
Фильтрация по городу: Фильтрация узлов сети по городу.
Кастомные разрешения
IsActiveUser: Разрешает доступ к API только активным пользователям.
JWT-аутентификация
Для доступа к API пользователи должны пройти аутентификацию с помощью JWT 
токенов.

Получение токена доступа

POST /api/token/
Content-Type: application/json
{
    "username": "yourusername",
    "password": "yourpassword"
}
Обновление токена

POST /api/token/refresh/
Content-Type: application/json
{
    "refresh": "yourrefresh_token"
}
Структура проекта
electronics_network: Основное приложение, содержащее модели, представления, 
сериализаторы и URL для работы с сетью.
users: Приложение для управления пользователями с функционалом регистрации и 
аутентификации.
Примечания
Убедитесь, что все необходимые зависимости установлены, запустив pip install -r requirements.txt.
Вы можете настроить базу данных и параметры JWT в файле settings.py.