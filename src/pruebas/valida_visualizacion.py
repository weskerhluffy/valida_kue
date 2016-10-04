'''
Created on 04/10/2016

@author: ernesto
'''
from selenium import webdriver
import requests

if __name__ == '__main__':
    driver = webdriver.Firefox()
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
    

    
    
