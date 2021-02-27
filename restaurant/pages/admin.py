from django.contrib import admin
from pages.models import Messages
from django.contrib.auth.models import User, Group

# Register your models here.
class MyAdminSite(admin.AdminSite):
    site_header = "24 Hours Italian Restaurant"
    site_title = "24 Hours Italian Restaurant"
    index_title = "24 Hours Italian Restaurant"

admin_site = MyAdminSite()
admin_site.register([User, Group])
admin_site.register(Messages)