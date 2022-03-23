from behave import when, then

from time import sleep


@when('Mitilid ko tamdaw {tilid}')
def Mitilid(context, tilid):
    context.browser.get(context.tsuki + '/falic')
    context.browser.find_element_by_id('id_sasalofen').send_keys(tilid)
    context.browser.find_element_by_tag_name('button').click()


@then("改 to {matamaay}")
def 改(context, matamaay):
    context.test.assertEqual(
        context.browser.find_element_by_id('masalofay').text(),
        matamaay
    )
