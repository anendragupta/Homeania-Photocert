from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^level/', views.level, name="level"),
    url(r'^home/static/media/pdf/(?P<filename>\{w{40})/$', views.pdf_download, name="pdf_download"),
    url(r'^first_level/', views.first_level, name="first_level"),
    url(r'^second_level/', views.second_level, name="second_level"),
    url(r'^third_level/', views.third_level, name="third_level"),
    url(r'^upload_image/', views.image_form_upload, name="image_form_upload")
]