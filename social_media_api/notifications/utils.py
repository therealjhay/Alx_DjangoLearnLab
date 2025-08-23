from django.contrib.contenttypes.models import ContentType
from .models import Notification

def create_notification(recipient, actor, verb, target):
    content_type = ContentType.objects.get_for_model(target)
    Notification.objects.create(
        recipient=recipient,
        actor=actor,
        verb=verb,
        target_content_type=content_type,
        target_object_id=target.pk
    )