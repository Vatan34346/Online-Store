import os

from django.shortcuts import render, get_object_or_404
from .models import Product, Category


def product_list(req):


    category_slug = req.GET.get('category')

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)
    else:
        products = Product.objects.all()

    categories = Category.objects.all()
    return render(req, "products/product_list.html", {"products": products, 'categories': categories, 'selected_category': category_slug})


def product_detail(req, product_id):
    product = get_object_or_404(Product, id= product_id)
    return render(req, "products/product_detail.html", {"product": product})




