from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from .serializers import ArticleListSerializer
from .models import Article

from rest_framework.permissions import IsAuthenticated

@permission_classes([IsAuthenticated])
@api_view(['GET','POST'])
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        pass