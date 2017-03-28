#
#  from django.conf.urls import url
#
# from questions.views import AboutView
#
# urlpatterns = [
#     url(r'^about$', AboutView.as_view(), name='about'),
# ]

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^about$', views.about, name='about'),
    url(r'^get$', views.get_post, name='get'),
    url(r'^post$', views.get_post, name='post'),
]