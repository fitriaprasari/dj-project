# from django.conf.urls import url,include
from django.urls import path,include
from django.contrib import admin

from . import views

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    # url(r'^about/', include('about.urls')),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^$', views.index),
    # url(r'^login/', views.login),
    # url(r'^register/', views.register),
    # url(r'^caripartner/', views.caripartner),
    # url(r'^transactions/', views.transactions),
    # path('',include('login.urls')),
    # path('/register',include('login.urls')),

    #home
    path('',views.index, name='index'),

    #login
    path('',include('login.urls')),
    path('register',include('login.urls')),

    #partners
    path('',include('partners.urls')),
    path('details(?P<value>\d+)/$',include('partners.urls')),
    # url(r'^pay/summary/(?P<value>\d+)/$', views.pay_summary, name='pay_summsary')),
    # path('register',include('login.urls')),
    # path('get_partner',include('partner.urls'))
]
