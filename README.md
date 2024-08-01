# Stripe integrations

### Target
Реализовать Django + Stripe API бэкенд со следующим функционалом и условиями:
Django Модель Item с полями (name, description, price) 
API с двумя методами:
- GET /buy/{id}, c помощью которого можно получить Stripe Session Id для оплаты выбранного Item. При выполнении этого метода c бэкенда с помощью python библиотеки stripe должен выполняться запрос stripe.checkout.Session.create(...) и полученный session.id выдаваться в результате запроса
- GET /item/{id}, c помощью которого можно получить простейшую HTML страницу, на которой будет информация о выбранном Item и кнопка Buy. По нажатию на кнопку Buy должен происходить запрос на /buy/{id}, получение session_id и далее  с помощью JS библиотеки Stripe происходить редирект на Checkout форму stripe.redirectToCheckout(sessionId=session_id)
  
Бонусные задачи: 
Запуск используя Docker
Использование environment variables
Просмотр Django Моделей в Django Admin панели
Запуск приложения на удаленном сервере, доступном для тестирования
Модель Order, в которой можно объединить несколько Item и сделать платёж в Stripe на содержимое Order c общей стоимостью всех Items
Модели Discount, Tax, которые можно прикрепить к модели Order и связать с соответствующими атрибутами при создании платежа в Stripe - в таком случае они корректно отображаются в Stripe Checkout форме. 
Добавить поле Item.currency, создать 2 Stripe Keypair на две разные валюты и в зависимости от валюты выбранного товара предлагать оплату в соответствующей валюте
Реализовать не Stripe Session, а Stripe Payment Intent.


### Запуск проекта:

## Первый вариант
```
git clone ...
```
Install dependencies, run virtual environment
```
python -m venv .venv
```
```
cd .venv/scripts
```
```
activate
```
```
pip install -r requirements.txt
``` 
Run Django, Postgres
```
cd Rishat
```
```
docker run --name postgres -e POSTGRES_PASSWORD=postgrespw -d postgres
```
```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Второй вариант - Docker
```
git clone ...
```
В терминале перейти в директорию, содержащую Dockerfile
```
docker-compose up -d --build
docker-compose exec app python Rishat/manage.py migrate --noinput
docker-compose exec app python Rishat/manage.py createsuperuser --username=admin
```
Перейти по адресу [localhost](http://127.0.0.1:8000/)

## Третий вариант - протестировать готовый вариант
Перейти по ссылке [autolist.site](http://autolist.site/)
Все функции доступны и работают. 
Пароль/логин от админк: admin/admin

# URL

- `/` - Главная(Домашняя) страница. 
Тут представлены все товары, которые есть в БД. Если их нет, то их можно добавить перейдя по ссылке:
- `api/v1/create_item` - Добавить товар на сайт. Указывается наименование, цена, описание и осуществляется выбор валюты. 
- `api/v1/update_item/<int:pk>` - Если мы хотим изменить товар (Цену, наименование и т.д). Также, можно удалить товар из Базы. 
- `item/<int:item_id>/` - Страница товара. Указывается описание товара и кнопка, которая совершает платеж с помощью JS библиотеки Stripe
- `buy/<int:item_id>/` - GET метод запроса stripe.checkout.Session.create(...). В ответ получаем session.id
- `intent/<int:item_id>` - На Главной странице, у карточки товара есть кнопка Intent. Реализован маленький Stripe Payment Intent.
- `my_cart/` - Страница Корзины. Тут будут все товары, которые мы добавили в корзину для единовременной покупки. 
В корзине автоматически конвертируется валюта и указывается общая цена.
- `add_to_cart/<int:item_id>/` - GET метод добавления товара в корзину. 
- `my_cart/<int:order_id>` - POST метод для удаления товара из корзины. 
- `buy_all/` - GET метод реализации покупки. При переходе на форму оплаты, товары также разделены по наименованию и цене. 
- `create_coupone/` - GET метод для создания скидки. Привязывается к id товару под номером 1. Если купить данный товар, то на него сразу будет учтена скидка. Если товара не будет/нету - Перенаправляется на Главную страницу. 
- `success/` и `cancel/` - Возращает при успехе/неудаче после формы. 
- `admin/` - Админ панель. Можно отследить все модели приложения.

## Что реализовано из бонусных задач? 
+ Запуск используя Docker
+ Использование environment variables
+ Просмотр Django Моделей в Django Admin панели
+ Запуск приложения на удаленном сервере, доступном для тестирования
+ Модель Order, в которой можно объединить несколько Item и сделать платёж в Stripe на содержимое Order c общей стоимостью всех Items
+ Модели Discount
+ Добавить поле Item.currency, создать 2 Stripe Keypair на две разные валюты и в зависимости от валюты выбранного товара предлагать оплату в соответствующей валюте
+ Реализовать не Stripe Session, а Stripe Payment Intent.
