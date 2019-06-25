from django.conf.urls import include, url
from django.contrib import admin
from accounts.views import register
urlpatterns = [
    # Examples:
    # url(r'^$', 'DonationConnection.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^register', register, name="register"),
    url(r'^admin/', include(admin.site.urls)),
]
