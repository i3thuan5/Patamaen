from django.shortcuts import render
import html


def falic(request):
    sasalofen = "nga'ay ho ,komaen kiso haw?"
    nisalofan = "Nga'ay ho, komaen kiso haw?"
    import diff_match_patch as dmp_module

    dmp = dmp_module.diff_match_patch()
    diff = dmp.diff_main("Hello World.", "Goodbye World.")
    print(diff)
    return render(
        request,
        template_name='patamaen/falic.html',
        context={
            'sasalofen': sasalofen,
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
