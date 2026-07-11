from django.shortcuts import render

def home(request):
    peoples =[
        {'name':'Abhijeet','age':15},
        {'name':'Shreyan','age':17},
        {'name':'prajyot','age':24},
        {'name':'Om','age':26},
    ]
    vegetables = ["pumpkin","tomato","potato"]
    return render(request,"index.html",context={"peoples":peoples, "vegetables":vegetables})

def about(request):
    return render(request,"about.html")# render function se about.html template ko render kar diya

def contact(request):
    print("*"*10)
    return render(request,"contact.html")