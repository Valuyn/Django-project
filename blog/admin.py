from django.contrib import admin
from .models import Post, Tag, Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('body', 'name__username')


admin.site.register(Comment, CommentAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'author', 'date_posted')
    list_filter = ('date_posted',)
    search_fields = ('title', 'author__username')


admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
