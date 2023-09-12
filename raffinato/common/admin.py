from django.contrib import admin
from raffinato.common.models import Comment


class CommentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Comment, CommentAdmin)
