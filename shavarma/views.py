from django.shortcuts import render,get_object_or_404,redirect
from .models import shavarmaModel,positionOfPoint,comment
from .forms import commentForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def homepage(request):
    data = shavarmaModel.objects.all().order_by('rating')
    return render(request, 'shavarma/homepage.html',{'data':data})

#Раскрывает пункты меню точки
def detailShavarma(request, id_point):
    object = get_object_or_404(shavarmaModel, id = id_point)
    position = positionOfPoint.objects.filter(id_point__id = id_point).order_by('rating')
    return render(request,'shavarma/detailPoint.html',{'data':object,'pos':position,'point':id_point})

#Функция выводит подробную статистику о конкретной позиции
def detailposition(request,id_point,id_pos):
    position = get_object_or_404(positionOfPoint, id = id_pos)
    comm = comment.objects.filter(point__id = id_pos)
    object = get_object_or_404(shavarmaModel, id = id_point)
    #Считает рейтинг качеств
    if len(comm) != 0:
        rate_tasty = sum([i.tasty for i in comm])/len(comm)
        rate_struct = sum([i.struct for i in comm])/len(comm)
        rate_orig = sum([i.orig for i in comm])/len(comm)
        position.rating = (rate_tasty+rate_struct+rate_orig)/3
        return render(request,'shavarma/detailposition.html',{'data':object,'pos':position,'com':comm,'tasty':rate_tasty,'struct':rate_struct,'orig':rate_orig})
    else:
        return render(request,'shavarma/detailposition.html',{'data':object,'pos':position,'com':comm})


#Позволяет создать отзыв
@login_required
def addcomment(request,id_point,id_pos):
    comm = comment.objects.filter(point__id = id_pos)
    position = get_object_or_404(positionOfPoint, id = id_pos)
    position_all = positionOfPoint.objects.filter(id_point__id = id_point).order_by('rating')
    object = get_object_or_404(shavarmaModel, id = id_point)
    if request.method == 'GET':
        return render(request,'shavarma/commentposition.html',{'data':object,'pos':position})
    else:
        infoForm = commentForm(request.POST)
        newTodo = infoForm.save(commit=False)
        newTodo.user = request.user
        newTodo.point = position
        newTodo.save()
        rate_tasty = sum([i.tasty for i in comm])/len(comm)
        rate_struct = sum([i.struct for i in comm])/len(comm)
        rate_orig = sum([i.orig for i in comm])/len(comm)
        position.rating = (rate_tasty+rate_struct+rate_orig)/3
        position.save()
        #Считает рейтинг шавермачной исходя из позиций
        object.rating = sum([i.rating for i in position_all])/len(position_all)
        object.save()
        return redirect(homepage)
