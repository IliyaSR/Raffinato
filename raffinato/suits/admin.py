from django.contrib import admin
from raffinato.suits.models import Suit


class SuitAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')


admin.site.register(Suit, SuitAdmin)
