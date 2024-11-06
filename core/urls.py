from django.contrib import admin
from django.urls import path,include
from core.views import *
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'product',ProductView)
router.register(r'user',UserView)
router.register(r'category',CategoryView)
router.register(r'image',ImageView)
router.register(r'order',OrderView)


urlpatterns = [
    path('',include(router.urls)),
    path('login/',LoginView.as_view(),name='login'),
    path('orderview/',OrderDetailView.as_view(),name='order'),
    path('orderbyuser/',OrderbyUser.as_view(),name='order-user'),
]
