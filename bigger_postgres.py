#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import psycopg2
import datetime
from random import randint
from faker import Faker
fake = Faker('es_ES')

# DATABASES
# Poblaciones
poblacions1 = ('Barcelona','Hospitalet de Llobregat','Badalona','Tarrasa','Sabadell','Lérida','Tarragona','Mataró','Santa Coloma de Gramanet','Reus','Gerona','San Cugat del Vallés','Cornellá de Llobregat','San Baudilio de Llobregat','Manresa','Rubí','Villanueva y Geltrú','Viladecans','Casteldefels','El Prat de Llobregat','Granollers','Sardañola del Vallés','Mollet del Vallés','Gavá','Esplugas de Llobregat','Figueras','San Felíu de Llobregat','Vich','Villafranca del Panadés','Blanes','Igualada','Lloret de Mar','Ripollet','Vendrell','San Adrián de Besós','Moncada y Reixach','Olot','Tortosa','San Juan Despí','Cambrils','Barberá del Vallés','San Pedro de Ribas','Salt','Sitges','San Vicente dels Horts','Premiá de Mar','Martorell','San Andrés de la Barca','Salou','Pineda de Mar','Santa Perpetua de Moguda','Molins de Rey','Valls','Calafell','Olesa de Montserrat','Castellar del Vallés','El Masnou','Palafrugell','Vilaseca','Esparraguera','San Felíu de Guixols','Amposta','Vilasar de Mar','Manlleu','San Quirico de Tarrasa','Rosas','Las Franquesas del Vallés','Bañolas','Parets del Vallés','Malgrat de Mar','Calella','Cardedeu','Palamós','San Celoni','Caldas de Montbui','Balaguer','San Justo Desvern','Tárrega','Tordera','Berga','Montornés del Vallés','Canovellas','La Garriga','Torredembarra','Arenys de Mar','Piera','Mollerusa','San Carlos de la Rápita','Llissá de Munt','Vallirana','Palau de Plegamans','Cubellas','Corbera de Llobregat','Canet de Mar','Torelló','Badia del Vallés','La Llagosta','San Sadurní de Noya','Santa Coloma de Farnés','Vilanova del Camí','Castellbisbal','Seo de Urgel','Abrera','Argentona','Cunit','Montroig','Deltebre','Montgat','Torroella de Montgrí','Pallejá','Castellón de Ampurias','San Juan de Torruella','La Bisbal del Ampurdán','Ripoll','Castillo de Aro','Calonge','La Roca del Vallés','San Andrés de Llavaneras','Premiá de Dalt','La Escala','Cassá de la Selva','Alella','Santa Margarita de Mombuy','Alcanar','Llinás del Vallés','Alcarrás','San Vicente de Castellet','Palafolls','Santa María de Palautordera','Solsona','Vilasar de Dalt','Cervera','Matadepera','Bigas','Cervelló','Montmeló','Puigcerdá','Arenys de Munt','Senmanat','San Fausto de Campcentellas','Tiana','San Fructuoso de Bages','Masquefa','La Ametlla','Roquetas','Polinyá','Llagostera','Santa Coloma de Cervelló','Tona','Vidreras','San Esteban de Sasroviras','Sampedor','Centellas','Viladecaballs','Santa Margarita y Monjós','Montblanch','Gelida','Cabrils','La Ametlla de Mar','Caldas de Malavella','Santa Eulalia de Ronsana','Massanet de la Selva','Guisona','Almacellas','Begas','Sallent de Llobregat','Ulldecona','Riudoms','Constantí','Llissá de Vall','Roda de Bará','Arbucias','Alpicat','Taradell','Teyá','Tremp','Vacarisas','Roda de Ter','Navás','Vandellós y Hospitalet del Infante','San Vicente de Montalt','Borjas Blancas','Navarclés','Suria','San Felíu de Codinas','Torrellas de Llobregat','Moyá','La Canonja','Cenia','Sils','San Antonio de Vilamajor','Artés','Tosa de Mar','San Hilario Sacalm','La Selva del Campo','Vilafant','Anglés','Arbós','Agramunt','Mora de Ebro','Viella Mitg Arán','Capellades','Vilanova del Vallés','Dosrius','Celrá','Santa Cristina de Aro','Alcover','Altafulla','San Pol de Mar','Bellpuig','Llansá','Sarriá de Ter','Gironella','Cardona','Bescanó','Martorellas','Torrefarrera','Pallaresos','Cabrera de Mar','Porqueras','Collbató','Canyellas','San Pedro de Vilamajor','La Aldea','Catllar','Puigreig','El Papiol','San Clemente de Llobregat','Hostalrich','Bagur','Riells','Espluga de Francolí','Torre de Claramunt','Flix','Santa Bárbara','Breda','Rocafort y Vilumara','Balenyá','Pobla de Mafumet','Ódena','Artesa de Segre','Olivella','Castellbell y Vilar','San Jaime de Enveija','Almenar','Morell','Olérdola','San Gregorio','Creixell','Camarles','La Bisbal del Panadés','La Ampolla','Quart','Seva','San Hipólito de Voltregá','Calaf','San Julián de Ramis','Juneda','San Juan de las Abadesas','Campdevánol','San Cipriano de Vallalta','Balsareny','Alcoletge','Santa Oliva','Santa Susana','La Junquera','Mora la Nueva','Viloví de Oñar','Las Masías de Voltregá','Guardiola','San Julián de Vilatorta','Bañeras','San Martín Sarroca','Roselló','Puebla de Segur','Gandesa','Alguaire','Subirats','Alfarrás','La Palma de Cervelló','Vall de Bas','San Juan les Fonts','Perelló','Monistrol de Montserrat','Cánoves','Castellvell','Els Hostalets de Pierola','Falset','Puebla de Montornés','Santa Coloma de Queralt','Cadaqués','Vallgorguina','Caldetas','Montbrió de Tarragona','Liñola','Ponts','Prats de Llusanés','San Esteban de Palautordera','Vilablareix','San Lorenzo de Hortóns','Gurb','Vallromanes','Fornells de la Selva','San Jaime dels Domenys','Pals','Aiguafreda','Aitona','Besalú','San Pedro de Torelló','Calldetenes','San Lorenzo Savall','San Pedro de Riudevitlles','Castelltersol','Pla de Santa María','Bell Lloch','Lloréns','Albiñana','Pont de Suert','Camprodón','Folgarolas','Arbeca','Mediona','Torres de Segre','Bellvís','Torregrosa','Amer','Avinyó','Torrellas de Foix','Cornellá del Terri','Vilallonga del Campo','Aviá','Albatarrech','Castellet y Gornal','Santa Eugenia de Berga','Sort','Bagá','Bellvey','Santa María de Corcó','La Pobla de Claramunt','San Pedro Pescador','Palau de Anglesola','San Quirico de Besora','Riudarenas','San Quintín de Mediona','Borjas del Campo','La Granada','La Sellera de Ter','Ullastrell','Bruch','Bellver de Cerdaña','Callús','Riudellots de la Selva','San Vicente de Torelló','Castellgalí','Batea','Viñols y Archs','Serós','Alforja','Vallfogona de Balaguer','Oliana','Perelada','Ribas de Freser','Castellví de Rosanes','Golmés','Las Presas','Alto Arán','Tivisa','Soses','Olesa de Bonesvalls','Bordils','Montrás','Forallac','Ascó','La Riera','Las Planas','La Secuita','Avinyonet del Penedés','Vallmoll','Albesa','Alp','Ibars de Urgel','Sarral','Aviñonet de Puig Ventós','Santa Pau','Caserras','Castellví de la Marca','Termens','Artesa de Lérida','Benavent de Lérida','Palau Sabardera','Fogars de la Selva','Llivia','Fontcuberta','Vallbona','Gualba','Almoster','Puigvert de Lérida','Torrelavit','Corbíns','Fonollosa','Miralcamp','Anglesola','Montmell','Cabrera de Igualada','Fontrubí','San Feliu de Pallarols','Navata','Perafort','San Acisclo de Vallalta','Cruilles, Monells y San Sadurní','Vall de Vianya','Bellcaire d Urgell','Fuliola','Santa Eulalia de Riuprimer','Vilarrodona','Sant Julià del Llor i Bonmatí','Castellnou de Bages','Benisanet','Corsá','Torá','Pla del Panadés','Horta de San Juan','Riudecols','Serchs','Llers','Cherta','Verges','San Martín de Tous','Olost','Vilanova de Bellpuig','Ribarroja de Ebro','Vilajuïga','Portbou','Gimenells i el Pla de la Font','Riudecañas')
comarques1 = ('Barcelonés','Barcelonés','Barcelonés','Vallés Occidental','Vallés Occidental','Segriá','Tarragonés','Maresme','Barcelonés','Bajo Campo','Gironés','Vallés Occidental','Bajo Llobregat','Bajo Llobregat','Bages','Vallés Occidental','Garraf','Bajo Llobregat','Bajo Llobregat','Bajo Llobregat','Vallés Oriental','Vallés Occidental','Vallés Oriental','Bajo Llobregat','Bajo Llobregat','Alto Ampurdán','Bajo Llobregat','Osona','Alto Penedés','La Selva','Anoia','La Selva','Vallés Occidental','Bajo Penedés','Barcelonés','Vallés Occidental','La Garrocha','Bajo Ebro','Bajo Llobregat','Bajo Campo','Vallés Occidental','Garraf','Gironés','Garraf','Bajo Llobregat','Maresme','Bajo Llobregat','Bajo Llobregat','Tarragonés','Maresme','Vallés Occidental','Bajo Llobregat','Alto Campo','Bajo Penedés','Bajo Llobregat','Vallés Occidental','Maresme','Bajo Ampurdán','Tarragonés','Bajo Llobregat','Bajo Ampurdán','Montsiá','Maresme','Osona','Vallés Occidental','Alto Ampurdán','Vallés Oriental','Pla de l Estany','Vallés Oriental','Maresme','Maresme','Vallés Oriental','Bajo Ampurdán','Vallés Oriental','Vallés Oriental','Noguera','Bajo Llobregat','Urgel','Maresme','Bergadá','Vallés Oriental','Vallés Oriental','Vallés Oriental','Tarragonés','Maresme','Anoia','Plana de Urgel','Montsiá','Vallés Oriental','Bajo Llobregat','Vallés Occidental','Garraf','Bajo Llobregat','Maresme','Osona','Vallés Occidental','Vallés Oriental','Anoia','La Selva','Anoia','Vallés Occidental','Alto Urgel','Bajo Llobregat','Maresme','Bajo Penedés','Bajo Campo','Bajo Ebro','Maresme','Bajo Ampurdán','Bajo Llobregat','Alto Ampurdán','Bages','Bajo Ampurdán','Ripollés','Bajo Ampurdán','Bajo Ampurdán','Vallés Oriental','Maresme','Maresme','Alto Ampurdán','Gironés','Maresme','Anoia','Montsiá','Vallés Oriental','Segriá','Bages','Maresme','Vallés Oriental','Solsonés','Maresme','Segarra','Vallés Occidental','Vallés Oriental','Bajo Llobregat','Vallés Oriental','Baja Cerdaña','Maresme','Vallés Occidental','Vallés Oriental','Maresme','Bages','Anoia','Vallés Oriental','Garraf','Vallés Occidental','Gironés','Bajo Llobregat','Osona','La Selva','Bajo Llobregat','Bages','Osona','Vallés Occidental','Alto Penedés','Cuenca de Barberá','Alto Penedés','Maresme','Bajo Ebro','La Selva','Vallés Oriental','La Selva','Segarra','Segriá','Bajo Llobregat','Bages','Montsiá','Bajo Campo','Tarragonés','Vallés Oriental','Tarragonés','La Selva','Segriá','Osona','Maresme','Pallars Jussá','Vallés Occidental','Osona','Bages','Bajo Campo','Maresme','Las Garrigas','Bages','Bages','Vallés Oriental','Bajo Llobregat','Moyanés','Tarragonés','Montsiá','La Selva','Vallés Oriental','Bages','La Selva','Selva','Bajo Campo','Alto Ampurdán','La Selva','Bajo Penedés','Urgel','Ribera de Ebro','Valle de Arán','Anoia','Vallés Oriental','Maresme','Gironés','Bajo Ampurdán','Alto Campo','Tarragonés','Maresme','Urgel','Alto Ampurdán','Gironés','Bergadá','Bages','Gironés','Vallés Oriental','Segriá','Tarragonés','Maresme','Pla de l Estany','Bajo Llobregat','Garraf','Vallés Oriental','Bajo Ebro','Tarragonés','Bergadá','Bajo Llobregat','Bajo Llobregat','La Selva','Bajo Ampurdán','La Selva','Cuenca de Barberá','Anoia','Ribera de Ebro','Montsiá','La Selva','Bages','Osona','Tarragonés','Anoia','Noguera','Garraf','Bages','Montsiá','Segriá','Tarragonés','Alto Penedés','Gironés','Tarragonés','Bajo Ebro','Bajo Penedés','Bajo Ebro','Gironés','Osona','Osona','Anoia','Gironés','Las Garrigas','Ripollés','Ripollés','Maresme','Bages','Segriá','Bajo Penedés','Maresme','Alto Ampurdán','Ribera de Ebro','La Selva','Osona','Bages','Osona','Bajo Penedés','Alto Penedés','Segriá','Pallars Jussá','Tierra Alta','Segriá','Alto Penedés','Segriá','Bajo Llobregat','La Garrocha','La Garrocha','Bajo Ebro','Bages','Vallés Oriental','Bajo Campo','Anoia','Priorato','Tarragonés','Cuenca de Barberá','Alto Ampurdán','Vallés Oriental','Maresme','Bajo Campo','Plana de Urgel','Noguera','Osona','Vallés Oriental','Gironés','Alto Penedés','Osona','Vallés Oriental','La Selva','Bajo Penedés','Bajo Ampurdán','Vallés Oriental','Segriá','La Garrocha','Osona','Osona','Vallés Occidental','Alto Penedés','Moyanés','Bajo Campo','Plana de Urgel','Bajo Penedés','Bajo Penedés','Alta Ribagorza','Ripollés','Osona','Las Garrigas','Alto Penedés','Segriá','Plana de Urgel','Plana de Urgel','La Selva','Bages','Alto Penedés','Pla de l Estany','Tarragonés','Bergadá','Segriá','Alto Penedés','Osona','Pallars Sobirá','Bergadá','Bajo Penedés','Osona','Anoia','Bajo Ampurdán','Plana de Urgel','Osona','La Selva','Alto Penedés','Bajo Campo','Alto Penedés','La Selva','Vallés Occidental','Anoia','Baja Cerdaña','Bages','La Selva','Osona','Bages','Tierra Alta','Bajo Campo','Segriá','Bajo Campo','Noguera','Alto Urgel','Alto Ampurdán','Ripollés','Bajo Llobregat','Plana de Urgel','La Garrocha','Valle de Arán','Ribera de Ebro','Segriá','Alto Penedés','Gironés','Bajo Ampurdán','Bajo Ampurdán','Ribera de Ebro','Tarragonés','La Garrocha','Tarragonés','Alto Penedés','Alto Campo','Noguera','Baja Cerdaña','Plana de Urgel','Cuenca de Barberá','Alto Ampurdán','La Garrocha','Bergadá','Alto Penedés','Noguera','Segriá','Segriá','Alto Ampurdán','La Selva','Baja Cerdaña','Pla de l Estany','Anoia','Vallés Oriental','Bajo Campo','Segriá','Alto Penedés','Segriá','Bages','Plana de Urgel','Urgel','Bajo Penedés','Anoia','Alto Penedés','La Garrocha','Alto Ampurdán','Tarragonés','Maresme','Bajo Ampurdán','La Garrocha','Noguera','Urgel','Osona','Alto Campo','La Selva','Bages','Ribera de Ebro','Bajo Ampurdán','Segarra','Alto Penedés','Tierra Alta','Bajo Campo','Bergadá','Alto Ampurdán','Bajo Ebro','Bajo Ampurdán','Anoia','Osona','Plana de Urgel','Ribera de Ebro','Alto Ampurdán','Alto Ampurdán','Segriá','Bajo Campo')
poblacions2 = ('La Pobla de Lillet','Bosost','Vilamalla','Seriñá','Puigpelat','Cabra del Campo','San Martín de Centellas','Botarell','Villanueva de la Barca','Masdenverge','Corbera de Ebro','Figaró-Montmany','Viloví','San Guim de Freixanet','Ullà','Isona y Conca Dellá','Santa María de Oló','Flassá','Pinell de Bray','Castellserá','Viladrau','La Fatarella','Montferrer Castellbó','Valle de Bohí','Puerto de la Selva','Granja de Escarpe','Os de Balaguer','Castellfullit de la Roca','Castelldáns','Cornudella','Ribera de Urgellet','San Cugat Sasgarrigas','San Lorenzo de Morunys','Calders','Las Cabanyas','Vimbodí','Les','Montagut y Oix','Verdú','Báscara','Montesquiu','Mayals','Vilanova de Segriá','Cabanas','Guardiola de Berga','Cerviá de Ter','Aldover','Vall-llobrega','Aiguamurcia','Olius','La Armentera','Camarasa Fontllonga','Vilabertran','Barbens','Pachs del Panadés','Aleixar','Tornabous','La Llacuna','Tivenys','Rasquera','San Bartolomé del Grau','Olván','Santa María de Martorellas de Arriba','Menarguens','Sudanell','Orgaña','Valles del Valira','Garriguella','San Jaime de Llierca','Jorba','Vilademuls','Fondarella','Saus','Ventalló','Agullana','Albí','Esterri de Aneu','Vilabella','Ginestar','Carme','San Felíu de Buxalleu','Maspujols','Alamús','Aiguaviva','Tortellá','La Galera','Lladó','Torre de Cabdella','San Miguel de Fluviá','Massanet de Cabrenys','Rellinars','Miravet','Albons','Castellnou de Seana','Llambillas','Sidamunt','Torroella de Fluviá','Portella','Fortiá','Massanas','San Jordi Desvalls','Vilasana','Benifallet','Masías de Roda','Granadella','Borrassà','Villalba Saserra','Torrelameo','Monistrol de Calders','Pratdip','Cerviá','Castellcir','Sant Martí de Río Corb','Orrius','Camós','San Pablo de Seguríes','Canet de Adri','Vilasacra','Villalba de los Arcos','Poal','Bràfim','Mongay','Rialp','Bellcaire','Torre del Español','Bonastre','Godall','Solivella','San Felíu Saserra','Vilaplana','Prades','San Quirico Safaja','San Mateo de Bages','Bot','Ager','Montanyola','La Riba','San Martín de Liémana','Mas de Barberáns','Torreflor','San Clemente Sasebas','Marsá','Capmany','Montellá Martinet','Garcia','Pauls','Talarn','Coll de Nargó','Castellolí','Vilaller','Masalcorreig','Querol','Oristá','Pau','Belianes','Darnius','Alfar','Castellón de Farfaña','Puente de Armentera','San Baudilio de Llusanés','Puigdalba','Salomó','Vilanova d Escornalbou','La Nou de Gaya','Prats del Rey','Colera','Plans d El Sió','Vinaixa','Rajadell','Guils de Cerdaña','Vilagrasa','Montoliu','Llanás','Pont de Molins','El Masroig','San Ramón','Barbará','Borredá','Maslloréns','Rodoñá','Camplloch','San Juan de Mollet','Pira','Campins','Llardecáns','Pontons','Penellas','Fogás de Monclús','Montmajor','Arnes','Avellanes Santa Liña','Vilavert','Palol de Rebardit','Riudaura','Asentiú','Preixéns','La Tallada','Fontanals de Cerdaña','Albiol','Nulles','Porrera','Conca de Dalt','Mayá de Moncal','Esponellà','La Pera','Viladamat','Vinebre','Castellfullit del Boix','Ger','Ribera del Dondara','Sanahuja','Vilada','Vespella','Vilanova de Meyá','Garrigás','Algerri','Juncosa','Osor','Albagés','Alió','Perafita','Espolla','Blancafort','Capsanes','Argelaguer','Alto Aneu','Preixana','Rourell','Ulldemolins','Freginals','Vilanant','Estany','Parlabá','Vilallonga de Ter','Bruñola','Ordis','Espluga Calva','Jafre','Sarroca','Soriguera','Bolvir','Torreserona','Alfara','Cubélls','Montferri','San Martín Sasgayolas','Santa Fe del Panadés','La Palma de Ebro','Sant Aniol de Finestrás','Gualta','Vall de Cardós','Poboleda','Espot','Salás del Pallars','Alás Serch','Llavorsí','Baix Pallars','Figuerola del Camp','Ibars de Noguera','Collsuspina','Peramola','Solerás','Puebla de Masaluca','Santa Leocadia de Algama','Juyá','Cabacés','Mieras','Molló','Cantallops','Alfés','Almatret','Suñé','Montseny','Tagamanent','Tabérnolas','La Guingueta','Vilanova de Sau','Bellaguarda','Orís','Copóns','Foixá','Pinós','Bellmunt del Priorato','Cistella','Valls d Aguilar','Palau Sator','Planolas','Puig Gros','Ullastret','Masarach','Terradas','Vilamacolum','Molá','Alpens','La Masó','Alins','Saldes','Gabet de la Conca','Torrebeses','Regencós','Isóbol','Navés','Rupit y Pruït','Llusá','Marganell','Guiamets','Guimerá','Madremaña','Bobera','Pedra y Coma','Riner','Malla','Talavera','Buadella','Fígols y Aliñá','Caseras','Lles','Crespiá','Vallbona de las Monjas','San Lorenzo de la Muga','Vallcebre','Brull','Odén','Espunyola','Prats y Sampsor','Rocafort de Queralt','Rupiá','San Martivell','Aguilar de Segarra','Alcanó','Baronía de Rialp','Riumors','Puigvert de Agramunt','Gratallops','Viure','San Julián de Cerdañola','San Ferreol','Las Bordas','Cabanellas','Dosaiguas','Basella','Oliola','Ogassa','Pontós','Lladorre','Rubió','Maldá','Gósol','Las Llosas','Omellóns','Argensola','Das','Pobla de Ciérvoles','La Bisbal de Falset','Viladasens','San Miguel de Campmajor','Aspa','Vilanova de la Aguda','Ciutadilla','Ossó de Sió','La Vansa Fornols','Las Pilas','Serra de Daró','Pinell','Prulláns','Vallfogona','Mura','Llovera','Ultramort','Biosca','Vilopriu','Pujalt','Calonge de Segarra','Gallifa','Vilella Baja','Espinelvas','Montolíu de Cervera','Beuda','Lladurs','Pedret y Marsá','Colomés','Masoteras','Talamanca','Bellmunt','Castell de Mur','Garidells','Vilosell','Gombreny','Santa María de Marlés','Selva de Mar','Sora','Pradell','Rabós','El Cogul','Mollet de Peralada','Setcasas','Santa Cecilia de Voltregá','Vilamaniscle','Milá','Tarroja','Estarás','Montreal','San Mori','Urús','Castellar del Riu','Veciana','Foradada','Sant Guim de la Plana','Pasanant','Queralbs','Vidrá','Colldejou','Abella de la Conca','Torrent','Gayá','Viver y Serrateix','Castellfollit de Riubregós','Salavinera','Prat de Compte','Torroja','Vilamós','Grañena de las Garrigas','Olujas','Floresta','Garrigolas','Castellar de Nuch','Aristot Toloríu','Vilahur','Llimiana','Santa María de Besora','Sagás','Montmaneu','Pardinas','San Cristóbal de Tosas','La Nou','Tirvia','Ciurana','Renau','Castellar de la Ribera','Albañá','San Andrés Salou','Argentera','La Morera de Montsant','Torms','Grañanella','Fontanillas','San Esteban de la Sarga','Guixes','Clariana de Cardener','Grañena','Orpí','Sales de Llierca','Omélls de Nagaya','Vilella Alta','Senterada','Santa María de Miralles','Josá Tuixent','Torre de Fontaubella','Campellas','Sarroca de Bellera','Estamariu','Tavertet','Alós de Balaguer','Arbolí','Lloá','Pontils','Vilanova de Prades','Conesa','Montclar','Farrera','La Figuera','Molsosa','Capafons','Llorach','San Martín del Bas','Vallclara','Iborra','Margalef de Montsant','Riu','Tarrés','Montornés de Segarra','Canejan','Maranges','Nalech','Vallfogona de Riucorb','Cabó','Fulleda','Capolat','Susqueda','San Agustín de Llusanés','Palau de Santa Eulalia','La Bajol','San Saturnino de Osormot','Cabanabona','Sobremunt','Granera','Arseguell','Bellprat','Castell del Areny','Esterri de Cardós','Tiurana','Arrés','Savallá del Condado','Cavá','Bausen','La Quart','Forés','Senant','Fígols','La Febró','Gisclareny','San Jaime de Frontanya')
comarques2 = ('Bergadá','Valle de Arán','Alto Ampurdán','Pla de l Estany','Alto Campo','Alto Campo','Osona','Bajo Campo','Segriá','Montsiá','Tierra Alta','Vallés Oriental','Alto Penedés','Segarra','Bajo Ampurdán','Pallars Jussá','Moyanés','Gironés','Tierra Alta','Urgel','Osona','Tierra Alta','Alto Urgel','Alta Ribagorza','Alto Ampurdán','Segriá','Noguera','La Garrocha','Las Garrigas','Priorato','Alto Urgel','Alto Penedés','Solsonés','Moyanés','Alto Penedés','Cuenca de Barberá','Valle de Arán','La Garrocha','Urgel','Alto Ampurdán','Osona','Segriá','Segriá','Alto Ampurdán','Bergadá','Gironés','Bajo Campo','Bajo Ampurdán','Alto Campo','Solsonés','Alto Ampurdán','Noguera','Alto Ampurdán','Plana de Urgel','Alto Penedés','Bajo Campo','Urgel','Anoia','Bajo Ebro','Ribera de Ebro','Osona','Bergadá','Vallés Oriental','Noguera','Segriá','Alto Urgel','Alto Urgel','Alto Ampurdán','La Garrocha','Anoia','Pla de l Estany','Plana de Urgel','Alto Ampurdán','Alto Ampurdán','Alto Ampurdán','Las Garrigas','Pallars Sobirá','Alto Campo','Ribera de Ebro','Anoia','La Selva','Bajo Campo','Segriá','Gironés','La Garrocha','Montsiá','Alto Ampurdán','Pallars Jussá','Alto Ampurdán','Alto Ampurdán','Vallés Occidental','Ribera de Ebro','Bajo Ampurdán','Plana de Urgel','Gironés','Plana de Urgel','Alto Ampurdán','Segriá','Alto Ampurdán','La Selva','Gironés','Plana de Urgel','Bajo Ebro','Osona','Las Garrigas','Alto Ampurdán','Vallés Oriental','Noguera','Moyanés','Bajo Campo','Las Garrigas','Moyanés','Urgel','Maresme','Pla de l Estany','Ripollés','Gironés','Alto Ampurdán','Tierra Alta','Plana de Urgel','Alto Campo','Noguera','Pallars Sobirá','Bajo Ampurdán','Ribera de Ebro','Bajo Penedés','Montsiá','Cuenca de Barberá','Bages','Bajo Campo','Bajo Campo','Moyanés','Bages','Tierra Alta','Noguera','Osona','Alto Campo','Gironés','Montsiá','Segarra','Alto Ampurdán','Priorato','Alto Ampurdán','Baja Cerdaña','Ribera de Ebro','Bajo Ebro','Pallars Jussá','Alto Urgel','Anoia','Alta Ribagorza','Segriá','Alto Campo','Osona','Alto Ampurdán','Urgel','Alto Ampurdán','Alto Ampurdán','Noguera','Alto Campo','Osona','Alto Penedés','Tarragonés','Bajo Campo','Tarragonés','Anoia','Alto Ampurdán','Segarra','Las Garrigas','Bages','Baja Cerdaña','Urgel','Segriá','Ripollés','Alto Ampurdán','Priorato','Segarra','Cuenca de Barberá','Bergadá','Bajo Penedés','Alto Campo','Gironés','Gironés','Cuenca de Barberá','Vallés Oriental','Segriá','Alto Penedés','Noguera','Vallés Oriental','Bergadá','Tierra Alta','Noguera','Cuenca de Barberá','Pla de l Estany','La Garrocha','Noguera','Noguera','Bajo Ampurdán','Baja Cerdaña','Bajo Campo','Alto Campo','Priorato','Pallars Jussá','La Garrocha','Pla de l Estany','Bajo Ampurdán','Alto Ampurdán','Ribera de Ebro','Bages','Baja Cerdaña','Segarra','Segarra','Bergadá','Tarragonés','Noguera','Alto Ampurdán','Noguera','Las Garrigas','La Selva','Las Garrigas','Alto Campo','Osona','Alto Ampurdán','Cuenca de Barberá','Priorato','La Garrocha','Pallars Sobirá','Urgel','Alto Campo','Priorato','Montsiá','Alto Ampurdán','Moyanés','Bajo Ampurdán','Ripollés','La Selva','Alto Ampurdán','Las Garrigas','Bajo Ampurdán','Segriá','Pallars Sobirá','Baja Cerdaña','Segriá','Bajo Ebro','Noguera','Alto Campo','Anoia','Alto Penedés','Ribera de Ebro','La Garrocha','Bajo Ampurdán','Pallars Sobirá','Priorato','Pallars Sobirá','Pallars Jussá','Alto Urgel','Pallars Sobirá','Pallars Sobirá','Alto Campo','Noguera','Moyanés','Alto Urgel','Las Garrigas','Tierra Alta','Alto Ampurdán','Gironés','Priorato','La Garrocha','Ripollés','Alto Ampurdán','Segriá','Segriá','Segriá','Vallés Oriental','Vallés Oriental','Osona','Pallars Sobirá','Osona','Las Garrigas','Osona','Anoia','Bajo Ampurdán','Solsonés','Priorato','Alto Ampurdán','Alto Urgel','Bajo Ampurdán','Ripollés','Las Garrigas','Bajo Ampurdán','Alto Ampurdán','Alto Ampurdán','Alto Ampurdán','Priorato','Osona','Alto Campo','Pallars Sobirá','Bergadá','Pallars Jussá','Segriá','Bajo Ampurdán','Baja Cerdaña','Solsonés','Osona','Osona','Bages','Priorato','Urgel','Gironés','Las Garrigas','Solsonés','Solsonés','Osona','Segarra','Alto Ampurdán','Alto Urgel','Tierra Alta','Baja Cerdaña','Pla de l Estany','Urgel','Alto Ampurdán','Bergadá','Osona','Solsonés','Bergadá','Baja Cerdaña','Cuenca de Barberá','Bajo Ampurdán','Gironés','Bages','Segriá','Noguera','Alto Ampurdán','Urgel','Priorato','Alto Ampurdán','Bergadá','La Garrocha','Valle de Arán','Alto Ampurdán','Bajo Campo','Alto Urgel','Noguera','Ripollés','Alto Ampurdán','Pallars Sobirá','Anoia','Cataluña','Bergadá','Ripollés','Las Garrigas','Anoia','Baja Cerdaña','Las Garrigas','Priorato','Gironés','Pla de l Estany','Segriá','Noguera','Urgel','Urgel','Alto Urgel','Cuenca de Barberá','Bajo Ampurdán','Solsonés','Baja Cerdaña','Ripollés','Bages','Solsonés','Bajo Ampurdán','Segarra','Bajo Ampurdán','Anoia','Anoia','Vallés Occidental','Priorato','Osona','Segarra','La Garrocha','Solsonés','Alto Ampurdán','Bajo Ampurdán','Segarra','Bages','Noguera','Pallars Jussá','Alto Campo','Las Garrigas','Ripollés','Bergadá','Alto Ampurdán','Osona','Priorato','Alto Ampurdán','Las Garrigas','Alto Ampurdán','Ripollés','Osona','Alto Ampurdán','Alto Campo','Segarra','Segarra','Alto Campo','Alto Ampurdán','Baja Cerdaña','Bergadá','Anoia','Noguera','Segarra','Cuenca de Barberá','Ripollés','Osona','Bajo Campo','Pallars Jussá','Bajo Ampurdán','Bages','Bergadá','Anoia','Anoia','Tierra Alta','Priorato','Valle de Arán','Las Garrigas','Segarra','Las Garrigas','Bajo Ampurdán','Bergadá','Alto Urgel','Alto Ampurdán','Pallars Jussá','Osona','Bergadá','Anoia','Ripollés','Ripollés','Bergadá','Pallars Sobirá','Alto Ampurdán','Tarragonés','Solsonés','Alto Ampurdán','Gironés','Bajo Campo','Priorato','Las Garrigas','Segarra','Bajo Ampurdán','Pallars Jussá','Solsonés','Solsonés','Segarra','Anoia','La Garrocha','Urgel','Priorato','Pallars Jussá','Anoia','Alto Urgel','Priorato','Ripollés','Pallars Jussá','Alto Urgel','Osona','Noguera','Bajo Campo','Priorato','Cuenca de Barberá','Cuenca de Barberá','Cuenca de Barberá','Bergadá','Pallars Sobirá','Priorato','Solsonés','Bajo Campo','Cuenca de Barberá','Osona','Cuenca de Barberá','Segarra','Priorato','Baja Cerdaña','Las Garrigas','Segarra','Valle de Arán','Baja Cerdaña','Urgel','Cuenca de Barberá','Alto Urgel','Las Garrigas','Bergadá','La Selva','Osona','Alto Ampurdán','Alto Ampurdán','Osona','Noguera','Osona','Moyanés','Alto Urgel','Anoia','Bergadá','Pallars Sobirá','Noguera','Valle de Arán','Cuenca de Barberá','Alto Urgel','Valle de Arán','Bergadá','Cuenca de Barberá','Cuenca de Barberá','Bergadá','Bajo Campo','Bergadá','Bergadá')
num_poblacions = len(poblacions1)+len(poblacions2)

