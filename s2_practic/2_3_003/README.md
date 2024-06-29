## Кейс-задача № 3 ##

### Тестировалось в окружениях: ###
* Astra Linux 1.7
  * Версия Python: 3.7
  * Версия Django: 1.11
* Devuan GNU/Linux 4
  * Версия Python: 3.9
  * Версия Django: 4.2

### На случай использования Nginx: ###
* Конфиг для nginx и юнит файл для gunicorn лежат в "other_conf"
* Конфиги настроены на каталог проекта, лежащий в "/var/www/django/"
* В "repair_journal/proj_rj/settings.py" вписать свои "ALLOWED_HOSTS"
* В "other_conf/etc/nginx/sites-available/repair_journal" вписать свой "server_name"
