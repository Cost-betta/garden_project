from rest_framework.pagination import LimitOffsetPagination


class ProjectLimitOffsetPagination(LimitOffsetPagination):
    """Пользовательский класс для пагинации основанный на limit/offset.

    Examples:
        http://api.example.org/accounts/?limit=100            - first 100
        http://api.example.org/accounts/?offset=400&limit=100 - fifth hundred/page
        http://api.example.org/accounts/?limit=null           - all records (in fact first million)
    """

    def get_limit(self, request):
        param = self.limit_query_param
        if param and request.query_params.get(param) == 'null':  # FIXME limit must be explicit, not null or large value
            return 10 ** 6

        return super().get_limit(request)
