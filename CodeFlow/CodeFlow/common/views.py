from django.views.generic import TemplateView
from django.contrib.contenttypes.models import ContentType
from CodeFlow.common.models import Comment, Like
from CodeFlow.common.serializers import CommentSerializer, LikeSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
class HomePageView(TemplateView):
    template_name = "common/home-page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_authenticated'] = self.request.user.is_authenticated
        return context


class CommentPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 20

class CommentListCreateView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = CommentPagination

    def get_queryset(self):
        content_type = ContentType.objects.get(model=self.kwargs['model_name'].lower())
        return Comment.objects.filter(content_type=content_type, object_id=self.kwargs['object_id'])

    def perform_create(self, serializer):
        content_type = ContentType.objects.get(model=self.kwargs['model_name'].lower())
        serializer.save(
            author=self.request.user,
            content_type=content_type,
            object_id=self.kwargs['object_id']
        )

class LikeToggleView(generics.GenericAPIView):
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, model_name, object_id):
        content_type = ContentType.objects.get(model=model_name.lower())

        existing_like = Like.objects.filter(
            content_type=content_type, object_id=object_id, user=request.user
        ).first()

        if existing_like:
            existing_like.delete()
            liked = False
        else:
            Like.objects.create(content_type=content_type, object_id=object_id, user=request.user)
            liked = True

        like_count = Like.objects.filter(
            content_type=content_type, object_id=object_id
        ).count()

        return Response({'liked': liked, 'like_count': like_count}, status=status.HTTP_200_OK)




