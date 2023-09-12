from django.db import models
from django.template.defaultfilters import slugify


class Shoes(models.Model):
    name = models.CharField(max_length=30)
    personal_photo = models.URLField()
    price = models.IntegerField()
    slug = models.SlugField(unique=True, editable=False)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(f"{self.name}--{self.id}")
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Comment(models.Model):
    text = models.TextField(max_length=300)
    date_time_of_publication = models.DateTimeField(auto_now_add=True)
    to_suit = models.ForeignKey(Shoes, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date_time_of_publication']

