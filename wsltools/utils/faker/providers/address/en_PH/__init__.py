# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

from collections import OrderedDict
from string import ascii_uppercase

from .. import Provider as AddressProvider


class Provider(AddressProvider):
    """
    Provider for addresses for en_PH locale

    Like many things in the Philippines, even addresses are more complicated than necessary. This provider is already
    a gross oversimplification, and it is still a lot more complicated VS providers from other locales despite taking
    shortcuts. Below are some tidbits of information that, as a whole, shaped the design decisions of this provider.

    - There are many levels of geopolitical division, thus many levels of local government:
        * There are three major island groups - Luzon, Visayas, Mindanao
        * Those major groups are divided into 17 different regions.
        * Each region is divided into provinces with the exception of the National Capital Region aka Metro Manila.
        * Each province is composed of multiple cities/municipalities.
        * Metro Manila, like a province, is composed of multiple cities/municipalities, but it is a region.
        * Each city/municipality is composed of multiple smaller local government units called barangays.
        * In some places, some barangays are divided further, and as of 2019, there are 42,045 barangays on record.
    - Metro Manila is part of Luzon geographically, but it is almost always treated as a separate entity politically,
      economically, statistically, and so on, since it is home to around 13% of the population despite being only around
      0.2% of the country's total land area.
    - Names of cities, municipalities, and barangays vary a lot. Furthermore, if a place has a non-English name, there
      will almost always be no English translation and vice-versa. It is essentially impossible to generate fake city,
      municipality, and barangay names in a similar manner used in the other "en" locales while being locale specific.
    - Subdivisions and other higher density housing (like high-rise condominiums) are popular in real estate.
    - The 13th floor is omitted in buildings like in many parts of the world.
    - The floor number distribution is partly based on the tallest buildings in the Philippines and partly anecdotal,
      but the general idea is that the higher the floor number is, the lower probability of it appearing. Furthermore,
      as the floor number approaches the highest floors of the tallest buildings, the probability plummets further.
    - The address distribution is based on the official 2015 population census.
    - Addresses should include a barangay, but it has been dropped to keep things sane, all things considered.
    - In addition to numbered floors, buildings have ground floors and may have lower ground, upper ground, mezzanine,
      and basement floors. Buildings may also have units on any of those floors, but the naming scheme varies, so they
      have been dropped, again to keep things sane.

    Sources:
    - https://en.wikipedia.org/wiki/Provinces_of_the_Philippines
    - https://en.wikipedia.org/wiki/List_of_cities_and_municipalities_in_the_Philippines
    - https://en.wikipedia.org/wiki/Barangay
    - https://en.wikipedia.org/wiki/Postal_addresses_in_the_Philippines
    - https://en.wikipedia.org/wiki/List_of_ZIP_codes_in_the_Philippines
    - https://www.phlpost.gov.ph/
    - http://en.wikipedia.org/wiki/List_of_tallest_buildings_in_the_Philippines
    - https://psa.gov.ph/sites/default/files/attachments/hsd/pressrelease/2015%20population%20counts%20Summary_0.xlsx
    """

    metro_manila_postcodes = tuple(x for x in range(400, 1849))
    luzon_province_postcodes = (
        tuple(x for x in range(1850, 5000))
        + tuple(x for x in range(5100, 5600))
    )
    visayas_province_postcodes = (
        tuple(x for x in range(5000, 5100))
        + tuple(x for x in range(5600, 5800))
        + tuple(x for x in range(6000, 6900))
    )
    mindanao_province_postcodes = (
        tuple(x for x in range(7000, 7600))
        + tuple(x for x in range(8000, 8900))
        + tuple(x for x in range(9000, 9900))
    )
    postcodes = (
        metro_manila_postcodes
        + luzon_province_postcodes
        + visayas_province_postcodes
        + mindanao_province_postcodes
    )
    metro_manila_lgus = (
        'Caloocan', 'Las Piñas', 'Makati', 'Malabon', 'Mandaluyong', 'Manila', 'Marikina', 'Muntinlupa', 'Navotas',
        'Parañaque', 'Pasay', 'Pasig', 'Pateros', 'Quezon City', 'San Juan', 'Taguig', 'Valenzuela',
    )
    province_lgus = (
        'Aborlan', 'Abra de Ilog', 'Abucay', 'Abulug', 'Abuyog', 'Adams', 'Agdangan', 'Aglipay', 'Agno', 'Agoncillo',
        'Agoo', 'Aguilar', 'Aguinaldo', 'Agutaya', 'Ajuy', 'Akbar', 'Al-Barka', 'Alabat', 'Alabel', 'Alamada',
        'Alaminos', 'Alangalang', 'Albuera', 'Alburquerque', 'Alcala', 'Alcantara', 'Alcoy', 'Alegria', 'Aleosan',
        'Alfonso Castañeda', 'Alfonso Lista', 'Alfonso', 'Aliaga', 'Alicia', 'Alilem', 'Alimodian', 'Alitagtag',
        'Allacapan', 'Allen', 'Almagro', 'Almeria', 'Aloguinsan', 'Aloran', 'Altavas', 'Alubijid', 'Amadeo',
        'Amai Manabilang', 'Ambaguio', 'Amlan', 'Ampatuan', 'Amulung', 'Anahawan', 'Anao', 'Anda', 'Angadanan', 'Angat',
        'Angeles', 'Angono', 'Anilao', 'Anini-y', 'Antequera', 'Antipas', 'Antipolo', 'Apalit', 'Aparri', 'Araceli',
        'Arakan', 'Arayat', 'Argao', 'Aringay', 'Aritao', 'Aroroy', 'Arteche', 'Asingan', 'Asipulo', 'Asturias',
        'Asuncion', 'Atimonan', 'Atok', 'Aurora', 'Ayungon', 'Baao', 'Babatngon', 'Bacacay', 'Bacarra', 'Baclayon',
        'Bacnotan', 'Baco', 'Bacolod-Kalawi', 'Bacolod', 'Bacolor', 'Bacong', 'Bacoor', 'Bacuag', 'Badian', 'Badiangan',
        'Badoc', 'Bagabag', 'Bagac', 'Bagamanoc', 'Baganga', 'Baggao', 'Bago', 'Baguio', 'Bagulin', 'Bagumbayan',
        'Bais', 'Bakun', 'Balabac', 'Balabagan', 'Balagtas', 'Balamban', 'Balanga', 'Balangiga', 'Balangkayan',
        'Balaoan', 'Balasan', 'Balatan', 'Balayan', 'Balbalan', 'Baleno', 'Baler', 'Balete', 'Baliangao', 'Baliguian',
        'Balilihan', 'Balindong', 'Balingasag', 'Balingoan', 'Baliuag', 'Ballesteros', 'Baloi', 'Balud', 'Balungao',
        'Bamban', 'Bambang', 'Banate', 'Banaue', 'Banaybanay', 'Banayoyo', 'Banga', 'Bangar', 'Bangued', 'Bangui',
        'Banguingui', 'Bani', 'Banisilan', 'Banna', 'Bansalan', 'Bansud', 'Bantay', 'Bantayan', 'Banton', 'Baras',
        'Barbaza', 'Barcelona', 'Barili', 'Barira', 'Barlig', 'Barobo', 'Barotac Nuevo', 'Barotac Viejo', 'Baroy',
        'Barugo', 'Basay', 'Basco', 'Basey', 'Basilisa', 'Basista', 'Basud', 'Batac', 'Batad', 'Batan', 'Batangas City',
        'Bataraza', 'Bato', 'Batuan', 'Bauan', 'Bauang', 'Bauko', 'Baungon', 'Bautista', 'Bay', 'Bayabas', 'Bayambang',
        'Bayang', 'Bayawan', 'Baybay', 'Bayog', 'Bayombong', 'Bayugan', 'Belison', 'Benito Soliven', 'Besao',
        'Bien Unido', 'Bilar', 'Biliran', 'Binalbagan', 'Binalonan', 'Biñan', 'Binangonan', 'Bindoy', 'Bingawan',
        'Binidayan', 'Binmaley', 'Binuangan', 'Biri', 'Bislig', 'Boac', 'Bobon', 'Bocaue', 'Bogo', 'Bokod', 'Bolinao',
        'Boliney', 'Boljoon', 'Bombon', 'Bongabon', 'Bongabong', 'Bongao', 'Bonifacio', 'Bontoc', 'Borbon', 'Borongan',
        'Boston', 'Botolan', 'Braulio E. Dujali', "Brooke's Point", 'Buadiposo-Buntong', 'Bubong', 'Bucay', 'Bucloc',
        'Buenavista', 'Bugallon', 'Bugasong', 'Buguey', 'Buguias', 'Buhi', 'Bula', 'Bulakan', 'Bulalacao', 'Bulan',
        'Buldon', 'Buluan', 'Bulusan', 'Bunawan', 'Burauen', 'Burdeos', 'Burgos', 'Buruanga', 'Bustos', 'Busuanga',
        'Butig', 'Butuan', 'Buug', 'Caba', 'Cabadbaran', 'Cabagan', 'Cabanatuan', 'Cabangan', 'Cabanglasan',
        'Cabarroguis', 'Cabatuan', 'Cabiao', 'Cabucgayan', 'Cabugao', 'Cabusao', 'Cabuyao', 'Cadiz', 'Cagayan de Oro',
        'Cagayancillo', 'Cagdianao', 'Cagwait', 'Caibiran', 'Cainta', 'Cajidiocan', 'Calabanga', 'Calaca', 'Calamba',
        'Calanasan', 'Calanogas', 'Calapan', 'Calape', 'Calasiao', 'Calatagan', 'Calatrava', 'Calauag', 'Calauan',
        'Calayan', 'Calbayog', 'Calbiga', 'Calinog', 'Calintaan', 'Calubian', 'Calumpit', 'Caluya', 'Camalaniugan',
        'Camalig', 'Camaligan', 'Camiling', 'Can-avid', 'Canaman', 'Candaba', 'Candelaria', 'Candijay', 'Candon',
        'Candoni', 'Canlaon', 'Cantilan', 'Caoayan', 'Capalonga', 'Capas', 'Capoocan', 'Capul', 'Caraga', 'Caramoan',
        'Caramoran', 'Carasi', 'Carcar', 'Cardona', 'Carigara', 'Carles', 'Carmen', 'Carmona', 'Carranglan',
        'Carrascal', 'Casiguran', 'Castilla', 'Castillejos', 'Cataingan', 'Catanauan', 'Catarman', 'Catbalogan',
        'Cateel', 'Catigbian', 'Catmon', 'Catubig', 'Cauayan', 'Cavinti', 'Cavite City', 'Cawayan', 'Cebu City',
        'Cervantes', 'Clarin', 'Claver', 'Claveria', 'Columbio', 'Compostela', 'Concepcion', 'Conner', 'Consolacion',
        'Corcuera', 'Cordon', 'Cordova', 'Corella', 'Coron', 'Cortes', 'Cotabato City', 'Cuartero', 'Cuenca', 'Culaba',
        'Culasi', 'Culion', 'Currimao', 'Cuyapo', 'Cuyo', 'Daanbantayan', 'Daet', 'Dagami', 'Dagohoy', 'Daguioman',
        'Dagupan', 'Dalaguete', 'Damulog', 'Danao', 'Dangcagan', 'Danglas', 'Dao', 'Dapa', 'Dapitan', 'Daraga', 'Daram',
        'Dasmariñas', 'Dasol', 'Datu Abdullah Sangki', 'Datu Anggal Midtimbang', 'Datu Blah T. Sinsuat',
        'Datu Hoffer Ampatuan', 'Datu Montawal', 'Datu Odin Sinsuat', 'Datu Paglas', 'Datu Piang', 'Datu Salibo',
        'Datu Saudi-Ampatuan', 'Datu Unsay', 'Dauin', 'Dauis', 'Davao City', 'Del Carmen', 'Del Gallego',
        'Delfin Albano', 'Diadi', 'Diffun', 'Digos', 'Dilasag', 'Dimasalang', 'Dimataling', 'Dimiao', 'Dinagat',
        'Dinalungan', 'Dinalupihan', 'Dinapigue', 'Dinas', 'Dingalan', 'Dingle', 'Dingras', 'Dipaculao', 'Diplahan',
        'Dipolog', 'Ditsaan-Ramain', 'Divilacan', 'Dolores', 'Don Carlos', 'Don Marcelino', 'Don Victoriano Chiongbian',
        'Doña Remedios Trinidad', 'Donsol', 'Dueñas', 'Duero', 'Dulag', 'Dumaguete', 'Dumalag', 'Dumalinao', 'Dumalneg',
        'Dumangas', 'Dumanjug', 'Dumaran', 'Dumarao', 'Dumingag', 'Dupax del Norte', 'Dupax del Sur', 'Echague',
        'El Nido', 'El Salvador', 'Enrile', 'Enrique B. Magalona', 'Enrique Villanueva', 'Escalante', 'Esperanza',
        'Estancia', 'Famy', 'Ferrol', 'Flora', 'Floridablanca', 'Gabaldon', 'Gainza', 'Galimuyod', 'Gamay', 'Gamu',
        'Ganassi', 'Gandara', 'Gapan', 'Garchitorena', 'Garcia Hernandez', 'Gasan', 'Gattaran',
        'General Emilio Aguinaldo', 'General Luna', 'General MacArthur', 'General Mamerto Natividad',
        'General Mariano Alvarez', 'General Nakar', 'General Salipada K. Pendatun', 'General Santos', 'General Tinio',
        'General Trias', 'Gerona', 'Getafe', 'Gigaquit', 'Gigmoto', 'Ginatilan', 'Gingoog', 'Giporlos', 'Gitagum',
        'Glan', 'Gloria', 'Goa', 'Godod', 'Gonzaga', 'Governor Generoso', 'Gregorio del Pilar', 'Guagua', 'Gubat',
        'Guiguinto', 'Guihulngan', 'Guimba', 'Guimbal', 'Guinayangan', 'Guindulman', 'Guindulungan', 'Guinobatan',
        'Guinsiliban', 'Guipos', 'Guiuan', 'Gumaca', 'Gutalac', 'Hadji Mohammad Ajul', 'Hadji Muhtamad',
        'Hadji Panglima Tahil', 'Hagonoy', 'Hamtic', 'Hermosa', 'Hernani', 'Hilongos', 'Himamaylan', 'Hinabangan',
        'Hinatuan', 'Hindang', 'Hingyon', 'Hinigaran', 'Hinoba-an', 'Hinunangan', 'Hinundayan', 'Hungduan', 'Iba',
        'Ibaan', 'Ibajay', 'Igbaras', 'Iguig', 'Ilagan', 'Iligan', 'Ilog', 'Iloilo City', 'Imelda', 'Impasugong',
        'Imus', 'Inabanga', 'Indanan', 'Indang', 'Infanta', 'Initao', 'Inopacan', 'Ipil', 'Iriga', 'Irosin', 'Isabel',
        'Isabela City', 'Isabela', 'Isulan', 'Itbayat', 'Itogon', 'Ivana', 'Ivisan', 'Jabonga', 'Jaen', 'Jagna',
        'Jalajala', 'Jamindan', 'Janiuay', 'Jaro', 'Jasaan', 'Javier', 'Jiabong', 'Jimalalud', 'Jimenez', 'Jipapad',
        'Jolo', 'Jomalig', 'Jones', 'Jordan', 'Jose Abad Santos', 'Jose Dalman', 'Jose Panganiban', 'Josefina',
        'Jovellar', 'Juban', 'Julita', 'Kabacan', 'Kabankalan', 'Kabasalan', 'Kabayan', 'Kabugao', 'Kabuntalan',
        'Kadingilan', 'Kalamansig', 'Kalawit', 'Kalayaan', 'Kalibo', 'Kalilangan', 'Kalingalan Caluang', 'Kananga',
        'Kapai', 'Kapalong', 'Kapangan', 'Kapatagan', 'Kasibu', 'Katipunan', 'Kauswagan', 'Kawayan', 'Kawit', 'Kayapa',
        'Kiamba', 'Kiangan', 'Kibawe', 'Kiblawan', 'Kibungan', 'Kidapawan', 'Kinoguitan', 'Kitaotao', 'Kitcharao',
        'Kolambugan', 'Koronadal', 'Kumalarang', 'La Carlota', 'La Castellana', 'La Libertad', 'La Paz', 'La Trinidad',
        'Laak', 'Labangan', 'Labason', 'Labo', 'Labrador', 'Lacub', 'Lagangilang', 'Lagawe', 'Lagayan', 'Lagonglong',
        'Lagonoy', 'Laguindingan', 'Lake Sebu', 'Lakewood', 'Lal-lo', 'Lala', 'Lambayong', 'Lambunao', 'Lamitan',
        'Lamut', 'Langiden', 'Languyan', 'Lantapan', 'Lantawan', 'Lanuza', 'Laoac', 'Laoag', 'Laoang', 'Lapinig',
        'Lapu-Lapu', 'Lapuyan', 'Larena', 'Las Navas', 'Las Nieves', 'Lasam', 'Laua-an', 'Laur', 'Laurel', 'Lavezares',
        'Lawaan', 'Lazi', 'Lebak', 'Leganes', 'Legazpi', 'Lemery', 'Leon B. Postigo', 'Leon', 'Leyte', 'Lezo', 'Lian',
        'Lianga', 'Libacao', 'Libagon', 'Libertad', 'Libjo', 'Libmanan', 'Libon', 'Libona', 'Libungan', 'Licab',
        'Licuan-Baay', 'Lidlidda', 'Ligao', 'Lila', 'Liliw', 'Liloan', 'Liloy', 'Limasawa', 'Limay', 'Linamon',
        'Linapacan', 'Lingayen', 'Lingig', 'Lipa', 'Llanera', 'Llorente', 'Loay', 'Lobo', 'Loboc', 'Looc', 'Loon',
        'Lope de Vega', 'Lopez Jaena', 'Lopez', 'Loreto', 'Los Baños', 'Luba', 'Lubang', 'Lubao', 'Lubuagan', 'Lucban',
        'Lucena', 'Lugait', 'Lugus', 'Luisiana', 'Lumba-Bayabao', 'Lumbaca-Unayan', 'Lumban', 'Lumbatan',
        'Lumbayanague', 'Luna', 'Lupao', 'Lupi', 'Lupon', 'Lutayan', 'Luuk', "M'lang", 'Maasim', 'Maasin', 'Maayon',
        'Mabalacat', 'Mabinay', 'Mabini', 'Mabitac', 'Mabuhay', 'Macabebe', 'Macalelon', 'MacArthur', 'Maco',
        'Maconacon', 'Macrohon', 'Madalag', 'Madalum', 'Madamba', 'Maddela', 'Madrid', 'Madridejos', 'Magalang',
        'Magallanes', 'Magarao', 'Magdalena', 'Magdiwang', 'Magpet', 'Magsaysay', 'Magsingal', 'Maguing', 'Mahaplag',
        'Mahatao', 'Mahayag', 'Mahinog', 'Maigo', 'Maimbung', 'Mainit', 'Maitum', 'Majayjay', 'Makato', 'Makilala',
        'Malabang', 'Malabuyoc', 'Malalag', 'Malangas', 'Malapatan', 'Malasiqui', 'Malay', 'Malaybalay', 'Malibcong',
        'Malilipot', 'Malimono', 'Malinao', 'Malita', 'Malitbog', 'Mallig', 'Malolos', 'Malungon', 'Maluso', 'Malvar',
        'Mamasapano', 'Mambajao', 'Mamburao', 'Mambusao', 'Manabo', 'Manaoag', 'Manapla', 'Manay', 'Mandaon', 'Mandaue',
        'Mangaldan', 'Mangatarem', 'Mangudadatu', 'Manito', 'Manjuyod', 'Mankayan', 'Manolo Fortich', 'Mansalay',
        'Manticao', 'Manukan', 'Mapanas', 'Mapandan', 'Mapun', 'Marabut', 'Maragondon', 'Maragusan', 'Maramag',
        'Marantao', 'Marawi', 'Marcos', 'Margosatubig', 'Maria Aurora', 'Maria', 'Maribojoc', 'Marihatag', 'Marilao',
        'Maripipi', 'Mariveles', 'Marogong', 'Masantol', 'Masbate City', 'Masinloc', 'Masiu', 'Maslog', 'Mataasnakahoy',
        'Matag-ob', 'Matalam', 'Matalom', 'Matanao', 'Matanog', 'Mati', 'Matnog', 'Matuguinao', 'Matungao', 'Mauban',
        'Mawab', 'Mayantoc', 'Maydolong', 'Mayorga', 'Mayoyao', 'Medellin', 'Medina', 'Mendez', 'Mercedes', 'Merida',
        'Mexico', 'Meycauayan', 'Miagao', 'Midsalip', 'Midsayap', 'Milagros', 'Milaor', 'Mina', 'Minalabac', 'Minalin',
        'Minglanilla', 'Moalboal', 'Mobo', 'Mogpog', 'Moises Padilla', 'Molave', 'Moncada', 'Mondragon', 'Monkayo',
        'Monreal', 'Montevista', 'Morong', 'Motiong', 'Mulanay', 'Mulondo', 'Munai', 'Muñoz', 'Murcia', 'Mutia',
        'Naawan', 'Nabas', 'Nabua', 'Nabunturan', 'Naga', 'Nagbukel', 'Nagcarlan', 'Nagtipunan', 'Naguilian', 'Naic',
        'Nampicuan', 'Narra', 'Narvacan', 'Nasipit', 'Nasugbu', 'Natividad', 'Natonin', 'Naujan', 'Naval', 'New Bataan',
        'New Corella', 'New Lucena', 'New Washington', 'Norala', 'Northern Kabuntalan', 'Norzagaray', 'Noveleta',
        'Nueva Era', 'Nueva Valencia', 'Numancia', 'Nunungan', 'Oas', 'Obando', 'Ocampo', 'Odiongan', 'Old Panamao',
        'Olongapo', 'Olutanga', 'Omar', 'Opol', 'Orani', 'Oras', 'Orion', 'Ormoc', 'Oroquieta', 'Oslob', 'Oton',
        'Ozamiz', 'Padada', 'Padre Burgos', 'Padre Garcia', 'Paete', 'Pagadian', 'Pagalungan', 'Pagayawan', 'Pagbilao',
        'Paglat', 'Pagsanghan', 'Pagsanjan', 'Pagudpud', 'Pakil', 'Palanan', 'Palanas', 'Palapag', 'Palauig', 'Palayan',
        'Palimbang', 'Palo', 'Palompon', 'Paluan', 'Pambujan', 'Pamplona', 'Panabo', 'Panaon', 'Panay', 'Pandag',
        'Pandami', 'Pandan', 'Pandi', 'Panganiban', 'Pangantucan', 'Pangil', 'Panglao', 'Panglima Estino',
        'Panglima Sugala', 'Pangutaran', 'Paniqui', 'Panitan', 'Pantabangan', 'Pantao Ragat', 'Pantar', 'Pantukan',
        'Panukulan', 'Paoay', 'Paombong', 'Paracale', 'Paracelis', 'Paranas', 'Parang', 'Pasacao', 'Pasil', 'Passi',
        'Pastrana', 'Pasuquin', 'Pata', 'Patikul', 'Patnanungan', 'Patnongon', 'Pavia', 'Payao', 'Peñablanca',
        'Peñaranda', 'Peñarrubia', 'Perez', 'Piagapo', 'Piat', 'Picong', 'Piddig', 'Pidigan', 'Pigcawayan', 'Pikit',
        'Pila', 'Pilar', 'Pili', 'Pililla', 'Pinabacdao', 'Pinamalayan', 'Pinamungajan', 'Piñan', 'Pinili', 'Pintuyan',
        'Pinukpuk', 'Pio Duran', 'Pio V. Corpuz', 'Pitogo', 'Placer', 'Plaridel', 'Pola', 'Polanco', 'Polangui',
        'Polillo', 'Polomolok', 'Pontevedra', 'Poona Bayabao', 'Poona Piagapo', 'Porac', 'Poro', 'Pototan',
        'Pozorrubio', 'Presentacion', 'President Carlos P. Garcia', 'President Manuel A. Roxas', 'President Quirino',
        'President Roxas', 'Prieto Diaz', 'Prosperidad', 'Pualas', 'Pudtol', 'Puerto Galera', 'Puerto Princesa', 'Pugo',
        'Pulilan', 'Pulupandan', 'Pura', 'Quezon', 'Quinapondan', 'Quirino', 'Ragay', 'Rajah Buayan', 'Ramon Magsaysay',
        'Ramon', 'Ramos', 'Rapu-Rapu', 'Real', 'Reina Mercedes', 'Remedios T. Romualdez', 'Rizal', 'Rodriguez',
        'Romblon', 'Ronda', 'Rosales', 'Rosario', 'Roseller Lim', 'Roxas City', 'Roxas', 'Sabangan', 'Sablan',
        'Sablayan', 'Sabtang', 'Sadanga', 'Sagada', 'Sagay', 'Sagbayan', 'Sagñay', 'Saguday', 'Saguiaran',
        'Saint Bernard', 'Salay', 'Salcedo', 'Sallapadan', 'Salug', 'Salvador Benedicto', 'Salvador', 'Samal',
        'Samboan', 'Sampaloc', 'San Agustin', 'San Andres', 'San Antonio', 'San Benito', 'San Carlos', 'San Clemente',
        'San Dionisio', 'San Emilio', 'San Enrique', 'San Esteban', 'San Fabian', 'San Felipe', 'San Fernando',
        'San Francisco', 'San Gabriel', 'San Guillermo', 'San Ildefonso', 'San Isidro', 'San Jacinto', 'San Joaquin',
        'San Jorge', 'San Jose de Buan', 'San Jose de Buenavista', 'San Jose del Monte', 'San Jose', 'San Juan',
        'San Julian', 'San Leonardo', 'San Lorenzo Ruiz', 'San Lorenzo', 'San Luis', 'San Manuel', 'San Marcelino',
        'San Mariano', 'San Mateo', 'San Miguel', 'San Narciso', 'San Nicolas', 'San Pablo', 'San Pascual', 'San Pedro',
        'San Policarpo', 'San Quintin', 'San Rafael', 'San Remigio', 'San Ricardo', 'San Roque', 'San Sebastian',
        'San Simon', 'San Teodoro', 'San Vicente', 'Sanchez-Mira', 'Santa Ana', 'Santa Barbara', 'Santa Catalina',
        'Santa Cruz', 'Santa Elena', 'Santa Fe', 'Santa Ignacia', 'Santa Josefa', 'Santa Lucia', 'Santa Magdalena',
        'Santa Marcela', 'Santa Margarita', 'Santa Maria', 'Santa Monica', 'Santa Praxedes', 'Santa Rita', 'Santa Rosa',
        'Santa Teresita', 'Santa', 'Santander', 'Santiago', 'Santo Domingo', 'Santo Niño', 'Santo Tomas', 'Santol',
        'Sapa-Sapa', 'Sapad', 'Sapang Dalaga', 'Sapian', 'Sara', 'Sarangani', 'Sariaya', 'Sarrat', 'Sasmuan', 'Sebaste',
        'Senator Ninoy Aquino', 'Sergio Osmeña Sr.', 'Sevilla', 'Shariff Aguak', 'Shariff Saydona Mustapha', 'Siasi',
        'Siaton', 'Siay', 'Siayan', 'Sibagat', 'Sibalom', 'Sibonga', 'Sibuco', 'Sibulan', 'Sibunag', 'Sibutad',
        'Sibutu', 'Sierra Bullones', 'Sigay', 'Sigma', 'Sikatuna', 'Silago', 'Silang', 'Silay', 'Silvino Lobos',
        'Simunul', 'Sinacaban', 'Sinait', 'Sindangan', 'Siniloan', 'Siocon', 'Sipalay', 'Sipocot', 'Siquijor',
        'Sirawai', 'Siruma', 'Sison', 'Sitangkai', 'Socorro', 'Sofronio Española', 'Sogod', 'Solana', 'Solano',
        'Solsona', 'Sominot', 'Sorsogon City', 'South Ubian', 'South Upi', 'Sual', 'Subic', 'Sudipen', 'Sugbongcogon',
        'Sugpon', 'Sulat', 'Sulop', 'Sultan Dumalondong', 'Sultan Kudarat', 'Sultan Mastura', 'Sultan Naga Dimaporo',
        'Sultan sa Barongis', 'Sultan Sumagka', 'Sumilao', 'Sumisip', 'Surallah', 'Surigao City', 'Suyo', "T'Boli",
        'Taal', 'Tabaco', 'Tabango', 'Tabina', 'Tabogon', 'Tabontabon', 'Tabuan-Lasa', 'Tabuelan', 'Tabuk', 'Tacloban',
        'Tacurong', 'Tadian', 'Taft', 'Tagana-an', 'Tagapul-an', 'Tagaytay', 'Tagbilaran', 'Tagbina', 'Tagkawayan',
        'Tago', 'Tagoloan II', 'Tagoloan', 'Tagudin', 'Tagum', 'Talacogon', 'Talaingod', 'Talakag', 'Talalora',
        'Talavera', 'Talayan', 'Talibon', 'Talipao', 'Talisay', 'Talisayan', 'Talugtug', 'Talusan', 'Tambulig',
        'Tampakan', 'Tamparan', 'Tampilisan', 'Tanauan', 'Tanay', 'Tandag', 'Tandubas', 'Tangalan', 'Tangcal', 'Tangub',
        'Tanjay', 'Tantangan', 'Tanudan', 'Tanza', 'Tapaz', 'Tapul', 'Taraka', 'Tarangnan', 'Tarlac City', 'Tarragona',
        'Tayabas', 'Tayasan', 'Taysan', 'Taytay', 'Tayug', 'Tayum', 'Teresa', 'Ternate', 'Tiaong', 'Tibiao', 'Tigaon',
        'Tigbao', 'Tigbauan', 'Tinambac', 'Tineg', 'Tinglayan', 'Tingloy', 'Tinoc', 'Tipo-Tipo', 'Titay', 'Tiwi',
        'Tobias Fornier', 'Toboso', 'Toledo', 'Tolosa', 'Tomas Oppus', 'Torrijos', 'Trece Martires', 'Trento',
        'Trinidad', 'Tuao', 'Tuba', 'Tubajon', 'Tubao', 'Tubaran', 'Tubay', 'Tubigon', 'Tublay', 'Tubo', 'Tubod',
        'Tubungan', 'Tuburan', 'Tudela', 'Tugaya', 'Tuguegarao', 'Tukuran', 'Tulunan', 'Tumauini', 'Tunga', 'Tungawan',
        'Tupi', 'Turtle Islands', 'Tuy', 'Ubay', 'Umingan', 'Ungkaya Pukan', 'Unisan', 'Upi', 'Urbiztondo', 'Urdaneta',
        'Uson', 'Uyugan', 'Valderrama', 'Valencia', 'Valladolid', 'Vallehermoso', 'Veruela', 'Victoria', 'Victorias',
        'Viga', 'Vigan', 'Villaba', 'Villanueva', 'Villareal', 'Villasis', 'Villaverde', 'Villaviciosa',
        'Vincenzo A. Sagun', 'Vintar', 'Vinzons', 'Virac', 'Wao', 'Zamboanga City', 'Zamboanguita', 'Zaragoza',
        'Zarraga', 'Zumarraga',
    )
    luzon_provinces = (
        'Abra', 'Albay', 'Apayao', 'Aurora', 'Bataan', 'Batanes', 'Batangas', 'Benguet', 'Bulacan', 'Cagayan',
        'Camarines Norte', 'Camarines Sur', 'Catanduanes', 'Cavite', 'Ifugao', 'Ilocos Norte', 'Ilocos Sur', 'Isabela',
        'Kalinga', 'La Union', 'Laguna', 'Marinduque', 'Masbate', 'Mountain Province', 'Nueva Ecija', 'Nueva Vizcaya',
        'Occidental Mindoro', 'Oriental Mindoro', 'Palawan', 'Pampanga', 'Pangasinan', 'Quezon', 'Quirino', 'Rizal',
        'Romblon', 'Sorsogon', 'Tarlac', 'Zambales',
    )
    visayas_provinces = (
        'Aklan', 'Antique', 'Biliran', 'Bohol', 'Capiz', 'Cebu', 'Eastern Samar', 'Guimaras', 'Iloilo', 'Leyte',
        'Negros Occidental', 'Negros Oriental', 'Northern Samar', 'Samar', 'Siquijor', 'Southern Leyte',
    )
    mindanao_provinces = (
        'Agusan del Norte', 'Agusan del Sur', 'Basilan', 'Bukidnon', 'Camiguin', 'Compostela Valley', 'Cotabato',
        'Davao del Norte', 'Davao del Sur', 'Davao Occidental', 'Davao Oriental', 'Dinagat Islands', 'Lanao del Norte',
        'Lanao del Sur', 'Maguindanao', 'Misamis Occidental', 'Misamis Oriental', 'Sarangani', 'South Cotabato',
        'Sultan Kudarat', 'Sulu', 'Surigao del Norte', 'Surigao del Sur', 'Tawi-Tawi', 'Zamboanga del Norte',
        'Zamboanga del Sur', 'Zamboanga Sibugay',
    )
    provinces = luzon_provinces + visayas_provinces + mindanao_provinces

    partitioned_building_number_formats = (
        '{{standalone_building_number}}?',
        '{{standalone_building_number}} ?',
        '{{standalone_building_number}}-?',
        '{{standalone_building_number}} Unit ?',
    )
    building_unit_number_formats = (
        'Unit {{floor_unit_number}}',
        'Room {{floor_unit_number}}',
        '{{floor_number}}F',
        '{{ordinal_floor_number}} Floor',
    )
    building_name_formats = (
        '{{last_name}} {{building_name_suffix}}',
        '{{random_object_name}} {{building_name_suffix}}',
    )
    building_name_suffixes = (
        'Apartment', 'Apartments',
        'Building', 'Building %', 'Building Tower %',
        'Condominiums', 'Condominiums %', 'Condominiums Tower %',
        'Place', 'Place %', 'Place Tower %',
        'Residences', 'Residences %', 'Residences Tower %',
        'Suites', 'Suites %', 'Suites Tower %',
        'Tower', 'Towers', 'Towers %',
    )
    subdivision_unit_number_formats = (
        'B{{subdivision_block_number}} L{{subdivision_lot_number}}',
        'Block {{subdivision_block_number}} Lot {{subdivision_lot_number}}',
    )
    subdivision_name_formats = (
        '{{last_name}} {{subdivision_name_suffix}}',
        '{{random_object_name}} {{subdivision_name_suffix}}',
    )
    subdivision_name_suffixes = (
        'Cove', 'Cove %', 'Cove Phase %',
        'Estates', 'Estates %', 'Estates Phase %',
        'Grove', 'Grove %', 'Grove Phase %',
        'Homes', 'Homes %', 'Homes Phase %',
        'Subdivision', 'Subdivision %', 'Subdivision Phase %',
        'Village', 'Village %', 'Village Phase %',
    )
    floor_numbers = OrderedDict([
        (str(x), 0.08) for x in range(2, 5)  # Floors 2 to 4, 24% of the time
    ] + [
        (str(x), 0.32356832089420257 / x) for x in range(5, 13)  # Floors 5 to 12, 33% of the time
    ] + [
        (str(x), 0.30341265418486174 / (x - 1)) for x in range(14, 30)  # Floors 14 to 29, 25% of the time
    ] + [
        (str(x), 0.30096338222652870 / (x - 1)) for x in range(30, 50)  # Floors 30 to 49, 16% of the time
    ] + [
        (str(x), 0.04570476167856688 / (x - 1)) for x in range(50, 75)  # Floors 50 to 74, 1.9% of the time
    ] + [
        (str(x), 0.003415677066138734 / (x - 1)) for x in range(75, 100)  # Floors 75 to 99, 0.1% of the time
    ])

    street_suffixes = OrderedDict([
        ('Avenue', 0.12),
        ('Avenue Extension', 0.01),
        ('Boulevard', 0.05),
        ('Boulevard Extension', 0.008),
        ('Circle', 0.002),
        ('Drive', 0.15),
        ('Drive Extension', 0.03),
        ('Expressway', 0.01),
        ('Extension', 0.05),
        ('Highway', 0.02),
        ('Road', 0.2),
        ('Road Extension', 0.04),
        ('Service Road', 0.01),
        ('Street', 0.3),
    ])
    street_name_formats = (
        '{{last_name}} {{street_suffix}}',
        '{{ordinal_street_number}} {{street_suffix}}',
        '{{gemstone_name}} {{street_suffix}}',
        '{{mountain_name}} {{street_suffix}}',
        '{{plant_name}} {{street_suffix}}',
        '{{space_object_name}} {{street_suffix}}',
    )
    street_address_formats = (
        '{{standalone_building_number}} {{street_name}}',
        '{{partitioned_building_number}} {{street_name}}',
        '{{subdivision_unit_number}} {{subdivision_name}}, {{street_name}}',
        '{{subdivision_unit_number}} {{street_name}}, {{subdivision_name}}',
        '{{standalone_building_number}} {{street_name}}, {{subdivision_name}}',
        '{{building_unit_number}} {{building_name}}, {{standalone_building_number}} {{street_name}}',
    )

    metro_manila_address_formats = (
        '{{street_address}}, {{metro_manila_lgu}}, {{metro_manila_postcode}} Metro Manila',
    )
    luzon_province_address_formats = (
        '{{street_address}}, {{province_lgu}}, {{luzon_province_postcode}} {{luzon_province}}',
    )
    visayas_province_address_formats = (
        '{{street_address}}, {{province_lgu}}, {{visayas_province_postcode}} {{visayas_province}}',
    )
    mindanao_province_address_formats = (
        '{{street_address}}, {{province_lgu}}, {{mindanao_province_postcode}} {{mindanao_province}}',
    )
    address_formats = OrderedDict([
        (metro_manila_address_formats, 0.127524),
        (luzon_province_address_formats, 0.485317),
        (visayas_province_address_formats, 0.148142),
        (mindanao_province_address_formats, 0.239017),
    ])

    def _ordinal_string(self, num):
        if isinstance(num, str):
            num = int(num)
        suffix = ['th', 'st', 'nd', 'rd', 'th'][min(num % 10, 4)]
        if 11 <= num % 100 <= 13:
            suffix = 'th'
        return str(num) + suffix

    def _create_postcode(self, postcodes):
        return '{postcode:04d}'.format(postcode=self.random_element(postcodes))

    def _create_address(self, address_formats):
        return self.generator.parse(self.random_element(address_formats))

    def metro_manila_postcode(self):
        return self._create_postcode(self.metro_manila_postcodes)

    def luzon_province_postcode(self):
        return self._create_postcode(self.luzon_province_postcodes)

    def visayas_province_postcode(self):
        return self._create_postcode(self.visayas_province_postcodes)

    def mindanao_province_postcode(self):
        return self._create_postcode(self.mindanao_province_postcodes)

    def postcode(self):
        return self._create_postcode(self.postcodes)

    def luzon_province(self):
        return self.random_element(self.luzon_provinces)

    def visayas_province(self):
        return self.random_element(self.visayas_provinces)

    def mindanao_province(self):
        return self.random_element(self.mindanao_provinces)

    def province(self):
        return self.random_element(self.provinces)

    def standalone_building_number(self):
        return str(self.random_int(min=1))

    def partitioned_building_number(self):
        pattern = self.lexify(
            self.random_element(self.partitioned_building_number_formats), letters=ascii_uppercase[:10],
        )
        return self.generator.parse(pattern)

    def building_number(self):
        if self.random_int() % 2 == 0:
            return self.standalone_building_number()
        else:
            return self.partitioned_building_number()

    def ordinal_street_number(self):
        return self._ordinal_string(self.random_int(1, 99))

    def floor_number(self):
        return self.random_element(self.floor_numbers)

    def ordinal_floor_number(self):
        return self._ordinal_string(self.floor_number())

    def floor_unit_number(self):
        return '{floor_number}{unit_number:02d}'.format(
            floor_number=self.floor_number(),
            unit_number=self.random_int(1, 40),
        )

    def building_unit_number(self):
        return self.generator.parse(self.random_element(self.building_unit_number_formats))

    def building_name(self):
        return self.generator.parse(self.random_element(self.building_name_formats))

    def building_name_suffix(self):
        return self.numerify(self.random_element(self.building_name_suffixes))

    def subdivision_block_number(self):
        return '{block_number:02d}'.format(block_number=self.random_int(1, 25))

    def subdivision_lot_number(self):
        return '{lot_number:02d}'.format(lot_number=self.random_int(1, 99))

    def subdivision_unit_number(self):
        return self.generator.parse(self.random_element(self.subdivision_unit_number_formats))

    def subdivision_name(self):
        return self.generator.parse(self.random_element(self.subdivision_name_formats))

    def subdivision_name_suffix(self):
        return self.numerify(self.random_element(self.subdivision_name_suffixes))

    def metro_manila_lgu(self):
        return self.random_element(self.metro_manila_lgus)

    def province_lgu(self):
        return self.random_element(self.province_lgus)

    def metro_manila_address(self):
        return self._create_address(self.metro_manila_address_formats)

    def luzon_province_address(self):
        return self._create_address(self.luzon_province_address_formats)

    def visayas_province_address(self):
        return self._create_address(self.visayas_province_address_formats)

    def mindanao_province_address(self):
        return self._create_address(self.mindanao_province_address_formats)

    def address(self):
        return self._create_address(self.random_element(self.address_formats))
