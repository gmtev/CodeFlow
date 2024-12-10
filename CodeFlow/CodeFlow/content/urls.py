from django.urls import path, include
from CodeFlow.content.views import QuestionListView, QuestionDetailView, QuestionCreateView, QuestionEditView, QuestionDeleteView
from CodeFlow.content.views import LectureListView, LectureCreateView, LectureEditView, LectureDeleteView, LectureDetailView
from CodeFlow.content.views import SectionCreateView, SectionEditView, SectionDeleteView, SectionDetailView

urlpatterns = [
    path('questions/', include([
        path('', QuestionListView.as_view(), name='questions'),
        path('create/', QuestionCreateView.as_view(), name='question-create'),
        path('<slug:slug>/', include([
            path('', QuestionDetailView.as_view(), name='question-details'),
            path('edit/', QuestionEditView.as_view(), name='question-edit'),
            path('delete/', QuestionDeleteView.as_view(), name='question-delete'),
        ])),
    ])),

    path('lectures/', include([
        path('', LectureListView.as_view(), name='lectures'),
        path('create/', LectureCreateView.as_view(), name='lecture-create'),
        path('<slug:slug>/', include([
            path('', LectureDetailView.as_view(), name='lecture-details'),
            path('edit/', LectureEditView.as_view(), name='lecture-edit'),
            path('delete/', LectureDeleteView.as_view(), name='lecture-delete'),
            path('sections/', include([
                path('create/', SectionCreateView.as_view(), name='section-create'),
                path('<int:pk>/', include([
                    path('', SectionDetailView.as_view(), name='section-details'),
                    path('edit/', SectionEditView.as_view(), name='section-edit'),
                    path('delete/', SectionDeleteView.as_view(), name='section-delete'),
                ])),
            ])),
        ])),
    ])),
]
