from django.urls import path
from . import views
from .views import CustomLoginView

urlpatterns = [
    path('upload/', views.upload_book, name='upload_book'),
    path('upload-success/', views.upload_success, name='upload_success'),
    path('', views.public_book_list, name='public_books'),
    path('dashboard/', views.contributor_dashboard, name='contributor_dashboard'),
    path('signup/', views.signup_view, name='signup'),
    path('books/', views.public_books, name='public_books'),
    path('books/<int:book_id>/', views.book_detail, name='book_detail'),
    path('review/', views.review_books, name='review_books'),
    path('review/<int:book_id>/', views.review_book_action, name='review_book'),
    path('books/<int:book_id>/', views.book_detail, name='book_detail'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', views.custom_logout_view, name='logout'),
]