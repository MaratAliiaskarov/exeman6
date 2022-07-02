from django.shortcuts import render

# Create your views here.
from webapp.models import Book


def index_view(request):
    books = Book.objects.order_by("-created_at")
    context = {"books": books}
    return render(request, 'index.html', context)


def create_book(request):
    if request.method == "GET":
        return render(request, "create.html")
    else:
        context = {
            "guest_name": request.POST.get("guest_name"),
            "from_email": request.POST.get("from_email"),
            "content": request.POST.get("content"),
        }
        return render(request, 'book_view.html', context)

