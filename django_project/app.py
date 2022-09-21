from django.contrib.admin.apps import AdminConfig


class BookAdminConfig(AdminConfig):
    default_site = 'django_project.admin.BookBoutAdminSite'
