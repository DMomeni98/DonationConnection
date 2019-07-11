from django.conf.urls import include, url
from django.contrib import admin
from products.views import add_product
from products.views import product_page
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Examples:
    # url(r'^$', 'DonationConnection.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'products/', add_product, name='add_product'),
    url(r'product_profile/', product_page, name='product_page'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
