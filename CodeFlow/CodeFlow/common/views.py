from django.views.generic import TemplateView
from django.contrib.contenttypes.models import ContentType
from rest_framework.generics import GenericAPIView
from django.shortcuts import get_object_or_404
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

# class CommentListCreateView(generics.ListCreateAPIView): other way of implementing the view below
#     serializer_class = CommentSerializer
#     permission_classes = [IsAuthenticated]
#     pagination_class = CommentPagination
#
#     def get_queryset(self):
#         content_type = ContentType.objects.get(model=self.kwargs['model_name'].lower())
#         return Comment.objects.filter(content_type=content_type, object_id=self.kwargs['object_id'])
#
#     def perform_create(self, serializer):
#         content_type = ContentType.objects.get(model=self.kwargs['model_name'].lower())
#         serializer.save(
#             author=self.request.user,
#             content_type=content_type,
#             object_id=self.kwargs['object_id']
#         )

class CommentListCreateView(GenericAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = CommentPagination


    def get_queryset(self):
        content_type = ContentType.objects.get(model=self.kwargs['model_name'].lower())
        return Comment.objects.filter(content_type=content_type, object_id=self.kwargs['object_id'])

    def get(self, request, *args, **kwargs):
        queryset = self.paginate_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request, *args, **kwargs):
        content_type = ContentType.objects.get(model=self.kwargs['model_name'].lower())
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(
                author=request.user,
                content_type=content_type,
                object_id=self.kwargs['object_id']
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentDeleteView(GenericAPIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        comment_id = kwargs.get('comment_id')
        if not comment_id:
            return Response({"detail": "Comment ID is required for deletion."}, status=status.HTTP_400_BAD_REQUEST)

        content_type = ContentType.objects.get(model=self.kwargs['model_name'].lower())

        comment = get_object_or_404(
            Comment,
            id=comment_id,
            content_type=content_type,
            object_id=self.kwargs['object_id'],
            author=request.user,
        )

        comment.delete()
        return Response({"detail": "Comment deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

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




