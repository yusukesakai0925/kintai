from django.shortcuts import render
from django.http.response import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from attendance.models import Attendances
from django.contrib.auth.models import User
from datetime import datetime
import pandas as pd

import logging
logging.basicConfig(level=logging.DEBUG,
format="%(asctime)s - %(levelname)s:%(name)s - %(message)s",
filename="./backup_database_log")

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'backup_database.html'
    login_url = '/accounts/login/'
 
class BackupDatabase(LoginRequiredMixin, TemplateView):
    login_url = '/accounts/login'
    def post(self, request, *args, **kwargs):
        push_type = request.POST.get('push_type')
        today = datetime.today()
        this_month = datetime.now().month
        all_user = User.objects.all()

        def make_all_attendance():
            attendance = Attendances.objects.all()
            all_attendance = pd.DataFrame(attendance.values)
            all_attendance.to_csv("../csv/" + this_month + user + "attendance")

        def make_todays_attendance():
            attendance = Attendances.objects.filter(
            attendance_time__date = today
            ).order_by('user_id')
            todays_attendance = pd.DataFrame(attendance.values)
            todays_attendance.to_csv("../csv/" + today + "attendance")
        
        def make_month_attendance(user):
            attendance = Attendances.objects.filter(
            user = User.objects.get(user=user),
            attendance_time__date = this_month
            ).order_by('attendance_date')
            month_attendance = pd.DataFrame(attendance.values)
            month_attendance.to_csv("../csv/" + this_month + user + "attendance")

        def make_month_all_attendance():
            attendance = Attendances.objects.filter(
            user = all_user,
            attendance_time__date = this_month
            ).order_by('attendance_date')
            month_attendance = pd.DataFrame(attendance.values)
            month_attendance.to_csv("../csv/" + this_month + user + "attendance")
        
        make_all_attendance()
        make_todays_attendance()
        for user in all_user:
            make_month_attendance(user)
        make_month_all_attendance()
        

        response_body = {"result": "success"}    
        return JsonResponse(response_body)


