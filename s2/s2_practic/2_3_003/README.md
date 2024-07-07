## Кейс-задача № 3 ##

> Для тестовой задачи будем использовать python-фреймворк Django.
> В качестве веб-сервера можно взять тот, что идет в составе фреймворка.
> БД - sqlite3.

### Тестировалось в окружении: ###
* Astra Linux 1.7
  * Python 3.7
  * Django 1.11
  * Nginx 1.22

### Web-приложение доступно по адресу: ###
* Локальный сервер в составе фреймворка: http://127.0.0.1:8000/rj/
* Сторонний веб сервер: PROTOCOL://YOUR_IP_OR_DNS:PORT/rj

### На случай использования Nginx: ###
* Конфиг для nginx и юнит файл для gunicorn лежат в "other_conf"
* Конфиги настроены на каталог проекта, лежащий в "/var/www/django/"
* В "repair_journal/proj_rj/settings.py" вписать свои "ALLOWED_HOSTS"
* В "other_conf/etc/nginx/sites-available/repair_journal" вписать свой "server_name"
