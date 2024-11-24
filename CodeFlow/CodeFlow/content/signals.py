from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.contrib.contenttypes.models import ContentType
from CodeFlow.content.models import Question, Lecture
from CodeFlow.commons.models import Comment, Like


@receiver(post_delete, sender=Question)
def delete_related_content_for_question(sender, instance, **kwargs):
    content_type = ContentType.objects.get_for_model(sender)

    Comment.objects.filter(
        content_type=content_type,
        object_id=instance.id
    ).delete()

    Like.objects.filter(
        content_type=content_type,
        object_id=instance.id
    ).delete()



@receiver(post_delete, sender=Lecture)
def delete_related_content_for_lecture(sender, instance, **kwargs):
    content_type = ContentType.objects.get_for_model(sender)

    Comment.objects.filter(
        content_type=content_type,
        object_id=instance.id
    ).delete()

    Like.objects.filter(
        content_type=content_type,
        object_id=instance.id
    ).delete()