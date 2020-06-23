from django.http import HttpResponse
from visitas_granada.models import Visita, Comentario
from django.template import loader
from django.shortcuts import render, redirect
from visitas_granada.forms import VisitaForm
from django.contrib import messages

from rest_framework import viewsets, permissions
from visitas_granada.serializers import VisitaSerializer, ComentarioSerializer
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework.parsers import JSONParser

import logging
logger = logging.getLogger(__name__)


def index(request):
    # Number of visit to show in main page
    num_show_visit = 3
    # Get all visit
    visit_list = Visita.objects.order_by('-id').all()
    total_visits = len(visit_list)
    visit_list = visit_list[:num_show_visit]
    context = {'visit_list': visit_list, 'total_visits': total_visits}
    return render(request, 'visitas_granada/index.html', context)


def detail(request, visit_id):
    try:
        visit = Visita.objects.get(pk=visit_id)
    except Visita.DoesNotExist:
        raise Http404("La visita con " + str(visit_id) + "no existe.")

    comment_list = Comentario.objects.all()
    return render(request, 'visitas_granada/detail.html', {'visit': visit, 'comment_list': comment_list})


def visit_list_view(request):
    visit_list = Visita.objects.order_by('-id').all()
    context = {'visit_list': visit_list}

    if (request.GET.get('DeleteButton')):
        Visita.objects.filter(id = request.GET.get('DeleteButton')).delete()
        messages.add_message(request, messages.INFO, 'Visita eliminada con éxito.')
        logger.info("Visit eliminated successfully")

    return render(request, 'visitas_granada/visit_list_view.html', context)


def new_visit(request):
    form = VisitaForm()

    if request.method == "POST":
        form = VisitaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'Nueva visita creada con éxito.')
            logger.info("Visit successfully created.")
            return redirect('visit_list_view')
    else:
        form = VisitaForm()

    return render(request, 'visitas_granada/new_visit.html', {'form': form})


def edit_visit(request, visit_id):
    try:
        visit = Visita.objects.get(pk=visit_id)
    except:
        logger.debug('Visit ' + str(visit_id) + ' not found.')
        return HttpResponse(status=404)

    if request.method == "POST":
        form = VisitaForm(request.POST, instance=visit)
        if form.is_valid():
            visit = form.save(commit=False)
            visit.save()
            messages.add_message(request, messages.INFO, 'Visita actualizada con éxito.')
            logger.info("Visit successfully edited.")
            return redirect('visit_list_view')
    else:
        form = VisitaForm(instance=visit)

    return render(request, 'visitas_granada/edit_visit.html', {'form': form})


class VisitaViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Visita.objects.all()
    serializer_class = VisitaSerializer


class ComentarioViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer


@csrf_exempt
def api_likes(request, visit_id):
    try:
        visit = Visita.objects.get(pk=visit_id)
    except:
        logger.debug('Visita ' + str(id) + ' no encontrada.')
        return HttpResponse(status=404)

    if request.method == 'GET':
        return JsonResponse({'likes': visit.likes})
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        visit.likes = data['likes']
        visit.save()
        return JsonResponse({'likes': visit.likes})
