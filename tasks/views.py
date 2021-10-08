from django.core import paginator
from django.shortcuts import render, redirect
from django.http import HttpResponse, response
import csv

from xlwt.Column import Column
from .models import *
from .forms import *
import xlwt
from django.core.paginator import Paginator 


# Create your views here.

def index(request):#to create the data
	tasks = Task.objects.all()
	form = TaskForm()
	p= Paginator(tasks,1)
	page=request.GET.get('page')
	task_list=p.get_page(page)
	if request.method =='POST':
		form = TaskForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('/')


	context = {'tasks':tasks,'form':form,'task_list':task_list}
	return render(request, 'tasks/list.html', context)








def updateTask(request, pk):# to update the task
	task = Task.objects.get(id=pk)

	form = TaskForm(instance=task)

	if request.method == 'POST':
		form = TaskForm(request.POST, instance=task)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}

	return render(request, 'tasks/update_task.html', context)

def deleteTask(request, pk):#to delete the task
	item = Task.objects.get(id=pk)

	if request.method == 'POST':
		item.delete()
		return redirect('/')

	context = {'item':item}
	return render(request, 'tasks/delete.html', context)
def export(request):# to export 
	response=HttpResponse(content_type="text/csv")
	writer=csv.writer(response)
	writer.writerow(['title'])

	for task in Task.objects.all().values_list('title'):
		writer.writerow(task)

	response['content-Disposition']='attachment; filename="task.csv"'

	return response





