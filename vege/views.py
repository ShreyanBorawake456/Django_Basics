from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator



# Create your views here.
@login_required(login_url='/login/')
def recipes(request):

    if request.method =="POST":  #post ki  madat se data forntend se backend me aaya
        data = request.POST
        recipe_image = request.FILES.get('recipe_image')
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')

        Recipe.objects.create(
            recipe_image = recipe_image,
            recipe_name = recipe_name,
            recipe_description = recipe_description,

        )# create method se data ko database me save kar diya

        return redirect('/recipes/')# redirect se page ko refresh kar diya taki naya data show ho jaye
    
    queryset = Recipe.objects.all()  # queryset me sabhi recipes ko fetch kiya

    if request.GET.get('search'):
        search = request.GET.get('search') # search ke basis pe data ko filter kiya
        queryset = queryset.filter(recipe_name__icontains=search) # recipe_name me search term ko check kiya aur filter kiya

    context = {'recipes': queryset} # context me recipes ko pass kiya taki template me use kar sake

    return render(request, 'recipes.html',context)

def delete_recipe(request, id):
    recipe = Recipe.objects.get(id=id) # id ke basis pe recipe ko fetch kiya
    recipe.delete() # delete method se recipe ko delete kar diya
    return redirect('/recipes/') # redirect se page ko refresh kar diya taki naya data show ho jaye 

def update_recipe(request, id):
    recipe = Recipe.objects.get(id=id) # id ke basis pe recipe ko fetch kiya
    if request.method =="POST": 
        recipe_image = request.FILES.get('recipe_image')
        recipe_name = request.POST.get('recipe_name')
        recipe_description = request.POST.get('recipe_description')

        recipe.recipe_image = recipe_image
        recipe.recipe_name = recipe_name
        recipe.recipe_description = recipe_description

        if recipe_image: # agar recipe_image exist karta hai to hi update karo
             recipe.recipe_image = recipe_image

        recipe.save() # save method se data ko database me save kar diya

        return redirect('/recipes/')# redirect se page ko refresh kar diya taki naya data show ho jaye
    context = {'recipe': recipe} # context me recipe ko pass kiya taki template me use kar sake  
    return render(request, 'update_recipe.html',context)


def login_page(request):

    if request.method == "POST": 
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists(): # agar username exist nahi karta hai to error message show kar diya
            messages.error(request, "Invalid username")
            return redirect('/login/') 
        
        user = authenticate(username=username, password=password) # is used to check whether the entered username and password are correct
        
        if user is None: # agar user None hai to matlab username ya password galat hai
            messages.error(request, "Invalid username or password")
            return redirect('/login/')
        
        else:
            login(request, user) # login method se user ko login kar diya
            return redirect('/recipes/')

    return render(request, 'login.html') # render karna mablab template ko show karna, login.html template ko show kar diya

def logout_page(request):
    logout(request)
    return redirect('/login/')

def register_page(request):
    if request.method == "POST": 
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username=username) # username ke basis pe user ko check kiya ki wo exist karta hai ya nahi

        if user.exists():
            messages.error(request, "Username already exists.")
            return redirect('/register/') # agar user exist karta hai to register page pe hi redirect kar diya

        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username
        )
        user.set_password(password)
        user.save()

        return redirect('/register/')
        messages.success(request, "Account created successfully.")

    return render(request, 'register.html')


def get_students(request):
    queryset = Student.objects.all() # sabhi students ko fetch kiya
    paginator = Paginator(queryset, 25)  # Show 25 contacts per page.

    page_number = request.GET.get("page", 1)  # agar page number nahi hai to default 1 set kar diya
    page_obj = paginator.get_page(page_number)
    return render(request, 'report/students.html', {'queryset': page_obj})

    print(page_obj)  # page_obj me current page ka data hai, isse template me use kar sakte hai

def success_page(request):
    return render(request, 'success_page.html')