from django.contrib.auth import get_user_model
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from CodeFlow.accounts.models import Profile
from CodeFlow.accounts.utils import send_welcome_email, send_goodbye_email
UserModel = get_user_model()

@receiver(post_save, sender=UserModel)
def create_profile(sender, instance, created, **kwargs):

    if created:
        Profile.objects.create(user=instance)
        send_welcome_email(instance.email, instance.username)

@receiver(post_delete, sender=UserModel)
def delete_profile(sender, instance, **kwargs):

    send_goodbye_email(instance.email, instance.username)