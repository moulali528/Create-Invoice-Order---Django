from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Invoice
from .serializers import InvoiceSerializer


# Create your views here.


def invoiceDetails(name):
    return HttpResponse('Dearils are coiming !!!')


@api_view(['GET'])
def invoiceList(request):
	tasks = Invoice.objects.all()
	serializer = InvoiceSerializer(tasks, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def invoiceDetails(request, pk):
      task = Invoice.objects.get(id=pk)
      context = {'task':task}
      serializer = InvoiceSerializer(task, many=False)
      return Response(serializer.data)
      
      


