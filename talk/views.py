from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import Baatkare
from django.db.models import Q
def login(req):
    if req.user.is_authenticated:
        return redirect("/chat/2")
    else:
        if req.method == "POST":
            username = req.POST.get('username')
            password = req.POST.get('password')
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(req, user)
                return redirect("/chat/2")
            else:
                messages.info(req, 'invalid user')
                return redirect("/login")
        else:
            return render(req, "login.html")

def index(req, user_id):
    if req.user.is_authenticated:
        if req.method == "POST":
            usermsg = req.POST.get('usermsg')
            oppo = req.POST.get('oppo')
            user = User.objects.get(id=req.user.id)
            oppuser = User.objects.get(id=oppo)
            p = Baatkare(userbot=user, oppsbot=oppuser, chatmsg=usermsg, reply=user)
            p.save()
            return redirect("/chat/"+oppo)

        username = req.GET.get('username')
        allusers = User.objects.exclude(id=req.user.id)
        userdata = get_object_or_404(User, pk=user_id)
        chats = Baatkare.objects.filter(Q(userbot=req.user.id)|Q(userbot=user_id)).filter(Q(oppsbot=user_id)|Q(oppsbot=req.user.id)).order_by('id')
        context = {'allusers': allusers, 'userdata': userdata, 'chats': chats}
        return render(req, "index.html", context)
    else:
        return redirect("/login")