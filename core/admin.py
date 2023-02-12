from django.contrib import admin
from core.models import Note,Assignment, Category


class NoteAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'title', 'category', 'urgency', 'important', 'created_in','modified')
    list_display_links = ('id', 'title')


admin.site.register(Note, NoteAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name',)
    list_display_links = ('id', 'name')


admin.site.register(Category, CategoryAdmin)


class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'assigned_to', 'note')
    list_display_links = ('id',)


admin.site.register(Assignment, AssignmentAdmin)
