import django_filters
from .models import LikeAnalytics


class LikeAnalyticsFilter(django_filters.FilterSet):
    from_date = django_filters.rest_framework.DateTimeFilter(field_name="date", lookup_expr='gte')
    to_date = django_filters.rest_framework.DateTimeFilter(field_name="date", lookup_expr='lte')
    class Meta:
        model = LikeAnalytics
        fields = ['from_date', 'to_date']
