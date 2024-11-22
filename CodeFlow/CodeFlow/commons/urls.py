from django.urls import path
from CodeFlow.commons import views


urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('like/<str:model_name>/<int:object_id>/', views.likes_functionality, name='like'),
    path('comment/<str:model_name>/<int:object_id>/', views.comment_functionality, name='comment')
]