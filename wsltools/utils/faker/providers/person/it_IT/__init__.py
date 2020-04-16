# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

from .. import Provider as PersonProvider


class Provider(PersonProvider):

    formats_male = (
        '{{first_name_male}} {{last_name}}',
        '{{first_name_male}} {{last_name}}',
        '{{first_name_male}} {{last_name}}',
        '{{first_name_male}} {{last_name}}',
        '{{first_name_male}} {{last_name}}-{{last_name}}',
        '{{prefix_male}} {{first_name_male}} {{last_name}}',
        '{{first_name_male}} {{last_name}} {{suffix_male}}',
        '{{prefix_male}} {{first_name_male}} {{last_name}} {{suffix_male}}',
    )

    formats_female = (
        '{{first_name_female}} {{last_name}}',
        '{{first_name_female}} {{last_name}}',
        '{{first_name_female}} {{last_name}}',
        '{{first_name_female}} {{last_name}}',
        '{{first_name_female}} {{last_name}}-{{last_name}}',
        '{{prefix_female}} {{first_name_female}} {{last_name}}',
        '{{first_name_female}} {{last_name}} {{suffix_female}}',
        '{{prefix_female}} {{first_name_female}} {{last_name}} {{suffix_female}}',
    )

    formats = formats_male + formats_female

    # source: https://en.wikipedia.org/w/index.php?title=Category:Italian_masculine_given_names
    first_names_male = (
        'Achille', 'Adamo', 'Adelmo', 'Adriano', 'Agnolo', 'Agostino',
        'Alberico', 'Alberto', 'Alderano', 'Aldo', 'Alessandro', 'Alessio', 'Alfio',
        'Alfredo', 'Alphons', 'Amadeo', 'Amedeo', 'Amico', 'Amleto', 'Angelo', 'Annibale',
        'Ansaldo', 'Antonello', 'Antonino', 'Antonio', 'Armando', 'Arnaldo', 'Arnulfo',
        'Arsenio', 'Arturo', 'Atenulf', 'Augusto', 'Azeglio', 'Baccio', 'Baldassare',
        'Bartolomeo', 'Benedetto', 'Benito', 'Benvenuto', 'Beppe', 'Bernardo', 'Biagio',
        'Bruno', 'Calcedonio', 'Calogero', 'Camillo', 'Carlo', 'Carmelo', 'Cesare',
        'Cipriano', 'Cirillo', 'Ciro', 'Claudio', 'Coluccio', 'Coriolano', 'Corrado',
        'Costantino', 'Costanzo', 'Damiano', 'Daniele', 'Danilo', 'Dante', 'Dario', 'Delfino',
        'Dino', 'Dionigi', 'Domenico', 'Donatello', 'Donato', 'Durante', 'Edoardo',
        'Elladio', 'Elmo', 'Emilio', 'Ennio', 'Enrico', 'Enzio', 'Enzo', 'Eraldo',
        'Ermanno', 'Ermenegildo', 'Ermes', 'Ernesto', 'Ettore', 'Ezio', 'Fabio', 'Fabrizio',
        'Fausto', 'Fedele', 'Federico', 'Federigo', 'Ferdinando', 'Filippo', 'Fiorenzo',
        'Fiorino', 'Flavio', 'Francesco', 'Franco', 'Fredo', 'Fulvio', 'Gabriele',
        'Gaetano', 'Galasso', 'Gaspare', 'Gastone', 'Geronimo', 'Giacinto', 'Giacobbe',
        'Giacomo', 'Giampaolo', 'Giampiero', 'Gian', 'Giancarlo', 'Gianfrancesco',
        'Gianfranco', 'Gianluca', 'Gianluigi', 'Gianmarco', 'Gianni', 'Gianpaolo',
        'Gianpietro', 'Gilberto', 'Gino', 'Gioacchino', 'Gioachino', 'Gioele', 'Gioffre',
        'Gionata', 'Giorgio', 'Giosuè', 'Giovanni', 'Girolamo', 'Giuliano', 'Giulio',
        'Giuseppe', 'Giustino', 'Goffredo', 'Graziano', 'Greco', 'Guarino', 'Guglielmo',
        'Guido', 'Gustavo', 'Hugo', 'Ignazio', 'Ippazio', 'Ivan', 'Ivo', 'Jacopo',
        'Lamberto', 'Lando', 'Laureano', 'Lazzaro', 'Leonardo', 'Leone', 'Leopoldo',
        'Liberto', 'Livio', 'Lodovico', 'Lorenzo', 'Luca', 'Luchino', 'Luciano', 'Lucio',
        'Ludovico', 'Luigi', 'Manuel', 'Marcantonio', 'Marcello', 'Marco', 'Mariano',
        'Mario', 'Martino', 'Martino', 'Massimiliano', 'Massimo', 'Matteo', 'Mattia',
        'Maurilio', 'Maurizio', 'Mauro', 'Michelangelo', 'Michele', 'Micheletto',
        'Michelotto', 'Milo', 'Mirco', 'Mirko', 'Nanni', 'Napoleone', 'Niccolò', 'Nico',
        'Nicola', 'Nicolò', 'Nino', 'Orazio', 'Oreste', 'Orlando', 'Osvaldo', 'Ottavio',
        'Ottone', 'Panfilo', 'Paolo', 'Paride', 'Pasqual', 'Pasquale', 'Patrizio',
        'Pellegrino', 'Pier', 'Pierangelo', 'Piergiorgio', 'Piergiuseppe', 'Pierluigi',
        'Piermaria', 'Piero', 'Pierpaolo', 'Piersanti', 'Pietro', 'Pompeo', 'Pomponio',
        'Puccio', 'Raffaele', 'Raffaellino', 'Raffaello', 'Raimondo', 'Ranieri',
        'Rembrandt', 'Renzo', 'Riccardo', 'Ricciotti', 'Roberto', 'Rocco', 'Rodolfo',
        'Rolando', 'Roman', 'Romeo', 'Romolo', 'Ronaldo', 'Rosario', 'Ruggero', 'Ruggiero',
        'Sabatino', 'Salvatore', 'Salvi', 'Sandro', 'Sante', 'Santino', 'Saverio',
        'Sebastiano', 'Sergius', 'Severino', 'Silvestro', 'Silvio', 'Simone', 'Stefano',
        'Telemaco', 'Temistocle', 'Tiziano', 'Toni', 'Tonino', 'Torquato', 'Tullio',
        'Ubaldo', 'Uberto', 'Ugo', 'Ugolino', 'Umberto', 'Valerio', 'Venancio',
        'Vincentio', 'Vincenzo', 'Virgilio', 'Vito', 'Vittorio',
    )
    # source: https://en.wikipedia.org/wiki/Category:Italian_feminine_given_names
    first_names_female = (
        'Adelasia', 'Adele', 'Adriana', 'Alessandra', 'Alessia',
        'Alina', 'Allegra', 'Amalia', 'Amanda', 'Angelica', 'Angelina', 'Anita',
        'Annalisa', 'Annamaria', 'Annetta', 'Annunziata', 'Antonella', 'Antonia',
        'Antonietta', 'Antonina', 'Aria', 'Aurora', 'Barbara', 'Beatrice', 'Berenice',
        'Bettina', 'Bianca', 'Bianca', 'Camilla', 'Carla', 'Carolina', 'Cassandra',
        'Caterina', 'Cecilia', 'Chiara', 'Claudia', 'Clelia', 'Concetta', 'Cristina',
        'Daria', 'Diana', 'Dina', 'Dolores', 'Donatella', 'Donna', 'Eleanora', 'Elena',
        'Eliana', 'Elisa', 'Elvira', 'Emma', 'Erika', 'Etta', 'Eugenia', 'Eva',
        'Evangelista', 'Fabia', 'Fabrizia', 'Federica', 'Fernanda', 'Fiamma', 'Filippa',
        'Flavia', 'Flora', 'Fortunata', 'Francesca', 'Gabriella', 'Gelsomina', 'Gemma',
        'Germana', 'Giada', 'Gianna', 'Giorgia', 'Giovanna', 'Giulia', 'Giuliana',
        'Giulietta', 'Giuseppina', 'Gloria', 'Graziella', 'Greca', 'Griselda', 'Ida',
        'Ilaria', 'Imelda', 'Iolanda', 'Irma', 'Isa', 'Isabella', 'Jolanda', 'Lara',
        'Laura', 'Lauretta', 'Letizia', 'Liana', 'Licia', 'Lidia', 'Liliana', 'Lilla',
        'Lina', 'Lisa', 'Livia', 'Lolita', 'Loredana', 'Loretta', 'Lucia', 'Luciana',
        'Lucrezia', 'Ludovica', 'Luigina', 'Luisa', 'Marcella', 'Margherita', 'Maria',
        'Maria', 'Maria', 'Mariana', 'Marina', 'Marisa', 'Marissa', 'Marta', 'Martina',
        'Matilda', 'Maura', 'Melania', 'Melina', 'Melissa', 'Mercedes', 'Michela', 'Milena',
        'Monica', 'Morena', 'Nadia', 'Natalia', 'Nedda', 'Nicoletta', 'Nina', 'Ninetta',
        'Olga', 'Ornella', 'Paloma', 'Paola', 'Paoletta', 'Patrizia', 'Paulina',
        'Pierina', 'Pina', 'Priscilla', 'Raffaella', 'Ramona', 'Renata', 'Rita', 'Roberta',
        'Romana', 'Romina', 'Rosa', 'Rosalia', 'Rosaria', 'Rosina', 'Rossana', 'Sandra',
        'Serafina', 'Serena', 'Silvia', 'Simonetta', 'Sole', 'Sonia', 'Sophia', 'Stefani',
        'Stefania', 'Stella', 'Susanna', 'Sylvia', 'Tatiana', 'Teresa', 'Tina', 'Tiziana',
        'Tonia', 'Valentina', 'Valeria', 'Vanessa', 'Veronica', 'Victoria',
        'Vincenza', 'Virginia', 'Viridiana', 'Vittoria', 'Zaira',
    )

    first_names = first_names_male + first_names_female

    # source: https://en.wiktionary.org/w/index.php?title=Category:Italian_surnames
    last_names = (
        'Abatantuono', 'Abate', 'Abba', 'Abbagnale', 'Accardo', 'Acerbi',
        'Adinolfi', 'Agazzi', 'Agnesi', 'Agostinelli', 'Agostini', 'Ajello',
        'Albertini', 'Alboni', 'Aldobrandi', 'Alfieri', 'Alfonsi', 'Alighieri', 'Almagià',
        'Aloisio', 'Alonzi', 'Altera', 'Amaldi', 'Amato', 'Ammaniti', 'Anastasi',
        'Andreotti', 'Andreozzi', 'Angeli', 'Angiolello', 'Anguillara', 'Anguissola',
        'Anichini', 'Antelami', 'Antonacci', 'Antonelli', 'Antonello', 'Antonetti',
        'Antonini', 'Antonioni', 'Antonucci', 'Aporti', 'Argan', 'Argentero', 'Argenti',
        'Argento', 'Argurio', 'Ariasso', 'Ariosto', 'Armani', 'Armellini', 'Asmundo',
        'Asprucci', 'Aulenti', 'Avogadro', 'Babati', 'Babato', 'Babbo', 'Bacosi', 'Badoer',
        'Badoglio', 'Baggio', 'Baglioni', 'Bajamonti', 'Bajardi', 'Balbi', 'Balbo', 'Balla',
        'Balotelli', 'Bandello', 'Baracca', 'Barbarigo', 'Barberini', 'Barcaccia', 'Barcella',
        'Barese', 'Baresi', 'Barillaro', 'Baroffio', 'Barozzi', 'Barracco', 'Barsanti',
        'Bartoli', 'Barzini', 'Basadonna', 'Bassi', 'Basso', 'Bataglia', 'Battaglia',
        'Battelli', 'Battisti', 'Bazzi', 'Beccaria', 'Beccheria', 'Beffa', 'Belletini',
        'Bellini', 'Bellocchio', 'Bellucci', 'Bellò', 'Bembo', 'Benedetti', 'Benigni',
        'Benussi', 'Berengario', 'Bergoglio', 'Berlusconi', 'Bernardi', 'Bernardini',
        'Bernetti', 'Bernini', 'Berrè', 'Bersani', 'Bertoli', 'Bertolucci', 'Bertoni',
        'Bettin', 'Bettoni', 'Bevilacqua', 'Biagi', 'Biagiotti', 'Bianchi', 'Bianchini',
        'Bignami', 'Bignardi', 'Binaghi', 'Bixio', 'Blasi', 'Boaga', 'Bocca', 'Boccaccio',
        'Boccherini', 'Boccioni', 'Bocelli', 'Bodoni', 'Boezio', 'Boiardo', 'Boitani', 'Boito',
        'Boldù', 'Bombieri', 'Bompiani', 'Bonanno', 'Bonatti', 'Bonaventura', 'Bondumier',
        'Bongiorno', 'Bonino', 'Bonolis', 'Bonomo', 'Borghese', 'Borgia', 'Borrani',
        'Borromeo', 'Borromini', 'Borroni', 'Borsellino', 'Borsiere', 'Borzomì', 'Bosio',
        'Bossi', 'Bosurgi', 'Botta', 'Bottaro', 'Botticelli', 'Bottigliero', 'Bova',
        'Bragadin', 'Bragaglia', 'Bramante', 'Brambilla', 'Brancaccio', 'Branciforte',
        'Brenna', 'Bresciani', 'Briccialdi', 'Brichese', 'Broggini', 'Broschi', 'Brugnaro',
        'Brunelleschi', 'Brunello', 'Bruno', 'Bruscantini', 'Bulzoni', 'Buonauro', 'Burcardo',
        'Buscetta', 'Busoni', 'Cabibbo', 'Caboto', 'Cabrini', 'Caccianemico', 'Caccioppoli',
        'Cadorna', 'Caetani', 'Cafarchia', 'Caffarelli', 'Cagnin', 'Cagnotto', 'Cainero',
        'Caironi', 'Calarco', 'Calbo', 'Calgari', 'Callegari', 'Callegaro', 'Calvo',
        'Camanni', 'Camicione', 'Camilleri', 'Camiscione', 'Cammarata', 'Campanella',
        'Campano', 'Campise', 'Camuccini', 'Canali', 'Canetta', 'Canevascini', 'Canil',
        'Cannizzaro', 'Canova', 'Cantimori', 'Capecchi', 'Capone', 'Cappelli', 'Capuana',
        'Caracciolo', 'Cardano', 'Carducci', 'Carfagna', 'Carli', 'Carnera', 'Carocci',
        'Carosone', 'Carpaccio', 'Carriera', 'Carullo', 'Caruso', 'Casadei', 'Casagrande',
        'Casale', 'Casaleggio', 'Casalodi', 'Casarin', 'Casellati', 'Casini', 'Cassarà',
        'Castelli', 'Castellitto', 'Castiglione', 'Castioni', 'Catalano', 'Catenazzi',
        'Cattaneo', 'Cavalcanti', 'Cavanna', 'Ceci', 'Celentano', 'Cendron', 'Ceravolo',
        'Ceri', 'Cerquiglini', 'Cerutti', 'Cesaroni', 'Cesarotti', 'Ceschi', 'Chechi',
        'Cheda', 'Cherubini', 'Chiappetta', 'Chiaramonte', 'Chiesa', 'Chigi', 'Chindamo',
        'Chinnici', 'Chittolini', 'Ciampi', 'Cianciolo', 'Ciani', 'Cibin', 'Cicala',
        'Cicilia', 'Cignaroli', 'Cilea', 'Cilibrasi', 'Cimarosa', 'Cimini', 'Cipolla',
        'Civaschi', 'Coardi', 'Cocci', 'Cociarelli', 'Colletti', 'Collina', 'Collodi',
        'Columbo', 'Combi', 'Comboni', 'Comencini', 'Comeriato', 'Comisso', 'Comolli',
        'Condoleo', 'Contarini', 'Conte', 'Conti', 'Contrafatto', 'Coppola', 'Corbo',
        'Corcos', 'Corradi', 'Correr', 'Cortese', 'Cossiga', 'Costalonga', 'Costanzi',
        'Cremonesi', 'Crespi', 'Crisafulli', 'Crispi', 'Cristoforetti', 'Cuda', 'Cugia',
        'Cundari', 'Cuomo', 'Curatoli', 'Curci', 'Curiel', 'Cusano', 'Cutrufo', 'Cutuli',
        'Cuzzocrea', 'Dalla', 'Dallapé', 'Dallara', 'Dandolo', 'Deledda', 'Delle', 'Dellucci',
        'Depero', 'Desio', 'Detti', 'Dibiasi', 'Disdero', 'Doglioni', 'Donarelli',
        'Donati', 'Donatoni', 'Donini', 'Donà', 'Doria', 'Dossetti', 'Dossi', 'Dovara',
        'Draghi', 'Druso', 'Dulbecco', 'Duodo', 'Durante', 'Duse', 'Eco',
        'Einaudi', 'Emanuelli', 'Emo', 'Endrizzi', 'Errani', 'Errigo', 'Esposito', 'Fabbri',
        'Fabrizi', 'Faggiani', 'Fagiani', 'Fagotto', 'Falcone', 'Falier', 'Fallaci',
        'Falloppio', 'Fantini', 'Fantoni', 'Fantozzi', 'Fanucci', 'Faranda', 'Farina',
        'Farinelli', 'Farnese', 'Fattori', 'Faugno', 'Favata', 'Federici', 'Federico',
        'Fermi', 'Ferrabosco', 'Ferragamo', 'Ferragni', 'Ferrante', 'Ferrara', 'Ferrari',
        'Ferraris', 'Ferrata', 'Ferrazzi', 'Ferretti', 'Ferrucci', 'Fibonacci', 'Ficino',
        'Fieramosca', 'Filangieri', 'Filippelli', 'Filippini', 'Filogamo', 'Filzi', 'Finetti',
        'Finotto', 'Finzi', 'Fioravanti', 'Fiorucci', 'Fischetti', 'Fittipaldi', 'Flaiano',
        'Florio', 'Fo', 'Foa', 'Foconi', 'Fogazzaro', 'Foletti', 'Folliero',
        'Fornaciari', 'Forza', 'Foscari', 'Foà', 'Fracci', 'Franceschi', 'Franscini',
        'Franzese', 'Frescobaldi', 'Fusani', 'Fuseli', 'Gabba', 'Gabbana', 'Gabrieli',
        'Gadda', 'Gaggini', 'Gagliano', 'Gagliardi', 'Gaiatto', 'Gaito', 'Galeati',
        'Galiazzo', 'Galilei', 'Galtarossa', 'Galuppi', 'Galvani', 'Gangemi', 'Gargallo',
        'Garibaldi', 'Garobbio', 'Garozzo', 'Garrone', 'Garzoni', 'Gasperi', 'Gatto', 'Gelli',
        'Gemito', 'Gentileschi', 'Gentili', 'Gentilini', 'Geraci', 'Germano', 'Giacconi',
        'Giacometti', 'Giammusso', 'Gianetti', 'Gianinazzi', 'Giannelli', 'Giannetti',
        'Giannini', 'Giannone', 'Giannotti', 'Giannuzzi', 'Gianvecchio', 'Gibilisco',
        'Gigli', 'Gilardoni', 'Ginese', 'Ginesio', 'Gioberti', 'Giolitti', 'Giorgetti',
        'Giovine', 'Giradello', 'Giulietti', 'Giunti', 'Giusti', 'Goldoni', 'Goldstein',
        'Golgi', 'Golino', 'Gonzaga', 'Gori', 'Gottardi', 'Gotti', 'Govoni', 'Gozzano',
        'Gozzi', 'Gradenigo', 'Gramsci', 'Granatelli', 'Grassi', 'Grasso', 'Gravina',
        'Greco', 'Greggio', 'Gregori', 'Gregorio', 'Gremese', 'Grifeo', 'Grimani',
        'Grisoni', 'Gritti', 'Grossi', 'Gualandi', 'Gualtieri', 'Guarana', 'Guarato',
        'Guariento', 'Guarneri', 'Gucci', 'Guglielmi', 'Guicciardini', 'Guidone', 'Guidotti',
        'Guinizzelli', 'Gullotta', 'Gulotta', 'Gussoni', 'Iacobucci', 'Iacovelli', 'Iadanza',
        'Iannelli', 'Iannotti', 'Iannucci', 'Iannuzzi', 'Impastato', 'Infantino',
        'Innocenti', 'Interiano', 'Interminei', 'Interminelli', 'Inzaghi', 'Ioppi', 'Jacuzzi',
        'Jilani', 'Jovinelli', 'Juvara', 'Lamborghini', 'Lancisi',
        'Lanfranchi', 'Lattuada', 'Leblanc', 'Legnante', 'Leonardi', 'Leoncavallo', 'Leone',
        'Leonetti', 'Leopardi', 'Lercari', 'Lerner', 'Letta', 'Lettiere', 'Ligorio',
        'Liguori', 'Lippomano', 'Littizzetto', 'Liverotti', 'Lollobrigida',
        'Lombardi', 'Lombardo', 'Lombroso', 'Longhena', 'Lopresti', 'Loredan', 'Lovato',
        'Lucarelli', 'Lucchesi', 'Lucciano', 'Luciani', 'Ludovisi', 'Luna', 'Lupo', 'Luria',
        'Lussu', 'Luxardo', 'Luzi', 'Maccanelli', 'Maderna', 'Maderno', 'Maffei',
        'Maggioli', 'Maglio', 'Magnani', 'Magrassi', 'Majewski', 'Majorana', 'Malacarne',
        'Malaparte', 'Malatesta', 'Malenchini', 'Malipiero', 'Malpighi', 'Manacorda',
        'Mancini', 'Mannoia', 'Manolesso', 'Mantegazza', 'Mantegna', 'Manunta', 'Manzoni',
        'Marangoni', 'Marazzi', 'Marcacci', 'Marconi', 'Marenzio', 'Marinetti', 'Marini',
        'Marino', 'Marrone', 'Marsili', 'Martinelli', 'Martucci', 'Marzorati', 'Mascagni',
        'Mascheroni', 'Maspero', 'Mastandrea', 'Mastroianni', 'Mattarella', 'Matteotti',
        'Mazzacurati', 'Mazzanti', 'Mazzeo', 'Mazzi', 'Mazzini', 'Mazzocchi', 'Medici',
        'Mengolo', 'Mennea', 'Mercadante', 'Mercalli', 'Mercantini', 'Mercati', 'Merisi',
        'Metella', 'Meucci', 'Mezzetta', 'Micca', 'Michelangeli', 'Micheletti',
        'Migliaccio', 'Milanesi', 'Mimun', 'Miniati', 'Missoni', 'Moccia', 'Mocenigo',
        'Modiano', 'Modigliani', 'Modugno', 'Mogherini', 'Molesini', 'Monaco', 'Mondadori',
        'Mondaini', 'Monduzzi', 'Moneta', 'Monicelli', 'Montalcini', 'Montalti', 'Montanari',
        'Montanariello', 'Montanelli', 'Monte', 'Montecchi', 'Montesano', 'Montessori',
        'Monteverdi', 'Monti', 'Morabito', 'Morandi', 'Morandini', 'Morellato', 'Moresi',
        'Moretti', 'Morgagni', 'Morlacchi', 'Morosini', 'Morpurgo', 'Morricone', 'Morrocco',
        'Mortati', 'Morucci', 'Moschino', 'Mozart', 'Munari', 'Muratori', 'Murialdo',
        'Murri', 'Musatti', 'Mussolini', 'Muti', 'Naccari', 'Nadi', 'Napolitano', 'Natta',
        'Navarria', 'Navone', 'Necci', 'Nibali', 'Nicoletti', 'Nicolini', 'Nicolucci',
        'Nievo', 'Niggli', 'Niscoromni', 'Nitti', 'Nitto', 'Nolcini', 'Nonis', 'Norbiato',
        'Nordio', 'Nosiglia', 'Notarbartolo', 'Novaro', 'Nugnes', 'Odescalchi', 'Offredi',
        'Oliboni', 'Olivetti', 'Omma', 'Onio', 'Onisto', 'Opizzi', 'Orengo', 'Orlando',
        'Orsini', 'Ortese', 'Ortolani', 'Oscuro', 'Ossani', 'Ossola', 'Ostinelli',
        'Ottino', 'Ovadia', 'Pace', 'Pacelli', 'Pacetti', 'Pacillo', 'Pacomio', 'Padovano',
        'Paganini', 'Pagliaro', 'Pagnotto', 'Palazzo', 'Palladio', 'Palmisano', 'Palombi',
        'Paltrinieri', 'Palumbo', 'Panatta', 'Panicucci', 'Panzera', 'Paoletti', 'Paolini',
        'Paolucci', 'Papafava', 'Papetti', 'Pareto', 'Parini', 'Parisi', 'Parmitano',
        'Parpinel', 'Parri', 'Paruta', 'Pascarella', 'Pasolini', 'Pasqua', 'Passalacqua',
        'Pastine', 'Pausini', 'Pavanello', 'Pavarotti', 'Pavone', 'Peano', 'Pederiva',
        'Pedersoli', 'Pedrazzini', 'Pedroni', 'Pellegrini', 'Pelli', 'Pellico', 'Pennetta',
        'Pepe', 'Peranda', 'Pergolesi', 'Perini', 'Perozzo', 'Persico', 'Pertile',
        'Pertini', 'Peruzzi', 'Petralli', 'Petrassi', 'Petrocelli', 'Petrucci',
        'Petrucelli', 'Petruzzi', 'Pezzali', 'Piacentini', 'Piane', 'Piazzi', 'Piccinni',
        'Piccio', 'Pietrangeli', 'Pigafetta', 'Pignatti', 'Pinamonte', 'Pincherle',
        'Pininfarina', 'Piovani', 'Pirandello', 'Pirelli', 'Pisacane', 'Pisani',
        'Pisano', 'Pisaroni', 'Pistoletto', 'Pizzamano', 'Pizzetti', 'Pizziol', 'Pizzo',
        'Platini', 'Poerio', 'Polani', 'Polesel', 'Polizzi', 'Pometta', 'Pontecorvo',
        'Ponti', 'Porcellato', 'Porzio', 'Pozzecco', 'Prada', 'Praga', 'Pratesi', 'Prati',
        'Priuli', 'Procacci', 'Prodi', 'Proietti', 'Pucci', 'Puccini', 'Pugliese',
        'Puglisi', 'Pulci', 'Quasimodo', 'Querini', 'Raimondi', 'Ramazzotti', 'Randazzo',
        'Rapisardi', 'Rastelli', 'Raurica', 'Ravaglioli', 'Redi', 'Regge', 'Renault',
        'Renier', 'Rensi', 'Renzi', 'Respighi', 'Riccardi', 'Riccati', 'Ricci',
        'Ricciardi', 'Ricolfi', 'Rienzo', 'Righi', 'Rinaldi', 'Rismondo', 'Ritacca', 'Rizzo',
        'Rizzoli', 'Rocca', 'Roccabonella', 'Roero', 'Romagnoli', 'Romano', 'Romiti',
        'Roncalli', 'Rosiello', 'Rosmini', 'Rosselli', 'Rossellini', 'Rossetti', 'Rossi',
        'Rossini', 'Roth', 'Rubbia', 'Ruberto', 'Ruffini', 'Ruggeri', 'Ruggieri', 'Russo',
        'Rusticucci', 'Sabatini', 'Sabbatini', 'Saffi', 'Sagese', 'Sagnelli', 'Sagredo',
        'Salandra', 'Salata', 'Salgari', 'Salieri', 'Salvemini', 'Salvini', 'Salvo',
        'Samele', 'Sandi', 'Sanguineti', 'Sansoni', 'Santi', 'Santorio', 'Santoro',
        'Sanudo', 'Saraceno', 'Saracino', 'Saragat', 'Satriani', 'Satta', 'Sauli', 'Sauro',
        'Savorgnan', 'Sbarbaro', 'Scaduto', 'Scalera', 'Scalfaro', 'Scamarcio', 'Scandone',
        'Scaramucci', 'Scarfoglio', 'Scarlatti', 'Scarpa', 'Scarpetta', 'Scarponi',
        'Schiaparelli', 'Schiavo', 'Schiavone', 'Schicchi', 'Scialpi', 'Scotti', 'Scotto',
        'Seddio', 'Segni', 'Segrè', 'Semitecolo', 'Serao', 'Serlupi', 'Sermonti',
        'Serraglio', 'Sforza', 'Sgalambro', 'Sgarbi', 'Sibilia', 'Siffredi', 'Silvestri',
        'Simeoni', 'Sinisi', 'Sismondi', 'Smirnoff', 'Sobrero', 'Soderini', 'Soffici',
        'Sokolov', 'Solari', 'Solimena', 'Sollima', 'Sommaruga', 'Sonnino', 'Soprano',
        'Soranzo', 'Sordi', 'Sorrentino', 'Spadafora', 'Spallanzani', 'Spanevello', 'Speri',
        'Spinelli', 'Spinola', 'Squarcione', 'Sraffa', 'Staglieno', 'Stefanelli', 'Stein',
        'Stoppani', 'Storladi', 'Stradivari', 'Strangio', 'Stucchi', 'Surian', 'T',
        'Tacchini', 'Taccola', 'Tafuri', 'Tagliafierro', 'Taliani', 'Taliercio', 'Tamborini',
        'Tamburello', 'Tamburi', 'Tamburini', 'Tanzini', 'Tarantini', 'Tarantino', 'Tarchetti',
        'Tartaglia', 'Tartini', 'Tasca', 'Tasso', 'Tassoni', 'Tebaldi', 'Tedesco', 'Telesio',
        'Tencalla', 'Terragni', 'Tiepolo', 'Tirabassi', 'Togliatti', 'Tognazzi', 'Toldo',
        'Tolentino', 'Tomaselli', 'Tomasetti', 'Tomasini', 'Tomei', 'Tommaseo', 'Toninelli',
        'Tonisto', 'Torlonia', 'Tornatore', 'Torricelli', 'Toscani', 'Toscanini', 'Toselli',
        'Tosi', 'Toso', 'Tosto', 'Totino', 'Tozzi', 'Tozzo', 'Traetta', 'Trapanese',
        'Trapani', 'Travaglia', 'Travaglio', 'Traversa', 'Travia', 'Trebbi', 'Treccani',
        'Tremonti', 'Trentin', 'Trentini', 'Tresoldi', 'Treves', 'Trevisan', 'Trevisani',
        'Trezzini', 'Trillini', 'Trincavelli', 'Trobbiani', 'Troisi', 'Trombetta', 'Tron',
        'Tropea', 'Trotta', 'Trupiano', 'Trussardi', 'Turati', 'Turchetta', 'Turchi',
        'Turci', 'Turrini', 'Tutino', 'Tuzzolino', 'Ubaldi', 'Udinese', 'Udinesi', 'Ughi',
        'Ungaretti', 'Valentino', 'Valguarnera', 'Valier', 'Valmarana', 'Vanvitelli',
        'Varano', 'Vasari', 'Vattimo', 'Vecellio', 'Vecoli', 'Veltroni', 'Vendetti',
        'Venditti', 'Veneziano', 'Venier', 'Vento', 'Venturi', 'Vercelloni', 'Verdi',
        'Verdone', 'Verga', 'Vergassola', 'Vergerio', 'Verri', 'Versace', 'Vespa',
        'Vespucci', 'Vezzali', 'Vianello', 'Vidoni', 'Vigliotti', 'Vigorelli', 'Villadicani',
        'Villarosa', 'Viola', 'Virgilio', 'Visconti', 'Visintini', 'Vismara', 'Vittadello',
        'Vitturi', 'Vivaldi', 'Viviani', 'Volta', 'Volterra', 'Zabarella', 'Zaccagnini',
        'Zaccardo', 'Zacchia', 'Zacco', 'Zaguri', 'Zamengo', 'Zamorani', 'Zampa', 'Zanazzo',
        'Zanichelli', 'Zanzi', 'Zarlino', 'Zecchini', 'Zeffirelli', 'Zetticci', 'Ziani',
        'Zichichi', 'Zito', 'Zola', 'Zoppetti', 'Zoppetto',
        )

    prefixes_female = ('Dott.', 'Sig.ra')
    prefixes_male = ('Dott.', 'Sig.')

    prefixes = ('Dott.', 'Sig.', 'Sig.ra')
