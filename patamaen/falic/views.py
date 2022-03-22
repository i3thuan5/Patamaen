from django.shortcuts import render
import diff_match_patch as dmp_module
import re
from falic.forms import MatamaForm


def falic(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = MatamaForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            sasalofen = form.cleaned_data['sasalofen']

    # if a GET (or any other method) we'll create a blank form
    else:
        form = MatamaForm()
        sasalofen = "nga'ay ho ,o maan ko sakalafi no miso?"

    # 字首大寫
    # "Nga'ay ho, komaen kiso haw?"
    nisalofan = sasalofen[0].upper() + sasalofen[1:]
    nisalofan = nisalofan.replace(' ,', ',')

    # nisalofan = nisalofan.replace(',k', ', k')
    nisalofan = re.sub('(,)([a-zA-Z])', pahanhanan, nisalofan)

    dmp = dmp_module.diff_match_patch()
    diff = dmp.diff_main(sasalofen, nisalofan)

    # diff = [
    #     (-1, 'n'),
    #     (1, 'N'),
    #     (0, "ga'ay ho"),
    #     (-1, ' '),
    #     (0, ','),
    #     (1, ' '),
    #     (0, 'komaen kiso haw?')
    # ]
    # [
    #     ('span', 'cakatama', 'N'),
    #     ('span', '', "ga'ay ho"),
    #     ('del', 'caaykatama', html.escape(' ')),
    #     ('span', '', ','),
    #     ('span', 'cakatama', html.escape(' ')),
    #     ('span', '', 'komaen kiso haw?'),
    # ]
    nisalofan = []
    for codad in diff:
        if codad[0] == -1:
            # nisalofan.append(
            #     ('span', 'cakatama', codad[1])
            # )
            pass
        elif codad[0] == 0:
            nisalofan.append(
                ('span', '', codad[1])
            )
        elif codad[0] == 1:
            nisalofan.append(
                ('span', 'cakatama', codad[1])
            )

    return render(
        request,
        template_name='patamaen/falic.html',
        context={
            'form': form,
            'nisalofan': nisalofan,
        },
    )


def pahanhanan(matama):
    return matama.group(1) + ' ' + matama.group(2)
