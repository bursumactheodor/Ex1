from django.db import models


class Users(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100, db_index=True)
    last_name=models.CharField(max_length=100,db_index=True)
    number_of_login = models.IntegerField()


    class Meta:
     def __str__(self):
        return self.first_name

