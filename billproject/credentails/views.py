from django.shortcuts import render,redirect
from . models import Registers
from dateutil.relativedelta import relativedelta
from datetime import datetime, timedelta
from django.http import HttpResponse
def sregister(request):
    register=Registers.objects.all()
    if request.method == 'POST':

        admn_no = request.POST.get('admn_no')

        sname = request.POST.get('sname')

        dob = request.POST.get('dob')

        aadharno = request.POST.get('aadharno')
        email_id = request.POST.get('email_id')

        phno = request.POST.get('phno')

        address = request.POST.get('address')

        course = request.POST.get('course')
        doj = request.POST.get('doj')
        duration = int(request.POST.get('duration'))
        end_date = (datetime.strptime(doj, '%Y-%m-%d') + relativedelta(months=duration)).strftime('%Y-%m-%d')

        mode = request.POST.get('mode')

        course_fee = int(request.POST.get('course_fee'))

        emi = int(request.POST.get('emi'))
        permonth = course_fee / emi
        register=Registers(admn_no=admn_no,sname=sname,dob=dob,aadharno=aadharno,email_id=email_id,
                                phno=phno,address=address,course=course,doj=doj,duration=duration,
                                end_date=end_date,mode=mode,course_fee=course_fee,emi=emi,permonth=permonth)
        register.save()
        print("Data Saved")

    else:
        doj = ''
        duration = ''
        end_date = ''

    context = {
        'doj': doj,
        'duration': duration,
        'end_date': end_date
    }


    return render(request,'studentregister.html',context)
def searchindex(request):
    register=Registers.objects.all()
    context={
        'register_list':register,
             }
    return render(request,'searchindex.html',context)
def detail(request,reg_id):
    register=Registers.objects.get(id=reg_id)
    return render(request,'registerdetail.html',{'register':register})
