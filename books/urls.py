from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('books/', views.books, name='books'),
    path('book/<int:book_id>/', views.view_book, name='view_book'),
    path('book/<int:book_id>/rent/', views.rent_book, name='rent_book'),
    path('book/<int:book_id>/checkout/', views.checkout, name='checkout'),
    path('about/', views.about, name='about'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)