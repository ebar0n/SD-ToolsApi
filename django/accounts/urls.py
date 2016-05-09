from django.conf.urls import include, url
from django.contrib.auth.views import logout

from accounts import views

urlpatterns = [
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^github/repositories$', views.GithubRepositoriesView.as_view(), name='repositories'),
    url(r'^logout/$', logout, {'next_page': '/'}, name="logout"),
]
