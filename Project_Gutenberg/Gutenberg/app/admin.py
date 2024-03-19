from django.contrib import admin
from app.models import Book,Bookshelf,Subject,DownloadLink
# Register your models here.
admin.site.register([Book,Bookshelf,Subject,DownloadLink])
