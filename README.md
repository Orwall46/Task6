# Тестовое задание

### Задание
См. [google.docs](https://docs.google.com/document/d/1RqJhk-pRDuAk4pH1uqbY9-8uwAqEXB9eRQWLSMM_9sI/edit#)

### Слово автора. 

Выполнение всех пунктов задания потребовало от меня примерно 8 часов работы. Основная трудность была с библиотекой JS от Stripe.
Почему то она у меня не хотела заводиться... Была ошибка в return response.json() -> Вот тут я долго мучался, но в итоге победил. 
От себя отмечу крутую документацию от Stripe. Все предельно ясно описано. Очень много валют для интеграции.


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

## Документация
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
