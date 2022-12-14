### Imports ###
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Employees
from charts import data

### Home view ###
def home(request):
   template = loader.get_template('home.html')
   return HttpResponse(template.render())

### Analysis view ###
def analysis(request):
   template = loader.get_template('analysis.html')
   context = data.happiness() | data.productivity() | data.breaks() | data.gender() | data.age_groups() | data.company_size() | data.remote_days()
   return HttpResponse(template.render(context, request))

### Survey view ###
def survey(request):
   template = loader.get_template('survey.html')
   return HttpResponse(template.render({}, request))

### Add observation ###
def survey_add(request):
   gender = request.POST['gender']
   age = request.POST['age']
   children = request.POST['children']
   rural = request.POST['rural']
   executive = request.POST['executive']
   employees = request.POST['employees']
   wfh_days = request.POST['wfh_days']
   more_breaks = request.POST['more_breaks']
   wfh_day_condition = request.POST['wfh_day_condition']
   productivity = request.POST['productivity']
   entry = Employees(gender=gender, age=age, children=children, rural=rural, executive=executive, employees=employees, wfh_days=wfh_days, more_breaks=more_breaks, wfh_day_condition=wfh_day_condition, productivity=productivity)
   entry.save()
   return HttpResponseRedirect(reverse('home'))
