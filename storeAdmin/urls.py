from django.urls import path
from . import views
from storePage import views as view

urlpatterns = [
    path("", views.login_view, name="login"),
    path("store/",view.store,name="store"),
    path("register/", views.register, name='register'),
    path("launch/", views.launch, name="launch"),
    path("product/",views.product,name="product"),
    path("delete/<int:product_id>/", views.delete_product, name="delete_product"),
    path("update/<int:product_id>/", views.update_product, name="update_product"),
]

