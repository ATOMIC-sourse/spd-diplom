from django.core.serializers import serialize
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render

from posts.models import Post, User, Like, Comment
from posts.serializers import PostSerializer, CommentSerializer


# Create your views here.

@api_view(['GET', 'POST'])
def news_feed(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        ser = PostSerializer(posts, many=True)
        return Response(ser.data)
    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

@api_view(['POST'])
def add_comment(request, post_id):
    try:
        post = Post.objects.get(pk = post_id)
    except Post.DoesNotExist:
        return Response(
            {"error": f"Пост с ID {post_id} не найден"},
            status=status.HTTP_404_NOT_FOUND
        )
    comment_data = request.data.copy()
    comment_data["POST"] = post.id
    serializer = CommentSerializer(data=comment_data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)
