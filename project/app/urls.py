from django.urls import path

from .views import BookListView, BookCreateView, BookDeleteView, BookUpdateView, BookDetailView, buy, orders

urlpatterns = [
    path('index', BookListView.as_view(), name='book-list'),
    path('create', BookCreateView.as_view(), name='book-create'),
    path('buy', buy, name='buy'),
    path('orders', orders, name='orders'),
    path('delete/<int:pk>', BookDeleteView.as_view(), name='book-delete'),
    path('update/<int:pk>', BookUpdateView.as_view(), name='book-update'),
    path('detail/<int:pk>', BookDetailView.as_view(), name='book-detail'),
]