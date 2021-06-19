from django.shortcuts import render

from django.http import HttpResponse

from .models import Book

def index(request):
    return HttpResponse("Hello World!")

def book_by_id(request, book_id):
    book = Book.objects.get(pk=book_id)
    
    return render(request, 'book.details.html', {'book':book})
    # return HttpResponse(f"Book: {book.title}, publish on {book.pub_date}")
    
