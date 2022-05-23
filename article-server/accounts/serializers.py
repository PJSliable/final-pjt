from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth import get_user_model
from movies.models import Movie
from movies.serializers import MovieSummarySerializer
from community.models import Review
from community.serializers import ReviewSerializer


class CustomRegisterSerializer(RegisterSerializer):
    # 추가 설정 필드: nickname
    nickname = serializers.CharField(max_length=30)

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['nickname'] = self.validated_data.get('nickname', '')
        return data

class ProfileSerializer(serializers.ModelSerializer):
    my_movies = MovieSummarySerializer(many=True, read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)
    class Meta:
        model = get_user_model()
        fields = ('username', 'my_movies', 'reviews','nickname', )



class ChangePasswordSerializer(serializers.Serializer):
    model = get_user_model()
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)