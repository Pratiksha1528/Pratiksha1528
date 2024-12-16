"""
URL configuration for fashionworld project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from fashion import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login.htnl',views.homepage,name='login.html'),
    path('signup.html',views.signup,name='signup.html'),
    path('navigation.html',views.navigation,name='navigation.html'),
    path('mens_wear.html',views.mens_wear,name='mens_wear.html'),
    path('jackets_and_coats.html',views.jackets_and_coats,name='jackets_and_coats.html'),
    path('shirts.html',views.shirts,name='shirts.html'),
    path('tshirts.html',views.tshirts,name='tshirts.html'),
    path('footwear.html',views.footwear,name='footwear.html'),
    path('about.html',views.about,name='about.html'),
    path('contact.html',views.contact,name='contact.html'),    
    path('watches.html',views.watches,name='watches.html'),
    path('tshirtscombo.html',views.tshirtscombo,name='tshrtscombo.html'),
    path('saree.html',views.saree,name='saree.html'),
    path('jewellary.html',views.jewellary,name='jewellary.html'),
    path('footwear1.html',views.footwear,name='footwear1.html'),
    path('dresses.html',views.dresses,name='dresses.html'),
    path('jacketsandshirts.html',views.jacketsandshirts,name='jacketsandshirts.html'),
    path('footwear1.html',views.footwear,name='footwear2.html'),
    path('traditionalwear.html',views.traditionalwear,name='traditionalwear.html'),
    path('traditionalwear1.html',views.traditionalwear1,name='traditionalwear1.html'),
]
