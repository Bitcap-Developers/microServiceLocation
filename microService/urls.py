from django.conf.urls import include, url
from django.contrib import admin
import app.views as v

urlpatterns = [
    # Examples:
    # url(r'^$', 'microService.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^nearestDHL$', v.nearestDHL, name='nearestDHL'),
    url(r'^track$', v.track, name='track'),
]
