
from django.views.generic import TemplateView
from CodeFlow.commons.forms import CommentForm
from CodeFlow.commons.models import Like
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required



class HomePageView(TemplateView):
    template_name = "common/home-page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_authenticated'] = self.request.user.is_authenticated
        return context


@login_required
def likes_functionality(request, model_name: str, object_id: int):
    content_type = get_object_or_404(ContentType, model=model_name.lower())

    liked_object = Like.objects.filter(
        content_type=content_type,
        object_id=object_id,
        user=request.user
    ).first()

    if liked_object:
        liked_object.delete()
    else:
        Like.objects.create(
            content_type=content_type,
            object_id=object_id,
            user=request.user
        )

    return redirect(request.META.get('HTTP_REFERER') + f'#{object_id}')


@login_required
def comment_functionality(request, model_name: str, object_id: int):
    content_type = get_object_or_404(ContentType, model=model_name.lower())

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.content_type = content_type
            comment.object_id = object_id
            comment.author = request.user
            comment.save()

    return redirect(request.META.get('HTTP_REFERER') + f'#{object_id}')