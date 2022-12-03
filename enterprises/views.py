import json
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Invoice, WorkImages
from django.contrib.auth.decorators import login_required
from django.db.models import Max
import datetime

from .utils import invoice_data_processor

# Create your views here.

def Home(request):
    images = WorkImages.objects.all()

    return render(request,'enterprises/home.html',context={"images":images})

def About(request):
    return render(request,'enterprises/about.html')

def Contact(request):
    return render(request,'enterprises/contact.html')

def Gallery(request):
    images= WorkImages.objects.all()
    context={ "images": images }
    
    return render(request,'enterprises/gallery.html', context)


def Boss(request):
    if not request.user.is_authenticated:
        return redirect('admin/login/?next=/boss')
    else:
        context={}
        context['invoices']=Invoice.objects.all().order_by('-id')
        return render(request,'enterprises/boss.html',context)

def CreateInvoice(request):
    #return render(request,'enterprises/invoice_create.html')
    if not request.user.is_authenticated:
        return redirect('admin/login/?next=/create')
    else:
        context = {}
        context['default_invoice_number'] = Invoice.objects.all().aggregate(Max('invoice_number'))['invoice_number__max']
        if not context['default_invoice_number']:
            context['default_invoice_number'] = 41
        else:
            context['default_invoice_number'] += 1

        context['default_invoice_date'] = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d')

        if request.method == 'POST':
            print("POST received - Invoice Data")

            invoice_data = request.POST


            invoice_data_processed = invoice_data_processor(invoice_data)
        
            # save invoice
            invoice_data_processed_json = json.dumps(invoice_data_processed)
            new_invoice = Invoice(
                                invoice_number=int(invoice_data['invoice-number']),
                                invoice_date=datetime.datetime.strptime(invoice_data['invoice-date'], '%Y-%m-%d'),
                                invoice_order_number=invoice_data['invoice-order-number'], 
                                invoice_order_number_2=invoice_data['invoice-order-number-2'],
                                invoice_to=invoice_data['invoice-to'],
                                invoice_heading=invoice_data['invoice-heading'],
                                invoice_json=invoice_data_processed_json)
            new_invoice.save()
            print("INVOICE SAVED")



            #return redirect('invoice_viewer', invoice_id=new_invoice.id)

        return render(request, 'enterprises/invoice_create.html', context)

def ViewInvoice(request,invoice_id):
    if not request.user.is_authenticated:
        return redirect('admin/login/?next=/boss')
    else:
        invoice_obj=get_object_or_404(Invoice,  id=invoice_id)
        context = {}
        context['invoice'] = invoice_obj
        context['invoice_data'] = json.loads(invoice_obj.invoice_json)
        total_amt=context['invoice_data']['invoice_total_amt']
        gst_rate=int(context['invoice_data']['gst_rate']) /100
        gst_amt=gst_rate*total_amt
        context['gst_amt'] = gst_amt
        


        return render(request, 'enterprises/invoice_printer.html',context)

def DeleteInvoice(request,invoice_id):
    if not request.user.is_authenticated:
        return redirect('admin/login/?next=/boss')
    else:
        invoice_obj=get_object_or_404(Invoice,  id=invoice_id)
        invoice_obj.delete()
        return redirect('boss')