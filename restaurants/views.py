from django.shortcuts import render, redirect
from .models import Restaurant
from .forms import RestaurantForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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


def restaurant_detail(request, restaurant_id):
    context = {
        "restaurant": Restaurant.objects.get(id=restaurant_id),
    }
    return render(request, 'restaurant_detail.html', context)


def restaurant_create(request):
    form = RestaurantForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect("restaurant_list")
    context = {
        "form": form,
    }
    return render(request, 'restaurant_create.html', context)

def restaurant_update(request, restaurant_id):
    item = Restaurant.objects.get(id=restaurant_id)
    form = RestaurantForm(request.POST or None, request.FILES or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect("restaurant_detail", restaurant_id=item.id)
    context = {
        "form": form,
        "item":item,
    }
    return render(request, 'restaurant_update.html', context)

def restaurant_delete(request, restaurant_id):
    Restaurant.objects.get(id=restaurant_id).delete()
    return redirect("restaurant_list")