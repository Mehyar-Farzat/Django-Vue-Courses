from django_filters import rest_framework as filters


class CourseFilter(filters.FilterSet):
    category = filters.CharFilter(field_name='category_id', method='filter_by_category')

    def filter_by_category(self,queryset,value):
        url_categories = value.split(',')
        return queryset.filter(category__id__in= url_categories)