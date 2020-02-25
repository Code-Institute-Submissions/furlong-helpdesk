from django.conf.urls import url, include
from .views import view_hours, view_completed_hours, view_bookCalendarEvents

urlpatterns = [
    url(r'^$', view_hours, name='view_hours'),
    url(r'^complete_hours$', view_completed_hours, name='view_completed_hours'),
    url(r'^view_bookCalendarEvents$', view_bookCalendarEvents, name='view_bookCalendarEvents'),
]
