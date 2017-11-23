from django.shortcuts import render, redirect
from .models import Restaurant, Item
from .forms import RestaurantForm, ItemForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404
from django.utils import timezone

def restaurant_list(request):
    restaurants = Restaurant.objects.all()

    paginator = Paginator(restaurants,2)

    page = request.GET.get('page')
    try:
        restaurants = paginator.page(page)
    except PageNotAnInteger:
        restaurants = paginator.page(1)
    except EmptyPage:
        restaurants = paginator.page(paginator.num_pages)
    context = {
        "restaurants": restaurants,
    }
    return render(request, 'restaurant_list.html', context)


def restaurant_detail(request, restaurant_slug):
    restaurant = Restaurant.objects.get(slug=restaurant_slug)
    items = restaurant.item_set.all()
    now = timezone.now().time()

    if not request.user.is_staff:
        items = items.filter(active=True)
    context = {
        "restaurant": restaurant,
        "items":items,
        "now":now,
    }
    return render(request, 'restaurant_detail.html', context)


def restaurant_create(request):
    if not request.user.is_staff:
        raise Http404
    form = RestaurantForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect("restaurant_list")
    context = {
        "form": form,
    }
    return render(request, 'restaurant_create.html', context)

def restaurant_update(request, restaurant_slug):
    if not request.user.is_staff:
        raise Http404
    item = Restaurant.objects.get(slug=restaurant_slug)
    form = RestaurantForm(request.POST or None, request.FILES or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect("restaurant_detail", restaurant_slug=item.slug)
    context = {
        "form": form,
        "item":item,
    }
    return render(request, 'restaurant_update.html', context)

def restaurant_delete(request, restaurant_slug):
    if not request.user.is_staff:
        raise Http404
    Restaurant.objects.get(slug=restaurant_slug).delete()
    return redirect("restaurant_list")

def item_create(request):
    if not request.user.is_staff:
        raise Http404
    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("restaurant_list")
    context = {
    "form": form,
    }
    return render(request, 'item_create.html', context)

def item_update(request, item_slug):
    if not request.user.is_staff:
        raise Http404
    instance = Item.objects.get(slug=item_slug)
    form = ItemForm(request.POST or None, instance = instance)
    if form.is_valid():
        form.save()
        return redirect("restaurant_list")
    context = {
    "form":form,
    "instance": instance,
    }
    return render(request, 'item_update.html', context)

def item_delete(request, item_slug):
    if not request.user.is_staff:
        raise Http404
    instance = Item.objects.get(slug=item_slug)
    instance.delete()
    return redirect("restaurant_list")