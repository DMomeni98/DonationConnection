from django.conf.urls import include, url
from django.contrib import admin
from products.views import add_product

urlpatterns = [
    # Examples:
    # url(r'^$', 'DonationConnection.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'products', add_product, name='add_product')
]
