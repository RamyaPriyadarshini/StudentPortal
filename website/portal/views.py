from django.shortcuts import render
from django.http import HttpResponse
from portal.models import Personal
from portal.models import Leave
from django.contrib.auth.decorators import login_required


@login_required
def profile(request):
    personal = Personal.objects.filter(user=request.user).values()[0]
    leave = Leave.objects.filter(user=request.user).values()[0]
    return render(request, 'portal/profile.html', {'personal': personal, 'leave': leave})
