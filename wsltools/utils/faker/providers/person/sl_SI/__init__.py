# coding=utf-8
from __future__ import unicode_literals

from .. import Provider as PersonProvider


class Provider(PersonProvider):
    formats = ['{{first_name}} {{last_name}}']

    first_names_male = [
        "Franc", "Janez", "Anton", "Ivan", "Jožef", "Andrej", "Marko",
        "Marjan", "Peter", "Milan", "Stanislav", "Matej", "Tomaž", "Branko",
        "Bojan", "Robert", "Boštjan", "Matjaž", "Gregor", "Luka", "Martin",
        "Rok", "Boris", "Dušan", "Igor", "Miha", "Dejan", "David", "Uroš",
        "Simon", "Jure", "Blaž", "Štefan", "Jan", "Drago", "Darko", "Klemen",
        "Nejc", "Žiga", "Jernej", "Miran", "Aleksander", "Roman", "Vladimir",
        "Matic", "Tadej", "Srečko", "Slavko", "Mirko", "Janko", "Žan",
        "Miroslav", "Borut", "Alojzij", "Damjan", "Stanko", "Aljaž", "Anže",
        "Danijel", "Mihael", "Matija", "Jaka", "Marijan", "Rudolf", "Alen",
        "Jakob", "Viktor", "Domen", "Sašo", "Iztok", "Goran", "Tilen",
        "Pavel", "Zvonko", "Edvard", "Zdravko", "Danilo", "Matevž", "Rajko",
        "Ludvik", "Zlatko", "Frančišek", "Bogdan", "Gorazd", "Samo", "Leon",
        "Dragan", "Emil", "Josip", "Nik", "Ciril", "Sandi", "Benjamin", "Vid",
        "Albin", "Franci", "Sebastjan", "Silvo", "Leopold", "Kristjan", "Tim",
        "Filip", "Damijan", "Erik", "Viljem", "Vincenc", "Željko", "Damir",
        "Aljoša", "Karel", "Daniel", "Dominik", "Miloš", "Stojan",
        "Franjo", "Valentin", "Davorin", "Maks", "Timotej", "Ladislav", "Niko",
        "Mark", "Nikola", "Bogomir", "Saša", "Vlado", "Karl", "Zdenko",
        "Grega", "Stjepan", "Davor", "Kristijan", "Ernest", "Maksimiljan",
        "Avgust", "Sebastijan", "Aleksandar", "Lovro", "Ivo", "Rado", "Tine",
        "Adolf", "Gal", "Valter", "Elvis", "Jasmin", "Ervin", "Jani", "Izidor",
        "Nenad", "Anej", "Petar", "Maj", "Metod", "Albert", "Bruno", "Radovan",
        "Nikolaj", "Feliks", "Karol", "Bernard", "Joško", "Rafael", "Edin",
        "Aleks", "Cvetko", "Rudi", "Miro", "Hasan", "Slobodan", "Mirsad",
    ]

    first_names_female = [
        "Marija", "Ana", "Irena", "Maja", "Mojca", "Jožefa", "Mateja",
        "Nataša", "Jožica", "Barbara", "Ivana", "Andreja", "Nina", "Petra",
        "Katja", "Sonja", "Milena", "Katarina", "Tatjana", "Anja", "Alenka",
        "Tanja", "Martina", "Vesna", "Tina", "Angela", "Urška", "Antonija",
        "Anica", "Kristina", "Dragica", "Nada", "Olga", "Špela", "Darja",
        "Marjeta", "Tjaša", "Eva", "Ljudmila", "Simona", "Vida", "Sara",
        "Zdenka", "Alojzija", "Lidija", "Suzana", "Marta", "Nika", "Sabina",
        "Silva", "Veronika", "Štefanija", "Stanislava", "Darinka", "Karmen",
        "Neža", "Brigita", "Anita", "Aleksandra", "Pavla", "Cvetka", "Metka",
        "Nevenka", "Monika", "Rozalija", "Natalija", "Slavica", "Marjana",
        "Branka", "Jasmina", "Vera", "Ema", "Saša", "Maša", "Lara", "Lucija",
        "Tamara", "Bernarda", "Danijela", "Klavdija", "Erika", "Romana",
        "Mira", "Jasna", "Klara", "Kaja", "Jelka", "Polona", "Julijana",
        "Valerija", "Sandra", "Matilda", "Tadeja", "Valentina", "Mihaela",
        "Amalija", "Albina", "Breda", "Karolina", "Sanja", "Teja", "Ines",
        "Zofija", "Ksenija", "Laura", "Cecilija", "Patricija", "Magdalena",
        "Manca", "Viktorija", "Maruša", "Vanja", "Vlasta", "Justina", "Nuša",
        "Emilija", "Melita", "Ljubica", "Lana", "Marica", "Gordana", "Marinka",
        "Polonca", "Nadja", "Milka", "Živa", "Urša", "Damjana", "Hana",
        "Tea", "Marijana", "Julija", "Ajda", "Nastja", "Milica", "Alja",
        "Štefka", "Slavka", "Jerneja", "Nives", "Dušanka", "Andrejka",
        "Irma", "Pia", "Jelena", "Marjanca", "Miroslava", "Lilijana", "Stanka",
        "Mirjam", "Neja", "Jolanda", "Zora", "Zvonka", "Hermina", "Rebeka",
        "Hedvika", "Blanka", "Larisa", "Erna", "Anka", "Roza", "Liljana",
        "Magda", "Daniela", "Jerica", "Taja", "Iris", "Adrijana", "Jadranka",
    ]

    first_names = first_names_female + first_names_male
    last_names = [
        "Novak", "Horvat", "Krajnc", "Kovačič", "Zupančič", "Kovač",
        "Potočnik", "Mlakar", "Vidmar", "Kos", "Golob", "Turk", "Božič",
        "Zupan", "Korošec", "Bizjak", "Hribar", "Kotnik", "Rozman",
        "Petek", "petek", "Kastelic", "Kolar", "Hočevar", "Žagar", "žagar",
        "Košir", "Koren", "Klemenčič", "Zajc", "Medved", "Knez", "Zupanc",
        "Pirc", "Hrovat", "Pavlič", "Kuhar", "kuhar", "Lah", "Zorko",
        "Sever", "Majcen", "Jerman", "Babič", "Tomažič", "Erjavec", "Jereb",
        "Kranjc", "Rupnik", "Perko", "Lesjak", "Breznik", "Pečnik", "Pavlin",
        "Dolenc", "Vidic", "Furlan", "Logar", "Tomšič", "Jenko", "Janežič",
        "ribič", "Žnidaršič", "Černe", "Maček", "Lešnik", "Fras",
        "Marolt", "Jelen", "Gregorič", "Blatnik", "Pintar", "Mihelič",
        "Kokalj", "Bezjak", "Leban", "Cerar", "Čeh", "čeh", "Jug",
        "Vidovič", "Rus", "Kobal", "Primožič", "Kocjančič", "Dolinar",
        "Lazar", "Kolenc", "Nemec", "Kolarič", "Lavrič", "Kodrič", "Kosi",
        "Mrak", "Debeljak", "Tavčar", "Žižek", "Krivec", "Zver",
        "Likar", "Žibert", "Jarc", "Vodopivec", "Kramberger", "Miklavčič",
        "Skok", "Toplak", "Petrovič", "Hribernik", "Leskovar", "Stopar",
        "Simonič", "Blažič", "Eržen", "Sitar", "Gorenc", "Železnik",
        "Šinkovec", "Jamnik", "Javornik", "Bukovec", "Hozjan", "Ramšak",
        "Filipič", "Kočevar", "Demšar", "Volk", "volk", "Gomboc",
        "Čuk", "Ilić", "Kokol", "Bregar", "Sušnik", "Pintarič", "Gorjup",
        "Jovanović", "Mavrič", "Kramar", "Lebar", "Rutar", "Koželj",
        "Popović", "Rajh", "Hodžić", "Rožman", "Resnik", "Šmid", "Kumer",
        "Godec", "Bergant", "Pogačnik", "Zemljič", "Hafner", "Tratnik",
        "Rožič", "Cvetko", "Ambrožič", "Bevc", "Mlinarič", "Mlinar",
        "Jerič", "Kalan", "Markovič", "Šuštar", "Bajc", "Kaučič",
        "Dolinšek", "Zalokar", "Pirnat", "Zorman", "Zakrajšek", "Štrukelj",
    ]
