from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import add_electronics_items, dashboardView, show_electronics_items

urlpatterns = [
    path("home/", dashboardView, name="home"),
    path("items/", show_electronics_items, name="item"),
    path("add_items/", add_electronics_items, name="add_item"),
]


# urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
