from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin



@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug' : ('title',)}
    list_filter = ('status', 'created_on')
    summernote_fields = ('content')
    list_displyay = ('title', 'slug', ' status', 'created_on')
    search_fields = ('title', 'content')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
