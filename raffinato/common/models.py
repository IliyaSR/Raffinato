from django.db import models
from raffinato.suits.models import Suit


class Comment(models.Model):
    text = models.TextField(max_length=300)
    date_time_of_publication = models.DateTimeField(auto_now_add=True)
    to_suit = models.ForeignKey(Suit, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date_time_of_publication']


class Sizes(models.Model):
    size = models.IntegerField()
    to_suit = models.ForeignKey(Suit, on_delete=models.CASCADE)
