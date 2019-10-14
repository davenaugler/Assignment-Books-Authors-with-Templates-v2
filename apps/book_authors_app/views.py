from django.shortcuts import render, HttpResponse, redirect
from .models import Book, Author

# Create your views here.
# def index(request):
#     return render(request, "book_author_app/index.html")

def addBookPage(request):
    context = {
        "all_books": Book.objects.all()
    }
    return render(request, "book_authors_app/addBook.html", context)

def addNewBook(request):
    print("Inside addNewBook")
    title = request.POST['title']
    desc = request.POST['desc']
    new_book = Book.objects.create(title=title, desc=desc)
    return redirect('/')

def addAuthorPage(request):
    context = {
        "all_authors": Author.objects.all()
    }
    return render(request, "book_authors_app/addAuthor.html", context)

def addNewAuthor(request):
    print("Inside of addNewAuthor")
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    notes = request.POST['notes']
    new_author = Author.objects.create(first_name=first_name, last_name=last_name, notes=notes)
    return redirect('/authors')

def viewBook(request, id):
    context = {
        'book_id': Book.objects.get(id=id),
        'books': Book.objects.get(id=id),
        
        # 'authors_assoc_with book': Author.objects.filter()
        "all_authors": Author.objects.all()
        # 'authored_books': books.authors.all()
    }
    return render(request, "book_authors_app/viewBook.html", context)

def viewAuthorAddBook(request):
    print(request.POST)
    # print(request.POST['book_id'])
    print(request.POST.get('author_id', 99))
    if request.method == "POST":
        # print("Inside viewAuthorAddBook", request.POST)
        (Book.objects.get(id=request.POST['book_id'])).authors.add(Author.objects.get(id=request.POST['author_id']))

    # return redirect(request.META.get('HTTP_REFERER'))
    # return redirect("/authors/"+book_id.id)
    return redirect(f"/authors/{request.POST['author_id']}")

def viewAuthor(request, id):
    context = {
        'author_id': Author.objects.get(id=id),
        'all_books': Book.objects.all()
    }
    return render(request, "book_authors_app/viewAuthor.html", context)

def viewBookAddAuthor(request):
    print("Inside viewBookAddAuthor")
    if request.method == "POST":
        (Author.objects.get(id=request.POST['author_id'])).books.add(Book.objects.get(id=request.POST['book_id']))
    # return redirect(request.META.get('HTTP_REFERER'))
    # print(request.POST)
    # # print(request.POST['book_id'])
    # print(request.POST.get('book_id', 99))
  
    return redirect(f"/books/{request.POST['book_id']}")

