from django.urls import path
from animal import views


urlpatterns = [
    path('/page_a/', views.page_a, ),
    path('/page_b/', views.page_b,),
    path('', views.page_c,),
    path('/create', views.create,),
    # path('', views.page_e, name='page_e'),
    # path('', views.page_f, name='page_f'),
    # path('', views.page_g, name='page_g'),
    # path('', views.page_h, name='page_h'),
    path('/', views.index),
]