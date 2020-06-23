import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','mi_sitio_web.settings')

import django
django.setup()

from visitas_granada.models import Visita, Comentario

if __name__ == "__main__":

    Visita.objects.all().delete()
    Comentario.objects.all().delete()

    visit_list = []
    comment_list = []

    # Añadiendo vist
    visit_list.append(Visita(nombre="Patio de los leones",
                            descripción="Visita al patio de los leones",
                            likes=12,
                            foto='patio_leones.jpeg'))

    visit_list.append(Visita(nombre="Generalife",
                            descripción="Paseo por el Generalife",
                            likes = 15,
                            foto='alhambra.jpg'))

    visit_list.append(Visita(nombre="Alcazaba",
                            descripción="Visita a la alcazaba",
                            likes = 8,
                            foto='alcazaba.jpg'))

    visit_list.append(Visita(nombre="Palacio de Comares",
                            descripción="Entrada gratuita al Palacio de Comares",
                            likes = 11,
                            foto='alhambra.jpg'))

    visit_list.append(Visita(nombre="Torre de la Vela",
                            descripción="Descuento para subir a la Torre de la Vela",
                            likes = 7,
                            foto='alhambra.jpg'))

    for visit in visit_list:
        visit.save()

    # Añadiendo comentarios
    comment_list.append(Comentario(visita=visit_list[0], texto='Increíble visita, la recomiendo sin duda.'))
    comment_list.append(Comentario(visita=visit_list[4], texto='La experiencia estuvo bien, pero algo cara.'))

    for comment in comment_list:
        comment.save()

    visit_more_than_10_likes = Visita.objects.raw('SELECT * FROM visitas_granada_visita WHERE likes > 10')

    for visit in visit_more_than_10_likes:
        print('Id: ' + str(visit.id))
        print('Nombre: ' + visit.nombre)
        print('Descripción: ' + visit.descripción)
        print('Likes: ' + str(visit.likes) + '\n')

    comentarios = Comentario.objects.all()

    for c in comentarios:
        print(c.texto)

    # print(Visita.objects.all())
