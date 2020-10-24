from django.shortcuts import render
from phones.models import Phone
from django.db.models import F


def show_catalog(request):
    template = 'catalog.html'
    phones = Phone.objects.all()
    sorting_condition = request.GET.get('sort')
    if sorting_condition == 'name':
        phones = Phone.objects.all().order_by('name')
    if sorting_condition == 'min_price':
        phones = Phone.objects.all().order_by(F('price').asc())
    if sorting_condition == 'max_price':
        phones = Phone.objects.all().order_by(F('price').desc())
    # for phone in phones:
    #     print(phone.name, phone.slug, phone.price, phone.image)
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {'phone': phone}
    return render(request, template, context)