# Productos
productes1 = ('Pienso Adult 1kg','Pienso Adult 1kg','Pienso Adult 1kg','Pienso Adult 1kg','Pienso Adult 1kg','Pienso Adult 1kg','Pienso Adult 2kg','Pienso Adult 2kg','Pienso Adult 2kg','Pienso Adult 2kg','Pienso Adult 2kg','Pienso Adult 2kg','Pienso Adult 4kg','Pienso Adult 4kg','Pienso Adult 4kg','Pienso Adult 4kg','Pienso Adult 4kg','Pienso Adult 4kg','Pienso Mini 1kg','Pienso Mini 1kg','Pienso Mini 1kg','Pienso Mini 1kg','Pienso Mini 1kg','Pienso Mini 1kg','Pienso Mini 2kg','Pienso Mini 2kg','Pienso Mini 2kg','Pienso Mini 2kg','Pienso Mini 2kg','Pienso Mini 2kg','Pienso Mini 4kg','Pienso Mini 4kg','Pienso Mini 4kg','Pienso Mini 4kg','Pienso Mini 4kg','Pienso Mini 4kg','Pienso Seco 1kg','Pienso Seco 1kg','Pienso Seco 1kg','Pienso Seco 1kg','Pienso Seco 1kg','Pienso Seco 1kg','Pienso Seco 2kg','Pienso Seco 2kg','Pienso Seco 2kg','Pienso Seco 2kg','Pienso Seco 2kg','Pienso Seco 2kg','Pienso Seco 4kg','Pienso Seco 4kg','Pienso Seco 4kg','Pienso Seco 4kg','Pienso Seco 4kg','Pienso Seco 4kg','Pienso Salmon y arroz','Pienso Salmon y arroz','Pienso Salmon y arroz','Pienso Salmon y arroz','Pienso Salmon y arroz','Pienso Salmon y arroz','Pienso Ternera y verduras','Pienso Ternera y verduras','Pienso Ternera y verduras','Pienso Ternera y verduras','Pienso Ternera y verduras','Pienso Ternera y verduras','Pienso Pollo y verduras','Pienso Pollo y verduras','Pienso Pollo y verduras','Pienso Pollo y verduras','Pienso Pollo y verduras','Pienso Pollo y verduras','Pienso Medium 2kg','Pienso Medium 2kg','Pienso Medium 2kg','Pienso Medium 2kg','Pienso Medium 2kg','Pienso Medium 2kg','Pienso Medium 4kg','Pienso Medium 4kg','Pienso Medium 4kg','Pienso Medium 4kg','Pienso Medium 4kg','Pienso Medium 4kg','Pienso Medium 1kg','Pienso Medium 1kg','Pienso Medium 1kg','Pienso Medium 1kg','Pienso Medium 1kg','Pienso Medium 1kg','Dental stick Mini 50gr','Dental stick Mini 50gr','Dental stick Mini 50gr','Dental stick Mini 50gr','Dental stick Mini 50gr','Dental stick Mini 50gr','Dental stick Mini 70gr','Dental stick Mini 70gr','Dental stick Mini 70gr','Dental stick Mini 70gr','Dental stick Mini 70gr','Dental stick Mini 70gr','Dental stick Medium 80gr','Dental stick Medium 80gr','Dental stick Medium 80gr','Dental stick Medium 80gr','Dental stick Medium 80gr','Dental stick Medium 80gr','Dental stick Medium 100gr','Dental stick Medium 100gr','Dental stick Medium 100gr','Dental stick Medium 100gr','Dental stick Medium 100gr','Dental stick Medium 100gr','Dental stick Maxi 120gr','Dental stick Maxi 120gr','Dental stick Maxi 120gr','Dental stick Maxi 120gr','Dental stick Maxi 120gr','Dental stick Maxi 120gr','Dental stick Maxi 150gr','Dental stick Maxi 150gr','Dental stick Maxi 150gr','Dental stick Maxi 150gr','Dental stick Maxi 150gr','Dental stick Maxi 150gr','Snack Maxi Salmón','Snack Maxi Salmón','Snack Maxi Salmón','Snack Maxi Salmón','Snack Maxi Salmón','Snack Maxi Salmón','Snack Maxi Pollo','Snack Maxi Pollo','Snack Maxi Pollo','Snack Maxi Pollo','Snack Maxi Pollo','Snack Maxi Pollo','Snack Maxi Ternera y verduras','Snack Maxi Ternera y verduras','Snack Maxi Ternera y verduras','Snack Maxi Ternera y verduras','Snack Maxi Ternera y verduras','Snack Maxi Ternera y verduras','Snack Maxi Sardina','Snack Maxi Sardina','Snack Maxi Sardina','Snack Maxi Sardina','Snack Maxi Sardina','Snack Maxi Sardina','Snack Mini Salmon','Snack Mini Salmon','Snack Mini Salmon','Snack Mini Salmon','Snack Mini Salmon','Snack Mini Salmon','Snack Mini Pollo','Snack Mini Pollo','Snack Mini Pollo','Snack Mini Pollo','Snack Mini Pollo','Snack Mini Pollo','Snack Mini Ternera y verduras','Snack Mini Ternera y verduras','Snack Mini Ternera y verduras','Snack Mini Ternera y verduras','Snack Mini Ternera y verduras','Snack Mini Ternera y verduras','Snack Mini Sardina','Snack Mini Sardina','Snack Mini Sardina','Snack Mini Sardina','Snack Mini Sardina','Snack Mini Sardina','Snack Medium Salmon','Snack Medium Salmon','Snack Medium Salmon','Snack Medium Salmon','Snack Medium Salmon','Snack Medium Salmon','Snack Medium Pollo','Snack Medium Pollo','Snack Medium Pollo','Snack Medium Pollo','Snack Medium Pollo','Snack Medium Pollo','Snack Medium Ternera y verduras','Snack Medium Ternera y verduras','Snack Medium Ternera y verduras','Snack Medium Ternera y verduras','Snack Medium Ternera y verduras','Snack Medium Ternera y verduras','Snack Medium Sardina','Snack Medium Sardina','Snack Medium Sardina','Snack Medium Sardina','Snack Medium Sardina','Snack Medium Sardina','Galletas 100gr Light','Galletas 100gr Light','Galletas 100gr Light','Galletas 100gr Light','Galletas 100gr Light','Galletas 100gr Light','Galletas 100gr Protein','Galletas 100gr Protein','Galletas 100gr Protein','Galletas 100gr Protein','Galletas 100gr Protein','Galletas 100gr Protein','Galletas 200gr Light','Galletas 200gr Light','Galletas 200gr Light','Galletas 200gr Light','Galletas 200gr Light','Galletas 200gr Light','Galletas 200gr Protein','Galletas 200gr Protein','Galletas 200gr Protein','Galletas 200gr Protein','Galletas 200gr Protein','Galletas 200gr Protein','Galletas Pack Ahorro Light','Galletas Pack Ahorro Light','Galletas Pack Ahorro Light','Galletas Pack Ahorro Light','Galletas Pack Ahorro Light','Galletas Pack Ahorro Light','Galletas Pack Ahorro Protein','Galletas Pack Ahorro Protein','Galletas Pack Ahorro Protein','Galletas Pack Ahorro Protein','Galletas Pack Ahorro Protein','Galletas Pack Ahorro Protein','Galletas Maxi Light','Galletas Maxi Light','Galletas Maxi Light','Galletas Maxi Light','Galletas Maxi Light','Galletas Maxi Light','Galletas Maxi Protein','Galletas Maxi Protein','Galletas Maxi Protein','Galletas Maxi Protein','Galletas Maxi Protein','Galletas Maxi Protein','Galletas Mini Light','Galletas Mini Light','Galletas Mini Light','Galletas Mini Light','Galletas Mini Light','Galletas Mini Light','Galletas Mini Protein','Galletas Mini Protein','Galletas Mini Protein','Galletas Mini Protein','Galletas Mini Protein','Galletas Mini Protein','Galletas Medium Light','Galletas Medium Light','Galletas Medium Light','Galletas Medium Light','Galletas Medium Light','Galletas Medium Light','Galletas Medium Protein','Galletas Medium Protein','Galletas Medium Protein','Galletas Medium Protein','Galletas Medium Protein','Galletas Medium Protein', 'Correa 3m','Correa 3m','Correa 3m','Correa 3m','Correa 3m','Correa 3m','Correa 3m','Correa 3m','Correa 3m','Correa 3m','Correa 3m','Correa 3m','Correa 3m','Correa 3m','Correa 3m','Correa 5m','Correa 5m','Correa 5m','Correa 5m','Correa 5m','Correa 5m','Correa 5m','Correa 5m','Correa 5m','Correa 5m','Correa 5m','Correa 5m','Correa 5m','Correa 5m','Correa 5m','Correa 7m','Correa 7m','Correa 7m','Correa 7m','Correa 7m','Correa 7m','Correa 7m','Correa 7m','Correa 7m','Correa 7m','Correa 7m','Correa 7m','Correa 7m','Correa 7m','Correa 7m','Correa extensible 2m','Correa extensible 2m','Correa extensible 2m','Correa extensible 2m','Correa extensible 2m','Correa extensible 2m','Correa extensible 2m','Correa extensible 2m','Correa extensible 2m','Correa extensible 2m','Correa extensible 2m','Correa extensible 2m','Correa extensible 2m','Correa extensible 2m','Correa extensible 2m','Correa extensible 5m','Correa extensible 5m','Correa extensible 5m','Correa extensible 5m','Correa extensible 5m','Correa extensible 5m','Correa extensible 5m','Correa extensible 5m','Correa extensible 5m','Correa extensible 5m','Correa extensible 5m','Correa extensible 5m','Correa extensible 5m','Correa extensible 5m','Correa extensible 5m','Cuenco unitario','Cuenco unitario','Cuenco unitario','Cuenco unitario','Cuenco unitario','Cuenco unitario','Cuenco unitario','Cuenco unitario','Cuenco unitario','Cuenco unitario','Cuenco unitario','Cuenco unitario','Cuenco unitario','Cuenco unitario','Cuenco unitario','Cuenco doble','Cuenco doble','Cuenco doble','Cuenco doble','Cuenco doble','Cuenco doble','Cuenco doble','Cuenco doble','Cuenco doble','Cuenco doble','Cuenco doble','Cuenco doble','Cuenco doble','Cuenco doble','Cuenco doble','Cepillo Maxi','Cepillo Maxi','Cepillo Maxi','Cepillo Maxi','Cepillo Maxi','Cepillo Maxi','Cepillo Maxi','Cepillo Maxi','Cepillo Maxi','Cepillo Maxi','Cepillo Maxi','Cepillo Maxi','Cepillo Maxi','Cepillo Maxi','Cepillo Maxi','Cepillo Mini','Cepillo Mini','Cepillo Mini','Cepillo Mini','Cepillo Mini','Cepillo Mini','Cepillo Mini','Cepillo Mini','Cepillo Mini','Cepillo Mini','Cepillo Mini','Cepillo Mini','Cepillo Mini','Cepillo Mini','Cepillo Mini','Champu','Champu','Champu','Champu','Champu','Champu','Champu','Champu','Champu','Champu','Champu','Champu','Champu','Champu','Champu','Champu hidratante','Champu hidratante','Champu hidratante','Champu hidratante','Champu hidratante','Champu hidratante','Champu hidratante','Champu hidratante','Champu hidratante','Champu hidratante','Champu hidratante','Champu hidratante','Champu hidratante','Champu hidratante','Champu hidratante','Champu cachorros','Champu cachorros','Champu cachorros','Champu cachorros','Champu cachorros','Champu cachorros','Champu cachorros','Champu cachorros','Champu cachorros','Champu cachorros','Champu cachorros','Champu cachorros','Champu cachorros','Champu cachorros','Champu cachorros','Champu acondicionador','Champu acondicionador','Champu acondicionador','Champu acondicionador','Champu acondicionador','Champu acondicionador','Champu acondicionador','Champu acondicionador','Champu acondicionador','Champu acondicionador','Champu acondicionador','Champu acondicionador','Champu acondicionador','Champu acondicionador','Champu acondicionador')
productes2 = ('Suavizante','Suavizante','Suavizante','Suavizante','Suavizante','Suavizante','Suavizante','Suavizante','Suavizante','Suavizante','Suavizante','Suavizante','Suavizante','Suavizante','Suavizante','Agua de Colonia','Agua de Colonia','Agua de Colonia','Agua de Colonia','Agua de Colonia','Agua de Colonia','Agua de Colonia','Agua de Colonia','Agua de Colonia','Agua de Colonia','Agua de Colonia','Agua de Colonia','Agua de Colonia','Agua de Colonia','Agua de Colonia','Cortador pelo','Cortador pelo','Cortador pelo','Cortador pelo','Cortador pelo','Cortador pelo','Cortador pelo','Cortador pelo','Cortador pelo','Cortador pelo','Cortador pelo','Cortador pelo','Cortador pelo','Cortador pelo','Cortador pelo','Toallitas','Toallitas','Toallitas','Toallitas','Toallitas','Toallitas','Toallitas','Toallitas','Toallitas','Toallitas','Toallitas','Toallitas','Toallitas','Toallitas','Toallitas','Arnes Mini','Arnes Mini','Arnes Mini','Arnes Mini','Arnes Mini','Arnes Mini','Arnes Mini','Arnes Mini','Arnes Mini','Arnes Mini','Arnes Mini','Arnes Mini','Arnes Mini','Arnes Mini','Arnes Mini','Arnes Maxi','Arnes Maxi','Arnes Maxi','Arnes Maxi','Arnes Maxi','Arnes Maxi','Arnes Maxi','Arnes Maxi','Arnes Maxi','Arnes Maxi','Arnes Maxi','Arnes Maxi','Arnes Maxi','Arnes Maxi','Arnes Maxi','Terrario','Terrario','Terrario','Terrario','Terrario','Terrario','Terrario','Terrario','Terrario','Terrario','Terrario','Terrario','Terrario','Terrario','Terrario','Chapa recambio','Chapa recambio','Chapa recambio','Chapa recambio','Chapa recambio','Chapa recambio','Chapa recambio','Chapa recambio','Chapa recambio','Chapa recambio','Chapa recambio','Chapa recambio','Chapa recambio','Chapa recambio','Chapa recambio','Pipeta','Pipeta','Pipeta','Pipeta','Pipeta','Pipeta','Pipeta','Pipeta','Pipeta','Pipeta','Pipeta','Pipeta','Pipeta','Pipeta','Pipeta','Juguete Cuerda','Juguete Cuerda','Juguete Cuerda','Juguete Cuerda','Juguete Cuerda','Juguete Cuerda','Juguete Cuerda','Juguete Cuerda','Juguete Cuerda','Juguete Cuerda','Juguete Cuerda','Juguete Cuerda','Juguete Cuerda','Juguete Cuerda','Juguete Cuerda','Juguete Hueso','Juguete Hueso','Juguete Hueso','Juguete Hueso','Juguete Hueso','Juguete Hueso','Juguete Hueso','Juguete Hueso','Juguete Hueso','Juguete Hueso','Juguete Hueso','Juguete Hueso','Juguete Hueso','Juguete Hueso','Juguete Hueso','Juguete Pelota','Juguete Pelota','Juguete Pelota','Juguete Pelota','Juguete Pelota','Juguete Pelota','Juguete Pelota','Juguete Pelota','Juguete Pelota','Juguete Pelota','Juguete Pelota','Juguete Pelota','Juguete Pelota','Juguete Pelota','Juguete Pelota','Juguete Fluffy Duck','Juguete Fluffy Duck','Juguete Fluffy Duck','Juguete Fluffy Duck','Juguete Fluffy Duck','Juguete Fluffy Duck','Juguete Fluffy Duck','Juguete Fluffy Duck','Juguete Fluffy Duck','Juguete Fluffy Duck','Juguete Fluffy Duck','Juguete Fluffy Duck','Juguete Fluffy Duck','Juguete Fluffy Duck','Juguete Fluffy Duck','Juguete Mapache','Juguete Mapache','Juguete Mapache','Juguete Mapache','Juguete Mapache','Juguete Mapache','Juguete Mapache','Juguete Mapache','Juguete Mapache','Juguete Mapache','Juguete Mapache','Juguete Mapache','Juguete Mapache','Juguete Mapache','Juguete Mapache','Juguete Spicky','Juguete Spicky','Juguete Spicky','Juguete Spicky','Juguete Spicky','Juguete Spicky','Juguete Spicky','Juguete Spicky','Juguete Spicky','Juguete Spicky','Juguete Spicky','Juguete Spicky','Juguete Spicky','Juguete Spicky','Juguete Spicky','Juguete Zapatilla Rosa','Juguete Zapatilla Rosa','Juguete Zapatilla Rosa','Juguete Zapatilla Rosa','Juguete Zapatilla Rosa','Juguete Zapatilla Rosa','Juguete Zapatilla Rosa','Juguete Zapatilla Rosa','Juguete Zapatilla Rosa','Juguete Zapatilla Rosa','Juguete Zapatilla Rosa','Juguete Zapatilla Rosa','Juguete Zapatilla Rosa','Juguete Zapatilla Rosa','Juguete Zapatilla Rosa','Juguete Cuerda','Juguete Cuerda','Juguete Cuerda','Juguete Cuerda','Juguete Cuerda','Juguete Cuerda','Juguete Cuerda','Juguete Cuerda','Juguete Cuerda','Juguete Cuerda','Juguete Cuerda','Juguete Cuerda','Juguete Cuerda','Juguete Cuerda','Juguete Cuerda','Juguete Frisbee','Juguete Frisbee','Juguete Frisbee','Juguete Frisbee','Juguete Frisbee','Juguete Frisbee','Juguete Frisbee','Juguete Frisbee','Juguete Frisbee','Juguete Frisbee','Juguete Frisbee','Juguete Frisbee','Juguete Frisbee','Juguete Frisbee','Juguete Frisbee','Juguete Wow bee','Juguete Wow bee','Juguete Wow bee','Juguete Wow bee','Juguete Wow bee','Juguete Wow bee','Juguete Wow bee','Juguete Wow bee','Juguete Wow bee','Juguete Wow bee','Juguete Wow bee','Juguete Wow bee','Juguete Wow bee','Juguete Wow bee','Juguete Wow bee','Juguete Crocodile','Juguete Crocodile','Juguete Crocodile','Juguete Crocodile','Juguete Crocodile','Juguete Crocodile','Juguete Crocodile','Juguete Crocodile','Juguete Crocodile','Juguete Crocodile','Juguete Crocodile','Juguete Crocodile','Juguete Crocodile','Juguete Crocodile','Juguete Crocodile','Juguete Strong Ball','Juguete Strong Ball','Juguete Strong Ball','Juguete Strong Ball','Juguete Strong Ball','Juguete Strong Ball','Juguete Strong Ball','Juguete Strong Ball','Juguete Strong Ball','Juguete Strong Ball','Juguete Strong Ball','Juguete Strong Ball','Juguete Strong Ball','Juguete Strong Ball','Juguete Strong Ball','Juguete Rubber Training','Juguete Rubber Training','Juguete Rubber Training','Juguete Rubber Training','Juguete Rubber Training','Juguete Rubber Training','Juguete Rubber Training','Juguete Rubber Training','Juguete Rubber Training','Juguete Rubber Training','Juguete Rubber Training','Juguete Rubber Training','Juguete Rubber Training','Juguete Rubber Training','Juguete Rubber Training','Juguete Guabu Berry Monster','Juguete Guabu Berry Monster','Juguete Guabu Berry Monster','Juguete Guabu Berry Monster','Juguete Guabu Berry Monster','Juguete Guabu Berry Monster','Juguete Guabu Berry Monster','Juguete Guabu Berry Monster','Juguete Guabu Berry Monster','Juguete Guabu Berry Monster','Juguete Guabu Berry Monster','Juguete Guabu Berry Monster','Juguete Guabu Berry Monster','Juguete Guabu Berry Monster','Juguete Guabu Berry Monster','Cama Maxi','Cama Maxi','Cama Maxi','Cama Maxi','Cama Maxi','Cama Maxi','Cama Maxi','Cama Maxi','Cama Maxi','Cama Maxi','Cama Maxi','Cama Maxi','Cama Maxi','Cama Maxi','Cama Maxi','Cama Mini','Cama Mini','Cama Mini','Cama Mini','Cama Mini','Cama Mini','Cama Mini','Cama Mini','Cama Mini','Cama Mini','Cama Mini','Cama Mini','Cama Mini','Cama Mini','Cama Mini','Cama Medium','Cama Medium','Cama Medium','Cama Medium','Cama Medium','Cama Medium','Cama Medium','Cama Medium','Cama Medium','Cama Medium','Cama Medium','Cama Medium','Cama Medium','Cama Medium','Cama Medium','Cama Class Plus','Cama Class Plus','Cama Class Plus','Cama Class Plus','Cama Class Plus','Cama Class Plus','Cama Class Plus','Cama Class Plus','Cama Class Plus','Cama Class Plus','Cama Class Plus','Cama Class Plus','Cama Class Plus','Cama Class Plus','Cama Class Plus','Manta Mini','Manta Mini','Manta Mini','Manta Mini','Manta Mini','Manta Mini','Manta Mini','Manta Mini','Manta Mini','Manta Mini','Manta Mini','Manta Mini','Manta Mini','Manta Mini','Manta Mini','Manta Cuadros Mini','Manta Cuadros Mini','Manta Cuadros Mini','Manta Cuadros Mini','Manta Cuadros Mini','Manta Cuadros Mini','Manta Cuadros Mini','Manta Cuadros Mini','Manta Cuadros Mini','Manta Cuadros Mini','Manta Cuadros Mini','Manta Cuadros Mini','Manta Cuadros Mini','Manta Cuadros Mini','Manta Cuadros Mini','Manta Maxi','Manta Maxi','Manta Maxi','Manta Maxi','Manta Maxi','Manta Maxi','Manta Maxi','Manta Maxi','Manta Maxi','Manta Maxi','Manta Maxi','Manta Maxi','Manta Maxi','Manta Maxi','Manta Maxi','Manta Cuadros Maxi','Manta Cuadros Maxi','Manta Cuadros Maxi','Manta Cuadros Maxi','Manta Cuadros Maxi','Manta Cuadros Maxi','Manta Cuadros Maxi','Manta Cuadros Maxi','Manta Cuadros Maxi','Manta Cuadros Maxi','Manta Cuadros Maxi','Manta Cuadros Maxi','Manta Cuadros Maxi','Manta Cuadros Maxi','Manta Cuadros Maxi','Balón Pet','Balón Pet','Balón Pet','Balón Pet','Balón Pet','Balón Pet','Balón Pet','Balón Pet','Balón Pet','Balón Pet','Balón Pet','Balón Pet','Balón Pet','Balón Pet','Balón Pet', 'Terrario Pequeño','Terrario Pequeño','Terrario Pequeño','Terrario Pequeño','Terrario Grande','Terrario Grande','Terrario Grande','Terrario Grande','Acuario Doble','Acuario Doble','Acuario Doble','Acuario Doble','Acuario Doble','Acuario Unitario','Acuario Unitario','Acuario Unitario','Acuario Unitario','Acuario Unitario')
fabricants1 = ('Purina','Royal Canin','Affinity','ACANA','Hills','Taste of the Wild','Purina','Royal Canin','Affinity','ACANA','Hills','Taste of the Wild','Purina','Royal Canin','Affinity','ACANA','Hills','Taste of the Wild','Purina','Royal Canin','Affinity','ACANA','Hills','Taste of the Wild','Purina','Royal Canin','Affinity','ACANA','Hills','Taste of the Wild','Purina','Royal Canin','Affinity','ACANA','Hills','Taste of the Wild','Purina','Royal Canin','Affinity','ACANA','Hills','Taste of the Wild','Purina','Royal Canin','Affinity','ACANA','Hills','Taste of the Wild','Purina','Royal Canin','Affinity','ACANA','Hills','Taste of the Wild','Purina','Royal Canin','Affinity','ACANA','Hills','Taste of the Wild','Purina','Royal Canin','Affinity','ACANA','Hills','Taste of the Wild','Purina','Royal Canin','Affinity','ACANA','Hills','Taste of the Wild','Purina','Royal Canin','Affinity','ACANA','Hills','Taste of the Wild','Purina','Royal Canin','Affinity','ACANA','Hills','Taste of the Wild','Purina','Royal Canin','Affinity','ACANA','Hills','Taste of the Wild','Purina','Royal Canin','Affinity','ACANA','Hills','Taste of the Wild','Purina','Royal Canin','Affinity','ACANA','Hills','Taste of the Wild','Purina','Royal Canin','Affinity','ACANA','Hills','Taste of the Wild','Purina','Royal Canin','Affinity','ACANA','Hills','Taste of the Wild','Purina','Royal Canin','Affinity','ACANA','Hills','Taste of the Wild','Purina','Royal Canin','Affinity','ACANA','Hills','Taste of the Wild','Purina','Royal Canin','Affinity','ACANA','Hills','Taste of the Wild','Purina','Royal Canin','Affinity','ACANA','Hills','Taste of the Wild','Purina','Royal Canin','Affinity','ACANA','Hills','Taste of the Wild','Purina','Royal Canin','Affinity','ACANA','Hills','Taste of the Wild','Purina','Royal Canin','Affinity','ACANA','Hills','Taste of the Wild','Purina','Royal Canin','Affinity','ACANA','Hills','Taste of the Wild','Purina','Royal Canin','Affinity','ACANA','Hills','Taste of the Wild','Purina','Royal Canin','Affinity','ACANA','Hills','Taste of the Wild','Purina','Royal Canin','Affinity','ACANA','Hills','Taste of the Wild','Purina','Royal Canin','Affinity','ACANA','Hills','Taste of the Wild','Purina','Royal Canin','Affinity','ACANA','Hills','Taste of the Wild','Purina','Royal Canin','Affinity','ACANA','Hills','Taste of the Wild','Purina','Royal Canin','Affinity','ACANA','Hills','Taste of the Wild','Purina','Royal Canin','Affinity','ACANA','Hills','Taste of the Wild','Purina','Royal Canin','Affinity','ACANA','Hills','Taste of the Wild','Purina','Royal Canin','Affinity','ACANA','Hills','Taste of the Wild','Purina','Royal Canin','Affinity','ACANA','Hills','Taste of the Wild','Purina','Royal Canin','Affinity','ACANA','Hills','Taste of the Wild','Purina','Royal Canin','Affinity','ACANA','Hills','Taste of the Wild','Purina','Royal Canin','Affinity','ACANA','Hills','Taste of the Wild','Purina','Royal Canin','Affinity','ACANA','Hills','Taste of the Wild','Purina','Royal Canin','Affinity','ACANA','Hills','Taste of the Wild','Purina','Royal Canin','Affinity','ACANA','Hills','Taste of the Wild','Purina','Royal Canin','Affinity','ACANA','Hills','Taste of the Wild','Instinct','TRUE Origins','KT-PETS','PETZilla','Farmology','Bravo','Dog Crew','Dukkier','Flux','Envy','JBL','Easy Walk','TLP','Zylkene','Urano Vet','Instinct','TRUE Origins','KT-PETS','PETZilla','Farmology','Bravo','Dog Crew','Dukkier','Flux','Envy','JBL','Easy Walk','TLP','Zylkene','Urano Vet','Instinct','TRUE Origins','KT-PETS','PETZilla','Farmology','Bravo','Dog Crew','Dukkier','Flux','Envy','JBL','Easy Walk','TLP','Zylkene','Urano Vet','Instinct','TRUE Origins','KT-PETS','PETZilla','Farmology','Bravo','Dog Crew','Dukkier','Flux','Envy','JBL','Easy Walk','TLP','Zylkene','Urano Vet','Instinct','TRUE Origins','KT-PETS','PETZilla','Farmology','Bravo','Dog Crew','Dukkier','Flux','Envy','JBL','Easy Walk','TLP','Zylkene','Urano Vet','Instinct','TRUE Origins','KT-PETS','PETZilla','Farmology','Bravo','Dog Crew','Dukkier','Flux','Envy','JBL','Easy Walk','TLP','Zylkene','Urano Vet','Instinct','TRUE Origins','KT-PETS','PETZilla','Farmology','Bravo','Dog Crew','Dukkier','Flux','Envy','JBL','Easy Walk','TLP','Zylkene','Urano Vet','Instinct','TRUE Origins','KT-PETS','PETZilla','Farmology','Bravo','Dog Crew','Dukkier','Flux','Envy','JBL','Easy Walk','TLP','Zylkene','Urano Vet','Instinct','TRUE Origins','KT-PETS','PETZilla','Farmology','Bravo','Dog Crew','Dukkier','Flux','Envy','JBL','Easy Walk','TLP','Zylkene','Urano Vet','Instinct','TRUE Origins','KT-PETS','PETZilla','Farmology','Bravo','Dog Crew','Dukkier','Flux','Envy','JBL','Easy Walk','TLP','Zylkene','Urano Vet','Instinct','TRUE Origins','KT-PETS','PETZilla','Farmology','Bravo','Dog Crew','Dukkier','Flux','Envy','JBL','Easy Walk','TLP','Zylkene','Urano Vet','Instinct','TRUE Origins','KT-PETS','PETZilla','Farmology','Bravo','Dog Crew','Dukkier','Flux','Envy','JBL','Easy Walk','TLP','Zylkene','Urano Vet','Instinct','TRUE Origins','KT-PETS','PETZilla','Farmology','Bravo','Dog Crew','Dukkier','Flux','Envy','JBL','Easy Walk','TLP','Zylkene','Urano Vet')
fabricants2 = ('Instinct','TRUE Origins','KT-PETS','PETZilla','Farmology','Bravo','Dog Crew','Dukkier','Flux','Envy','JBL','Easy Walk','TLP','Zylkene','Urano Vet','Instinct','TRUE Origins','KT-PETS','PETZilla','Farmology','Bravo','Dog Crew','Dukkier','Flux','Envy','JBL','Easy Walk','TLP','Zylkene','Urano Vet','Instinct','TRUE Origins','KT-PETS','PETZilla','Farmology','Bravo','Dog Crew','Dukkier','Flux','Envy','JBL','Easy Walk','TLP','Zylkene','Urano Vet','Instinct','TRUE Origins','KT-PETS','PETZilla','Farmology','Bravo','Dog Crew','Dukkier','Flux','Envy','JBL','Easy Walk','TLP','Zylkene','Urano Vet','Instinct','TRUE Origins','KT-PETS','PETZilla','Farmology','Bravo','Dog Crew','Dukkier','Flux','Envy','JBL','Easy Walk','TLP','Zylkene','Urano Vet','Instinct','TRUE Origins','KT-PETS','PETZilla','Farmology','Bravo','Dog Crew','Dukkier','Flux','Envy','JBL','Easy Walk','TLP','Zylkene','Urano Vet','Instinct','TRUE Origins','KT-PETS','PETZilla','Farmology','Bravo','Dog Crew','Dukkier','Flux','Envy','JBL','Easy Walk','TLP','Zylkene','Urano Vet','Instinct','TRUE Origins','KT-PETS','PETZilla','Farmology','Bravo','Dog Crew','Dukkier','Flux','Envy','JBL','Easy Walk','TLP','Zylkene','Urano Vet','Instinct','TRUE Origins','KT-PETS','PETZilla','Farmology','Bravo','Dog Crew','Dukkier','Flux','Envy','JBL','Easy Walk','TLP','Zylkene','Urano Vet','Instinct','TRUE Origins','KT-PETS','PETZilla','Farmology','Bravo','Dog Crew','Dukkier','Flux','Envy','JBL','Easy Walk','TLP','Zylkene','Urano Vet','Instinct','TRUE Origins','KT-PETS','PETZilla','Farmology','Bravo','Dog Crew','Dukkier','Flux','Envy','JBL','Easy Walk','TLP','Zylkene','Urano Vet','Instinct','TRUE Origins','KT-PETS','PETZilla','Farmology','Bravo','Dog Crew','Dukkier','Flux','Envy','JBL','Easy Walk','TLP','Zylkene','Urano Vet','Instinct','TRUE Origins','KT-PETS','PETZilla','Farmology','Bravo','Dog Crew','Dukkier','Flux','Envy','JBL','Easy Walk','TLP','Zylkene','Urano Vet','Instinct','TRUE Origins','KT-PETS','PETZilla','Farmology','Bravo','Dog Crew','Dukkier','Flux','Envy','JBL','Easy Walk','TLP','Zylkene','Urano Vet','Instinct','TRUE Origins','KT-PETS','PETZilla','Farmology','Bravo','Dog Crew','Dukkier','Flux','Envy','JBL','Easy Walk','TLP','Zylkene','Urano Vet','Instinct','TRUE Origins','KT-PETS','PETZilla','Farmology','Bravo','Dog Crew','Dukkier','Flux','Envy','JBL','Easy Walk','TLP','Zylkene','Urano Vet','Instinct','TRUE Origins','KT-PETS','PETZilla','Farmology','Bravo','Dog Crew','Dukkier','Flux','Envy','JBL','Easy Walk','TLP','Zylkene','Urano Vet','Instinct','TRUE Origins','KT-PETS','PETZilla','Farmology','Bravo','Dog Crew','Dukkier','Flux','Envy','JBL','Easy Walk','TLP','Zylkene','Urano Vet','Instinct','TRUE Origins','KT-PETS','PETZilla','Farmology','Bravo','Dog Crew','Dukkier','Flux','Envy','JBL','Easy Walk','TLP','Zylkene','Urano Vet','Instinct','TRUE Origins','KT-PETS','PETZilla','Farmology','Bravo','Dog Crew','Dukkier','Flux','Envy','JBL','Easy Walk','TLP','Zylkene','Urano Vet','Instinct','TRUE Origins','KT-PETS','PETZilla','Farmology','Bravo','Dog Crew','Dukkier','Flux','Envy','JBL','Easy Walk','TLP','Zylkene','Urano Vet','Instinct','TRUE Origins','KT-PETS','PETZilla','Farmology','Bravo','Dog Crew','Dukkier','Flux','Envy','JBL','Easy Walk','TLP','Zylkene','Urano Vet','Instinct','TRUE Origins','KT-PETS','PETZilla','Farmology','Bravo','Dog Crew','Dukkier','Flux','Envy','JBL','Easy Walk','TLP','Zylkene','Urano Vet','Instinct','TRUE Origins','KT-PETS','PETZilla','Farmology','Bravo','Dog Crew','Dukkier','Flux','Envy','JBL','Easy Walk','TLP','Zylkene','Urano Vet','Instinct','TRUE Origins','KT-PETS','PETZilla','Farmology','Bravo','Dog Crew','Dukkier','Flux','Envy','JBL','Easy Walk','TLP','Zylkene','Urano Vet','Instinct','TRUE Origins','KT-PETS','PETZilla','Farmology','Bravo','Dog Crew','Dukkier','Flux','Envy','JBL','Easy Walk','TLP','Zylkene','Urano Vet','Instinct','TRUE Origins','KT-PETS','PETZilla','Farmology','Bravo','Dog Crew','Dukkier','Flux','Envy','JBL','Easy Walk','TLP','Zylkene','Urano Vet','Instinct','TRUE Origins','KT-PETS','PETZilla','Farmology','Bravo','Dog Crew','Dukkier','Flux','Envy','JBL','Easy Walk','TLP','Zylkene','Urano Vet','Instinct','TRUE Origins','KT-PETS','PETZilla','Farmology','Bravo','Dog Crew','Dukkier','Flux','Envy','JBL','Easy Walk','TLP','Zylkene','Urano Vet','Instinct','TRUE Origins','KT-PETS','PETZilla','Farmology','Bravo','Dog Crew','Dukkier','Flux','Envy','JBL','Easy Walk','TLP','Zylkene','Urano Vet','Instinct','TRUE Origins','KT-PETS','PETZilla','Farmology','Bravo','Dog Crew','Dukkier','Flux','Envy','JBL','Easy Walk','TLP','Zylkene','Urano Vet','Instinct','TRUE Origins','KT-PETS','PETZilla','Farmology','Bravo','Dog Crew','Dukkier','Flux','Envy','JBL','Easy Walk','TLP','Zylkene','Urano Vet', 'Flux','Envy','JBL','Easy Walk','Flux','Envy','JBL','Easy Walk','Instinct','TRUE Origins','KT-PETS','PETZilla','Envy','Instinct','TRUE Origins','KT-PETS','PETZilla','Envy')

