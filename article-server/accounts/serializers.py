from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from movies.serializers import MovieSummarySerializer, ReviewSerializer
from django.contrib.auth import get_user_model


class CustomRegisterSerializer(RegisterSerializer):
    # 추가 설정 필드: nickname
    nickname = serializers.CharField(max_length=30)

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['nickname'] = self.validated_data.get('nickname', '')
        return data

class ProfileSerializer(serializers.ModelSerializer):
    like_movies = MovieSummarySerializer(many=True)
    reviews = ReviewSerializer(many=True)
    class Meta:
        model = get_user_model()
        fields = ('username', 'like_movies', 'reviews', )