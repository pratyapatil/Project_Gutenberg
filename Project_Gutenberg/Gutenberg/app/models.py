from django.db import models

 

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    language = models.CharField(max_length=50)
    subjects = models.ManyToManyField('Subject')
    bookshelves = models.ManyToManyField('Bookshelf')
    book_id=models.IntegerField(null=True)
 

class Subject(models.Model):
    name = models.CharField(max_length=100)

class Bookshelf(models.Model):
    name = models.CharField(max_length=100)

class DownloadLink(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    link = models.URLField()
    count=models.IntegerField(null=True)
    mime_type = models.CharField(max_length=50)
