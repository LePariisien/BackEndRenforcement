from rest_framework.pagination import PageNumberPagination

class LivrePagination(PageNumberPagination):
    page_size = 5 
    page_size_query_param = 'page_size'
    max_page_size = 100

class EmpruntPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 50