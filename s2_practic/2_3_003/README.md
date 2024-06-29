Кейс-задача № 3

---
Тестировалось в окружениях:
- ОС: Astra Linux 1.7
- Версия Python: 3.7
- Версия Django: 1.11


- ОС: Devuan GNU/Linux 4
- Версия Python: 3.9
- Версия Django: 4.2
---

В каталоге "other_conf" лежит конфиг для nginx и юнит файл для gunicorn. Конфиги настроены на каталог проекта, лежащий в "/var/www/django/"

P.S.\
В "repair_journal/proj_rj/settings.py" проставить свои "ALLOWED_HOSTS". В "other_conf/etc/nginx/sites-available/repair_journal" проставить свой "server_name"
