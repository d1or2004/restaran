from django.shortcuts import render, redirect
from .models import MasterChef, FoodMenu, TableOnline, Testimonial, Contact, ProductType, Costumer
from django.views import View


class LandingView(View):
    def get(self, request):
        menus = FoodMenu.objects.all()
        tables = TableOnline.objects.all()
        chefs = MasterChef.objects.all()
        costumer = Costumer.objects.all()
        testimonial = Testimonial.objects.all()

        return render(request, "main/index.html", context={
            "menus": menus,
            "tables": tables,
            "chefs": chefs,
            "costumer": costumer,
            "testimonial": testimonial
        })

    def post(self, request):
        ism = request.POST['ism']
        email = request.POST['email']
        date_time = request.POST['data_time']
        number_of_people = request.POST['number_of_people']
        requests = request.POST['requests']
        menu = TableOnline(ism=ism, email=email, date_time=date_time, number_of_people=number_of_people,
                           requests=requests)
        menu.save()
        return redirect('landing')


class AboutView(View):
    def get(self, request):
        chefs = MasterChef.objects.all()
        return render(request, "main/about.html", context={"chefs": chefs})


class ServicesView(View):
    def get(self, request):
        return render(request, "main/service.html")


class MenuView(View):
    def get(self, request):
        foodmenus = FoodMenu.objects.all()
        return render(request, "main/menu.html", context={"foodmenus": foodmenus})


class MunuDetailView(View):
    def get(self, request, id):
        producttype = ProductType.objects.get(id=id)
        return render(request, "main/munu.html", context={"producttype": producttype})


class TableOnlineView(View):
    def get(self, request):
        tables = TableOnline.objects.all()
        return render(request, "main/table.html", context={"tables": tables})

    # def post(self, request):
    #     tables = TableOnline.objects.all()


class BookTableOnlineView(View):
    def get(self, request):
        return render(request, "main/booking.html")

    # def post(self, request):
    #
    #     ism = request.POST['ism']
    #     email = request.POST['email']
    #     date_time = request.POST['data_time']
    #     number_of_people = request.POST['number_of_people']
    #     requests = request.POST['requests']
    #     menu = TableOnline(ism=ism, email=email, date_time=date_time, number_of_people=number_of_people,
    #                        requests=requests)
    #     menu.save()
    #     return redirect('booktableonline')


class OurTeamView(View):
    def get(self, request):
        team = MasterChef.objects.all()
        return render(request, "main/team.html",context={"team": team})


class TestimonialView(View):
    def get(self, request):
        testimonial = Testimonial.objects.all()
        return render(request, "main/testimonial.html", context={"testimonial": testimonial})


class ContactView(View):
    def get(self, request):
        return render(request, "main/contact.html")

    def post(self, request):
        first_name = request.POST['first_name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        contact = Contact(first_name=first_name, email=email, subject=subject, message=message)
        contact.save()
        return redirect('contact')
