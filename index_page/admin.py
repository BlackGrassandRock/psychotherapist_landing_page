from django.contrib import admin
from .models import IndexContent, Comments, Events, Services, Posts, DopFieldsIndex, Subscribers


class DopFieldsIndexAdmin(admin.StackedInline):
    model = DopFieldsIndex
    extra = 1


@admin.register(IndexContent)
class IndexContentAdmin(admin.ModelAdmin):
    inlines = [DopFieldsIndexAdmin]
    fields = ['section_title', 'title', 'image',]
    list_display = ('section_title', 'title',)
    list_filter = ('section_title',)
    search_fields = ('title', 'id', 'section_title',)


@admin.register(Comments, Posts)
class ContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'status',)
    list_filter = ('status',)
    search_fields = ('title', 'id',)


@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_of_event', 'status',)
    list_filter = ('status',)
    search_fields = ('title', 'id', 'link',)


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('title', 'status',)
    list_filter = ('status',)
    search_fields = ('title', 'id', 'link',)


@admin.register(Subscribers)
class SubscribersAdmin(admin.ModelAdmin):
    list_display = ('mail',)
    search_fields = ('mail',)