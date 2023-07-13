from django.urls import path
from .views import dashboardView, show_electronics_items, add_electronics_items
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("home/", dashboardView, name="home"),
    path("items/", show_electronics_items, name="item"),
    path("add_items/", add_electronics_items, name="add_item"),
]


# urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