# Animales domesticos y grandes
especies1 = ('Chinchilla','Codorniz','Conejillo de indias','Conejo blanco europeo','Cerdo doméstico','Cobaya','Cotorra','Gato','Gato montés','Guacamayo','Hámster','Hurón','Iguana','Paloma','Perro','Pez naranja','Pez azul','Pez payaso','Rana','Ratón','Serpiente','Tortuga agua','Tortuga Caspio','Loro','Perdiz')
clases1 = ('Roedor','Ave','Roedor','Roedor','Mamifero','Mamifero','Ave','Mamifero','Mamifero','Ave','Roedor','Roedor','Reptil','Ave','Mamifero','Pez','Pez','Pez','Anfibio','Roedor','Reptil','Reptil','Reptil','Ave','Ave')
especies2 = ('Alce','Alpaca','Asno','Avestruz','Buey','Bufalo','Burro','Caballo','Cabra','Camello', 'Cerdo','Cordero','Gacela','Gallina','Gallo','Ganso','Llama','Mapache','Mulo','Oveja','Pato','Pavo','Reno','Toro','Vaca')
clases2 = ('Mamifero','Mamifero','Mamifero','Mamifero','Mamifero','Mamifero','Mamifero','Mamifero', 'Mamifero', 'Mamifero','Mamifero','Mamifero','Mamifero','Ave','Ave','Ave','Mamifero','Mamifero','Mamifero','Mamifero','Ave','Ave','Mamifero','Mamifero','Mamifero')


