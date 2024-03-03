# Opetussovellus

Helsingin Yliopiston Tietokannat ja web-ohjelmointi -kurssia varten kehitetty sovellus, jonka avulla 
opettajat voivat luoda yksinkertaisia tenttejä tukeakseen opiskelijoiden oppimista.


## Dokumentaatio

- [Määrittelydokumentti](https://github.com/ThomasGrundstrom/opetussovellus/blob/main/dokumentaatio/maarittelydokumentti.md)
- [Käyttöohje](https://github.com/ThomasGrundstrom/opetussovellus/blob/main/dokumentaatio/kayttoohje.md)


## Sovelluksen nykyinen tilanne

- Sovellukseen voi rekisteröidä käyttäjän ja kirjautua sisään olemassaolevalla käyttäjätunnuksella ja salasanalla. 
- Rekisteröitymisen yhteydessä voi valita olevansa opettaja.

#### Jos rekisteröidyt normaaliksi käyttäjäksi: 

- Näet etusivulla kaikki opettajien luomat tentit ja pääset suorittamaan niitä klikkaamalla "Go to exam"-tekstiä.
- Kysymyksiin vastataan kirjoittamalla tekstiä vastauskenttään.
- Vastattuasi kysymykseen, näkyviin tulee sivu, jolla voit verrata antamaasi vastausta opettajan määrittelemään mallivastaukseen.
- Saat suoritettua tentin vastaamalla kaikkiin kysymyksiin. 
- Kun tentti on suoritettu, näet tenttisivulta kaikki kysymykset, antamasi vastaukset ja mallivastaukset.
- Voit poistaa antamasi vastaukset tietokannasta ja aloittaa tentin suorittamisen alusta painamalla "Retake exam"-painiketta.

#### Jos hankit rekisteröitymisen yhteydessä opettajan oikeudet:

- Voit käyttää samoja toiminnallisuuksia kuin normaalitkin käyttäjät.
- Voit luoda tenttejä etusivulla klikkaamalla "New exam"-tekstiä.
- Tenttiin voi lisätä kysymys-mallivastaus-pareja.
- Voit poistaa etusivulta itse luomiasi tenttejä klikkaamalla "Delete exam"-painiketta.
- Näet tenttisivulta (sivu, joka tulee näkyviin klikattuasi etusivulla "Go to exam"-tekstiä) tentin suorittajien määrän ja käyttäjänimet.
