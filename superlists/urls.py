from django.conf.urls import include, url

from lists import views as list_views
from lists import urls as list_urls
from lists.views import HomePageView

urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^lists/', include(list_urls)),
    # url(r'^admin/', include(admin.site.urls)),
]
