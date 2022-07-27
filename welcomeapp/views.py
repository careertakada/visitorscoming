from os import times
from django.shortcuts import render, redirect
from sklearn.metrics import precision_score
from .models import Visitors

# Create your views here.
def input(request):
    return render(request, 'input.html')

def output(request):
    if request.method == 'POST':
        name = request.POST.get('input_name')
        name1 = request.POST.get('company')
        name2 = request.POST.get('person')
        name3 = request.POST.get('tantousya')
        name4 = request.POST.get('accompany')
        name5 = request.POST.get('text1')
        name6 = request.POST.get('dates')
        name7 = request.POST.get('time')
        name8 = request.POST.get('affair1')
        name9 = request.POST.get('affair2')
        Visitors.objects.create(person_name=name,company=name1,accompany=name4,text1=name5,person=name2,dates=name6,\
            times=name7,tantousya=name3,affair1=name8,affair2=name9)
        context = {
            'output_name': name,
            'company_name': name1,
            'person': name2,
            'tantousya': name3,
            'accompany': name4,
            'text1': name5,
            'dates': name6,
            'time': name7,
            'affair1':name8,
            'affair2':name9,

            }
        print(name)
        print(context)


    return render(request, 'output.html', context)

    
     
def kanri(request):
   visitors_list=Visitors.objects.all()
   context={'visitors':visitors_list}
   return render(request, 'kanri.html', context) 

def edit(request, pk):
    visitor_object=Visitors.objects.get(id=pk)
    if request.method == 'POST':
        name=request.POST.get('edit1')
        company_name=request.POST.get('edit2')
        ninzu=request.POST.get('edit3')
        entry_time=request.POST.get('edit4')
        texts=request.POST.get('edit25')
        accompany=request.POST.get('edit5')
        texts1=request.POST.get('edit26')

        print(name)
        print(company_name)

        visitor_object.person_name=name
        visitor_object.company=company_name
        visitor_object.person=ninzu
        visitor_object.visit_time=entry_time
        visitor_object.affair1=texts
        visitor_object.accompany=accompany
        visitor_object.affair2=texts1
        visitor_object.save()
        return redirect('kanri')

    else:
        # 下にcontextを後で追加
        context={'visitor':visitor_object}

        return render(request, 'edit_del.html', context)

def delete(request, pk):
    visitor_object=Visitors.objects.get(id=pk)
    print(visitor_object)
    visitor_object.delete()
    print(visitor_object)
    return redirect('kanri')