from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=50)


    @staticmethod
    def get_all_categories():
        return Categories.objects.all()


    def __str__(self):
        return self.name

