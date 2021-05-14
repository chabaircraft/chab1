from django.db.models import Q
from django.shortcuts import render,redirect
from.models import tb_products
from django.conf import settings
from django.core.mail import send_mail

def index(request):
    return render(request, "index.html")



def search(request):
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(part_number__exact=query)## |
        )
        results =tb_products.objects.filter(qset)
    else:
        results = []
    return render(request,"prueba.html", {"results": results, "query": query})

def send(request):
     if request.method =="POST":
        asunto=request.POST["txtasunto"]
        message=request.POST["mensaje"]+"|Remitente: "+request.POST["txtemail"]
        email_from=settings.EMAIL_HOST_USER
        email_para=["chabaircraftparts@gmail.com"] 
        send_mail(asunto, message, email_from, email_para, fail_silently=False)
        return render(request,"prueba2.html")
     return render(request,"prueba2.html")
   