from rest_framework import serializers
from posts.models import User, Comment, Post, Like, likes_count


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['author', 'post', 'text', 'created_at']

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = [f'likes_count']


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = User.objects.create_user(
            username= validated_data['username'],
            email= validated_data['email'],
            password= validated_data['password']
        )
        var = user.save
        return var


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'text', 'image', 'created_at', 'comments', "likes_count"]
    comments = CommentSerializer(many=True)
    likes_count = serializers.SerializerMethodField()

    def get_likes_count(self, post_id):
        return post_id.likes.count()

