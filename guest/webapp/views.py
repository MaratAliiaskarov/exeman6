from django.shortcuts import render

# Create your views here.

def index_view(request):
    query = request.GET.get("name")
    context = {"create_book": create_book}
    return render(request, 'index.html', context)


def create_book(request):
    if request.method == "GET":
        return render(request, "create.html")
    else:
        context = {
            "name": request.POST.get("name"),
            "from_email": request.POST.get("from_email"),
            "content": request.POST.get("content"),
        }
        return render(request, 'index.html', context)

