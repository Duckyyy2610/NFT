from collections import Counter
from math import ceil
import random
from django.shortcuts import render, redirect, HttpResponse
from django.db.models import Count
from NFTapp.models import User, NFTProduct, Topic,\
                             NFTProductOwner, Type, NFTBlog, \
                                BlogSection, BlogComment, ProductComment,\
                                FAQ, FAQTitle, NFTProductFavorite, \
                                Cart, CartItem
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect
from django.urls import reverse

def error_403_csrf_failure(request, reason=""):
    """
    To fix this issue:
        1. User opens tab A and tab B, and both show the login in form.
        2. User logs in on tab A, this will destroy the Anonymous session, and create a new one (for security)
        3. Then user logs in on tab B
            - The CSRF token for the Anonymous session is now invalid
            - Since the user is already logged, we just redirect them to refresh the page
    """
    if request.path == '/login/' and request.user.is_authenticated:
        next = request.GET.get('next', '/')
        return HttpResponseRedirect(next)

    url = reverse('login') + '?next=' + request.path
    context = {
        'page_title': "Authentication Error",
        'continue_url': url,
        'reason': reason,
    }
    response = render(request, "core.base/403_csrf.html", context=context)
    response.status_code = 403
    return response

def cal_times_to_read(blogs):
    average_wpm = 238
    blogs_context = {}
    for blog in blogs:
        words_of_blog = sum([len(str(section.content).split()) for section in blog.blog_section.all()])
        blogs_context[blog] = ceil(words_of_blog / average_wpm)
    return blogs_context

def product_rarity_rank():
    rarity_rank = {}
    products = NFTProduct.objects.all().order_by('rarity')
    cnt = 1
    for product in products:
        rarity_rank.update({product: cnt})
        cnt += 1
    return rarity_rank

def classify_1(data, query_set):
    if data == 'trending':
        return query_set.annotate(num_owners=Count('owners')).order_by('-num_owners')
    elif data == 'rarity':
        return query_set.order_by('rarity')
    elif data == 'date-created-new':
        return query_set.order_by('created_at')
    elif data == 'date-created-old':
        return query_set.order_by('-created_at')
    elif data == 'price-highest':
        return query_set.order_by('-price')
    return query_set.order_by('price')

def add_search_data(view_func):
    def wrapper(request, *args, **kwargs):
        user_search = []
        for user in User.objects.filter(is_superuser=0).values():
            user_search.append({
                'id': str(user['id']),
                'name': user['name'],
                'image': user['avatar'],
                'redirect_url': 'profile'
            })

        product_search = []
        for product in NFTProduct.objects.values():
            product_search.append({
                'id': str(product['id']),
                'name': product['name'],
                'image': product['image'],
                'redirect_url': 'collection1'
            })

        blog_search = []
        for blog in NFTBlog.objects.values():
            blog_search.append({
                'id': str(blog['id']),
                'name': blog['title'],
                'image': blog['image'],
                'redirect_url': 'blog'
            })

        search_data = user_search + product_search + blog_search
        request.search_data = sorted(search_data, key=lambda x : x['name'])
        return view_func(request, *args, **kwargs)

    return wrapper

def add_cart_data(view_func):
    def wrapper(request, *args, **kwargs):
        cart_products = Cart.objects.get(user=request.user).products.all()
        request.cart_products = cart_products
        return view_func(request, *args, **kwargs)
    return wrapper