# Formación nombre de las granjas
pre = ('', 'Granja', 'Avícola', 'Agro')
sufix = ('El', 'La')
num_botigues = 600
num_granges = 300

num_productes = len(productes1)+len(productes2)
num_fabricants = len(fabricants1)+len(fabricants2)
num_especies = len(especies1)+len(especies2)
num_prod_bot = 20000

# Nombres de animales
animals1 = ('Bradley','Barkley','Yukon','Shiner','Amos','Peter','Crackers','Tuck','Yogi','Kitty','Dutchess','Turner','Travis','Newt','Kenya','Kiwi','Iris','Titus','Yellow','Cobweb','Jazz','Nakita','Felix','Hanna','Tristan','Emmy','Higgins','Eddy','Tux','Harley','Mona','Pumpkin','Abbey','Blue','Bessie','Lucky','Brando','Pudge','Jags','Nana','Zeke','Frosty','Petey','Sara','Ralph','Lexus','Cutie','Kujo','Astro','Gretchen','Rosebud','Grady','Mini','Dobie','Cricket','Pandora','Ajax','Darcy','Hercules','Belle','Lynx','Callie','Rowdy','Pogo','Smudge','Doggon’','Barclay','Bosley','Clicker','Scooby','Laddie','Rhett','Piglet','Erin','Alex','Chamberlain','Greta','Tuffy','Teddy-Bear','Diva','Friday','Harry','Hardy','Minnie','Nickers','Romeo','Toffee','Tom','Mandy','Suzy','Garfield','Spencer','Tipr','Murphy','Bobbie','Chiquita','Lola','Cujo','Autumn','Vinny','Nona','Thelma','Vinnie','Peppy','Brie','Rolex','Pebbles','Rexy','Cisco','Levi','Peanut','Dusty','Yoda','Willow','Pretty','Kallie','Athena','Whiskey','Linus','Hailey','Mercle','Emma','Jess','Emily','Porky','Duffy','Dino','Sweetie-pie','Simone','Braggs','Charlie','Jolie','Zippy','Chico','Whispy','Ellie','Dinky','Kramer','Nina','Bubbles','Poncho','Pickles','Oliver','Sabrina','Cheyenne','Charmer','Hobbes','Comet','Miss Kitty','Bogey','Binky','Snuffles','Kelly','Hannah','Duncan','Nathan','Miko','Humphrey','Scooter','Samson','Velvet','Nitro','Alfie','Ivy','Checkers','Macho','Kelsey','Sumo','Bug','Tiki','Kyra','Frodo','Spunky','Boris','Odie','JR','Claire','Jenny','Dash','Thumper','Tiggy','Turbo','Edgar','Sox','Snickers','Rosa','Nellie','Sneakers','Brit','Misty','Nibbles','Ollie','Codi','Shadow','Rico','Queenie','Furball','Volvo','Echo','Reilly','Paco','Skeeter','Freckles','Buckeye','Ralphie','Houdini','Bentley','Rebel','Mittens','Pirate','Taylor','Pepsi','Corky','Buddy','Griffen','Charles','George','Barney','Pepper','Tripod','Izzy','Baby','Butterscotch','Buttons','Purdy','Boomer','Sly','Chaos','Kato','Nena','Joey','Dandy','Kayla','Hallie','Skip','Parker','Toby','Dave','Brodie','Greenie','Chucky','Dewey','Sheba','Coco','Scottie','Barbie','Raison','Bones','Eifel','Ty','Smoke','Patty','Phoenix','Sammy','Roxanne','Gabriella','Eva','Speed','Papa','King','Bully','Noodles','Bugsy','Nikki','Opie','Bella','Patch','Doc','Fritz','Silky','Beanie','Mattie','Lassie','Holly','Scrappy','Fluffy','Blackjack','AJ','Pepe','Wyatt','Homer','Poppy','Sabine','Wizard','Cubs','Muffy','Sassy','Wiz','Skittles','Ranger','Ruchus','Elwood','Milo','Jamie','Biablo','Dottie','Ziggy','Luna','Timber','Chipper','Ebony','Sassie','Jackson','Clyde','Koda','Jet','Guinness','Barley','Logan','Koty','Popcorn','Flower','Chrissy','Mister','Zack','Thor','Dots','Ozzie','Dempsey','Mitzy','Koba','Squeeky','Sweet-pea','Gilbert','Jewel','Teddy','Valinto','Nickie','Biggie','Prissy','Spirit','Bosco','Gretel','Dixie','Spanky','Atlas','Punkin','Louis','Magnolia','Tobie','Plato','Haley','Miller','Sailor','Jake','Toto','Kipper','Piper','Magic','Layla','Babykins','Rascal','Hoover','Zoey','Archie','Pooh','Chic','Pugsley','Booker','Aries','Fred','Wallace','Allie','JJ','Porkchop','Elvis','Beau','Paddington','Ruffe','Montgomery','Annie','Weaver','Yin','Mitch','Oscar','Kona','Tanner','Gator','Westie','Butterball','Chad','Precious','Dillon','Bugsey','Beans','Wayne','KC','Yeller','Tootsie','Lacey','Lily','Panther','Digger','Jethro','Giant','Babe','Coal','Lou','Jersey','Tally')
animals2 = ('Isabella','Fiona','Kasey','Scruffy','Vito','Tinky','Bacchus','Moose','Grace','Sasha','Ryder','Elmo','Mckenzie','Bruiser','Moochie','Wilson','T-Bone','Bonnie','Marley','Meggie','Joy','Finnegan','Buster','Nikita','Chance','Pippy','Frankie','Nala','Figaro','Julius','Daisy','Dozer','Buttercup','Dreamer','Ashes','Pip-squeek','Smokey','Indy','Fifi','Maggie-moo','Trixie','Maya','Argus','Rocky','Diamond','Ace','Nibby','Sierra','Doodles','Tippy','Luci','Cassie','Megan','Rin Tin Tin','Wiggles','Snowball','Butter','Dudley','Amy','Booster','Dodger','Kiki','Lilly','Butchy','Mary Jane','Einstein','Rover','Twinkle','Elliot','Stella','Commando','Gavin','Penny','Jessie','Twiggy','Brutus','Maggie','Missy','Ruffer','Lizzy','Libby','Gucci','Clifford','Shasta','Rusty','Flint','Candy','Mango','Tammy','Brook','Birdie','Ricky','Andy','Pinto','Wesley','Birdy','Joker','Diesel','Chocolate','Cole','Trinity','Jewels','Nosey','Stich','Bridgette','Monty','Pete','Hugo','Blondie','Carley','Kerry','Missie','Slick','Salty','Domino','Hunter','Jade','Dee','Howie','Monkey','Snowflake','Hope','Petie','Nero','Aires','Dutches','Franky','Mariah','Scarlett','Cyrus','Boone','Lovey','Maverick','Mackenzie','Ming','Titan','Jackpot','Heather','Bootie','Morgan','Hershey','Freddy','Jackie','Pablo','Tyler','Kurly','Wrinkles','Clover','Otto','Pooch','Mocha','Jagger','Tyson','Leo','Mr Kitty','Pearl','Poochie','Tramp','Wags','Isabelle','Toni','Gabby','Puck','Moses','Jesse','Captain','Pookie','Kosmo','Taco','Princess','Snoopy','Miasy','Thyme','Blaze','Barnaby','Spot','Blackie','Merlin','Reggie','Audi','Grizzly','Baron','Godiva','Boo','Schotzie','Peaches','Lexi','Maxwell','Arnie','Latte','Brownie','Roman','Dylan','Trooper','Max','Louie','Billy','Snoop','Mindy','Happyt','Mitzi','Sampson','Ashley','Chaz','Kismet','Beamer','Buffie','Flash','Bongo','Freeway','Tigger','Nico','Hank','Cali','Sebastian','Jingles','Riley','Huey','Jazmie','Kane','Niko','Walter','Tessa','Billie','Miles','Sadie','Misha','Pedro','Monster','Big Foot','Klaus','Frisco','Charisma','Chivas','Mollie','Tabetha','Nike','Picasso','Bodie','Cha Cha','Apollo','Cleo','India','Newton','Dexter','Raven','May','Cindy','Jack','Stuart','Heidi','Lulu','Ripley','Bebe','Major','Beaux','Napoleon','Norton','Taffy','Earl','Prancer','Maddie','Quinn','Trouble','Chippy','Mikey','Skipper','Natasha','Jojo','Jimmuy','Bernie','Rex','Pluto','Babbles','Shorty','Cooper','Chloe','Vava','Snuggles','Guido','Blast','Pokey','Pooh Bear','Jasmine','Woofie','Kid','Bart','Panda','Cherokee','Cocoa','Goober','Sparky','Wilber','Curly','Stanley','Armanti','Mimi','Moonshine','Boots','Yang','Tucker','Johnny','Sandy','Timmy','Lazarus','Chase','Deacon','Lincoln','Luke','Barker','Chyna','Itsy','Sarge','Rufus','Buffy','Tito','Bobby','Cookie','Dragster','Squirt','Millie','Brooke','Gunner','Porter','Mcduff','Grover','Bullwinkle','Thunder','Aggie','Brandy','Bitsy','Webster','Tiny','Brittany','Jasper','Skippy','Abby','Kibbles','Winnie','Lili','Wrigley','Skinny','Noel','Rambler','Pasha','Tabby','Cubby','Mischief','Sophia','Susie','Mookie','Goose','Mary','Bridgett','Lucy','Sky','Tilly','Chessie','Wolfgang','Jenna','Fresier','Gidget','Gasby','Sophie','Lady','Augie','Hudson','Wally','Skyler','Tess','Sage','Sundance','Benji','Rosy','Stinky','Porche','Georgia','Sawyer','Whiskers','Patches','Gunther','Gus','Gigi','Sonny','Sparkle','Moocher','Cosmo','Prince','Chanel','Scout','Dude','Lefty','Pinky','Basil','Joe','Rags','Cassis','Silvester','Bam-bam','Benson')
num_animals_doms = 10000
num_animals_grans = 2500

