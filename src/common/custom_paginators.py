from rest_framework.pagination import LimitOffsetPagination
from django.conf import settings

class CustomPagination(LimitOffsetPagination):
    limit_query_param = 'limit'
    offset_query_param = 'offset'
    max_limit = settings.REST_FRAMEWORK['PAGE_SIZE']