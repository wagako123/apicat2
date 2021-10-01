from django.shortcuts import render
from .models import CarMake, carInstance, CarModel, CarType, Car
# Create your views here.

def index(request):
    """View function to specify the site hompage"""

    #generate a count of all the cars in the system'
    cars_count = Car.objects.all().count()
    car_instance_count = carInstance.objects.all().count()

    #generate table from the DB
    car_list= Car.objects.all()


    #count the number of available cars
    num_cars_available = carInstance.objects.filter(status__exact = 'a').count()

    number_of_visits = request.session.get('number_of_visits', 0)
    request.session['number_of_visits'] = number_of_visits + 1

    #Context Specifies how the data will be presented in the rendered view
    context = {
        'cars_count': cars_count,
        'num_cars_available': num_cars_available,
        'car_instance_count': car_instance_count,
        'number_of_visits': number_of_visits,
        'car_list':car_list,
        #'num_toyota': num_toyota,
    }

    #Render a HTML file, index.html containing the data in the context
    return render(request, 'index.html', context=context)
