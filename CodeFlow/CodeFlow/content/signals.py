from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from CodeFlow.content.models import Lecture

@receiver(pre_save, sender=Lecture)
def generate_slug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(f"{instance.lecture_title}-{instance.id}")
