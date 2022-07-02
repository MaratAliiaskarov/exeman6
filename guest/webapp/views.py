from django.shortcuts import render

# Create your views here.

def index_view(request):
    query = request.GET.getlist("name", "rrrrrr")
    print(query)
    context = {"name": query, "test": "lalalal"}
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

