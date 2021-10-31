from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name='news'),
    path('<int:news_id>',views.article,name='article')
]