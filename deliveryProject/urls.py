from django.conf.urls.static import static
from django.contrib import admin
from django.template.defaulttags import url
from django.urls import path, include, re_path

from delivery.views import *
from deliveryProject import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path("about/", about, name='about'),
    path("courier/", show_courier, name='courier'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('search/', Search.as_view(), name='search'),
    path('fav/<int:id>', favourite_add, name='favourite_add'),
    path('favourites', favourite_list, name='favourite_list'),
    path('product/<int:product_id>/', show_product, name='product'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('delivery', create_delivery, name='create_delivery'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler_404 = pageNotFound