sexes = ('M', 'F')

# Trabajadores
especialitats = ('Veterinaria', 'Paseador', 'Peluqueria', 'Estetica')
num_treb_botiga = 1500
num_treb_granja = 750


# Servicios
serveis = ('Corte de pelo','Baño','Paseo','Limpieza de dientes','Corte de uñas','Lavado de pelo','Medicina Preventiva','Analitica de Sangre','Radiologia Digital','Ecografia','Obstetricia','Medicina Interna','Dermatologia','Cirugia')
professional = ('Peluqueria','Peluqueria','Paseador','Estetica','Estetica','Peluqueria','Veterinaria','Veterinaria','Veterinaria','Veterinaria','Veterinaria','Veterinaria','Veterinaria','Veterinaria')
#num_serveis = 20000
num_serveis_doms = 15000
num_serveis_granja = 5000

# Qtat productes
num_qtat_producte = 5000

# Producte_especie
num_prod_esp = 7500


def r(lim):
  "0 <= random int < lim"
  return randint(0, lim-1)


################ 1 POBLACIONS
def create_poblacions(cur):
  print("%d towns will be inserted." % num_poblacions)
  cur.execute("DROP TABLE IF EXISTS poblacio CASCADE")
  cur.execute("""CREATE TABLE poblacio 
  (nom VARCHAR(50) PRIMARY KEY NOT NULL, 
  comarca VARCHAR(30) NOT NULL, 
  UNIQUE(nom,comarca))""")
  
  i = 0
  k = 0   
  booli = False
  for i in range(num_poblacions):
    print(i+1, end = '\r')
    if k < len(poblacions1) and booli == False:
      nom = poblacions1[k]
    elif k < len(poblacions2):
      nom = poblacions2[k]

    if k < len(comarques1) and booli == False:
      comarca = comarques1[k]
      if k == len(comarques1)-1:
        booli = True
        k = -1
    elif k < len(comarques2):
      comarca = comarques2[k]
    
    k += 1

    try:
      cur.execute("INSERT INTO poblacio VALUES ('%s', '%s')" % (nom, comarca))
    except psycopg2.IntegrityError as e:
      conn.rollback()
      print("Error inserting (%s, %s). Error information: %s" % (nom, comarca, e))
    conn.commit()


