from django.shortcuts import render
import diff_match_patch as dmp_module


def falic(request):
    sasalofen = "nga'ay ho ,komaen kiso haw?"
    nisalofan = "Nga'ay ho, komaen kiso haw?"

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
            'sasalofen': sasalofen,
            'nisalofan': nisalofan,
        },
    )
