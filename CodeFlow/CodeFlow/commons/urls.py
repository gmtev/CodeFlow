from django.urls import path
from CodeFlow.commons.views import CommentListCreateView, LikeToggleView, HomePageView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('api/comments/<str:model_name>/<int:object_id>/', CommentListCreateView.as_view(), name='api-comments'),
    path('api/likes/<str:model_name>/<int:object_id>/', LikeToggleView.as_view(), name='api-likes'),
]