################ 2 BOTIGUES
def create_botigues(cur):
  print("%d shops will be inserted." % num_botigues)
  cur.execute("DROP TABLE IF EXISTS botiga CASCADE")
  cur.execute("""CREATE TABLE botiga 
  (ID VARCHAR(10) PRIMARY KEY NOT NULL, 
  poblacio VARCHAR(50) NOT NULL,
  FOREIGN KEY(poblacio) REFERENCES poblacio(nom) ON UPDATE CASCADE ON DELETE RESTRICT)""")

  for i in range(num_botigues):
    print(i+1, end = '\r')
    
    lista = randint(0,1)

    if lista == 0:
      npob = randint(1, len(poblacions1)-1)
      poblacio = poblacions1[npob]

    else:
      npob = randint(1, len(poblacions2)-1)
      poblacio = poblacions2[npob]

    
    code = poblacio[:2]
    nombre = randint(100000, 200000)
    guion = "-"
    ID = code+guion+str(nombre)
    try:
      cur.execute("INSERT INTO botiga VALUES ('%s', '%s')" % (ID, poblacio))
    except psycopg2.IntegrityError as e:
      conn.rollback()
      print("Error inserting (%s, %s). Error information: %s" % (ID, poblacio, e))
    conn.commit()


################ 3 PRODUCTES
def create_productes(cur):
  print("%d products will be inserted." % num_productes)
  cur.execute("DROP TABLE IF EXISTS producte CASCADE")
  cur.execute("""CREATE TABLE producte 
  (referencia VARCHAR(15) PRIMARY KEY NOT NULL, 
  nom VARCHAR(50) NOT NULL, 
  preu VARCHAR(10) NOT NULL, 
  fabricant VARCHAR(20) NOT NULL)""")

  i = 0
  k = 0
  booli = False
  for i in range(num_productes):
    print(i+1, end = '\r')
    #print("Valor de k: %s" % k)
    if k < len(productes1) and booli == False:
      nom = productes1[k]
      #print("Valor de k: %s" % k)
    elif k < len(productes2):
      nom = productes2[k]

    if k < len(fabricants1) and booli == False:
      fabricant = fabricants1[k]
      if k == len(fabricants1)-1:
        booli = True
        k = -1
    elif k < len(fabricants2):
      fabricant = fabricants2[k]
    
    k += 1


    if nom.count('4kg') > 0:
      preu1 = randint(25,38)
    elif nom.count('2kg') > 0:
      preu1 = randint(15,22)
    elif nom.count('1kg') > 0:
      preu1 = randint(10,20)
    elif nom.count('2m') > 0:
      preu1 = randint(5,10)
    elif nom.count('3m') > 0:
      preu1 = randint(5,10)
    elif nom.count('5m') > 0:
      preu1 = randint(10,14)
    elif nom.count('7m') > 0:
      preu1 = randint(15,18)
    elif nom.count('Terrario') > 0:
      preu1 = randint(70,120)
    elif nom.count('Acuario') > 0:
      preu1 = randint(100,180)
    elif nom.count('Champu') > 0:
      preu1 = randint(5,15)
    elif nom.count('Galleta') > 0:
      preu1 = randint(5,18)
    elif nom.count('Snack') > 0:
      preu1 = randint(4,12)  
    elif nom.count('Dental') > 0:
      preu1 = randint(6,12)
    elif nom.count('Pienso') > 0:
      preu1 = randint(7,24)
    elif nom.count('Juguete') > 0:
      preu1 = randint(10,30)  
    elif nom.count('Cama') > 0:
      preu1 = randint(15,40)
    elif nom.count('Manta') > 0:
      preu1 = randint(10,23)
    else:
      preu1 = randint(10,25)

    ref1 = fabricant[:3]
    ref2 = "_"
    ref3 = randint(100000, 999999)
    referencia = ref1+ref2+str(ref3)

    preu2 = "€"
    preu = str(preu1)+preu2
    try:
      cur.execute("INSERT INTO producte VALUES ('%s', '%s', '%s', '%s')" % (referencia, nom, preu, fabricant))
    except psycopg2.IntegrityError as e:
      conn.rollback()
      print("Error inserting (%s, %s, %s, %s). Error information: %s" % (referencia, nom, preu, fabricant, e))
    conn.commit()


