from django.shortcuts import render
from .models import UserUI, UserUIPosition
from django.contrib.auth.decorators import login_required
from .forms import UserUIAddForm
from django.contrib.auth.models import User
import random

chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
def create_pass():
    for n in range(number):
        password =''
        for i in range(length):
            password += random.choice(chars)
        return password


# Create your views here.
def index(request):
    return render(request, 'index.html')

@login_required
def addUserUI(request):
    NewUserUI = UserUIAddForm(request.POST)
    if request.method == 'POST':
        if NewUserUI.is_valid():
            fioForm = NewUserUI.data['fio']
            needUserForm = NewUserUI.data['needUser']
            x_Form = NewUserUI.data['Pos_x']
            y_Form = NewUserUI.data['Pos_y']
            item = Block(nonce = int(nonce_a), time = datetime.datetime.now(), msg=msg_a)
            item = UserUI(fio = fioForm, needUserForm = needUserForm)
            if item.validate():
                item.save()
                NewUserUIPos = UserUIPosition(pos_x = x_Form, pos_y = y_Form, UserUIConnect = item)
                NewUserUIPos.save()
                if needUserForm:
                    NewUser = User.objects.create_user(username=fioForm[:3]+19, password=create_pass())
                    NewUser.save()
    return render(request, 'add.html', {'form': NewUserUI})


def Tree(request):
    Tree = UserUI.objects.all()
    TreePos = UserUIPosition.objects.all()
    context = {'Tree': Tree, 'TreePos': TreePos}
    return render(request, 'tree.html', context)