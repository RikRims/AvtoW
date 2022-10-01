from django.urls import path
from .views import *

urlpatterns = [
    path('', homelist.as_view(), name='home'),
    path('about/', about, name='about'),
    path('orders/', orderlist.as_view(), name='orderlist'),
    path('product/<slug:product_id>', detailproduct.as_view(), name='product'),
    path('orders/<int:order_id>', detailorders, name='orders'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register /', RegisterUser.as_view(), name='register'),
    path('category/<slug:cat_slag>', showCategory.as_view(), name='select')
]
