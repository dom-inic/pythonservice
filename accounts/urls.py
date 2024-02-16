from django.urls import path
from .views import ProtectedResourceView, UserList, UserDetail

urlpatterns = [
    path('protected-resource/', ProtectedResourceView.as_view(), name='protected-resource'),
    path('users/', UserList.as_view(), name='users-list'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
]