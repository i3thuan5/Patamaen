from django.shortcuts import render
import html


def falic(request):
    return render(
        request,
        template_name='patamaen/falic.html',
        context={
            'sentence': "Tomay nga'ay ho,komaen kiso haw?",
            'matamaay': [
                ('span', 'cakatama', 'N'),
                ('span', '', "ga'ay ho"),
                ('del', 'caaykatama', html.escape(' ')),
                ('span', '', ','),
                ('span', 'cakatama', html.escape(' ')),
                ('span', '', 'komaen kiso haw?'),
            ]
        },
    )
