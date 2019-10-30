from django.shortcuts import render

from userinfo.forms import UserInfoForm, RawUserInfoForm
from userinfo.models import UserInfo

# Create your views here.

"""
    Pure Django Form
"""

# def userinfo_create_view(request):
#     my_form = RawUserInfoForm()
#     if request.method == "POST":    
#         # Creating an instance of RawUserInfoForm
#         my_form = RawUserInfoForm(request.POST)
#         if my_form.is_valid():
#             # now the data is good
#             print(my_form.cleaned_data)
#             UserInfo.objects.create(**my_form.cleaned_data)
#         else:
#             print(my_form.errors)
#     context = {
#         "form": my_form,
#     }
#     return render(request, "userinfos/userinfo_create.html", context)

"""
    Raw HTML Form
"""

# def userinfo_create_view(request):
#     # print(request.GET) # not recommended, GET is an unsafe method to store data
#     # print(request.POST) # POST is better in security
#     if request.method == "POST": # Makes sure, that the form is using the right method
#         my_new_title = request.POST.get('title')
#         print(my_new_title)
#         # UserInfo.objects.create(title=my_new_title)
#     context = {}
#     return render(request, "userinfos/userinfo_create.html", context)


def userinfo_create_view(request):
    form = UserInfoForm(request.POST or None)
    if form.is_valid():
        form.save()
        # re-render the form after hitting save
        form = UserInfoForm()

    # Acces via the obj variable connected to the models class Userinfo
    context = {
        'form': form,
    }
    # "userinfo/detail.html": look inside of the 'userinfo' folder in the 
    #   template folder, take the detail.html there
    return render(request, "userinfos/userinfo_create.html", context)

def userinfo_detail_view(request):
    obj = UserInfo.objects.get(id=1)
    # --- harcoded context dictionary ---
    # context = {
    #     'name'   : obj.name,
    #     'age'    : obj.age,
    #     'date'   : obj.date,
    #     'comments': obj.comments,
    # }

    # Acces via the obj variable connected to the models class Userinfo
    context = {
        'object': obj,
    }
    # "userinfo/detail.html": look inside of the 'userinfo' folder in the 
    #   template folder, take the detail.html there
    return render(request, "userinfos/userinfo_detail.html", context)