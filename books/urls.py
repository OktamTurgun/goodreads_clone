from django.urls import path
from .views import home_view, book_detail_view

app_name = 'books'

urlpatterns = [
    path('', home_view, name='home'),
    path('<int:pk>/', book_detail_view, name='detail')
]
