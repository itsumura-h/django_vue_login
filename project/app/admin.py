from django.contrib import admin
from .models import User, LoginToken, Group, GroupUser, Studio, Room, Current, Booking, Equipment, EquipmentKind

# Register your models here.
admin.site.register(User)

class TokenAdmin(admin.ModelAdmin):
    fields = ['user', 'token', 'access_datetime',]
admin.site.register(LoginToken, TokenAdmin)

admin.site.register(Group)

admin.site.register(GroupUser)

admin.site.register(Studio)

admin.site.register(Room)

admin.site.register(Current)

admin.site.register(Booking)

admin.site.register(Equipment)

admin.site.register(EquipmentKind)
