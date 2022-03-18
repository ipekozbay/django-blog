from django.http import HttpResponse
from django.shortcuts import render

data = {
    "blogs":[
        {
            "id": 1,
            "title" : "js",
            "image": "js.jpeg",
            "is_active": True,
            "is_home": False,

            "description": "good course"
        },
                {
            "id": 2,
            "title" : "django",
            "image": "django2.jpeg",
            "is_active": True,
            "is_home": True,

            "description": "good course"
        },
                {
            "id": 3,
            "title" : "web",
            "image": "web.jpeg",
            "is_active": False,
            "is_home": True,

            "description": "good course"
        },
    ]
}
def index(request):
    context = {
        "blogs": data["blogs"]
    }
    return render(request,"blog/index.html",context)

def blogs(request):
    context = {
        "blogs": data["blogs"]
    }
    return render(request,"blog/blogs.html",context)  
     
def blog_details(request,id):
    return render(request,"blog/blog-details.html",{
        "id":id
    })