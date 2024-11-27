from django import forms
from CodeFlow.content.models import Question, Lecture, Section
from django.core.files.uploadedfile import UploadedFile
from django.core.exceptions import ValidationError

class QuestionBaseForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'text', 'picture']

        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Question title'}),
            'text': forms.Textarea(attrs={
                'placeholder': 'Describe your question...',
                'rows': 5
            }),
        }


        labels = {
            'title': 'Question title',
            'text': 'Question description',
        }

    def clean_picture(self):
        file = self.cleaned_data.get('picture')

        if file:
            if isinstance(file, UploadedFile):
                if file.size > 5 * 1024 * 1024:
                    raise ValidationError("File shouldn't be larger than 5MB.")

        return file


class QuestionCreateForm(QuestionBaseForm):
    pass


class QuestionEditForm(QuestionBaseForm):
    class Meta(QuestionBaseForm.Meta):
        model = Question
        fields = ['title', 'text', 'picture', 'is_answered']

class QuestionDeleteForm(QuestionBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['disabled'] = True
            field.widget.attrs['readonly'] = True


class LectureBaseForm(forms.ModelForm):
    class Meta:
        model = Lecture
        fields = ['title', 'text']

        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title of lecture'}),
            'text': forms.Textarea(attrs={
                'placeholder': 'Describe your lecture...',
                'rows': 5
            }),
        }

        labels = {
            'title': 'Lecture title',
            'text': 'Description of lecture',
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


class SectionBaseForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = ['section_name', 'text']
        widgets = {
            'section_name': forms.TextInput(attrs={'placeholder': 'Title of section'}),
            'text': forms.Textarea(attrs={
                'placeholder': 'Content of section...',
                'rows': 5
            }),
        }

        labels = {
            'section_name': 'Section title',
            'text': 'Section content',
        }

class SectionCreateForm(SectionBaseForm):
    pass


class SectionEditForm(SectionBaseForm):
    pass

