from rest_framework import serializers
from .models import Notification
from accounts.serializers import UserSerializer
from posts.serializers import PostSerializer
from django.contrib.contenttypes.models import ContentType

class NotificationSerializer(serializers.ModelSerializer):
    actor = serializers.ReadOnlyField(source='actor.username')
    target_object_id = serializers.IntegerField()
    
    class Meta:
        model = Notification
        fields = ['id', 'actor', 'verb', 'timestamp', 'is_read', 'target_content_type', 'target_object_id']
        read_only_fields = ['id', 'actor', 'verb', 'timestamp', 'is_read']