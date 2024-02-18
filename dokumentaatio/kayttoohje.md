# Käyttöohje

### PostgreSQL

Asenna PostgreSQL koneellesi. Ohjeet tietokannan asentamiseen löytyvät [PostgreSQL:n sivulta.](https://www.postgresql.org/download/)
Itselläni käytössä on fuksiläppäri ja käytin asennukseen skriptiä ja ohjeita, jotka löytyvät [täältä.](https://github.com/hy-tsoha/local-pg)

### Opetussovellus

**Kloonaa repositorio ja siirry src-kansioon. Luo kansioon .env -tiedosto. Tiedoston sisällön tulee olla seuraavanlainen:**

SECRET_KEY=(salainen avain)

DATABASE_URL=(tietokannan paikallinen osoite)


**Kun .env -tiedosto on luotu, pysy edelleen src-kansiossa ja syötä seuraavat komennot:**


`python3 -m venv venv`

`source venv/bin/activate`

`pip install -r ../requirements.txt`


**Suorita schema.sql komennolla:**


`psql < schema.sql`


**Käynnistä sovellus komennolla:**


`flask run`

