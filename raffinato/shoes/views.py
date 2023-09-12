from django.shortcuts import render
from raffinato.shoes.models import Shoes


def all_shoes(request):
    shoes_all = Shoes.objects.all()

    context = {
        "shoes_all": shoes_all
    }

    return render(request, template_name='shoes/all_shoes.html', context=context)


def add_shoes(request):
    return render(request, template_name='shoes/add_shoes.html')


def view_shoes(request, pk, shoe_slug):
    shoe = Shoes.objects.get(slug=shoe_slug)
    price = shoe.price
    name = shoe.name
    photo = shoe.personal_photo
    comments = shoe.comment_set.all()
    context = {
        'shoe': shoe,
        'price': price,
        'name': name,
        'photo': photo,
        'comments': comments,
    }

    return render(request, template_name='shoes/view_shoes.html', context=context)
