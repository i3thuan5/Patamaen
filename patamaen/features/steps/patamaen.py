from behave import when, then


@when('Mitilid ko tamdaw {tilid}')
def Mitilid(context, tilid):
    context.browser.get(context.test.live_server_url + '/falic')
    context.browser.find_element_by_id('id_sasalofen').send_keys(tilid)
    context.browser.find_element_by_tag_name('button').click()


@then("改 to {matamaay}")
def 改(context, matamaay):
    context.test.assertEqual(
        context.browser.find_element_by_id('masalofay').text,
        matamaay
    )
