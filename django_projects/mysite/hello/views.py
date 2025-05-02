from django.http import HttpRequest, HttpResponse
from django.views import View
from django.views import generic


class IndexView(generic.ListView):
    template_name = "hello/index.html"
    context_object_name = "reverse_urls"

    def get_queryset(self):
        return [
            ("hello:sessions", "Session Counter"),
            ("hello:cookies", "Cookie Game"),
        ]


class SessionCounterView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        visit_count: int = request.session.get("visit_count", 0) + 1
        request.session["visit_count"] = visit_count
        if visit_count > 4:
            del request.session["visit_count"]
        response = f"Your session has visited this page {visit_count} time{'s' if visit_count > 1 else ''}"
        response = response.encode("utf-8")
        response = HttpResponse(response)
        response.set_cookie("dj4e_cookie", "997f60c2", max_age=1000)
        return response


class CookieCounterView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        cookie_counter = request.COOKIES.get("cookie_counter", "0")
        cookie_counter = int(cookie_counter)
        response = HttpResponse(
            f"Your current cookie_counter value is: {request.COOKIES.get('cookie_counter')}"
        )
        response.set_cookie("cookie_counter", str(cookie_counter + 1))
        return response
