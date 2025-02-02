from django.shortcuts import render , redirect
from animal.models import Animal
from django.contrib import messages

# Create your views here.


def page_a (request):
    return render(request, 'page_a.html')
def page_b (request):
    return render(request, 'page_b.html')

def page_c (request):
    return render(request, 'page_c.html')


def create(request):
    if request.method == "POST":
        base_name = request.POST['base_name']
        scien_name = request.POST['scien_name']
        weight = request.POST['weight_name']
        number = request.POST['number_name']
        place = request.POST['place_name']
        print(base_name,scien_name,weight,number,place)

        # Save Data

        animal = Animal.objects.create(
            base_name = base_name,
            scien_name = scien_name,
            weight = weight,
            number = number,
            place = place,
        )
        Animal.save()

        messages.success(request, "Successful!")

        return redirect("/animal")

    else:
        return render(request, 'create.html')
    
def index(request):
        animal = Animal.objects.all()
        return render(request, 'index.html', {'animals': animal})