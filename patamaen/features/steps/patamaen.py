from behave import when, then

from time import sleep


@when('Mitilid ko tamdaw {tilid}')
def Mitilid(context, tilid):
    print(context.tsuki + '/falic')
    sleep(10)
    context.browser.get(context.tsuki + '/falic')
    context.browser.find_element_by_id('id_sasalofen').send_keys('tilid')
    context.browser.find_element_by_name('button').click()


@then("改 to {matamaay}")
def 改(context, matamaay):
    print(context.browser.find_element_by_name('button').text())
    raise NotImplementedError(u'STEP: Then 改 to Ci Panay kako, nga\'ay ho?')
    context.browser.find_element_by_name('button').text()
