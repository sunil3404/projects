from rest_framework.serializers import ModelSerializer
from .models import Issue,IssueType, Status, Comment
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['email']
        extra_kwargs = {'email': {'validators' : []}}

class StorySerializer(ModelSerializer):
    class Meta:
        model = IssueType
        fields = ['story', 'id']

class StatusSerializer(ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'

class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class IssueSerializer(ModelSerializer):
    assigned_to = UserSerializer()
    def update(self, instance, validated_data):
        user_email = validated_data['assigned_to']
        instance.assigned_to = User.objects.get(email=user_email['email'])
        instance.summary = validated_data.get('summary', instance.summary)
        instance.status = validated_data.get('status', instance.status)
        instance.issue_type = validated_data.get('issue_type', instance.issue_type)
        instance.save()
        return instance
    class Meta:
        model = Issue
        fields = '__all__'
    
        
       
