from django.db import models


class Category(models.Model):
    id = models.IntegerField
    name = models.CharField(max_length=254)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Packages(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    id = models.IntegerField
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        verbose_name_plural = 'Packages'

    def __str__(self):
        return self.name
