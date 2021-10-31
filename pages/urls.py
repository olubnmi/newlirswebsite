from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('faq',views.faq,name='faq'),
    path('contact',views.contact,name='contact'),
    path('about/ec',views.ec,name='ec'),
    path('about/da',views.da,name='da'),
    path('about/dbs',views.dbs,name='dbs'),
    path('about/dhr',views.dhr,name='dhr'),
    path('about/dissd',views.dissd,name='dissd'),
    path('about/dls',views.dls,name='dls'),
    path('about/dnga',views.dnga,name='dnga'),
    path('about/dpit',views.dpit,name='dpit'),
    path('about/dta',views.dta,name='dta'),
]