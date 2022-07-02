from django.shortcuts import render

# Create your views here.
from webapp.models import Book, STATUS_CHOICES


def index_view(request):
    books = Book.objects.order_by("-created_at")
    context = {"books": books}
    return render(request, 'index.html', context)


def create_book(request):
    if request.method == "GET":
        return render(request, "create.html", {"statuses": STATUS_CHOICES})
    else:
        guest_name = request.POST.get("guest_name")
        from_email = request.POST.get("from_email")
        content = request.POST.get("content")
        status = request.POST.get("status")
        new_book = Book.objects.create(guest_name=guest_name, from_email=from_email, content=content, status=status)
        context = {"book": new_book}

        return render(request, 'book_view.html', context)
