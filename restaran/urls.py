from django.urls import path
from .views import LandingView, AboutView, MenuView, TableOnlineView, ServicesView, BookTableOnlineView, OurTeamView, \
    TestimonialView, ContactView, MunuDetailView

urlpatterns = [
    path('', LandingView.as_view(), name='landing'),
    path('about/', AboutView.as_view(), name='about'),
    path('foodmenu/', MenuView.as_view(), name='foodmenu'),
    path('tableonline/', TableOnlineView.as_view(), name='tableonline'),
    path('services/', ServicesView.as_view(), name='services'),
    path('booktableonline/', BookTableOnlineView.as_view(), name='booktableonline'),
    path('ourteam/', OurTeamView.as_view(), name='ourteam'),
    path('testimonial/', TestimonialView.as_view(), name='testimonial'),
    path('contact/', ContactView.as_view(), name='contact'),
    path("<int:id>", MunuDetailView.as_view(), name='munudetail'),

]
