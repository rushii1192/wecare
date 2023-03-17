from django.shortcuts import render,HttpResponse
from .models import DoctorModel



# Create your views here.
def createDoctor(request):
    if request.method == 'POST':
        doctor = DoctorModel(
            name=request.POST.get('name'), 
            email=request.POST.get('email'),
        )
        doctor.save()

        return HttpResponse("Successfully created")
    
    return render(request, 'register.html')

def updateDoctor(request):
    if request.method == 'POST':
        doctor = DoctorModel(
            name=request.POST.get('name'), 
            email=request.POST.get('email'),
        )
        doctor.save()







# reference for update model from geekforgeeks 
# # create your views here. 
# def detail_view(request, id):
#     context ={}
#     context["data"] = GeeksModel.objects.get(id = id)

#     return render(request, "detail_view.html", context)

# # update view for details
# def update_view(request, id):
#     context ={}
#     obj = get_object_or_404(GeeksModel, id = id)
#     # pass the object as instance in form
#     form = GeeksForm(request.POST or None, instance = obj)
#     # save the data from the form and
#     # redirect to detail_view
#     if form.is_valid():
#         form.save()
#         return HttpResponseRedirect("/"+id)
#     # add form dictionary to context
#     context["form"] = form
#     return render(request, "update_view.html", context)