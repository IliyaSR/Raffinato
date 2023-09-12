from django.contrib import admin
from raffinato.shoes.models import Shoes, Comment


class ShoesAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')


admin.site.register(Shoes, ShoesAdmin)


class CommentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Comment, CommentAdmin)



