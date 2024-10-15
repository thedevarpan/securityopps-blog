from django.urls import path
from.import views

urlpatterns = [
    path("", views.Home, name = "Home"),
    path("blog/", views.Blog, name = "Blog"),
    path("about/", views.About, name = "About"),
    path("contact/", views.Contact, name = "Contact"),
    path("category/", views.CategoryDetail, name = "CategoryDetail"),
    path("blog-detail/<slug:slug>", views.BlogDetail, name = "BlogDetail"),
]