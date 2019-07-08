from django.conf.urls import include, url
from django.contrib import admin
from charity.views import charity_register

urlpatterns = [
    # Examples:
    # url(r'^$', 'DonationConnection.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^charity_register', charity_register, name="charity_register")
]
