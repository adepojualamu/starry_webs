from django.views.generic import TemplateView
from django.urls import path
from home.views import ContactView


urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html"), name="home"),
    path('contact/', ContactView.as_view(), name="contact")
]