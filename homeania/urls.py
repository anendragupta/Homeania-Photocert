from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_view
from home.views import UserFormView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/', include('home.urls', namespace="home")),

    #Registartion/login and logout URL
    url(r'^register/', UserFormView.as_view(), name='register'),
    url(r'^login/', auth_view.login, name="login"),
    url(r'^logout/', auth_view.logout, name='logout'),

    #password Reset URL
    url(r'^passowrd_reset/$', auth_view.password_reset, name='password_reset'),
    url(r'^passowrd_reset/done/$', auth_view.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',auth_view.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$',auth_view.password_reset_complete, name='password_reset_complete'),

]
