from django.contrib import admin
from django.urls import include, path
from .views import landing_page

urlpatterns = [
    path('', landing_page, name='landing_page'),

    path('admin/', admin.site.urls),
    path('auth/', include('accounts.urls')),
    # path('books/', include('books.urls')),
]
