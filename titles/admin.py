from django.contrib import admin

from .models import Title, Category, Genre


class GenreAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug")
    search_fields = ("name",)
    list_filter = ("slug",)
    empty_value_display = "-пусто-"


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug")
    search_fields = ("name",)
    list_filter = ("slug",)
    empty_value_display = "-пусто-"


class TitleAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "year",
        "description",
        "rating",
        "category",
    )
    search_fields = ("name",)
    list_filter = ("name",)
    empty_value_display = "-пусто-"


admin.site.register(Category, CategoryAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Title, TitleAdmin)

