from django.core.paginator import Paginator


def paginations(request, posts_list):
    paginator = Paginator(posts_list, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return page_obj