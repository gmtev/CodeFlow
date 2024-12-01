from django.contrib.auth.views import LogoutView
from django.urls import path, include
from CodeFlow.accounts import views

urlpatterns = [
    path('login/', views.CustomUserLoginView.as_view(), name='login'),
    path('register/', views.CustomUserRegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/<int:pk>/', include([
        path('', views.ProfileDetailView.as_view(), name='profile-details'),
        path('edit/', views.ProfileEditView.as_view(), name='profile-edit'),
        path('edit-credentials/', views.CustomUserEditView.as_view(), name='credentials-edit'),
        path('delete/', views.ProfileDeleteView.as_view(), name='profile-delete'),
    ]))
]