################ 4 PRODUCTES_BOTIGA
def create_producte_botiga(cur):
  print("%d productes_botigues will be inserted." % num_prod_bot)
  cur.execute("DROP TABLE IF EXISTS producte_botiga CASCADE")
  cur.execute("""CREATE TABLE producte_botiga 
  (ID_botiga VARCHAR(10) NOT NULL, 
  ref_producte VARCHAR(15) NOT NULL,
  FOREIGN KEY(ID_botiga) REFERENCES botiga(ID) ON UPDATE CASCADE ON DELETE CASCADE,
  FOREIGN KEY(ref_producte) REFERENCES producte(referencia) ON UPDATE CASCADE ON DELETE CASCADE, 
  PRIMARY KEY(ID_botiga, ref_producte))""")

  for i in range(num_prod_bot):
    print(i+1, end = '\r')
    cur.execute("SELECT ID FROM botiga ORDER BY RANDOM() LIMIT 1")
    ID_botiga = cur.fetchone()[0]
    cur.execute("SELECT referencia FROM producte ORDER BY RANDOM() LIMIT 1")
    ref_producte = cur.fetchone()[0]
    cur.execute("SELECT * FROM producte_botiga WHERE ID_botiga='%s' AND ref_producte='%s'" % (ID_botiga, ref_producte))
    while bool(cur.fetchone()):
      cur.execute("SELECT ID FROM botiga ORDER BY RANDOM() LIMIT 1")
      ID_botiga = cur.fetchone()[0]
      cur.execute("SELECT * FROM producte_botiga WHERE ID_botiga='%s' AND ref_producte='%s'" % (ID_botiga, ref_producte))

    try:
      cur.execute("INSERT INTO producte_botiga VALUES ('%s', '%s')" % (ID_botiga, ref_producte))
    except psycopg2.IntegrityError as e:
      conn.rollback()
      print("Error inserting (%s, %s). Error information: %s" % (ID_botiga, ref_producte, e))
    conn.commit()


################ 5 GRANGES
def create_granges(cur):
  print("%d farms will be inserted." % num_granges)
  cur.execute("DROP TABLE IF EXISTS granja CASCADE")
  cur.execute("""CREATE TABLE granja 
  (nom VARCHAR(50) PRIMARY KEY NOT NULL, 
  poblacio VARCHAR(50) NOT NULL, 
  botiga_conveni VARCHAR(10) NOT NULL, 
  FOREIGN KEY(botiga_conveni) REFERENCES botiga(ID) ON UPDATE CASCADE ON DELETE RESTRICT, 
  UNIQUE(nom, poblacio))""")

  for i in range(num_granges):
    print(i+1, end = '\r')
    
    lista = randint(0,1)
    if lista == 0:
      npob = randint(1, len(poblacions1)-1)
      pob = poblacions1[npob]
      com = comarques1[npob]
    else:
      npob = randint(1, len(poblacions2)-1)
      pob = poblacions2[npob]
      com = comarques2[npob]

    ### Se escoge una tienda al azar con la que hacer el convenio
    cur.execute("SELECT ID FROM botiga ORDER BY RANDOM() LIMIT 1")
    botiga_conveni = cur.fetchone()[0]

    ### Se guarda la poblacion de la tienda con la que hacer el convenio
    cur.execute("SELECT poblacio FROM botiga WHERE ID LIKE '%s'" % (botiga_conveni))
    poblacio_botiga = cur.fetchone()[0]


    ### Se guarda la comarca de la tienda 
    cur.execute("SELECT comarca FROM poblacio WHERE nom LIKE '%s'" % (poblacio_botiga))
    comarca = cur.fetchone()[0]

    cur.execute("SELECT nom FROM poblacio WHERE comarca LIKE '%s' ORDER BY RANDOM() LIMIT 1" % (comarca))
    poblacio = cur.fetchone()[0]

    ### Se escoge un nombre random para la Granja
    nom1 = fake.last_name()
    nom2 = fake.prefix()
    nom3 = fake.last_name()
    space = " "
    randnum1 = randint(0, 3)
    randnum2 = randint(0, 1)
    suf1 = pre[randnum1]
    suf2 = sufix[randnum2]

    if suf1 != '':
      nom = suf1+space+suf2+space+nom1+space+nom2+space+nom3
    else:
      nom = suf2+space+nom1+space+nom2+space+nom3

    try:
      cur.execute("INSERT INTO granja VALUES ('%s', '%s', '%s')" % (nom, poblacio, botiga_conveni))
    except psycopg2.IntegrityError as e:
      conn.rollback()
      print("Error inserting (%s, %s, %s). Error information: %s" % (nom, poblacio, botiga_conveni, e))
    conn.commit()


################ 6 ESPECIES
def create_especies(cur):
  print("%d species will be inserted." % num_especies)
  cur.execute("DROP TABLE IF EXISTS especie CASCADE")
  cur.execute("""CREATE TABLE especie 
  (nom VARCHAR(30) PRIMARY KEY NOT NULL, 
  classe VARCHAR(15) NOT NULL)""")

  i = 0
  k = 0
  booli = False
  for i in range(num_especies):
    print(i+1, end = '\r')

    if k < len(especies1) and booli == False:
      nom = especies1[k]
    elif k < len(especies2):
      nom = especies2[k]

    if k < len(clases1) and booli == False:
      classe = clases1[k]
      if k == len(clases1)-1:
        booli = True
        k = -1
    elif k < len(clases2):
      classe = clases2[k]
    
    k += 1

    try:
      cur.execute("INSERT INTO especie VALUES ('%s', '%s')" % (nom, classe))
    except psycopg2.IntegrityError as e:
      conn.rollback()
      print("Error inserting (%s, %s). Error information: %s" % (nom, classe, e))
    conn.commit()


################ 7 PRODUCTE ESPECIE
def create_prod_esp(cur):
  print("%d producte_especie will be inserted." % num_prod_esp)
  cur.execute("DROP TABLE IF EXISTS producte_especie CASCADE")
  cur.execute("""CREATE TABLE producte_especie 
  (ref_producte VARCHAR(15) NOT NULL, 
  especie VARCHAR(30) NOT NULL,
	FOREIGN KEY (ref_producte) REFERENCES producte(referencia) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY (especie) REFERENCES especie(nom) ON UPDATE CASCADE ON DELETE CASCADE, 
  PRIMARY KEY(ref_producte, especie))""")

  for i in range(num_prod_esp):
    print(i+1, end = '\r')

    # Referencia producto
    cur.execute("SELECT referencia FROM producte ORDER BY RANDOM() LIMIT 1")
    ref_producte = cur.fetchone()[0]
    
    # Nombre producto
    cur.execute("SELECT nom FROM producte WHERE referencia LIKE '%s'" % (ref_producte))
    nom = cur.fetchone()[0]

    # Cribado animales acuaticos
    if nom.count('Terrario') > 0:
      cur.execute("SELECT nom FROM especie WHERE nom LIKE 'Tortuga%' ORDER BY RANDOM() LIMIT 1")
      especie = cur.fetchone()[0]
    elif nom.count('Acuario') > 0:
      cur.execute("SELECT nom FROM especie WHERE nom LIKE 'Pez%' ORDER BY RANDOM() LIMIT 1")
      especie = cur.fetchone()[0]
    else:
      cur.execute("SELECT nom FROM especie WHERE (nom NOT LIKE 'Pez%' AND nom NOT LIKE 'Tortuga%') ORDER BY RANDOM() LIMIT 1")
      especie = cur.fetchone()[0]

    try:
      cur.execute("INSERT INTO producte_especie VALUES ('%s', '%s')" % (ref_producte, especie))
    except psycopg2.IntegrityError as e:
      conn.rollback()
      print("Error inserting (%s, %s). Error information: %s" % (ref_producte, especie, e))
    conn.commit()


################ 8 ANIMAL DOMESTIC
def create_animal_dom(cur):
  print("%d animals domestics will be inserted." % num_animals_doms)
  cur.execute("DROP TABLE IF EXISTS animal_domestic CASCADE")
  cur.execute("""CREATE TABLE animal_domestic 
  (numxip BIGINT PRIMARY KEY NOT NULL, 
  nom VARCHAR(30) NOT NULL, 
  especie VARCHAR(30) NOT NULL, 
  sexe CHAR(1) NOT NULL,
  data_naix DATE NOT NULL, 
  ID_botiga VARCHAR(10) NOT NULL,
  FOREIGN KEY (especie) REFERENCES especie(nom) ON UPDATE CASCADE ON DELETE RESTRICT, 
  FOREIGN KEY (ID_botiga) REFERENCES botiga(ID) ON UPDATE CASCADE ON DELETE CASCADE)""")

  
  for i in range(num_animals_doms):
    print(i+1, end = '\r')
    numxip = randint(10000000000,99999999999)
    numlist = randint(0,399)
    twolists = randint(0,1)
    if twolists == 0:
      nom = animals1[numlist]
    else:
      nom = animals2[numlist]

    sexe = sexes[twolists]
    esp = randint(0,14)
    especie = especies1[esp]
    
    data_naix = fake.date_time_between(start_date="-12y", end_date="now")
    
    cur.execute("SELECT ID FROM botiga ORDER BY RANDOM() LIMIT 1")
    ID_botiga = cur.fetchone()[0]

    try:
      cur.execute("INSERT INTO animal_domestic VALUES ('%s', '%s', '%s', '%s', '%s',  '%s')" % (numxip, nom, especie, sexe, data_naix, ID_botiga))
    except psycopg2.IntegrityError as e:
      conn.rollback()
      print("Error inserting (%s, %s, %s, %s, %s, %s). Error information: %s" % (numxip, nom, especie, sexe, data_naix, ID_botiga, e))
    conn.commit()

################ 9 ANIMAL GRANJA
def create_animal_gran(cur):
  print("%d animals grans will be inserted." % num_animals_grans)
  cur.execute("DROP TABLE IF EXISTS animal_granja CASCADE")
  cur.execute("""CREATE TABLE animal_granja 
  (numxip BIGINT PRIMARY KEY NOT NULL, 
  nom VARCHAR(30) NOT NULL, 
  especie VARCHAR(30) NOT NULL, 
  sexe CHAR(1) NOT NULL,
  data_naix DATE NOT NULL, 
  granja VARCHAR(50) NOT NULL,
  FOREIGN KEY (especie) REFERENCES especie(nom) ON UPDATE CASCADE ON DELETE RESTRICT,
  FOREIGN KEY (granja) REFERENCES granja(nom) ON UPDATE CASCADE ON DELETE CASCADE)""")

  
  for i in range(num_animals_grans):
    print(i+1, end = '\r')
    numxip = randint(10000000000,99999999999)
    numlist = randint(0,399)
    twolists = randint(0,1)
    if twolists == 0:
      nom = animals1[numlist]
    else:
      nom = animals2[numlist]

    sexe = sexes[twolists]
    esp = randint(0,14)
    especie = especies2[esp]
    
    data_naix = fake.date_time_between(start_date="-25y", end_date="now")
    
    cur.execute("SELECT nom FROM granja ORDER BY RANDOM() LIMIT 1")
    granja = cur.fetchone()[0]

    try:
      cur.execute("INSERT INTO animal_granja VALUES ('%s', '%s', '%s', '%s', '%s',  '%s')" % (numxip, nom, especie, sexe, data_naix, granja))
    except psycopg2.IntegrityError as e:
      conn.rollback()
      print("Error inserting (%s, %s, %s, %s, %s, %s). Error information: %s" % (numxip, nom, especie, sexe, data_naix, granja, e))
    conn.commit()


################ 10 TREBALLADOR BOTIGA
def create_treballador_botiga(cur):
  print("%d shop workers will be inserted." % num_treb_botiga)
  cur.execute("DROP TABLE IF EXISTS treballador_botiga CASCADE")
  cur.execute("""CREATE TABLE treballador_botiga 
  (codiempleat VARCHAR(15) PRIMARY KEY NOT NULL, 
  nom VARCHAR(20) NOT NULL, 
  cognoms VARCHAR(35) NOT NULL, 
  especialitzacio VARCHAR(20) NOT NULL,
  telefon INT, 
  botiga VARCHAR(10) NOT NULL, 
  FOREIGN KEY (botiga) REFERENCES botiga(ID) ON UPDATE CASCADE ON DELETE CASCADE,
  UNIQUE(telefon))""")

  for i in range(num_treb_botiga):
    print(i+1, end = '\r')
    nom = fake.first_name()

    # Cognoms
    cognom1 = fake.last_name()
    cognom2 = fake.last_name()
    space = " "
    guion = "-"
    cognoms = cognom1+space+cognom2

    # Codi empleat
    codi1 = cognom1[:2]
    codi2 = cognom2[:2]
    codi = randint(1000,9999)
    codiempleat = codi1+codi2+guion+str(codi)

    # Especializacio
    randesp = randint(0,3)
    especialitzacio = especialitats[randesp]

    # Telf
    num = "6"
    telf = randint(10000000,99999999)
    telefon = num+str(telf)

    #print (telefon)
    cur.execute("SELECT ID FROM botiga ORDER BY RANDOM() LIMIT 1")
    botiga = cur.fetchone()[0]

    try:
      cur.execute("INSERT INTO treballador_botiga VALUES ('%s', '%s', '%s', '%s', '%s',  '%s')" % (codiempleat, nom, cognoms, especialitzacio, telefon, botiga))
    except psycopg2.IntegrityError as e:
      conn.rollback()
      print("Error inserting (%s, %s, %s, %s, %s, %s). Error information: %s" % (codiempleat, nom, cognoms, especialitzacio, telefon, botiga, e))
    conn.commit()


