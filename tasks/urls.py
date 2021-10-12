from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name="list"),
	path('update_task/<str:pk>/', views.updateTask, name="update_task"),
	path('dele/admin/login/?next=/admin/te/<str:pk>/', views.deleteTask, name="deleteit"),
	path('export/',views.export,name="export"),
	path('import',views.simple_upldad,name="import"),
	# path('exporter',views.export_excel,name="excel_export"),
]