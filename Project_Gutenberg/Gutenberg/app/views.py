from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.db.models import Q
from app.models import Book
from app.serializers import BookSerializer
from app.pagination import CustomPageNumberPagination
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.db import models

 
class GetALLBooks(APIView):
    @swagger_auto_schema(
        operation_description="This API is used for getting All Books",
        operation_summary="Get all Books",
        tags=['Book'],
        manual_parameters=[
            openapi.Parameter('page', openapi.IN_QUERY, type=openapi.TYPE_STRING, default='1',description='Provide page number'),
            openapi.Parameter('page_size', openapi.IN_QUERY, type=openapi.TYPE_STRING, default='20',description='Provide how many records you want'),
        ]
    )
    def get(self, request):
        try:
            books_sorted_by_sold_copies = Book.objects.annotate(sold_copies_count=models.Count('downloadlink')).order_by('-sold_copies_count')
            paginator = CustomPageNumberPagination()
            paginated_books = paginator.paginate_queryset(books_sorted_by_sold_copies, request)
            serializer = BookSerializer(paginated_books, many=True)
            return paginator.get_paginated_response(serializer.data)
        except Exception as e:
            return Response({'status': status.HTTP_400_BAD_REQUEST, 'Response': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class SearchAPI(APIView):
    @swagger_auto_schema(
        operation_description="This API is used to search for books based on specified criteria",
        operation_summary="Search Books",
        tags=['Book'],
        manual_parameters=[
            openapi.Parameter('page', openapi.IN_QUERY, type=openapi.TYPE_STRING, default='1',description='Provide page number'),
            openapi.Parameter('page_size', openapi.IN_QUERY, type=openapi.TYPE_STRING, default='10',description='Provide how many records you want'),
        ],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'title': openapi.Schema(type=openapi.TYPE_STRING, default=""),
                'author': openapi.Schema(type=openapi.TYPE_STRING, default=""),
                'language': openapi.Schema(type=openapi.TYPE_STRING, default=""),
                'topic': openapi.Schema(type=openapi.TYPE_STRING, default=""),
            }
        ),
    )
    def post(self, request):
        try:
            title = request.data.get('title', '').lower()
            author = request.data.get('author', '').lower()
            language = request.data.get('language', '').lower()
            topic = request.data.get('topic', '').lower()
            query = Q(title__icontains=title) | Q(author__icontains=author) | Q(language__icontains=language) | Q(subjects__name__icontains=topic) | Q(bookshelves__name__icontains=topic)
            filtered_books = Book.objects.filter(query)
            paginator = CustomPageNumberPagination()
            paginated_books = paginator.paginate_queryset(filtered_books, request)
            serializer = BookSerializer(paginated_books, many=True)
            return paginator.get_paginated_response(serializer.data)
        except Exception as e:
            return Response({'status': status.HTTP_400_BAD_REQUEST, 'Response': str(e)}, status=status.HTTP_400_BAD_REQUEST)