################ 11 TREBALLADOR GRANJA
def create_treballador_granja(cur):
  print("%d farm workers will be inserted." % num_treb_granja)
  cur.execute("DROP TABLE IF EXISTS treballador_granja CASCADE")
  cur.execute("""CREATE TABLE treballador_granja 
  (codiempleat VARCHAR(15) PRIMARY KEY NOT NULL, 
  nom VARCHAR(20) NOT NULL, 
  cognoms VARCHAR(35) NOT NULL, 
  especialitzacio VARCHAR(20) NOT NULL DEFAULT 'Veterinaria', 
  telefon INT, 
  granja VARCHAR(50) NOT NULL, 
  FOREIGN KEY (granja) REFERENCES granja(nom) ON UPDATE CASCADE ON DELETE CASCADE,
  UNIQUE(telefon))""")

  for i in range(num_treb_granja):
    print(i+1, end = '\r')
    nom = fake.first_name()

    # Cognoms
    cognom1 = fake.last_name()
    cognom2 = fake.last_name()
    space = " "
    guion = "-"
    cognoms = cognom1+space+cognom2

    # Codi empleat
    codi1 = cognom1[:2]
    codi2 = cognom2[:2]
    codi = randint(1000,9999)
    codiempleat = codi1+codi2+guion+str(codi)

    # Especializacio
    especialitzacio = "Veterinaria"

    # Telf
    num = "6"
    telf = randint(10000000,99999999)
    telefon = num+str(telf)

    cur.execute("SELECT nom FROM granja ORDER BY RANDOM() LIMIT 1")
    granja = cur.fetchone()[0]

    try:
      cur.execute("INSERT INTO treballador_granja VALUES ('%s', '%s', '%s', '%s', '%s', '%s')" % (codiempleat, nom, cognoms, especialitzacio, telefon, granja))
    except psycopg2.IntegrityError as e:
      conn.rollback()
      print("Error inserting (%s, %s, %s, %s, %s, %s). Error information: %s" % (codiempleat, nom, cognoms, especialitzacio, telefon, granja, e))
    conn.commit()

'''
################ 12 SERVEI
def create_servei(cur):
  print("%d services will be inserted." % num_serveis)
  cur.execute("DROP TABLE IF EXISTS servei CASCADE")
  cur.execute("""CREATE TABLE servei 
  (referencia VARCHAR(15) PRIMARY KEY NOT NULL, 
  nom VARCHAR(20) NOT NULL, 
  preu VARCHAR(5) NOT NULL, 
  data_realitzacio DATE NOT NULL,
  UNIQUE(referencia,nom))""")

  for i in range(num_serveis):
    print(i+1, end = '\r')

    # Nombre servicio
    randservei = randint(0,13)
    nom = serveis[randservei]

    # Precios
    if professional[randservei] == "Veterinaria":
      preu1 = randint(60,100)
    elif professional[randservei] == "Peluqueria":
      preu1 = randint(15,40)
    elif professional[randservei] == "Paseador":
      preu1 = randint(10,25)
    elif professional[randservei] == "Estetica":
      preu1 = randint(20,40)

    # Fecha realización
    data_realitzacio = fake.date_time_between(start_date="-3y", end_date="now")

    # Referencia
    t = data_realitzacio
    t2 = t.strftime('%Y/%m/&d')
    codi1 = t2[:4]
    codi2 = nom[:2]
    codi3 = randint(1000000,9999999)
    guion = "-"
    referencia = codi2+guion+str(codi1)+guion+str(codi3)

    # Precio
    eur = "€"
    preu = str(preu1)+eur
    try:
      cur.execute("INSERT INTO servei VALUES ('%s', '%s', '%s', '%s')" % (referencia, nom, preu, data_realitzacio))
    except psycopg2.IntegrityError as e:
      conn.rollback()
      print("Error inserting (%s, %s, %s, %s). Error information: %s" % (referencia, nom, preu, data_realitzacio, e))
    conn.commit()
'''

################ 13 SERVEI DOMÈSTIC
def create_servei_dom(cur):
  print("%d home services will be inserted." % num_serveis_doms)
  
  '''cur.execute("""CREATE TABLE servei_domestic 
  (referencia VARCHAR(15) PRIMARY KEY NOT NULL, 
  treballador VARCHAR(15) NOT NULL, 
  xip_animal BIGINT NOT NULL, 
  FOREIGN KEY (referencia) REFERENCES servei(referencia) ON UPDATE CASCADE ON DELETE CASCADE, 
  FOREIGN KEY (treballador) REFERENCES treballador_botiga(codiempleat) ON UPDATE CASCADE ON DELETE RESTRICT, 
  FOREIGN KEY (xip_animal) REFERENCES animal_domestic(numxip) ON UPDATE CASCADE ON DELETE RESTRICT)""")'''
  
  cur.execute("DROP TABLE IF EXISTS servei_domestic CASCADE")
  cur.execute("""CREATE TABLE servei_domestic
  (referencia VARCHAR(20) PRIMARY KEY NOT NULL, 
  nom VARCHAR(20) NOT NULL, 
  preu VARCHAR(5) NOT NULL, 
  data_realitzacio DATE NOT NULL,
  treballador VARCHAR(20) NOT NULL,
  xip_animal BIGINT NOT NULL,
  FOREIGN KEY (treballador) REFERENCES treballador_botiga(codiempleat) ON UPDATE CASCADE ON DELETE RESTRICT, 
  FOREIGN KEY (xip_animal) REFERENCES animal_domestic(numxip) ON UPDATE CASCADE ON DELETE RESTRICT)""")

  for i in range(num_serveis_doms):
    print(i+1, end = '\r')

    # Nombre servicio
    randservei = randint(0,13)
    nom = serveis[randservei]
    especialitat = professional[randservei]

    # Precios
    if professional[randservei] == "Veterinaria":
      preu1 = randint(60,100)
    elif professional[randservei] == "Peluqueria":
      preu1 = randint(15,40)
    elif professional[randservei] == "Paseador":
      preu1 = randint(10,25)
    elif professional[randservei] == "Estetica":
      preu1 = randint(20,40)


    # Treballador
    cur.execute("SELECT codiempleat FROM treballador_botiga WHERE especialitzacio='%s' ORDER BY RANDOM() LIMIT 1" % (especialitat))
    treballador = cur.fetchone()[0]

    # Fecha realización
    data_realitzacio = fake.date_time_between(start_date="-3y", end_date="now")

    # Animal
    cur.execute("SELECT numxip FROM animal_domestic ORDER BY RANDOM() LIMIT 1")
    xip_animal = cur.fetchone()[0]
    
    # Referencia
    t = data_realitzacio
    t2 = t.strftime('%Y/%m/&d')
    codi1 = t2[:4]
    codi2 = nom[:2]
    codi3 = randint(1000000,9999999)
    guion = "-"
    letra = "B"
    referencia = codi2+guion+str(codi1)+guion+str(codi3)+guion+letra

    # Precio
    eur = "€"
    preu = str(preu1)+eur

    try:
      cur.execute("INSERT INTO servei_domestic VALUES ('%s', '%s', '%s', '%s', '%s', '%s')" % (referencia, nom, preu, data_realitzacio, treballador, xip_animal))
    except psycopg2.IntegrityError as e:
      conn.rollback()
      print("Error inserting (%s, %s, %s, %s, %s, %s). Error information: %s" % (referencia, nom, preu, data_realitzacio, treballador, xip_animal, e))
    conn.commit()


################ 14 SERVEI GRANJA
def create_servei_granja(cur):
  print("%d farm services will be inserted." % num_serveis_granja)
  cur.execute("DROP TABLE IF EXISTS servei_granja CASCADE")
  '''cur.execute("""CREATE TABLE servei_granja 
  (referencia VARCHAR(15) PRIMARY KEY NOT NULL, 
  treballador VARCHAR(15) NOT NULL, 
  xip_animal BIGINT NOT NULL,
  FOREIGN KEY (referencia) REFERENCES servei(referencia) ON UPDATE CASCADE ON DELETE CASCADE,
  FOREIGN KEY (treballador) REFERENCES treballador_granja(codiempleat) ON UPDATE CASCADE ON DELETE RESTRICT,
  FOREIGN KEY (xip_animal) REFERENCES animal_granja(numxip) ON UPDATE CASCADE ON DELETE RESTRICT)""")'''

  cur.execute("""CREATE TABLE servei_granja
  (referencia VARCHAR(20) PRIMARY KEY NOT NULL, 
  nom VARCHAR(20) NOT NULL, 
  preu VARCHAR(5) NOT NULL, 
  data_realitzacio DATE NOT NULL,
  treballador VARCHAR(20) NOT NULL,
  xip_animal BIGINT NOT NULL,
  FOREIGN KEY (treballador) REFERENCES treballador_granja(codiempleat) ON UPDATE CASCADE ON DELETE RESTRICT, 
  FOREIGN KEY (xip_animal) REFERENCES animal_granja(numxip) ON UPDATE CASCADE ON DELETE RESTRICT)""")

  for i in range(num_serveis_granja):
    print(i+1, end = '\r')
    
    # Referencia
    '''cur.execute("SELECT referencia FROM servei ORDER BY RANDOM() LIMIT 1")
    referencia = cur.fetchone()[0]

    # Sólo servicios de veterinaria
    codiref = referencia[:2]

    while codiref == "Co" or codiref == "Ba" or codiref == "Pa" or codiref == "Li" or codiref == "La":
      cur.execute("SELECT referencia FROM servei ORDER BY RANDOM() LIMIT 1")
      referencia = cur.fetchone()[0]
      codiref = referencia[:2]'''

    # Nombre servicio
    randservei = randint(5,13)
    nom = serveis[randservei]

    # Precio
    preu = randint(60,100)

    # Fecha realización
    data_realitzacio = fake.date_time_between(start_date="-3y", end_date="now")

    # Treballador
    cur.execute("SELECT codiempleat FROM treballador_granja WHERE especialitzacio='Veterinaria' ORDER BY RANDOM() LIMIT 1")
    treballador = cur.fetchone()[0]

    # Animal
    cur.execute("SELECT numxip FROM animal_granja ORDER BY RANDOM() LIMIT 1")
    xip_animal = cur.fetchone()[0]

    # Referencia
    t = data_realitzacio
    t2 = t.strftime('%Y/%m/&d')
    codi1 = t2[:4]
    codi2 = nom[:2]
    codi3 = randint(1000000,9999999)
    guion = "-"
    letra = "G"
    referencia = codi2+guion+str(codi1)+guion+str(codi3)+guion+letra

    try:
      cur.execute("INSERT INTO servei_granja VALUES ('%s', '%s', '%s', '%s', '%s', '%s')" % (referencia, nom, preu, data_realitzacio, treballador, xip_animal))
    except psycopg2.IntegrityError as e:
      conn.rollback()
      print("Error inserting (%s, %s, %s, %s, %s, %s). Error information: %s" % (referencia, nom, preu, data_realitzacio, treballador, xip_animal, e))
    conn.commit()


################ 15 QTAT PRODUCTE
def create_qtat_producte(cur):
  print("%d qtat producte will be inserted." % num_qtat_producte)
  cur.execute("DROP TABLE IF EXISTS qtat_producte CASCADE")
  cur.execute("""CREATE TABLE qtat_producte 
  (ref_servei VARCHAR(20) NOT NULL, 
  ref_producte VARCHAR(15) NOT NULL, 
  unitat INT NOT NULL,
  FOREIGN KEY (ref_servei) REFERENCES servei_domestic(referencia) ON UPDATE CASCADE ON DELETE CASCADE, 
  FOREIGN KEY (ref_producte) REFERENCES producte(referencia) ON UPDATE CASCADE ON DELETE CASCADE, 
  PRIMARY KEY(ref_servei, ref_producte))""")

  for i in range(num_qtat_producte):
    print(i+1, end = '\r')
    
    # Unitat
    cur.execute("SELECT referencia FROM servei_domestic ORDER BY RANDOM() LIMIT 1")
    ref_servei = cur.fetchone()[0]

    cur.execute("SELECT nom FROM servei_domestic WHERE referencia LIKE '%s'" % (ref_servei))
    nom = cur.fetchone()[0]
    k = serveis.index(nom)

    unitat = randint(1, 3)
    cur.execute("SELECT referencia FROM producte ORDER BY RANDOM() LIMIT 1")
    ref_producte = cur.fetchone()[0]

    try:
      cur.execute("INSERT INTO qtat_producte VALUES ('%s', '%s', '%s')" % (ref_servei, ref_producte, unitat))
    except psycopg2.IntegrityError as e:
      conn.rollback()
      print("Error inserting (%s, %s, %s). Error information: %s" % (ref_servei, ref_producte, unitat, e))
    conn.commit()


# Programa principal
# Conexión servidor UPC
conn = psycopg2.connect(host="ubiwan.epsevg.upc.edu", user="est_e7667734", password="dB.e7667734", dbname="est_e7667734", options="-c search_path=practica")

# Conexión en local
#conn = psycopg2.connect(host="localhost", user="userdabd", password="dabd", dbname="dabd")
cur = conn.cursor()

create_poblacions(cur)            # 1
create_botigues(cur)              # 2
create_productes(cur)             # 3
create_producte_botiga(cur)       # 4
create_granges(cur)               # 5
create_especies(cur)              # 6
create_prod_esp(cur)              # 7
create_animal_dom(cur)            # 8
create_animal_gran(cur)           # 9
create_treballador_botiga(cur)    # 10
create_treballador_granja(cur)    # 11
#create_servei(cur)               # 12
create_servei_dom(cur)            # 13
create_servei_granja(cur)         # 14
create_qtat_producte(cur)         # 15

cur.close()
