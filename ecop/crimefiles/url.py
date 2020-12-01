from django.conf.urls import include,url
from django.contrib import admin


from django.views.generic import TemplateView
from .views import (
	complaint_create,
	complaint_detail,
	complaint_list,
	complaint_update,
	fir_create,
	copstatus_create,
	casestatus_create,
        LoginView,
	caseclose,
	
	)

app_name = "test"
urlpatterns = [
	# url(r'^login$',login),
	url(r'^login/$',LoginView.as_view(template_name='login_form.html'),name='login'),
	url(r'^createcomplaint$',complaint_create),
	url(r'^(?P<id>\d+)/createfir$',fir_create),
	url(r'^(?P<id>\d+)/createcopstatus$',copstatus_create),
	url(r'^(?P<id>\d+)/createcasestatus$',casestatus_create),
	url(r'^(?P<id>\d+)/closecase$',caseclose),
	url(r'^$', complaint_list,name="list"),
	url(r'^(?P<id>\d+)/edit$', complaint_update,name="update"),
	url(r'^(?P<id>\d+)/$', complaint_detail,name="detail"),
	
   
	]

