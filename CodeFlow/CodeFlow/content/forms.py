from django import forms
from CodeFlow.content.models import Question, Lecture


class QuestionBaseForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_title', 'text', 'picture']

        widgets = {
            'question_title': forms.TextInput(attrs={'placeholder': 'Question title'}),
            'text': forms.Textarea(attrs={
                'placeholder': 'Describe your question...',
                'rows': 5
            }),
        }


        labels = {
            'question_title': 'Question title',
            'text': 'Question description',
        }


class QuestionCreateForm(QuestionBaseForm):
    pass


class QuestionEditForm(QuestionBaseForm):
    class Meta(QuestionBaseForm.Meta):
        model = Question
        fields = ['question_title', 'text', 'picture', 'is_answered']

class QuestionDeleteForm(QuestionBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['disabled'] = True
            field.widget.attrs['readonly'] = True


class LectureBaseForm(forms.ModelForm):
    class Meta:
        model = Lecture
        fields = ['lecture_title', 'text']

        widgets = {
            'lecture_title': forms.TextInput(attrs={'placeholder': 'Title of lecture'}),
            'text': forms.Textarea(attrs={
                'placeholder': 'Your learning material...',
                'rows': 5
            }),
        }

        labels = {
            'lecture_title': 'Lecture title',
            'text': 'Learning material',
        }


class LectureCreateForm(LectureBaseForm):
    pass


class LectureEditForm(LectureBaseForm):
    pass


class LectureDeleteForm(LectureBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['disabled'] = True
            field.widget.attrs['readonly'] = True