from django.shortcuts import render, redirect
from raffinato.suits.forms import AddForm
from raffinato.suits.models import Suit


def shop_list(request):
    all_suits = Suit.objects.all()

    context = {
        "all_suits": all_suits
    }

    return render(request, template_name='suits/shop-list.html', context=context)


def add_suit(request):
    if request.method == 'GET':
        form = AddForm()
    else:
        form = AddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('shop_list')

    context = {
        'form': form,
    }

    return render(request, template_name='suits/add_suit.html', context=context)


def edit_suit(request, pk):
    return render(request, template_name='suits/edit_suit.html')


def details_suit(request, pk, suit_slug):
    suit = Suit.objects.get(slug=suit_slug)
    price = suit.price
    name = suit.name
    photo = suit.personal_photo
    comments = suit.comment_set.all()
    context = {
        'suit': suit,
        'price': price,
        'name': name,
        'photo': photo,
        'comments': comments,
    }

    return render(request, template_name='suits/details-suit-page.html', context=context)
