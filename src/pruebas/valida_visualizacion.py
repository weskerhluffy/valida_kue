'''
Created on 04/10/2016

@author: ernesto
'''
from selenium import webdriver
import requests
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import os

if __name__ == '__main__':
    #  XXX: https://stackoverflow.com/questions/40186299/selenium-opens-browser-but-doesnt-load-page
    #  XXX: https://stackoverflow.com/questions/6682009/selenium-firefoxprofile-exception-cant-load-the-profile
    #  XXX: https://stackoverflow.com/questions/20289598/python-selenium-import-my-regular-firefox-profile-add-ons
    # XXX: https://stackoverflow.com/questions/37247336/selenium-use-of-firefox-profile
    binary = FirefoxBinary(r'/Applications/Firefox.app/Contents/MacOS/firefox-bin')
#    gecko = os.path.normpath(os.path.join(os.path.dirname(__file__), 'geckodriver'))
    gecko = "/Users/ernesto/workspace_weba/valida_kue/src/pruebas/geckodriver"
    print("geco esta {}".format(gecko))
    profile = FirefoxProfile("/Users/ernesto/Library/Application Support/Firefox/Profiles/mff1vbld.cagada")
    driver = webdriver.Firefox(firefox_profile=profile, firefox_binary=binary, executable_path=gecko)
    driver.get("http://aptitude.kueski.com/")
    print("pagina abierta")
    # TODO: Validar que haya registros, y si no, dar al menos 1 de alta.
    primer_td = driver.find_element_by_xpath("//tbody/tr[2]/td[1]")
    id_a_borrar = int(primer_td.text)
    print("id a borrar %u" % id_a_borrar)
    
    # TODO: Disparar el borrado desde el link de la pagina.
    r = requests.get("http://aptitude.kueski.com/delete_entry?id=%u" % id_a_borrar)
    print("al borrar el status %u" % int(r.status_code))
    
    # TODO: Guardar el contenido de la pagina de error.
    assert int(r.status_code) == 200, "Al intentar borrar el registro %u se produjo un error." % (id_a_borrar)
    
    
    r = requests.get("http://aptitude.kueski.com/detail?id=%u" % id_a_borrar)
    print("al consultar el borrado el status %u" % int(r.status_code))
    
    assert int(r.status_code) == 200, "Se borro el registro %u y la aplicacion debe manejar peticiones para registros no existentes." % (id_a_borrar)
    

    
    
