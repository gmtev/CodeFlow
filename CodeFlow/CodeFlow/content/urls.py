from django.urls import path, include
from CodeFlow.content.views import QuestionListView, QuestionDetailView, QuestionCreateView, QuestionEditView, QuestionDeleteView
from CodeFlow.content.views import LectureListView, LectureCreateView, LectureEditView, LectureDeleteView, LectureDetailView
urlpatterns = [
    path('questions/', include([
        path('', QuestionListView.as_view(), name='questions'),
        path('create/', QuestionCreateView.as_view(), name='question-create'),
        path('<slug:slug>/', QuestionDetailView.as_view(), name='question-details'),
        path('<slug:slug>/edit/', QuestionEditView.as_view(), name='question-edit'),
        path('<slug:slug>/delete/', QuestionDeleteView.as_view(), name='question-delete'),
    ])),

    path('lectures/', include([
        path('', LectureListView.as_view(), name='lectures'),
        path('create/', LectureCreateView.as_view(), name='lecture-create'),
        path('<slug:slug>/', LectureDetailView.as_view(), name='lecture-details'),
        path('<slug:slug>/edit/', LectureEditView.as_view(), name='lecture-edit'),
        path('<slug:slug>/delete/', LectureDeleteView.as_view(), name='lecture-delete'),
    ])),
]
