from django.db import models

class login_db(models.Model):
  login = models.CharField(max_length = 32)
  passwd = models.CharField(max_length = 32)
  rights = models.CharField(max_length = 32)
  session = models.CharField(max_length = 32)
  surname = models.CharField(max_length = 32)
  first_name = models.CharField(max_length = 32)
  last_name = models.CharField(max_length = 32)
  locked = models.IntegerField(default = 0)
