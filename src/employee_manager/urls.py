"""employee_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

import imp
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse, HttpRequest
from apps.products.models import Product, Order

def get_users(request:HttpRequest):
    '''
    # return web user name
    '''
    request.user.sex
    return HttpResponse(f'Some user {request.user}, {request.user.sex}, {request.user.is_anonymous}')



def create_order(request):
    '''
    # create view
    '''
    rows = Product.objects.all()

    table = []
    for row in rows:
        table.append(row)

    return HttpResponse(f'New page {table[0]} {table[1]}')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', get_users),
    path('order/', create_order),
]
