from articles.models import Article

"""
django 환경설정 필수 Using settings without setting DJANGO_SETTINGS_MODULE
https://docs.djangoproject.com/en/4.0/topics/settings/#using-settings-without-setting-django-settings-module

실행방법)
python script.py

manage.py => 장고 환경 관련 기능을 실행하게 해줌
"""

from django.conf import settings

settings.configure(DEBUG=True)

# 1. 수집한 데이터 불러오기
# API, CSV 파일..
# articles = [...]

# 2. Article 테이블에 넣기
# Tip. 한 번에 여러 개 넣을 때는 bulk_create 사용
# for article in articles:
#     Article.objects.create(
#         title=article.title,
#         ...
#     )