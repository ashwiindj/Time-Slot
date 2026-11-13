from django.shortcuts import render
from django.db.models import Case, When, IntegerField
from .models import TimeSlot

def timetable_view(request):

    timetable = TimeSlot.objects.annotate(
        day_order=Case(
            When(day='Monday', then=1),
            When(day='Tuesday', then=2),
            When(day='Wednesday', then=3),
            When(day='Thursday', then=4),
            When(day='Friday', then=5),
            When(day='Saturday', then=6),
            output_field=IntegerField()
        )
    ).order_by('day_order', 'start_time')

    return render(
        request,
        'timetable/timetable.html',
        {'timetable': timetable}
    )
