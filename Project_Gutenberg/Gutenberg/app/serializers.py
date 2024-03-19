from rest_framework import serializers
from .models import Book, Subject, Bookshelf, DownloadLink

class DownloadLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = DownloadLink
        fields = ['link', 'mime_type']

class BookSerializer(serializers.ModelSerializer):
    subjects = serializers.StringRelatedField(many=True)
    bookshelves = serializers.StringRelatedField(many=True)
    download_links = DownloadLinkSerializer(many=True, source='downloadlink_set')

    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'language', 'subjects', 'bookshelves', 'download_links']
