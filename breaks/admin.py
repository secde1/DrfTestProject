from django.contrib import admin

from breaks.models import organisations


@admin.register(organisations.Organisation)
class OrganisationsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'director',)


@admin.register(organisations.Group)
class OrganisationsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'manager', 'min_active',)
