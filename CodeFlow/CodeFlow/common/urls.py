from django.urls import path
from CodeFlow.common.views import CommentListCreateView, LikeToggleView, HomePageView, CommentDeleteView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('api/comments/<str:model_name>/<int:object_id>/', CommentListCreateView.as_view(), name='api-comments'),
    path('api/comments/<str:model_name>/<int:object_id>/<int:comment_id>/', CommentDeleteView.as_view(), name='api-comments-delete'),
    path('api/likes/<str:model_name>/<int:object_id>/', LikeToggleView.as_view(), name='api-likes'),
]