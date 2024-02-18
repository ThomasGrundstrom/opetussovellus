# opetussovellus

Helsingin Yliopiston Tietokannat ja web-ohjelmointi -kurssia varten kehitetty sovellus, jonka avulla 
opettajat voivat luoda yksinkertaisia tenttejä tukeakseen opiskelijoiden oppimista. Tarkempi kuvaus löytyy [määrittelydokumentista](https://github.com/ThomasGrundstrom/opetussovellus/blob/main/dokumentaatio/maarittelydokumentti.md)


## Dokumentaatio

- [Määrittelydokumentti](https://github.com/ThomasGrundstrom/opetussovellus/blob/main/dokumentaatio/maarittelydokumentti.md)
- [Käyttöohje](https://github.com/ThomasGrundstrom/opetussovellus/blob/main/dokumentaatio/kayttoohje.md)


## Sovelluksen nykyinen tilanne

Sovellukseen voi rekisteröidä käyttäjän ja kirjautua sisään olemassaolevalla käyttäjätunnuksella ja salasanalla. 
Rekisteröitymisen yhteydessä voi valita olevansa opettaja. Jos käyttäjä ei ole opettaja, hän näkee kirjautumisen jälkeen etusivulla 
kaikki tietokannassa olevat tentit ja pääsee suorittamaan tenttejä klikkaamalla "Go to exam"-tekstiä. Kun tentissä vastaa kysymykseen, 
tulee näkyviin sivu, jolla voi verrata omaa vastausta mallivastaukseen. Tentin saa suoritettua vastaamalla kaikkiin kysymyksiin. 
Opettajat voivat kaiken edellä mainitun lisäksi luoda uusia tenttejä. Toistaiseksi tenttiin voi lisätä vain kysymyksiä, joihin vastataan kirjoittamalla tekstiä vastauslaatikkoon.
