from django.http import HttpResponseRedirect, HttpRequest, HttpResponse
from django.views import generic


class IndexView(generic.ListView):
    template_name = "home/index.html"
    context_object_name = "reverse_urls"

    def get_queryset(self):
        return [
            ("polls:index", "A Polls Application"),
            ("hello:index", "Cookies And Sessions"),
        ]
