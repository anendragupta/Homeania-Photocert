from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^level/', views.level, name="level"),
    url(r'^home/static/media/pdf/(?P<filename>\{w{40})/$', views.pdf_download, name="pdf_download"),
    url(r'^first_level/', views.first_level, name="first_level"),
    url(r'^second_level/', views.second_level, name="second_level"),
    url(r'^third_level/', views.third_level, name="third_level"),
    url(r'^practical_test/', views.image_form_upload, name="image_form_upload"),
    url(r'^quiz/(?P<level_id>[0-9]+)/$', views.quiz_question, name='quiz_question'),
    url(r'^logout/', views.logout_view, name='logout'),
]