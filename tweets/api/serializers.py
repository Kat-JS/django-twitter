from accounts.api.serializers import UserSerializer
from rest_framework import serializers
from tweets.models import Tweet

# serializer used for display
class TweetSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Tweet
        fields = ('id', 'user', 'created_at', 'content')

# used for create new tweet
class TweetCreateSerializer(serializers.ModelSerializer):
    content = serializers.CharField(min_length=6, max_length=140)

    class Meta:
        model = Tweet
        fields = ('content',)

    # used in serializers.save()
    def create(self, validated_data):
        # context request passed in serializer constructor
        user = self.context['request'].user
        content = validated_data['content']
        tweet = Tweet.objects.create(user=user, content=content)
        return tweet