import os
import django
import pandas as pd
import random
 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Gutenberg.settings')
django.setup()

 
from app.models import Book, Subject, Bookshelf, DownloadLink

 
def import_data_from_csv(file_path):
    mime_types = [
            'text/plain',
            'text/html',
            'application/json',
            'application/xml',
            'image/jpeg',
            'image/png',
            'application/pdf',
            'audio/mpeg',
            'video/mp4',
            'application/msword'
        ]
   
    df = pd.read_csv(file_path)
    sl = ['English','Spanish','Mandarin Chinese','Portuguese','Russian','Japanese','German']
    

    for index, row in df.iterrows():
        sl1 = random.choice(sl)
        title = row['Title']
        author = row['Author']
        genre = 'Text'  
        language = sl1   
        bookshelves_data = row['Bookshelf'].split(',') if isinstance(row['Bookshelf'], str) else []
        book, created = Book.objects.get_or_create(
            title=title,
            author=author,
            genre=genre,
            language=language
        )

        for shelf_name in bookshelves_data:
            bookshelf, created = Bookshelf.objects.get_or_create(name=shelf_name.strip())
            book.bookshelves.add(bookshelf)

        
 
        

        # Generate a random MIME type
        random_mime_type = random.choice(mime_types)
        link = row['Link']
        mime_type = random_mime_type   
        count=random.randint(1,600)
        DownloadLink.objects.create(book=book, link=link, mime_type=mime_type,count=count)

 
if __name__ == '__main__':
    import_data_from_csv(r'C:\Users\Asus\Desktop\gutenberg_metadata.csv')
