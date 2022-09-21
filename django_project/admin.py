from django.contrib import admin


class BookBoutAdminSite(admin.AdminSite):
    site_title = "django_project Admin Site"
    site_header = "Welcome to the  Admin Interface"
    index_title = "django_project Index"
