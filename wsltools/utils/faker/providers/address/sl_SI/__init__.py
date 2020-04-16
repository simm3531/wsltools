# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

from .. import Provider as AddressProvider


class Provider(AddressProvider):

    city_formats = ('{{city_name}}', )

    street_name_formats = ('{{street_name}}', )
    street_address_formats = ('{{street_name}} {{building_number}}', )
    address_formats = ('{{street_address}}\n{{postcode}} {{city}}', )

    building_number_formats = ('###', '##', '#', '#a', '#b', '#c')

    postcode_formats = ('####', )

    cities = (
        "Ajdovščina", "Bled", "Bovec", "Brežice", "Celje", "Cerknica",
        "Črnomelj", "Domžale", "Dravograd", "Gornja Radgona", "Gornji Grad",
        "Grosuplje", "Hrastnik", "Idrija", "Ilirska Bistrica", "Izola",
        "Jesenice", "Kamnik", "Kobarid", "Kočevje", "Koper",
        "Kostanjevica na Krki", "Kranj", "Krško", "Laško",
        "Lenart v Slovenskih goricah", "Lendava", "Litija", "Ljubljana",
        "Ljutomer", "Logatec", "Maribor", "Medvode", "Mengeš", "Metlika",
        "Mežica", "Murska Sobota", "Nova Gorica", "Novo mesto", "Ormož",
        "Piran", "Postojna", "Prevalje", "Ptuj", "Radeče", "Radovljica",
        "Ravne na Koroškem", "Ribnica", "Rogaška Slatina",
        "Ruše", "Sevnica", "Sežana", "Slovenj Gradec", "Slovenska Bistrica",
        "Slovenske Konjice", "Šempeter pri Gorici", "Šentjur", "Škofja Loka",
        "Šoštanj", "Tolmin", "Trbovlje", "Trebnje", "Tržič", "Turnišče",
        "Velenje", "Vipava", "Vipavski Križ", "Višnja Gora", "Vrhnika",
        "Zagorje ob Savi", "Žalec", "Železniki", "Žiri",
    )

    streets = (
        "Abramova ulica", "Adamičeva ulica", "Adamič-Lundrovo nabrežje",
        "Ajdovščina", "Aleševa ulica", "Alešovčeva ulica",
        "Aljaževa ulica", "Ambrožev trg", "Ameriška ulica",
        "Andrićeva ulica", "Anžurjeva ulica", "Apihova ulica",
        "Argentinska ulica", "Arharjeva cesta", "Arkova ulica",
        "Artačeva ulica", "Aškerčeva cesta", "Avčinova ulica",
        "Avsečeva ulica", "Avstrijska ulica", "Avšičeva cesta",
        "Ažmanova ulica", "Babičeva ulica", "Badjurova ulica",
        "Balinarska pot", "Baragova ulica", "Barjanska cesta",
        "Bavdkova ulica", "Baznikova ulica", "Bazoviška ulica",
        "Beethovnova ulica", "Belačeva ulica", "Beljaška ulica",
        "Berčičeva ulica", "Berčonova pot", "Berdajsova ulica",
        "Bernekerjeva ulica", "Bernikova ulica", "Betettova cesta",
        "Bezenškova ulica", "Bežigrad", "Bičevje", "Bilečanska ulica",
        "Bitenčeva ulica", "Bizjakova ulica", "Bizjanova ulica",
        "Bizovški štradon", "Blasnikova ulica", "Blasov breg",
        "Bleiweisova cesta", "Bobenčkova ulica", "Bobrova ulica",
        "Bognarjeva pot", "Bohinjčeva ulica", "Bohoričeva ulica",
        "Boletova ulica", "Bolgarska ulica", "Borovniška ulica",
        "Borštnikov trg", "Borutova ulica", "Božičeva ulica",
        "Brankova ulica", "Bratinova ulica", "Bratislavska cesta",
        "Bratov Jakopičev ulica", "Bratov Kunovarjev ulica",
        "Bravničarjeva ulica", "Brdnikova ulica", "Breg", "Bregarjeva ulica",
        "Breznikova ulica", "Brglezov štradon", "Brilejeva ulica",
        "Brodarjev trg", "Brodska cesta", "Burnikova ulica", "Cankarjev vrh",
        "Cankarjevo nabrežje", "Carja Dušana ulica", "Celarčeva ulica",
        "Celjska ulica", "Celovška cesta", "Cerkniška ulica",
        "Cerutova ulica", "Cesta Andreja Bitenca", "Cesta Ceneta Štuparja",
        "Cesta Dolomitskega odreda", "Cesta II. grupe odredov",
        "Cesta Ljubljanske brigade", "Cesta na Bellevue", "Cesta na Bokalce",
        "Cesta na Brinovec", "Cesta na Brod", "Cesta na Ježah",
        "Cesta na Kope", "Cesta na Laze", "Cesta na Loko", "Cesta na Mesarico",
        "Cesta na Ozare", "Cesta na Poljane", "Cesta na Prevoje",
        "Cesta na Urh", "Cesta na Vrhovce", "Cesta slov. kmečkih uporov",
        "Cesta Urške Zatlerjeve", "Cesta v Dvor", "Cesta v Gameljne",
        "Cesta v Hrastje", "Cesta v hrib", "Cesta v Kleče", "Cesta v Kostanj",
        "Cesta v Legarico", "Cesta v Mestni log", "Cesta v Pečale",
        "Cesta v Prod", "Cesta v Rožno dolino", "Cesta v Šmartno",
        "Cesta v Zeleni log", "Cesta v Zgornji log", "Cesta vstaje",
        "Cesta 24. junija", "Cesta 25 talcev", "Cesta 27. aprila",
        "Chengdujska cesta", "Chopinov prehod", "Cigaletova ulica",
        "Cilenškova ulica", "Cimermanova ulica", "Cimpermanova ulica",
        "Cizejeva ulica", "Clevelandska ulica", "Colnarjeva ulica",
        "Cvetlična pot", "Čampova ulica", "Čanžekova ulica",
        "Čargova ulica", "Čebelarska ulica", "Čehova ulica",
        "Čepelnikova ulica", "Čepovanska ulica", "Čerinova ulica",
        "Černigojeva ulica", "Černivčeva ulica", "Červanova ulica",
        "Čevljarska ulica", "Čižmanova ulica", "Čopova ulica", "Črna pot",
        "Črnuška cesta", "Črtomirova ulica", "Čučkova ulica",
        "Dajnkova ulica", "Dalmatinova ulica", "Danile Kumarjeve ulica",
        "Dečkova ulica", "Dečmanova ulica", "Delakova ulica",
        "Demšarjeva cesta", "Derčeva ulica", "Dergančeva ulica",
        "Dermotova ulica", "Detelova ulica", "Devinska ulica", "Devova ulica",
        "Divjakova ulica", "Do proge", "Dobrajčeva ulica", "Dobrdobska ulica",
        "Dolenjska cesta", "Dolgi breg", "Dolgi most", "Dolharjeva ulica",
        "Dolinarjeva ulica", "Dolinškova ulica", "Dolničarjeva ulica",
        "Dolomitska ulica", "Drabosnjakova ulica", "Draga", "Draveljska ulica",
        "Dražgoška ulica", "Drenikov vrh", "Drenikova ulica",
        "Dunajska cesta", "Dvojna ulica", "Dvorakova ulica", "Dvorni trg",
        "Eipprova ulica", "Ellerjeva ulica", "Emonska cesta",
        "Erbežnikova ulica", "Erjavčeva cesta", "Fabianijeva ulica",
        "Fani Grumove ulica", "Ferberjeva ulica", "Filipičeva ulica",
        "Flajšmanova ulica", "Flandrova ulica", "Forsterjeva ulica",
        "Franketova ulica", "Frankopanska ulica", "Frenkova pot",
        "Friškovec", "Funtkova ulica", "Fužinska cesta", "Gabrov trg",
        "Gača", "Galičeva ulica", "Galjevica", "Gallusovo nabrežje",
        "Gasilska cesta", "Gasparijeva ulica", "Gašperšičeva ulica",
        "Gerbičeva ulica", "Gestrinova ulica", "Glavarjeva ulica",
        "Gledališka stolba", "Glinška ulica", "Glinškova ploščad",
        "Glonarjeva ulica", "Gmajnice", "Gobarska pot", "Godeževa ulica",
        "Gola Loka", "Golarjeva ulica", "Goljarjeva pot", "Golouhova ulica",
        "Goriška ulica", "Gorjančeva ulica", "Gorjupova ulica",
        "Gornji Rudnik I", "Gornji Rudnik II", "Gornji Rudnik III",
        "Gornji trg", "Goropečnikova ulica", "Gortanova ulica",
        "Gospodinjska ulica", "Gosposka ulica", "Gosposvetska cesta",
        "Govekarjeva ulica", "Gozdna pot", "Grablovičeva ulica",
        "Gradišče", "Gradnikova ulica", "Grafenauerjeva ulica",
        "Grajski drevored", "Grajzerjeva ulica", "Gramozna pot",
        "Grassellijeva ulica", "Gregorčičeva ulica", "Gregorinova ulica",
        "Grintovška ulica", "Grobeljca", "Grobeljska pot", "Groharjeva cesta",
        "Groznikova ulica", "Grška ulica", "Grško", "Gruberjevo nabrežje",
        "Grudnovo nabrežje", "Gubčeva ulica", "Gunceljska cesta",
        "Gustinčarjeva ulica", "Gustinčičeva ulica", "Hacetova ulica",
        "Hafnerjeva ulica", "Hajdrihova ulica", "Hauptmanca",
        "Hladilniška pot", "Hladnikova cesta", "Hlebčeva ulica",
        "Hotimirova ulica", "Hradeckega cesta", "Hranilniška ulica",
        "Hribarjevo nabrežje", "Hribernikova ulica", "Hribovska pot",
        "Hrvaška ulica", "Hrvatski trg", "Hubadova ulica", "Hudourniška pot",
        "Idrijska ulica", "Igriška ulica", "Ilešičeva ulica",
        "Ilovški štradon", "Industrijska cesta", "Ingličeva ulica",
        "Italijanska ulica", "Izletniška ulica", "Ižanska cesta",
        "Jakčeva ulica", "Jakhljeva ulica", "Jakopičev drevored",
        "Jakopičevo sprehajališče", "Jakšičeva ulica", "Jalnova ulica",
        "Jamova cesta", "Janežičeva cesta", "Janova ulica", "Janševa ulica",
        "Jarčeva ulica", "Jarnikova ulica", "Jarše", "Jarška cesta",
        "Javorškova ulica", "Jazbečeva pot", "Jelinčičeva ulica",
        "Jenkova ulica", "Jensenova ulica", "Jerajeva ulica",
        "Jeranova ulica", "Jesenkova ulica", "Jesihov štradon",
        "Jezerska ulica", "Ježa", "Ježica", "Joškov štradon",
        "Jurčičev trg", "Jurčkova cesta", "Juričeva ulica",
        "Juvanova ulica", "K reaktorju", "Kadilnikova ulica",
        "Kajuhova ulica", "Kalingerjeva ulica", "Kalinova ulica",
        "Kaminova ulica", "Kamniška ulica", "Kamnogoriška cesta",
        "Kančeva ulica", "Kanonijeva cesta", "Kantetova ulica",
        "Kapusova ulica", "Kardeljeva ploščad", "Karingerjeva ulica",
        "Karunova ulica", "Kastelčeva ulica", "Kašeljska cesta",
        "Kavadarska cesta", "Kavčičeva ulica", "Kavškova ulica",
        "Kekčeva ulica", "Kermaunerjeva ulica", "Kernova cesta",
        "Kerševanova ulica", "Keržičeva ulica", "Kettejeva ulica",
        "Kladezna ulica", "Klančarjeva ulica", "Kleče",
        "Klemenova ulica", "Kleparska steza", "Ključavničarska ulica",
        "Klunova ulica", "Kmečka pot", "Knafljev prehod",
        "Knezov štradon", "Knezova ulica", "Knobleharjeva ulica",
        "Koblarjeva ulica", "Kocbekova ulica", "Kocenova ulica",
        "Kocjanova ulica", "Kočenska ulica", "Kodrova ulica",
        "Kogojeva ulica", "Kogovškova ulica", "Kokaljeva ulica",
        "Kolarjeva ulica", "Kolesarska pot", "Koleševa ulica",
        "Kolinska ulica", "Kolmanova ulica", "Kolodvorska ulica",
        "Komanova ulica", "Komenskega ulica", "Kongresni trg",
        "Kopališka ulica", "Kopitarjeva ulica", "Kopna pot", "Koprska ulica",
        "Koreninova ulica", "Koroška ulica", "Korotanska ulica",
        "Kosančeva ulica", "Koseskega ulica", "Koseška cesta",
        "Kosmačeva ulica", "Kosova ulica", "Kosovelova ulica",
        "Koširjeva ulica", "Kotnikova ulica", "Kovačeva ulica",
        "Kovaška ulica", "Kovinarska ulica", "Kozakova ulica",
        "Kozinova ulica", "Kozlarjeva pot", "Koželjeva ulica",
        "Krakovski nasip", "Kraljeva ulica", "Kranerjeva ulica",
        "Kraška ulica", "Kratka pot", "Kratka steza", "Kregarjeva ulica",
        "Kreljeva ulica", "Kremžarjeva ulica", "Krimska ulica",
        "Krištofova ulica", "Kriva pot", "Krivec", "Križevniška soteska",
        "Križna ulica", "Krmčeva ulica", "Krmeljeva ulica",
        "Kropova ulica", "Krošljeva ulica", "Krovska ulica", "Krožna pot",
        "Kržičeva ulica", "Kudrova ulica", "Kuhljeva cesta",
        "Kumerdejeva ulica", "Kumerjeve ulica", "Kumrovška ulica",
        "Kurilniška ulica", "Kurirska ulica", "Kusoldova ulica",
        "Kuštrinova ulica", "Kuzeletova ulica", "Kuzmičeva ulica",
        "Lahova pot", "Lajovčeva ulica", "Laknerjeva ulica", "Lakotence",
        "Lampetova ulica", "Lamutova ulica", "Langusova ulica", "Latinski trg",
        "Lavrinova ulica", "Layerjeva ulica", "Lazarjeva ulica",
        "Legatova ulica", "Lemeževa ulica", "Lepi pot", "Lepodvorska ulica",
        "Leskovičeva ulica", "Letališka cesta", "Levarjeva ulica",
        "Levičnikova ulica", "Levstikov trg", "Levstikova ulica",
        "Linhartov podhod", "Linhartova cesta", "Lipahova ulica",
        "Litijska cesta", "Litostrojska cesta", "Livada", "Livarska ulica",
        "Ločnikarjeva ulica", "Lončarska steza", "Lorenzova cesta",
        "Lovrenčičeva ulica", "Lovska ulica", "Lovšetova ulica",
        "Lubejeva ulica", "Luize Pesjakove ulica", "Lunačkova ulica",
        "Mačja steza", "Mačkov kot", "Mačkova ulica", "Madžarska ulica",
        "Magistrova ulica", "Maistrova ulica", "Majaronova ulica",
        "Majde Vrhovnikove ulica", "Majorja Lavriča ulica", "Makucova ulica",
        "Mala ulica", "Mala vas", "Malejeva ulica", "Malenškova ulica",
        "Malgajeva ulica", "Mali štradon", "Mali trg", "Malnarjeva ulica",
        "Marčenkova ulica", "Marentičeva ulica", "Mareška pot",
        "Marice Kovačeve ulica", "Marincljeva ulica", "Marinovševa cesta",
        "Maroltova ulica", "Martina Krpana ulica", "Martinčeva ulica",
        "Martinova ulica", "Marušičeva ulica", "Masarykova cesta",
        "Matjanova pot", "Matjaževa ulica", "Maurerjeva ulica",
        "Mazovčeva pot", "Med hmeljniki", "Medarska ulica", "Medenska cesta",
        "Medveščkova ulica", "Mekinčeva ulica", "Melikova ulica",
        "Mencingerjeva ulica", "Merčnikova ulica", "Merosodna ulica",
        "Mesesnelova ulica", "Mestni trg", "Meškova ulica", "Metelkova ulica",
        "Miheličeva cesta", "Mihov štradon", "Miklavčeva ulica",
        "Miklošičeva cesta", "Mikuževa ulica", "Milčetova pot",
        "Mire Lenardičeve ulica", "Mirje", "Mirna pot", "Mislejeva ulica",
        "Mizarska pot", "Mladinska ulica", "Mlake", "Mlinska pot",
        "Močnikova ulica", "Mokrška ulica", "Molekova ulica",
        "Moškričeva ulica", "Mrharjeva ulica", "Mrzelova ulica",
        "Murkova ulica", "Murnikova ulica", "Murnova ulica", "Muzejska ulica",
        "Na cvetači", "Na delih", "Na dolih", "Na gaju", "Na gmajni",
        "Na Herši", "Na jami", "Na klančku", "Na Korošci", "Na Palcah",
        "Na požaru", "Na produ", "Na Rojah", "Na Stolbi", "Na Straški vrh",
        "Na Trati", "Na Žalah", "Nade Ovčakove ulica", "Nadgoriška cesta",
        "Nahlikova ulica", "Nahtigalova ulica", "Nanoška ulica",
        "Nazorjeva ulica", "Nebotičnikov prehod", "Nedohova ulica",
        "Njegoševa cesta", "Nova ulica", "Novakova pot", "Novakova ulica",
        "Novi trg", "Novinarska ulica", "Novo naselje", "Novo Polje, cesta I",
        "Novo Polje, cesta III", "Novo Polje, cesta IV",
        "Novo Polje, cesta V", "Novo Polje, cesta VI", "Novo Polje, cesta VII",
        "Novo Polje, cesta X", "Novo Polje, cesta XI", "Novo Polje, cesta XII",
        "Novo Polje, cesta XIV", "Novo Polje, cesta XIX",
        "Novo Polje, cesta XVI", "Novo Polje, cesta XVII",
        "Novo Polje, cesta XXI", "Novo Polje, cesta XXIII", "Novosadska ulica",
        "Ob daljnovodu", "Ob dolenjski železnici", "Ob Farjevcu",
        "Ob Ljubljanici", "Ob Mejašu", "Ob potoku", "Ob pristanu", "Ob Savi",
        "Ob studencu", "Ob zdravstvenem domu", "Ob zeleni jami", "Ob zelenici",
        "Ob žici", "Obirska ulica", "Obrežna steza", "Obrije",
        "Ocvirkova ulica", "Ogrinčeva ulica", "Okiškega ulica",
        "Omahnova ulica", "Omejčeva ulica", "Omersova ulica",
        "Oražnova ulica", "Orlova ulica", "Osenjakova ulica",
        "Osojna pot", "Osojna steza", "Osterčeva ulica", "Ovčakova ulica",
        "Pahorjeva ulica", "Palmejeva ulica", "Papirniška pot",
        "Park Ajdovščina", "Park Arturo Toscanini",
        "Parmova ulica", "Parmska cesta", "Partizanska ulica",
        "Pavlovčeva ulica", "Pavšičeva ulica", "Pečarjeva ulica",
        "Pečnik", "Pečnikova ulica", "Pegamova ulica", "Perčeva ulica",
        "Periška cesta", "Perkova ulica", "Peršinova cesta",
        "Pesarska cesta", "Pestotnikova ulica", "Peščena pot",
        "Petkova ulica", "Petkovškovo nabrežje", "Petrčeva ulica",
        "Pilonova ulica", "Pionirska pot", "Pipanova pot", "Pirnatova ulica",
        "Planinska cesta", "Planinškova ulica", "Plečnikov podhod",
        "Plemljeva ulica", "Plešičeva ulica", "Pleteršnikova ulica",
        "Pločanska ulica", "Pod akacijami", "Pod bregom", "Pod bresti",
        "Pod bukvami", "Pod Debnim vrhom", "Pod gabri", "Pod gozdom",
        "Pod hrasti", "Pod hribom", "Pod hruško", "Pod jelšami",
        "Pod jezom", "Pod ježami", "Pod Kamno gorico", "Pod klancem",
        "Pod lipami", "Pod topoli", "Pod Trančo", "Pod turnom", "Pod vrbami",
        "Podgornikova ulica", "Podgorska cesta", "Podgrajska cesta",
        "Podjunska ulica", "Podlimbarskega ulica", "Podmilščakova ulica",
        "Podrožniška pot", "Podsmreška cesta", "Podutiška cesta",
        "Pogačarjev trg", "Pohlinova ulica", "Poklukarjeva ulica",
        "Polakova ulica", "Polanškova ulica", "Poljanska cesta",
        "Polje", "Polje, cesta I", "Polje, cesta II", "Polje, cesta III",
        "Polje, cesta VI", "Polje, cesta VIII", "Polje, cesta X",
        "Polje, cesta XIV", "Polje, cesta XL", "Polje, cesta XLII",
        "Polje, cesta XLVI", "Polje, cesta XVI", "Polje, cesta XVIII",
        "Polje, cesta XXII", "Polje, cesta XXIV", "Polje, cesta XXVI",
        "Polje, cesta XXX", "Polje, cesta XXXII", "Polje, cesta XXXIV",
        "Polje, cesta XXXVIII", "Poljedelska ulica", "Poljska pot",
        "Porentova ulica", "Posavskega ulica", "Postojnska ulica",
        "Pot do šole", "Pot Draga Jakopiča", "Pot heroja Trtnika",
        "Pot k igrišču", "Pot k ribniku", "Pot k Savi", "Pot k sejmišču",
        "Pot k studencu", "Pot na Breje", "Pot na Drenikov vrh",
        "Pot na Golovec", "Pot na goro", "Pot na Gradišče", "Pot na Grič",
        "Pot na Labar", "Pot na mah", "Pot na most", "Pot na Orle",
        "Pot na Visoko", "Pot na Zduše", "Pot Rdečega križa",
        "Pot v boršt", "Pot v Čeželj", "Pot v dolino", "Pot v Goričico",
        "Pot v hribec", "Pot v mejah", "Pot v Mlake", "Pot v Podgorje",
        "Pot v Zeleni gaj", "Pot za Brdom", "Pot za razori",
        "Potokarjeva ulica", "Potrčeva ulica", "Povšetova ulica",
        "Prašnikarjeva ulica", "Praznikova ulica", "Pražakova ulica",
        "Pred Savljami", "Predjamska cesta", "Predor pod Gradom",
        "Preglov trg", "Prekmurska ulica", "Prelčeva ulica", "Preloge",
        "Premrlova ulica", "Preradovićeva ulica", "Preserska ulica",
        "Prešernov trg", "Prešernova cesta", "Pretnarjeva ulica",
        "Pri borštu", "Pri brvi", "Pri malem kamnu", "Pri mostiščarjih",
        "Pribinova ulica", "Prijateljeva ulica", "Primorska ulica",
        "Prinčičeva ulica", "Prisojna ulica", "Prištinska ulica", "Privoz",
        "Proletarska cesta", "Prule", "Prušnikova ulica", "Prvomajska ulica",
        "Pšatnik", "Pšatska pot", "Ptujska ulica", "Pučnikova ulica",
        "Puharjeva ulica", "Puhova ulica", "Puhtejeva ulica",
        "Puterlejeva ulica", "Putrihova ulica", "Raičeva ulica",
        "Rakovniška ulica", "Rakuševa ulica", "Ramovševa ulica",
        "Ravbarjeva ulica", "Ravna pot", "Ravnikova ulica",
        "Razgledna steza", "Reber", "Reboljeva ulica", "Rečna ulica",
        "Regentova cesta", "Resljeva cesta", "Reška ulica",
        "Ribičičeva ulica", "Ribji trg", "Ribniška ulica",
        "Rimska cesta", "Rjava cesta", "Robbova ulica", "Robičeva ulica",
        "Rodičeva ulica", "Rojčeva ulica", "Romavhova ulica", "Rosna pot",
        "Rotarjeva ulica", "Rovšnikova ulica", "Rozmanova ulica",
        "Rožanska ulica", "Rožičeva ulica", "Rožna dolina, cesta I",
        "Rožna dolina, cesta III", "Rožna dolina, cesta IV",
        "Rožna dolina, cesta V", "Rožna dolina, cesta VI",
        "Rožna dolina, cesta VIII", "Rožna dolina, cesta X",
        "Rožna dolina, cesta XII", "Rožna dolina, cesta XIII",
        "Rožna dolina, cesta XV", "Rožna dolina, cesta XVII",
        "Rožna ulica", "Rudnik I", "Rudnik II", "Rudnik III", "Runkova ulica",
        "Ruska ulica", "Rutarjeva ulica", "Sadinja vas", "Sajovčeva ulica",
        "Samova ulica", "Saškova ulica", "Sattnerjeva ulica",
        "Savinova ulica", "Savinškova ulica", "Savlje", "Savska cesta",
        "Sedejeva ulica", "Selanov trg", "Selanova ulica",
        "Setnikarjeva ulica", "Seunigova ulica", "Simončičeva ulica",
        "Siva pot", "Skapinova ulica", "Sketova ulica", "Skopčeva ulica",
        "Skrbinškova ulica", "Slape", "Slapnikova ulica", "Slavčja ulica",
        "Slomškova ulica", "Slovenčeva ulica", "Slovenska cesta",
        "Smoletova ulica", "Smrekarjeva ulica", "Smrtnikova ulica",
        "Snebersko nabrežje", "Snežniška ulica", "Snojeva ulica",
        "Sojerjeva ulica", "Sončna pot", "Sostrska cesta", "Soška ulica",
        "Soteška pot", "Soussenska ulica", "Sovretova ulica",
        "Spodnji Rudnik I", "Spodnji Rudnik II", "Spodnji Rudnik III",
        "Spodnji Rudnik V", "Spomeniška pot", "Srebrničeva ulica",
        "Srednja pot", "Stadionska ulica", "Staničeva ulica",
        "Stara Ježica", "Stara slovenska ulica", "Stare Črnuče",
        "Stari trg", "Stegne", "Steletova ulica", "Sternadova ulica",
        "Stiška ulica", "Stolpniška ulica", "Stoženska ulica", "Stožice",
        "Stražarjeva ulica", "Streliška ulica", "Stritarjeva ulica",
        "Strmeckijeva ulica", "Strmi pot", "Strniševa cesta",
        "Strossmayerjeva ulica", "Strugarska ulica", "Strupijevo nabrežje",
        "Suhadolčanova ulica", "Sulčja ulica", "Svetčeva ulica",
        "Šarhova ulica", "Šentjakob", "Šentviška ulica",
        "Šerkova ulica", "Šestova ulica", "Šibeniška ulica",
        "Šinkov štradon", "Šišenska cesta", "Šivičeva ulica",
        "Škerljeva ulica", "Škofova ulica", "Škrabčeva ulica",
        "Šlandrova ulica", "Šlosarjeva ulica", "Šmarna gora",
        "Šmartinska cesta", "Šmartno", "Španova pot", "Španska ulica",
        "Štajerska cesta", "Štebijeva cesta", "Štefančeva ulica",
        "Štembalova ulica", "Štepanjska cesta", "Štepanjsko nabrežje",
        "Štirnova ulica", "Štradon čez Prošco", "Štrekljeva ulica",
        "Študentovska ulica", "Štukljeva cesta", "Štula",
        "Šturmova ulica", "Šubičeva ulica", "Šumarjeva ulica",
        "Švabićeva ulica", "Švarova ulica", "Švegljeva cesta", "Tabor",
        "Tacenska cesta", "Tavčarjeva ulica", "Tbilisijska ulica",
        "Tesarska ulica", "Teslova ulica", "Tesna ulica", "Tesovnikova ulica",
        "Tiha ulica", "Tiranova ulica", "Tischlerjeva ulica",
        "Tivolska cesta", "Tkalska ulica", "Tobačna ulica", "Tolminska ulica",
        "Tomačevo", "Tomačevska cesta", "Tomažičeva ulica",
        "Tometova ulica", "Tominškova ulica", "Tomišeljska ulica",
        "Toplarniška ulica", "Topniška ulica", "Torkarjeva ulica",
        "Tratnikova ulica", "Travniška ulica", "Trbeže", "Trdinova ulica",
        "Trebušakova ulica", "Trg francoske revolucije",
        "Trg mladih", "Trg mladinskih delov. brigad", "Trg narodnih herojev",
        "Trg prekomorskih brigad", "Trg republike", "Trg 9. maja",
        "Trinkova ulica", "Trnovčeva ulica", "Trnovska ulica",
        "Trpinčeva ulica", "Trstenjakova ulica", "Trtnikova ulica",
        "Tržaška cesta", "Tržna ulica", "Tugomerjeva ulica",
        "Turnerjeva ulica", "Turnsko nabrežje", "Udvančeva ulica",
        "Ulica aktivistov", "Ulica Alme Sodnik", "Ulica Andreja Kumarja",
        "Ulica Angelce Ocepkove", "Ulica Angele Ljubičeve",
        "Ulica borca Petra", "Ulica borcev za severno mejo",
        "Ulica bratov Bezlajev", "Ulica bratov Blanč", "Ulica bratov Jančar",
        "Ulica bratov Komel", "Ulica bratov Kraljič", "Ulica bratov Martinec",
        "Ulica bratov Novak", "Ulica bratov Rozmanov", "Ulica bratov Škofov",
        "Ulica bratov Učakar", "Ulica bratov Židan",
        "Ulica Dušana Kraigherja", "Ulica Ernesta Kramerja",
        "Ulica Franca Nebca", "Ulica Francke Jerasove", "Ulica Franja Novaka",
        "Ulica gledališča BTC", "Ulica Goce Delčeva",
        "Ulica Gubčeve brigade", "Ulica Hermana Potočnika",
        "Ulica Ivana Roba", "Ulica Ivanke Kožuh", "Ulica Ivice Pirjevčeve",
        "Ulica Janeza Pavla II.", "Ulica Janeza Rožiča",
        "Ulica Jožeta Jame", "Ulica Jožeta Japlja", "Ulica Jožeta Mirtiča",
        "Ulica Konrada Babnika", "Ulica Koroškega bataljona",
        "Ulica Lizike Jančarjeve", "Ulica Lojzeta Spacala",
        "Ulica Lovre Klemenčiča", "Ulica Malči Beličeve",
        "Ulica Marije Drakslerjeve", "Ulica Marije Hvaličeve",
        "Ulica Marje Boršnikove", "Ulica Marka Šlajmerja",
        "Ulica Milana Majcna", "Ulica Milke Kerinove", "Ulica Minke Bobnar",
        "Ulica Mirka Jurce", "Ulica Mirka Tomšiča", "Ulica Miroslava Turka",
        "Ulica Molniške čete", "Ulica na Grad", "Ulica Nade Čamernikove",
        "Ulica Olge Mohorjeve", "Ulica padlih borcev", "Ulica Pariške komune",
        "Ulica Pohorskega bataljona", "Ulica Polonce Čude",
        "Ulica prvoborcev", "Ulica Rezke Dragarjeve", "Ulica Rezke Klopčič",
        "Ulica Rudolfa Janežiča", "Ulica Staneta Severja",
        "Ulica Štefke Zbašnikove", "Ulica talcev",
        "Ulica Tončke Čečeve", "Ulica v Kokovšek",
        "Ulica Vide Pregarčeve", "Ulica Vladimirja Trampuža",
        "Ulica Zore Ragancinove", "Ulica Žanke Erjavec",
        "Ulica 15. aprila", "Ulica 15. maja", "Ulica 24. avgusta",
        "Ulica 4. julija", "Ulica 7. septembra", "Ulica 9. junija",
        "Uršičev štradon", "Usnjarska ulica", "V Češnjico", "V dolini",
        "V Karlovce", "V Karlovce", "V Kladeh", "V Murglah", "V Sige",
        "V Varde", "V Zalar", "Vagajeva ulica", "Valjavčeva ulica",
        "Valvasorjeva ulica", "Vandotova ulica", "Vaška pot",
        "Večna pot", "Vegova ulica", "Velebitska ulica",
        "Veliki štradon", "Velikovška ulica", "Velnarjeva ulica",
        "Verovškova ulica", "Veršičeva ulica", "Veselova ulica",
        "Videmska ulica", "Vidergarjeva ulica", "Vidičeva ulica",
        "Vidovdanska cesta", "Vilharjev podhod", "Vilharjeva cesta",
        "Vinterca", "Vipavska ulica", "Vipotnikova ulica", "Viška cesta",
        "Vižmarska pot", "Vodmatska ulica", "Vodmatski trg", "Vodna steza",
        "Vodnikova cesta", "Vodnikovo naselje", "Vodovodna cesta",
        "Vogelna ulica", "Vojkova cesta", "Volaričeva ulica",
        "Vošnjakova ulica", "Vozna pot na Grad", "Vožarski pot",
        "Vrazov trg", "Vrbovec", "Vrbska ulica", "Vregova ulica",
        "Vrhovci, cesta I", "Vrhovci, cesta II", "Vrhovci, cesta III",
        "Vrhovci, cesta IX", "Vrhovci, cesta V", "Vrhovci, cesta VI",
        "Vrhovci, cesta X", "Vrhovci, cesta XI", "Vrhovci, cesta XII",
        "Vrhovci, cesta XIV", "Vrhovci, cesta XIX", "Vrhovci, cesta XV",
        "Vrhovci, cesta XVII", "Vrhovci, cesta XVIII", "Vrhovci, cesta XX",
        "Vrhovci, cesta XXII", "Vrhovci, cesta XXVI", "Vrhovci, cesta XXVIII",
        "Vrhovci, cesta XXXII", "Vrhovčeva ulica", "Vrhovnikova ulica",
        "Vrtača", "Vrtna ulica", "Vrtnarska cesta", "Vulčeva ulica",
        "Vzajemna ulica", "Windischerjeva ulica", "Wolfova ulica",
        "Za Garažami", "Za gasilskim domom", "Za Gradom", "Za krajem",
        "Za opekarno", "Za partizanskim domom", "Za progo", "Za vasjo",
        "Zadnikarjeva ulica", "Zadobrovška cesta", "Zadružna ulica",
        "Zajčeva pot", "Zajčevi dvori", "Zakotnikova ulica",
        "Zalaznikova ulica", "Zaletelova ulica", "Zaloška cesta",
        "Zarnikova ulica", "Zasavska cesta", "Zatišje", "Zavetiška ulica",
        "Završje", "Zbašnikova ulica", "Zdešarjeva cesta",
        "Zelena pot", "Zelenova ulica", "Zeljarska ulica",
        "Zevnikova ulica", "Zidarjev štradon", "Ziherlova ulica",
        "Zlatek", "Znamenjska ulica", "Zofke Kvedrove ulica", "Zoisova cesta",
        "Zupanova ulica", "Zvezda", "Zvezdarska ulica", "Zvezna ulica",
        "Žabarjeva ulica", "Žabjak", "Žalska ulica", "Žaucerjeva ulica",
        "Žeje", "Železna cesta", "Železnikarjeva ulica", "Žerjalova ulica",
        "Židankova ulica", "Židovska steza", "Židovska ulica",
        "Živaličeva ulica", "Živinozdravska ulica", "Žolgerjeva ulica",

    )

    states = (
        'Pomurksa', 'Podravska', 'Koroška', 'Savinjska', 'Zasavska',
        'Spodnjeposavska', 'Jugovzhodna Slovenija', 'Osrednjeslovenska',
        'Gorenjska', 'Notranjsko - kraška', 'Goriška', 'Obalno - kraška',
    )

    countries = (
        "Afganistan", "Islamska republika Afganistan", "Albanija",
        "Alžirija", "Ljudska demokratična republika Alžirija", "Andora",
        "Angola", "Republika Angola", "Antigva in Barbuda", "Argentina",
        "Armenija", "Republika Armenija", "Avstralija", "Avstrija",
        "Azerbajdžan", "Azerbajdžanska republika", "Bahami", "Zveza Bahami",
        "Država Bahrajn", "Bangladeš", "Ljudska republika Bangladeš",
        "Belgija", "Kraljevina Belgija", "Belize", "Belorusija",
        "Benin", "Republika Benin", "Bocvana", "Republika Bocvana",
        "Republika Bolgarija", "Bolivija", "Republika Bolivija",
        "Brazilija", "Federativna republika Brazilija", "Brunej",
        "Burkina Faso", "Burundi", "Republika Burundi", "Butan",
        "Ciper", "Republika Ciper", "Čad", "Republika Čad", "Češka",
        "Čile", "Republika Čile", "Črna gora", "Republika Črna gora",
        "Kraljevina Danska", "Dominika", "Zveza Dominika",
        "Džibuti", "Republika Džibuti", "Egipt", "Arabska republika Egipt",
        "Republika Ekvador", "Ekvatorialna Gvineja", "Eritreja",
        "Estonija", "Republika Estonija", "Etiopija", "Fidži",
        "Filipini", "Republika Filipini", "Finska", "Republika Finska",
        "Francoska republika", "Gabon", "Gabonska republika", "Gambija",
        "Gana", "Republika Gana", "Grčija", "Helenska republika", "Grenada",
        "Gvajana", "Republika Gvajana", "Gvatemala", "Republika Gvatemala",
        "Republika Gvineja", "Gvineja Bissau", "Republika Gvineja Bissau",
        "Republika Haiti", "Honduras", "Republika Honduras", "Hrvaška",
        "Indija", "Republika Indija", "Indonezija", "Republika Indonezija",
        "Republika Irak", "Iran", "Islamska republika Iran", "Irska",
        "Republika Islandija", "Italija", "Italijanska republika", "Izrael",
        "Jamajka", "Japonska", "Jemen", "Republika Jemen", "Jordanija",
        "Južna Afrika", "Republika Južna Afrika", "Južna Koreja",
        "Kambodža", "Kraljevina Kambodža", "Kamerun", "Republika Kamerun",
        "Katar", "Država Katar", "Kazahstan", "Republika Kazahstan", "Kenija",
        "Kirgizistan", "Kirgiška republika", "Kiribati", "Kitajska",
        "Kolumbija", "Republika Kolumbija", "Komori",
        "Kongo", "Republika Kongo", "Demokratična republika Kongo",
        "Republika Kostarika", "Kuba", "Republika Kuba", "Kuvajt",
        "Laos", "Laoška ljudska demokratična republika", "Latvija",
        "Lesoto", "Kraljevina Lesoto", "Libanon", "Libanonska republika",
        "Republika Liberija", "Libija", "Libijska arabska džamahirija",
        "Lihtenštajn", "Kneževina Lihtenštajn", "Litva", "Republika Litva",
        "Veliko vojvodstvo Luksemburg", "Madagaskar", "Republika Madagaskar",
        "Republika Madžarska", "Makedonija", "Republika Makedonija", "Malavi",
        "Maldivi", "Republika Maldivi", "Malezija", "Mali", "Republika Mali",
        "Republika Malta", "Maroko", "Kraljevina Maroko", "Marshallovi otoki",
        "Mauritius", "Republika Mauritius", "Mavretanija",
        "Mehika", "Združene mehiške države", "Mikronezija",
        "Mjanmar", "Zveza Mjanmar", "Moldavija", "Moldavija, Republika",
        "Kneževina Monako", "Mongolija", "Mozambik", "Republika Mozambik",
        "Republika Namibija", "Nauru", "Republika Nauru", "Nemčija",
        "Nepal", "Kraljevina Nepal", "Niger", "Republika Niger", "Nigerija",
        "Nikaragva", "Republika Nikaragva", "Nizozemska",
        "Norveška", "Kraljevina Norveška", "Nova Zelandija", "Oman",
        "Pakistan", "Islamska republika Pakistan", "Palau", "Republika Palau",
        "Republika Panama", "Papua Nova Gvineja", "Paragvaj",
        "Peru", "Republika Peru", "Poljska", "Republika Poljska",
        "Portugalska republika", "Romunija", "Ruanda", "Republika Ruanda",
        "Ruska federacija", "Saint Kitts in Nevis", "Saint Lucia",
        "Salomonovi otoki", "Salvador", "Republika Salvador", "San Marino",
        "Sao Tome in Principe", "Demokratična republika Sao Tome in Principe",
        "Kraljevina Saudova Arabija", "Sejšeli", "Republika Sejšeli",
        "Republika Senegal", "Severna Koreja",
        "Sierra Leone", "Republika Sierra Leone", "Singapur",
        "Sirija", "Sirska arabska republika", "Slonokoščena obala",
        "Slovaška", "Slovaška republika", "Slovenija", "Republika Slovenija",
        "Somalska demokratična republika", "Srbija", "Republika Srbija",
        "Sudan", "Republika Sudan", "Surinam", "Republika Surinam", "Svazi",
        "Španija", "Kraljevina Španija", "Šrilanka",
        "Švedska", "Kraljevina Švedska", "Švica",
        "Tadžikistan", "Republika Tadžikistan", "Tajska",
        "Tajvan", "Tajvan, Provinca Kitajske", "Tanzanija",
        "Togo", "Togoška republika", "Tonga", "Kraljevina Tonga",
        "Republika Trinidad in Tobago", "Tunizija", "Republika Tunizija",
        "Republika Turčija", "Turkmenistan", "Tuvalu", "Uganda",
        "Ukrajina", "Urugvaj", "Vzhodna republika Urugvaj", "Uzbekistan",
        "Vanuatu", "Republika Vanuatu", "Vatikan",
        "Velika Britanija", "Združeno kraljestvo",
        "Venezuela", "Republika Venezuela", "Vietnam",
        "Vzhodni Timor", "Demokratična republika Vzhodni Timor",
        "Samoa", "Neodvisna država Zahodna Samoa", "Zambija",
        "Združene države Amerike", "Združene države",
        "Združeni arabski emirati", "Zelenortski otoki",
    )

    def city_name(self):
        return self.random_element(self.cities)

    def street_name(self):
        return self.random_element(self.streets)

    def state(self):
        return self.random_element(self.states)
