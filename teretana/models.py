from django.db import models

class Card(models.Model):
    description = models.CharField(max_length=20)
    price = models.IntegerField(max_length=10)

    def str(self):
        return self.description

class Member(models.Model):
    name = models.CharField(max_length=50)
    card_type = models.ForeignKey(Card, on_delete = models.CASCADE)

    def str(self):
        return self.name

