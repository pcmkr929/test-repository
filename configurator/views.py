from django.shortcuts import render
from django.views import generic

from configurator.models import InstanceConfig
from configurator.models import MQTTConfig
from configurator.models import SQLConfig
from configurator.forms import InstanceForm
from configurator.forms import MQTTForm
from configurator.forms import SQLForm

# Create your views here.

# def home_view(request):
#     # form = UserInfoForm(request.POST or None)
#     # if form.is_valid():
#     #     form.save()
#     #     # re-render the form after hitting save
#     #     form = UserInfoForm()

#     # # Acces via the obj variable connected to the models class Userinfo
#     # context = {
#     #     'form': form,
#     # }
#     # # "userinfo/detail.html": look inside of the 'userinfo' folder in the 
#     # #   template folder, take the detail.html there
#     # return render(request, "userinfos/userinfo_create.html", context)
#     context = {

#     }

#     return render(request, "configurator/home_view.html", context)

# def userinfo_create_view(request):
#     form = UserInfoForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         # re-render the form after hitting save
#         form = UserInfoForm()

#     # Acces via the obj variable connected to the models class Userinfo
#     context = {
#         'form': form,
#     }
#     # "userinfo/detail.html": look inside of the 'userinfo' folder in the 
#     #   template folder, take the detail.html there
#     return render(request, "userinfos/userinfo_create.html", context)






# In a function, the data in a form should received

#def instance_choice:

#class InstanceView(models.)



def instance_view(request):
    form2 = InstanceConfig.INSTANCE_CHOICES
    form = InstanceForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = InstanceForm
    context = {
        'form': form,   # 'form': form,
    }

    if request.method == 'POST':
        # THIS WAY YOU CAN READ WHICH VALUE IS CHOSEN AT 
        #   THE DROPDOWN-MENU FORM, ACCESS VIA THE
        #   LIST VARIABLE NAME 'instance_type'
        type_chosen = request.POST.get('instance_type')
        print(request.POST.get('instance_type'))
        print(InstanceConfig.objects.all())
        
        # if type_chosen == 'opc':
        #     print("OPC Chosen")

    return render(request, "configurator/instance_view.html", context)































def base_view(request):

    return render(request, "configurator/home.html")

def mqtt_config_view(request):
    print(request.user)
    form = MQTTForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = MQTTForm

    context = {
        'form': form,
    }

    return render(request, "configurator/mqtt_view.html", context)

def sql_config_view(request):
    form = SQLForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = SQLForm

    context = {
        'form': form,
    }

    return render(request, "configurator/sql_view.html", context)