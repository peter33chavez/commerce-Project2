from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create_listing", views.create_listing, name="create_listing"),
    path("<int:listing_id>", views.listing_page, name='listing_page'),
    path("updated/<int:listing_id>", views.update_wishlist, name='update_wishlist'),
    path("closed/<int:listing_id>", views.listing_status, name='listing_status'),
    path("categorySearch", views.category_search, name='category_search'),
    path("results/<str:category_item>", views.category, name='category'),
    path("wishlist", views.wishlist, name='wishlist')
]

