## license WTFPL
## https://en.wikipedia.org/wiki/WTFPL

from bs4 import BeautifulSoup

URL = "http://www.education.gouv.fr/pid24302/annuaire-resultat-recherche.html?lycee_name="
html = BeautifulSoup(URL,'lxml')
