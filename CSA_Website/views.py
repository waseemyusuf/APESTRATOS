from django.shortcuts 		   import render




# Create your views here.
def home(request ):



	return render(request, "base/base_plate.html")

def home_fr(request ):


	return render(request, "base/base_plate_2.html")