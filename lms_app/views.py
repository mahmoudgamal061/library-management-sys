from django.shortcuts import redirect, render,get_object_or_404
from .models import *
from .forms import *
# Create your views here.
def index(request):
    if request.method == 'POST':
        add_book=BookForm(request.POST,request.FILES)
        if add_book.is_valid():
            add_book.save()
    if request.method == 'POST':
        add_cat=CategoryForm(request.POST)
        if add_cat.is_valid():
            add_cat.save()
    
    context={
        'category' :Category.objects.all(),
        'books':Book.objects.all(),
        'form' : BookForm(),
        'formcat':CategoryForm(),
        'allbooks': Book.objects.filter(active=True).count(),
        'booksold': Book.objects.filter(status='sold').count(),
        'bookrental': Book.objects.filter(status='rental').count(),
        'bookavailable': Book.objects.filter(status='available').count(),
        
    }
    return render(request,'pages/index.html',context)
def books(request):
    search=Book.objects.all()
    title=None
    if 'search_name' in request.GET:
        title=request.GET['search_name']
        if title:
            search = search.filter(title__icontains=title)
    context={
        'category' :Category.objects.all(),
        'books':search,
        'formcat':CategoryForm(),

    }
    return render(request,'pages/books.html',context)

def update(request,slug):
    book_id=Book.objects.get(slug=slug)
    if request.method == 'POST':
        book_save=BookForm(request.POST,request.FILES,instance=book_id)
        book_save.save()
        return redirect('/')
    else:
        book_save=BookForm(instance=book_id)
    context={
        'form':book_save
    }
    
    return render(request,'pages/update.html',context)


def delete(request,slug):
    # book_delete=Book.objects.get(slug=slug)
    book_delete=get_object_or_404(Book,slug=slug)
    if request.method=="POST":
        book_delete.delete()
        return redirect('/')
    return render(request,'pages/delete.html')

# totalbooksold=0
#     for i in Book.objects.values('status','price'):
#         if i['status']=='sold':
#             if i['price'] != None:
#                 totalbooksold += int(i['price'])
#     #-------
#     totalbookrental = 0
#     for i in Book.objects.values('status', 'total_rental'):
#         if i['status'] == 'rental':
#             if i['total_rental'] != None:
#                 totalbookrental += int(i['total_rental'])
#     # -------
#     fullprofits = totalbooksold + totalbookrental
