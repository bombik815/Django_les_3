from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Book


def books_view(request):
    template = 'books/books_list.html'
    books_list = Book.objects.all().order_by('pub_date')

    context = {'books':books_list }
    return render(request, template, context)


def books_detail(request, pub_date):
    template = 'books/books_detail.html'
    books_detail = Book.objects.filter(pub_date=pub_date)

    list_date=[]
    all_list_pub_date = Book.objects.all().values_list('pub_date').order_by('pub_date')

    for item_date in all_list_pub_date:
        list_date.append(str(item_date[0]))

    if pub_date in list_date:
        curent_index = list_date.index(pub_date)
        if curent_index == 0:
            date_before = list_date[curent_index]
            date_next= list_date[curent_index+1]
        else:
            date_before = list_date[curent_index-1]
            date_next = list_date[curent_index + 1]
    else:
        date_before = list_date[0]
        date_next = list_date[1]

    all_books = Book.objects.all()
    paginator = Paginator(all_books, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
                'date_before':date_before,
                'date_next': date_next,
                'book_detail':page_obj
                }
    return  render(request, template, context=context)

