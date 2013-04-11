from django.contrib import admin
from blog.models import Entry, Comment


class CommentInline(admin.StackedInline):
#class CommentInline(admin.TabularInline):
    model = Comment
    extra = 3


class EntryAdmin(admin.ModelAdmin):
    fields = ['title', 'pub_date', 'body']
    list_display = ('pub_date', 'title')
    search_fields = ['title']
    date_hierarchy = 'pub_date'
    list_filter = ['pub_date']
    inlines = [CommentInline]
admin.site.register(Entry, EntryAdmin)


class CommentAdmin(admin.ModelAdmin):
        pass
admin.site.register(Comment, CommentAdmin)
