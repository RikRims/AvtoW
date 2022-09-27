from django.urls import path
from .views import *

urlpatterns = [
    path('', homelist.as_view(), name='home'),
    path('about/', about, name='about'),
    path('product/<int:product_id>', detailproduct.as_view(), name='product'),
    path('login/', login, name='login'),
    path('category/<slug:cat_slag>', showCategory.as_view(), name='select')
]
