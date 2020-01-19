from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Menu, MenuPage, Address, Category, Contact, ContactPage, Home, OpenHours, Ingredient, About, Logo, SocialMedia
from translations.admin import TranslatableAdmin, TranslationInline


class InlineTranslationAdmin(TranslatableAdmin):
    inlines = [TranslationInline, ]


class IngredientsInline(admin.StackedInline):
    model = Menu.ingredients.through
    extra = 1


class MenuAdmin(admin.ModelAdmin):
    inlines = [TranslationInline]
    filter_horizontal = ("ingredients",)


class MenuInline(admin.StackedInline):
    model = Category.menu_items.through
    extra = 1


class CategoryAdmin(admin.ModelAdmin):
    inlines = [TranslationInline]
    filter_horizontal = ("menu_items", )


# Register your models here.
admin.site.register(Menu, MenuAdmin)
admin.site.register(MenuPage, InlineTranslationAdmin)
admin.site.register(Address)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Contact)
admin.site.register(ContactPage, InlineTranslationAdmin)
admin.site.register(Home, InlineTranslationAdmin)
admin.site.register(OpenHours)
admin.site.register(Ingredient, InlineTranslationAdmin)
admin.site.register(About, InlineTranslationAdmin)
admin.site.register(Logo)
admin.site.register(SocialMedia)

admin.site.site_header = _('Site Admin Panel')
