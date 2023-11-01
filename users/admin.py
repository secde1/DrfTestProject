from django.contrib import admin

from users.models.users import User


@admin.register(User)  # noqa
class UsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name',)



