from django.shortcuts import render
import html


def falic(request):
    return render(
        request,
        template_name='patamaen/falic.html',
        context={
            'sasalofen': "Tomay nga'ay ho,komaen kiso haw?",
            'nisalofan': [
                ('span', 'cakatama', 'N'),
                ('span', '', "ga'ay ho"),
                ('del', 'caaykatama', html.escape(' ')),
                ('span', '', ','),
                ('span', 'cakatama', html.escape(' ')),
                ('span', '', 'komaen kiso haw?'),
            ]
        },
    )
