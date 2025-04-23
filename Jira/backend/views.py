from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import IssueSerializer, UserSerializer, StorySerializer, StatusSerializer, CommentSerializer
from .models import Issue, IssueType, Status, Comment
from django.contrib.auth import get_user_model

User = get_user_model()

@api_view(['GET'])
def jira_home(request):
    issues = Issue.objects.all()
    serializer = IssueSerializer(issues, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_issue(request, pk):
    issue = Issue.objects.filter(id=pk).first()
    if not issue:
        return Response({'Detail' : f'Issue with {pk} does not exist'},
                        status.HTTP_404_NOT_FOUND)
    serializer = IssueSerializer(issue, many=False)
    return Response(serializer.data)
    
    
@api_view(['PUT'])
def update_issue(request, pk):
    data = request.data
    print(data)
    issue = Issue.objects.get(id=pk)
    serializer = IssueSerializer(instance=issue, data=data)
    if serializer.is_valid(raise_exception=True):
        print("Inside", serializer.validated_data)
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def create_issue(request):
    issue = Issue.objects.create(summary=request.data['summary'], 
                                 assigned_to=User.objects.get(email=request.data['assigned_to']),
                                 issue_type=IssueType.objects.get(story=request.data['issue_type']),
                                 status=Status.objects.get(status=request.data['status']))
    serializer = IssueSerializer(instance=issue, many=False)
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_issue(request, pk):
    issue = Issue.objects.get(id=pk)
    issue.delete()
    return Response('Issue is SuccesFully Deleted')

'''Comment APIS'''
@api_view(['GET'])
def get_comments(request, id):
    print(id)
    post = Comment.objects.filter(issue_id=id)
    serializer = CommentSerializer(post, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_comment(request):

    comment = Comment.objects.create(post=request.data['post'], 
                                 user=User.objects.get(email=request.data['user']),
                                 issue_id=Issue.objects.get(id=request.data['issue_id']))
    serializer = CommentSerializer(instance=comment, many=False)
    return Response(serializer.data)

''' STATUS APIS '''
@api_view(['GET'])
def get_status(request):
    status = Status.objects.all()
    serializer = StatusSerializer(status, many=True)
    return Response(serializer.data)

''' Story APIS'''
@api_view(['GET'])
def get_stories(request):
    story = IssueType.objects.all()
    serializer = StorySerializer(story, many=True)
    return Response(serializer.data)

'''USER APIS'''
@api_view(['GET'])
def get_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def register_user(request):
    data = request.data
    if data['password'] != data['confirm_password']:
        return Response('User Password and confirm Password dont match')
    jirauser = User.objects.create(username=data['username'], 
                                    email=data['email'],
                                    password=data['password'])
    serializer = UserSerializer(instance=jirauser, many=False)
    return Response(serializer.data)
