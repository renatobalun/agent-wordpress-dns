# **Sveobuhvatni Vodič za Rješavanje Najčešćih WordPress Grešaka**

## **Uvod**

WordPress, kao dominantna platforma za izradu web stranica, pokreće značajan dio interneta. Njegova popularnost proizlazi iz fleksibilnosti, prilagodljivosti i bogatog ekosustava tema i dodataka. Međutim, kao i svaki složeni softverski sustav, WordPress nije imun na povremene tehničke probleme i greške. Ove greške, iako ponekad frustrirajuće, u većini slučajeva imaju dobro dokumentirane uzroke i provjerena rješenja.

Cilj ovog izvještaja je osnažiti korisnike WordPressa – bilo da su vlasnici stranica, administratori ili developeri – znanjem potrebnim za samostalno identificiranje, dijagnosticiranje i rješavanje najčešćih problema s kojima se mogu susresti. Nadalje, izvještaj će ponuditi uvid u preventivne mjere i najbolje prakse održavanja koje mogu značajno smanjiti učestalost pojavljivanja ovih grešaka. Važno je shvatiti da WordPress greške često nisu izolirani incidenti, već simptomi dubljih problema vezanih uz konfiguraciju servera, kompatibilnost softverskih komponenti unutar WordPress ekosustava ili nedovoljno održavanje. Razumijevanje ovih temeljnih uzroka ključno je ne samo za otklanjanje trenutnog problema, već i za osiguravanje dugoročne stabilnosti i optimalnog funkcioniranja web stranice. Kroz sustavan pristup dijagnostici i primjenu preporučenih rješenja, korisnici mogu prevladati tehničke izazove i osigurati da njihova WordPress stranica radi besprijekorno.

## **I. Najčešće Greške u WordPressu: Opisi, Uzroci i Detaljna Rješenja**

Ovaj odjeljak detaljno obrađuje specifične greške koje se najčešće javljaju prilikom korištenja WordPress platforme. Za svaku grešku pružit će se iscrpan opis, navesti tipični uzroci te ponuditi konkretni, korak-po-korak vodiči za njihovo otklanjanje. Razumijevanje prirode svake greške prvi je korak prema njenom uspješnom rješavanju.

Kako bi se korisnicima olakšalo snalaženje i brza identifikacija problema, slijedi tablica sa sažetkom najčešćih grešaka, njihovim kratkim opisom i tipičnim kategorijama uzroka. Ova tablica služi kao brzi referentni vodič koji može usmjeriti korisnika prema relevantnom dijelu izvještaja.

| Naziv Greške | Kratki Opis (što korisnik vidi) | Tipični Uzrok(ci) |
| :---- | :---- | :---- |
| Internal Server Error (Greška 500\) | Generička serverska greška, stranica nedostupna. | Plugin/Tema, Server (PHP limiti, .htaccess), Konfiguracija WP-a |
| White Screen of Death (WSoD \- Bijeli Ekran Smrti) | Potpuno bijeli ekran bez ikakvih poruka o grešci. | Plugin/Tema, Server (PHP memorija), Sintaksna greška |
| Error Establishing Database Connection | Poruka da WordPress ne može uspostaviti vezu s bazom podataka. | Baza podataka (kredencijali, server), Konfiguracija WP-a (wp-config.php) |
| 404 Not Found (Stranica Nije Pronađena) | Server ne može pronaći traženi URL. | Konfiguracija WP-a (permalinkovi), Server (.htaccess) |
| Parse Error / Syntax Error | Poruka o grešci u PHP kodu, npr. "unexpected T\_STRING". | Sintaksna greška (PHP kod) |
| Problemi s Učitavanjem Slika / Medijskih Datoteka | HTTP greška pri uploadu, nefunkcionalan gumb "Dodaj medij", pokvarene slike. | Server (dozvole, PHP limiti), Plugin/Tema, Konfiguracija WP-a |
| WordPress Stranica Prijave Osvježava se ili Preusmjerava | Nemogućnost prijave jer se login stranica stalno osvježava ili preusmjerava. | Konfiguracija WP-a (URL-ovi), Kolačići/Cache, Plugin/Tema |
| WordPress Ne Šalje E-poštu | Problemi s isporukom emailova sa stranice (kontakt forme, obavijesti). | Server (PHP mail() funkcija), Konfiguracija WP-a (SMTP) |
| Zaglavljivanje u Načinu Održavanja | Stranica prikazuje poruku o održavanju i ne izlazi iz tog stanja. | Konfiguracija WP-a (.maintenance datoteka) |
| Greška Prekoračenja Memorijskog Limita (Allowed Memory Size Exhausted) | Fatalna greška zbog nedostatka PHP memorije. | Server (PHP memorija), Plugin/Tema |
| Greška Prekoračenja Maksimalnog Vremena Izvršavanja (Max Execution Time) | Fatalna greška jer PHP skripta predugo traje. | Server (PHP vrijeme izvršavanja), Plugin/Tema (neefikasan kod) |
| 403 Forbidden (Pristup Zabranjen) | Server odbija pristup traženom resursu. | Server (dozvole, .htaccess), Plugin (sigurnosni) |
| "Sorry, You Are Not Allowed to Access This Page" | Nemogućnost pristupa određenim dijelovima admin sučelja. | Konfiguracija WP-a (korisničke uloge, prefiks baze), Plugin/Tema, Dozvole |
| "Installation Failed: Could Not Create Directory" | Greška prilikom instalacije teme/plugina zbog nemogućnosti stvaranja direktorija. | Server (dozvole za pisanje) |
| Greška Neispravnih Dozvola za Datoteke | Opći problemi uzrokovani pogrešnim dozvolama datoteka/mapa. | Server (dozvole) |
| Upozorenja o Miješanom Sadržaju (Mixed Content Warnings) | HTTPS stranica učitava resurse preko HTTP-a, preglednik javlja upozorenje. | Konfiguracija WP-a (URL-ovi), Sadržaj (HTTP linkovi) |
| ERR\_TOO\_MANY\_REDIRECTS (Previše Preusmjeravanja) | Preglednik zaglavljen u beskonačnoj petlji preusmjeravanja. | Konfiguracija WP-a (URL-ovi), Server (.htaccess, SSL), Plugin (preusmjeravanje, cache) |
| DNS\_PROBE\_FINISHED\_NXDOMAIN | Preglednik ne može razriješiti domenu u IP adresu. | DNS problem (izvan WP-a) |
| "Destination Folder Already Exists" | Greška pri instalaciji teme/plugina jer odredišna mapa već postoji. | Datotečni sustav (postojeća mapa) |
| Greška Nedostajuće Stilske Datoteke Teme (Theme Stylesheet Missing Error) | Poruka da nedostaje style.css datoteka prilikom instalacije/aktivacije teme. | Struktura teme (style.css datoteka) |

### **1\. Internal Server Error (Greška 500\)**

Detaljan Opis:  
Greška 500, poznata kao "Internal Server Error", jedna je od najčešćih i najfrustrirajućih grešaka u WordPressu. Radi se o generičkoj poruci servera koja ukazuje da je došlo do neočekivanog problema na serveru, ali server ne može preciznije identificirati što je pošlo po zlu.1 Ova greška obično čini cijelu web stranicu nedostupnom.  
Najčešći Uzroci:  
Uzroci ove greške su brojni, što otežava dijagnostiku:

* **Oštećena .htaccess datoteka:** Ova konfiguracijska datoteka Apache servera može sadržavati greške ili biti oštećena, što dovodi do problema.1  
* **PHP vremensko ograničenje ili iscrpljena memorija:** Ako PHP skripta zahtijeva više resursa (vremena ili memorije) nego što je server konfiguriran da dopusti, može doći do ove greške.2  
* **Problemi s pluginovima ili temama:** Loše kodirani, nekompatibilni ili oštećeni pluginovi i teme čest su izvor greške 500\.1  
* **Problemi sa serverom (hosting):** Ponekad problem leži u samom hosting okruženju, poput problema s hardverom ili softverom servera.1  
* **Oštećene WordPress jezgrene datoteke:** Iako rjeđe, oštećenje osnovnih WordPress datoteka također može uzrokovati ovu grešku.2

Koraci za Rješavanje:  
S obzirom na raznolikost uzroka, rješavanje zahtijeva sustavan pristup:

1. **Provjera .htaccess datoteke:** Pristupite datotekama vaše stranice putem FTP-a ili File Managera. Pronađite .htaccess datoteku u korijenskom direktoriju i preimenujte je (npr. u .htaccess\_old). Osvježite stranicu. Ako radi, problem je bio u .htaccess datoteci. Generirajte novu tako da odete u WordPress admin sučelje na Postavke \> Trajne veze (Permalinks) i kliknete "Spremi promjene".1  
2. **Povećanje PHP memorijskog limita:** Uredite wp-config.php datoteku dodavanjem linije define('WP\_MEMORY\_LIMIT', '256M'); prije retka /\* That's all, stop editing\! Happy publishing. \*/.2 Možete pokušati i s većim vrijednostima poput 512M.  
3. **Deaktivacija svih pluginova:** Putem FTP-a, preimenujte mapu wp-content/plugins u nešto poput plugins\_old ili plugins.stop.1 Ako stranica proradi, problem je u jednom od pluginova. Vratite naziv mape plugins i zatim u WordPress admin sučelju aktivirajte pluginove jedan po jedan, testirajući stranicu nakon svake aktivacije, kako biste pronašli krivca.1  
4. **Prebacivanje na zadanu WordPress temu:** Ako ste nedavno mijenjali temu ili se postojeća ažurirala, pokušajte se prebaciti na zadanu WordPress temu (npr. Twenty Twenty-Four). To možete učiniti preimenovanjem mape vaše aktivne teme u wp-content/themes putem FTP-a.1 Ako stranica radi s zadanom temom, problem je u vašoj temi.  
5. **Provjera PHP verzije:** Nekompatibilnost s određenom PHP verzijom može uzrokovati probleme. Pokušajte promijeniti PHP verziju putem kontrolnog panela vašeg hostinga.2  
6. **Omogućavanje WP\_DEBUG:** Dodajte define('WP\_DEBUG', true); i define('WP\_DEBUG\_LOG', true); u wp-config.php kako biste dobili detaljnije poruke o greškama koje mogu ukazati na uzrok.2  
7. **Kontaktiranje hosting providera:** Ako ništa od navedenog ne pomogne, problem može biti na strani servera. Obratite se tehničkoj podršci vašeg hostinga.1  
8. **Vraćanje sigurnosne kopije:** Ako imate nedavnu sigurnosnu kopiju, vraćanje stranice može biti najbrže rješenje.2  
9. **Zamjena WordPress jezgrenih datoteka:** Preuzmite svježu kopiju WordPressa s wordpress.org. Putem FTP-a, izbrišite mape wp-admin i wp-includes s vašeg servera (NE dirajte wp-content mapu i wp-config.php datoteku). Zatim prenesite nove wp-admin i wp-includes mape s preuzete arhive.2

Greška 500 često služi kao pokazatelj širih problema. Iako neposredni okidač može biti oštećena .htaccess datoteka ili problematičan plugin, temeljni uzrok ponekad leži u nedovoljnim resursima servera, kao što su ograničena PHP memorija ili prekratko vrijeme izvršavanja skripti.2 Stoga, čak i ako privremeno rješenje poput popravka .htaccess datoteke ili deaktivacije plugina upali, važno je razmotriti i performanse hosting paketa. Ako server konstantno radi na granici svojih mogućnosti, greška 500 se može ponovno pojaviti s drugim pluginom ili prilikom izvršavanja zahtjevnije operacije. Ovo naglašava važnost odabira adekvatnog hostinga koji može podržati potrebe vaše WordPress stranice.

### **2\. White Screen of Death (WSoD \- Bijeli Ekran Smrti)**

Detaljan Opis:  
"Bijeli ekran smrti" (WSoD) je problem gdje se vaša web stranica, bilo frontend (ono što posjetitelji vide) ili backend (WordPress administratorsko sučelje), prikazuje kao potpuno prazan, bijeli ekran.5 Ne prikazuju se nikakve poruke o grešci niti bilo kakve druge informacije, što može biti izuzetno zbunjujuće i alarmantno za vlasnike stranica.4  
Najčešći Uzroci:  
Dva glavna problema obično uzrokuju WSoD:

* **Iscrpljen PHP memorijski limit:** WordPress, kao PHP aplikacija, ima dodijeljen memorijski limit od strane servera. Ako skripta pokuša iskoristiti više memorije od dopuštene, stranica se može srušiti i prikazati WSoD.5  
* **Neispravan plugin ili tema:** Loše kodiran, nekompatibilan ili nedavno ažuriran plugin ili tema može izazvati kritične greške koje rezultiraju bijelim ekranom.5 Čak i mala sintaksna greška u datoteci poput functions.php može biti uzrok.

**Koraci za Rješavanje:**

1. **Povećanje PHP memorijskog limita:** Ovo je često prvi korak. Uredite wp-config.php datoteku dodavanjem ili izmjenom linije define('WP\_MEMORY\_LIMIT', '128M'); ili define('WP\_MEMORY\_LIMIT', '256M');.5 Ako to ne pomogne, limit se može pokušati povećati i putem php.ini ili .htaccess datoteke, ili kontaktiranjem hosting providera.  
2. **Deaktivacija svih pluginova:** Ako povećanje memorije ne riješi problem, vjerojatno je krivac plugin. Putem FTP-a, pristupite mapi wp-content i preimenujte mapu plugins (npr. u plugins\_deactivated).5 Ako stranica proradi, preimenujte mapu natrag u plugins, a zatim unutar nje preimenujte mape pojedinačnih pluginova jednu po jednu (ili ih aktivirajte jednu po jednu kroz admin sučelje ako mu možete pristupiti) dok ne pronađete problematični plugin.  
3. **Prebacivanje na zadanu WordPress temu:** Ako deaktivacija pluginova ne pomogne, problem može biti u aktivnoj temi. Putem FTP-a, u mapi wp-content/themes, preimenujte mapu vaše trenutne teme.5 WordPress će se automatski prebaciti na zadanu temu. Ako WSoD nestane, vaša tema je uzrok.  
4. **Omogućavanje WP\_DEBUG moda:** Budući da WSoD ne prikazuje greške, ključno je omogućiti WordPress debug mod. U wp-config.php datoteku dodajte:  
   PHP  
   define( 'WP\_DEBUG', true );  
   define( 'WP\_DEBUG\_LOG', true );  
   define( 'WP\_DEBUG\_DISPLAY', false );  
   @ini\_set( 'display\_errors', 0 );  
   Ovo će zapisivati PHP greške u wp-content/debug.log datoteku, što može otkriti točan uzrok problema.2  
5. **Provjera sintaksnih grešaka:** Ako ste nedavno ručno uređivali PHP datoteke (npr. functions.php), provjerite jeste li napravili sintaksnu grešku (npr. zaboravljeni ; ili }).5  
6. **Brisanje cachea:** Obrišite cache preglednika te serverski cache (ako ga koristite putem plugina ili hostinga).5  
7. **Ponovna instalacija WordPress jezgrenih datoteka:** U rijetkim slučajevima, oštećene jezgrene datoteke mogu uzrokovati WSoD. Ovo uključuje zamjenu mapa wp-admin i wp-includes svježim kopijama, pazeći da ne prebrišete wp-content mapu i wp-config.php datoteku.5

WSoD je posebno frustrirajući zbog potpunog nedostatka informacija na ekranu. Upravo zato, prije nego što se krene s masovnom deaktivacijom pluginova ili tema, prioritet bi trebao biti omogućavanje prikaza ili logiranja grešaka putem WP\_DEBUG moda.2 Time se "bijeli ekran" može pretvoriti u konkretnu PHP poruku o grešci koja ukazuje na problematičnu datoteku, funkciju ili liniju koda. Dobivanje ove informacije značajno sužava polje pretrage i usmjerava daljnje korake rješavanja, pretvarajući nasumično pogađanje u ciljanu dijagnostiku.

### **3\. Error Establishing Database Connection (Greška pri Uspostavljanju Veze s Bazom Podataka)**

Detaljan Opis:  
Poruka "Error Establishing A Database Connection" jasno ukazuje da WordPress ne može uspostaviti komunikaciju s MySQL bazom podataka.1 Budući da su u bazi pohranjeni svi ključni podaci vaše web stranice – uključujući objave, stranice, korisničke informacije, postavke tema i pluginova – ova greška čini vašu stranicu potpuno nefunkcionalnom.5  
**Najčešći Uzroci:**

* **Pogrešni podaci za povezivanje u wp-config.php:** Ovo je najčešći uzrok. Datoteka wp-config.php sadrži ključne informacije kao što su naziv baze podataka (DB\_NAME), korisničko ime (DB\_USER), lozinka (DB\_PASSWORD) i naziv hosta baze podataka (DB\_HOST). Ako je bilo koji od ovih podataka netočan, WordPress se neće moći povezati.1  
* **Problemi s web serverom ili serverom baze podataka:** Server na kojem se nalazi vaša baza podataka može biti nedostupan, preopterećen ili u kvaru.1  
* **Oštećena baza podataka:** U nekim slučajevima, tablice unutar WordPress baze podataka mogu postati oštećene.  
* **Prekoračen limit baze podataka:** Neki hosting provideri, posebno na dijeljenim (shared) paketima, mogu nametnuti ograničenja na veličinu baze podataka.1  
* **Hakirana stranica:** Napadači mogu izmijeniti wp-config.php datoteku ili oštetiti bazu podataka.1

**Koraci za Rješavanje:**

1. **Provjera i ispravljanje podataka u wp-config.php:** Pristupite wp-config.php datoteci u korijenskom direktoriju vaše WordPress instalacije putem FTP-a. Pažljivo provjerite jesu li vrijednosti za DB\_NAME, DB\_USER, DB\_PASSWORD i DB\_HOST točne. Ove podatke obično dobivate od svog hosting providera.1 Vrijednost za DB\_HOST je često localhost, ali može varirati.  
2. **Kontaktiranje hosting providera:** Ako su podaci u wp-config.php ispravni, problem bi mogao biti sa serverom baze podataka. Kontaktirajte podršku vašeg hostinga i pitajte ih je li server baze podataka aktivan i radi li ispravno.1  
3. **Popravak baze podataka:** WordPress ima ugrađenu funkciju za popravak baze. Dodajte liniju define('WP\_ALLOW\_REPAIR', true); u wp-config.php datoteku. Zatim u pregledniku posjetite URL vasastranica.com/wp-admin/maint/repair.php. Nakon popravka, obavezno uklonite dodanu liniju iz wp-config.php.  
4. **Provjera limita baze podataka:** Prijavite se u kontrolni panel vašeg hostinga i provjerite iskorištenost prostora vaše baze podataka. Ako je limit dosegnut, možda ćete trebati optimizirati bazu ili zatražiti povećanje limita.1  
5. **Provjera znakova hakiranja:** Pregledajte wp-config.php i druge ključne datoteke na sumnjive izmjene. Razmislite o skeniranju stranice sigurnosnim alatima.1  
6. **Vraćanje sigurnosne kopije baze podataka:** Ako sumnjate na oštećenje ili imate nedavnu sigurnosnu kopiju, vraćanje baze podataka može riješiti problem.

Ova greška snažno naglašava kritičnu ulogu wp-config.php datoteke. Ona sadrži "ključne informacije" 1 bez kojih WordPress ne može funkcionirati. Čak i najmanja tipfelerska greška u vjerodajnicama za bazu podataka može rezultirati potpunom nedostupnošću stranice. Ovo ne samo da ukazuje na potrebu za iznimnom pažnjom prilikom unosa ili izmjene ovih podataka, već i na važnost zaštite same wp-config.php datoteke od neovlaštenog pristupa. Preporučuje se postavljanje strožih dozvola za ovu datoteku (npr. 600 ili 440\) kako bi se smanjio rizik od kompromitacije.2 Redovito sigurnosno kopiranje ove datoteke, zajedno s ostatkom stranice, također je od presudne važnosti.

### **4\. 404 Not Found (Stranica Nije Pronađena)**

Detaljan Opis:  
Greška 404 Not Found javlja se kada server ne može pronaći resurs (stranicu, objavu, sliku ili drugu datoteku) koji je korisnik zatražio putem URL-a.2 Često se događa da glavna stranica i administratorsko sučelje rade normalno, ali pojedinačne objave ili stranice vraćaju 404 grešku.6  
**Najčešći Uzroci:**

* **Problemi s permalinkovima (trajnim vezama):** Ovo je najčešći uzrok. Problemi s konfiguracijom permalinkova, posebno nakon migracije stranice, promjene strukture URL-a ili problema s .htaccess datotekom, mogu dovesti do 404 grešaka.6  
* **Neispravna ili oštećena .htaccess datoteka:** Ova datoteka upravlja načinom na koji server obrađuje URL-ove i preusmjeravanja. Ako je oštećena ili sadrži pogrešna pravila, server neće moći ispravno mapirati URL na sadržaj.6  
* **Problemi s dozvolama datoteka ili mapa:** Iako rjeđe, neispravne dozvole mogu spriječiti server da pristupi određenim datotekama.  
* **Tipfeleri u URL-u:** Korisnik je možda unio pogrešan URL.2  
* **Sadržaj je izbrisan ili premješten:** Tražena stranica ili objava je možda izbrisana ili joj je promijenjen URL bez postavljanja preusmjeravanja.

**Koraci za Rješavanje:**

1. **Ponovno generiranje permalinkova:** Ovo je najčešće i najjednostavnije rješenje. Prijavite se u WordPress administratorsko sučelje, idite na Postavke \> Trajne veze (Permalinks). Ništa ne mijenjajte, samo kliknite gumb "Spremi promjene". Ovo će prisiliti WordPress da ponovno generira pravila u .htaccess datoteci.6  
2. **Ručno uređivanje ili generiranje nove .htaccess datoteke:** Ako ponovno generiranje permalinkova ne uspije, možda ćete morati ručno urediti .htaccess datoteku. Pristupite joj putem FTP-a u korijenskom direktoriju WordPressa. Možete je privremeno preimenovati (npr. u .htaccess\_old) i zatim ponoviti korak 1\. Alternativno, možete stvoriti novu .htaccess datoteku i unijeti zadani WordPress kod 3:  
   Apache  
   \# BEGIN WordPress  
   \<IfModule mod\_rewrite.c\>  
   RewriteEngine On  
   RewriteBase /  
   RewriteRule ^index\\.php$ \- \[L\]  
   RewriteCond %{REQUEST\_FILENAME}\!-f  
   RewriteCond %{REQUEST\_FILENAME}\!-d  
   RewriteRule. /index.php \[L\]  
   \</IfModule\>  
   \# END WordPress

3. **Provjera URL-a na tipfelere:** Osigurajte da je URL koji pokušavate pristupiti točno napisan.2  
4. **Brisanje cachea:** Obrišite cache preglednika i DNS cache na vašem računalu.2 Također, ako koristite plugin za cacheiranje na WordPressu, ispraznite i taj cache.  
5. **Deaktivacija pluginova:** Neki pluginovi, posebno oni za preusmjeravanje, sigurnost ili SEO, mogu utjecati na URL-ove. Privremeno ih deaktivirajte kako biste vidjeli rješava li to problem.  
6. **Provjera postoji li sadržaj:** Uvjerite se da stranica ili objava koju pokušavate otvoriti zaista postoji i da nije izbrisana ili u statusu skice.

Greške 404 često su direktno povezane s načinom na koji WordPress i web server interpretiraju i obrađuju URL-ove. Ključnu ulogu u tom procesu igraju postavke permalinkova unutar WordPressa i direktive unutar .htaccess datoteke (na Apache serverima). WordPress koristi "lijepe" permalinkove (npr. vasastranica.com/naziv-objave/) koje .htaccess datoteka, putem mod\_rewrite modula, pretvara u stvarne upite koje server može razumjeti (npr. vasastranica.com/index.php?p=123). Ako su postavke permalinkova u WordPress bazi podataka neusklađene s pravilima u .htaccess datoteci, ili ako je .htaccess datoteka oštećena ili nedostaje, server neće moći ispravno mapirati zatraženi URL na odgovarajući WordPress sadržaj, što rezultira 404 greškom.6 Stoga, bilo kakva promjena u strukturi URL-a, migracija na novi server, ili problemi s .htaccess datotekom mogu lako dovesti do masovnih 404 grešaka. Provjera i ispravljanje ovih elemenata trebali bi biti prioritet prilikom dijagnosticiranja 404 problema.

### **5\. Parse Error / Syntax Error (Greška Parsiranja / Sintaksna Greška)**

Detaljan Opis:  
Parse error ili syntax error javlja se kada postoji greška u sintaksi PHP koda vaše WordPress stranice. Poruka o grešci obično je prilično jasna i često ukazuje na datoteku i liniju koda gdje se problem nalazi, npr. "Parse error – syntax error, unexpected T\_FUNCTION..." ili slično.4 Ova greška prekida izvršavanje PHP skripte i može učiniti cijelu stranicu ili njen dio nedostupnim.  
**Najčešći Uzroci:**

* **Ručno dodavanje ili izmjena PHP koda:** Najčešće se javlja nakon što korisnik pokuša dodati isječak koda (snippet) u datoteku functions.php teme, ili u datoteke nekog plugina ili teme.4  
* **Tipfelerske greške u kodu:** Čak i najmanje greške poput zaboravljenog točka-zareza (;) na kraju linije, nedostajuće ili viška vitičaste zagrade ({ ili }), nezatvorenih navodnika, pogrešno napisanih PHP funkcija ili varijabli mogu uzrokovati ovu grešku.4  
* **Problematičan kod u nedavno instaliranom ili ažuriranom pluginu/temi:** Ponekad, novi ili ažurirani plugin ili tema mogu sadržavati sintaksne greške.6  
* **Nekompatibilnost PHP verzije:** Stariji kod može sadržavati sintaksu koja nije podržana u novijim verzijama PHP-a, ili obrnuto.

**Koraci za Rješavanje:**

1. **Identifikacija problematične datoteke i linije koda:** Poruka o grešci obično navodi točnu putanju do datoteke i broj linije gdje je PHP parser naišao na problem.4  
2. **Pristup datoteci putem FTP-a ili File Managera:** Koristite FTP klijent (npr. FileZilla) ili File Manager u vašem hosting kontrolnom panelu kako biste pristupili navedenoj datoteci.4  
3. **Ispravljanje sintaksne greške:** Otvorite datoteku u tekstualnom editoru. Ako ste nedavno dodavali ili mijenjali kod, pažljivo pregledajte te izmjene. Potražite očite greške poput nedostajućih točka-zareza, zagrada, navodnika itd..4 Ako niste sigurni kako ispraviti grešku, možete pokušati privremeno ukloniti (ili komentirati) nedavno dodani kod kako biste vidjeli hoće li to riješiti problem.  
4. **Korištenje online PHP syntax checker-a:** Ako niste sigurni u čemu je greška, možete kopirati problematični dio koda u online PHP syntax checker (npr. spomenut u 6) koji vam može pomoći identificirati problem.  
5. **Deaktivacija/brisanje problematičnog plugina/teme:** Ako je greška uzrokovana nedavno instaliranim ili ažuriranim pluginom/temom, a ne možete pristupiti admin sučelju, preimenujte mapu tog plugina/teme putem FTP-a kako biste ga deaktivirali.  
6. **Vraćanje na prethodnu verziju datoteke:** Ako imate sigurnosnu kopiju datoteke prije nego što je greška nastala, vraćanje na tu verziju može biti najbrže rješenje.  
7. **Spremanje i ponovno učitavanje:** Nakon ispravljanja greške, spremite datoteku i ponovno je prenesite na server ako koristite FTP. Zatim osvježite stranicu u pregledniku.4

Ova vrsta greške direktna je posljedica problema unutar samog PHP koda. Ona jasno ukazuje na rizike koje korisnici, posebno oni s manje programerskog iskustva, preuzimaju kada izravno mijenjaju PHP datoteke svoje WordPress instalacije.4 PHP je jezik koji ne oprašta sintaksne pogreške; čak i naizgled beznačajan propust, poput nedostajućeg točka-zareza, može zaustaviti izvršavanje cijele skripte i srušiti stranicu. Stoga je iznimno važno biti oprezan. Preporučuje se da se bilo kakve izmjene koda prvo testiraju u lokalnom ili staging (testnom) okruženju, a ne izravno na produkcijskoj (živoj) stranici. Korištenje child tema za modifikacije funkcionalnosti ili izgleda teme je također dobra praksa jer štiti originalne datoteke teme od izmjena i olakšava ažuriranja. Prije bilo kakvih ručnih izmjena koda, uvijek je nužno napraviti potpunu sigurnosnu kopiju stranice.

### **6\. Problemi s Učitavanjem Slika / Medijskih Datoteka (Image Upload Issues / Media Errors)**

Detaljan Opis:  
Problemi s učitavanjem slika i drugih medijskih datoteka u WordPressu mogu se manifestirati na različite načine, uključujući generičku HTTP grešku prilikom pokušaja učitavanja 2, nefunkcioniranje gumba "Dodaj medij" u klasičnom editoru, prikazivanje ikona pokvarenih datoteka u medijskoj biblioteci umjesto sličica, ili pojavu poruke "Došlo je do pogreške prilikom obrezivanja vaše slike" prilikom uređivanja.2  
Najčešći Uzroci:  
Spektar mogućih uzroka je širok:

* **Pogrešne dozvole za datoteke/mape:** Najčešće se radi o nedovoljnim dozvolama za pisanje u mapu wp-content/uploads.2  
* **Serverska ograničenja:** PHP konfiguracija na serveru može imati preniske vrijednosti za upload\_max\_filesize (maksimalna veličina datoteke za upload), post\_max\_size (maksimalna veličina POST zahtjeva) ili memory\_limit (PHP memorijski limit).2  
* **Nedopušteni znakovi u nazivu datoteke:** Specijalni znakovi (npr. apostrofi, uskličnici, hrvatski dijakritički znakovi) u nazivima datoteka mogu uzrokovati probleme.2  
* **Sukobi s pluginovima ili temom:** Neki pluginovi (posebno oni za optimizaciju slika ili sigurnost) ili loše kodirana tema mogu ometati proces učitavanja.2  
* **Stara verzija PHP-a:** Zastarjela verzija PHP-a na serveru može biti nekompatibilna s WordPressom ili procesima obrade slika.2  
* **Nedostatak GD biblioteke ili ImageMagicka:** Ove PHP ekstenzije su potrebne za obradu slika (promjena veličine, obrezivanje). Ako nedostaju na serveru, doći će do grešaka.2  
* **Problemi s privremenom mapom na serveru:** WordPress prvo sprema učitane datoteke u privremenu mapu. Ako s tom mapom postoje problemi (npr. puna je ili nema dozvole), učitavanje neće uspjeti.2  
* **Istekla sesija prijave:** Ako je korisnička sesija istekla tijekom procesa učitavanja.2  
* **Problemi s "Add Media" gumbom:** Može biti uzrokovan JavaScript greškama zbog konflikta plugina/teme.2

**Koraci za Rješavanje:**

1. **Provjera i ispravljanje dozvola:** Osigurajte da mapa wp-content/uploads i njene podmape imaju dozvole 755\.2 To se radi putem FTP klijenta.  
2. **Povećanje PHP limita:** Kontaktirajte svog hosting providera ili, ako imate pristup, uredite php.ini, .htaccess ili wp-config.php datoteku kako biste povećali vrijednosti za upload\_max\_filesize, post\_max\_size i memory\_limit.2 Na primjer, u .htaccess možete dodati:  
   Apache  
   php\_value upload\_max\_filesize 64M  
   php\_value post\_max\_size 64M  
   php\_value memory\_limit 256M

3. **Preimenovanje datoteke:** Prije učitavanja, preimenujte datoteku tako da koristi samo slova, brojeve, crtice i podvlake, te da nema razmaka ili specijalnih znakova.2 Smanjite veličinu datoteke ako je prevelika.  
4. **Privremena deaktivacija pluginova i teme:** Deaktivirajte sve pluginove i prebacite se na zadanu WordPress temu (npr. Twenty Twenty-Four) kako biste provjerili postoji li konflikt.2 Ako problem nestane, reaktivirajte ih jedan po jedan.  
5. **Ažuriranje PHP verzije:** Provjerite koristite li preporučenu, stabilnu verziju PHP-a. Ažuriranje se obično radi preko hosting kontrolnog panela.2  
6. **Provjera GD biblioteke/ImageMagicka:** Pitajte svog hosting providera jesu li ove PHP ekstenzije instalirane i omogućene.2  
7. **Osvježavanje stranice / brisanje cachea / ponovna prijava:** Ponekad jednostavno osvježavanje stranice, brisanje cachea preglednika ili ponovna prijava mogu riješiti privremene probleme.2 Pokušajte s drugim preglednikom.  
8. **Rješavanje problema s "Add Media" gumbom:** Ako gumb ne radi, provjerite konzolu preglednika (Developer Tools) na JavaScript greške. Možete pokušati dodati define('CONCATENATE\_SCRIPTS', false); u wp-config.php.2  
9. **Provjera privremene mape:** Kontaktirajte hosting da provjere status privremene mape za učitavanje.2

Problemi s medijskim datotekama u WordPressu mogu biti prilično složeni za dijagnosticiranje jer njihovi uzroci mogu ležati na vrlo različitim razinama sustava. Za razliku od, primjerice, sintaksne greške koja ima jasan uzrok u lošem kodu, problemi s učitavanjem slika mogu proizaći iz konfiguracije datotečnog sustava servera (dozvole), PHP postavki (memorijski limiti, maksimalne veličine datoteka), samog WordPress softvera (konflikti plugina ili tema), pa čak i nedostajućih serverskih modula neophodnih za obradu slika (poput GD biblioteke).2 Ova višeslojnost znači da korisnik mora sustavno provjeravati svaki potencijalni izvor problema, od najjednostavnijih (npr. naziv datoteke) do složenijih (npr. serverska konfiguracija). Rješavanje ovih problema često zahtijeva više strpljenja, tehničkog znanja, a ponekad i izravnu suradnju s tehničkom podrškom hosting providera, posebno kada su u pitanju serverske postavke ili moduli.

### **7\. WordPress Stranica Prijave Osvježava se ili Preusmjerava (Login Page Refreshing/Redirecting Issue)**

Detaljan Opis:  
Ovaj problem se javlja kada korisnik pokuša pristupiti WordPress administratorskom sučelju. Nakon unosa korisničkog imena i lozinke na wp-login.php stranici i klika na "Log In", stranica se jednostavno ponovno učita (osvježi) ili nakratko preusmjeri, a zatim vrati natrag na stranicu za prijavu.5 Korisnik ostaje zaglavljen u petlji i ne može pristupiti nadzornoj ploči.  
**Najčešći Uzroci:**

* **Netočne vrijednosti za Site URL i Home URL:** Ovo je primarni uzrok. Ako su WordPress Address (URL) i Site Address (URL) pogrešno konfigurirani u WordPress postavkama ili definirani u wp-config.php datoteci, WordPress se zbuni oko toga kamo preusmjeriti korisnika nakon prijave.5  
* **Problemi s kolačićima ili cacheom preglednika:** Zastarjeli ili oštećeni kolačići i cache preglednika mogu ometati proces prijave.5  
* **Oštećena .htaccess datoteka:** Problemi s .htaccess datotekom mogu uzrokovati neočekivana preusmjeravanja.5  
* **Konflikt s pluginom ili temom:** Neki pluginovi (posebno sigurnosni ili oni koji modificiraju proces prijave) ili teme mogu uzrokovati ovaj problem.5  
* **Problemi s SSL konfiguracijom:** Ako je SSL certifikat nedavno dodan ili nije ispravno konfiguriran, može doći do problema s preusmjeravanjem između HTTP i HTTPS verzija stranice.5

**Koraci za Rješavanje:**

1. **Definiranje Site URL i Home URL u wp-config.php:** Ovo je najčešće rješenje. Pristupite wp-config.php datoteci putem FTP-a i dodajte sljedeće dvije linije, zamjenjujući https://vasastranica.com s vašom stvarnom adresom stranice (pazite na http:// ili https:// i www prefiks ako ga koristite) 5:  
   PHP  
   define('WP\_SITEURL', 'https://vasastranica.com');  
   define('WP\_HOME', 'https://vasastranica.com');

2. **Brisanje kolačića i cachea preglednika:** Obrišite kolačiće i cache za vašu web stranicu u postavkama preglednika, ili pokušajte se prijaviti koristeći anonimni (incognito) način rada.5  
3. **Preimenovanje .htaccess datoteke:** Putem FTP-a, preimenujte .htaccess datoteku u korijenskom direktoriju (npr. u .htaccess\_old). Pokušajte se prijaviti. Ako uspije, idite na Postavke \> Trajne veze u WordPress adminu i kliknite "Spremi promjene" kako biste generirali novu, ispravnu .htaccess datoteku.5  
4. **Deaktivacija pluginova:** Putem FTP-a, preimenujte mapu wp-content/plugins (npr. u plugins\_old) kako biste deaktivirali sve pluginove. Pokušajte se prijaviti. Ako uspije, vratite naziv mape i aktivirajte pluginove jedan po jedan kako biste pronašli krivca.5  
5. **Prebacivanje na zadanu temu:** Putem FTP-a, preimenujte mapu vaše aktivne teme u wp-content/themes (npr. u moja-tema\_old). Pokušajte se prijaviti. Ako uspije, problem je u vašoj temi.5  
6. **Provjera SSL konfiguracije:** Ako ste nedavno instalirali SSL, provjerite jesu li sve postavke ispravne i da li se koristi HTTPS u Site URL i Home URL.5

Ispravna konfiguracija WordPress adrese (Site URL) i adrese web-mjesta (Home URL) od temeljne je važnosti za pravilno funkcioniranje WordPressa. Ovi URL-ovi se koriste za interno usmjeravanje, generiranje linkova i, ključno, za proces prijave. Ako su ovi URL-ovi neispravni ili nekonzistentni (npr. jedan s www, drugi bez; jedan HTTP, drugi HTTPS), WordPress ne može ispravno preusmjeriti korisnika na administratorsko sučelje nakon uspješne autentifikacije, što dovodi do petlje osvježavanja ili preusmjeravanja.5 Ovaj problem posebno često izlazi na vidjelo tijekom ili nakon migracije web stranice na novi server ili domenu, ili prilikom promjene SSL statusa, ako se URL-ovi ne ažuriraju dosljedno na svim potrebnim mjestima (u bazi podataka i/ili wp-config.php datoteci). To naglašava potrebu za iznimnom pažnjom i provjerom ovih postavki prilikom bilo kakvih značajnijih promjena u okruženju ili adresi stranice, jer njihova neispravnost može dovesti do potpunog gubitka pristupa administrativnom dijelu.

### **8\. WordPress Ne Šalje E-poštu (Not Sending Email Issue)**

Detaljan Opis:  
Ovaj problem se javlja kada vaša WordPress stranica ne uspijeva poslati e-poštu. To može uključivati e-poštu iz kontaktnih obrazaca, obavijesti o registraciji novih korisnika, e-poštu za resetiranje lozinke, obavijesti o komentarima ili bilo koju drugu e-poštu koju bi WordPress ili njegovi pluginovi trebali slati.5  
**Najčešći Uzroci:**

* **Hosting server nije ispravno konfiguriran za korištenje PHP mail() funkcije:** Mnogi hosting serveri, posebno na dijeljenim (shared) okruženjima, nemaju PHP mail() funkciju optimalno konfiguriranu, ili je ona ograničena radi sprječavanja spama.6  
* **Mail server hostinga ima lošu reputaciju ili ga primateljski serveri blokiraju:** E-pošta poslana putem PHP mail() funkcije s dijeljenih servera često biva označena kao spam ili potpuno blokirana od strane popularnih email servisa (poput Gmaila, Outlooka) jer joj nedostaju odgovarajući mehanizmi autentifikacije.6  
* **Plugin za kontaktnu formu nije ispravno konfiguriran:** Ako koristite plugin za kontakt formu, njegove postavke za slanje e-pošte možda nisu ispravne.  
* **Sigurnosni pluginovi ili vatrozid:** Neki sigurnosni pluginovi ili vatrozid na serveru mogu blokirati odlaznu e-poštu.

**Koraci za Rješavanje:**

1. **Korištenje SMTP (Simple Mail Transfer Protocol) servisa i WordPress SMTP plugina:** Ovo je najpouzdanije i preporučeno rješenje. Umjesto oslanjanja na PHP mail() funkciju servera, e-pošta se šalje putem vanjskog, dediciranog SMTP servisa (npr. SendGrid, Mailgun, Gmail SMTP, Sendinblue).  
   * Instalirajte SMTP plugin poput WP Mail SMTP, Easy WP SMTP ili neki drugi.5  
   * Kreirajte račun kod odabranog SMTP providera (mnogi nude besplatne planove za manji obim slanja).  
   * Konfigurirajte SMTP plugin s podacima koje ste dobili od SMTP providera. To obično uključuje SMTP host, port, metodu enkripcije (SSL/TLS), te korisničko ime i lozinku ili API ključ za autentifikaciju.6  
2. **Provjera postavki plugina za kontaktnu formu:** Uvjerite se da su postavke unutar vašeg plugina za kontaktnu formu (npr. "To" email adresa, "From" email adresa) ispravno postavljene.  
3. **Kontaktiranje hosting providera:** Možete pitati svog hosting providera je li PHP mail() funkcija ispravno konfigurirana i postoje li kakva ograničenja. Međutim, čak i ako funkcionira, SMTP je generalno bolja opcija za isporučivost.6  
4. **Provjera spam filtera:** Zamolite primatelje da provjere svoje spam/junk mape. Ako e-pošta tamo završava, to je jak pokazatelj da trebate prijeći na SMTP.

Oslanjanje na zadanu PHP mail() funkciju za slanje e-pošte iz WordPressa često je izvor problema i nepouzdano rješenje.6 Ova funkcija uvelike ovisi o konfiguraciji web servera, a serveri, posebno oni na dijeljenom hostingu, često nemaju optimalno postavljene parametre za slanje e-pošte ili nameću stroga ograničenja kako bi spriječili zloupotrebu za slanje spama. Nadalje, e-pošta poslana putem mail() funkcije obično nema odgovarajuće SPF, DKIM i DMARC zapise, što su standardi za autentifikaciju e-pošte. Zbog toga, primateljski mail serveri (poput Gmaila, Outlooka) takvu e-poštu često tretiraju sumnjičavo, usmjeravajući je u spam mapu ili je čak potpuno blokirajući prije nego što stigne do primatelja. Korištenje vanjskog SMTP (Simple Mail Transfer Protocol) servisa, putem odgovarajućeg WordPress plugina, zaobilazi ove probleme.6 SMTP servisi su specijalizirani za slanje e-pošte, koriste pravilnu autentifikaciju, imaju bolju reputaciju servera i pružaju alate za praćenje isporučivosti. Stoga bi korisnici trebali proaktivno razmotriti postavljanje SMTP-a za svoju WordPress stranicu kako bi osigurali pouzdanu isporuku e-pošte, umjesto da čekaju da se pojave problemi s PHP mail() funkcijom.

### **9\. Zaglavljivanje u Načinu Održavanja (Stuck in Maintenance Mode)**

Detaljan Opis:  
Kada WordPress ažurira svoju jezgru, teme ili pluginove, automatski postavlja stranicu u način održavanja. Tijekom tog kratkog perioda, posjetiteljima se prikazuje poruka poput "Briefly unavailable for scheduled maintenance. Check back in a minute.".7 Problem nastaje kada stranica ostane "zaglavljena" u ovom načinu rada čak i nakon što je proces ažuriranja trebao biti završen.6  
**Najčešći Uzroci:**

* **Neuspješno brisanje .maintenance datoteke:** WordPress stvara privremenu datoteku pod nazivom .maintenance u korijenskom direktoriju instalacije tijekom procesa ažuriranja. Ova datoteka signalizira WordPressu da prikaže poruku o održavanju. Ako je proces ažuriranja prekinut (npr. zbog problema s vezom, isteka vremena servera, ručnog prekida) ili ako dođe do greške tijekom ažuriranja, WordPress možda neće automatski izbrisati ovu datoteku.7

Koraci za Rješavanje:  
Rješenje je obično vrlo jednostavno:

1. **Pristup datotekama stranice putem FTP-a ili File Managera:** Povežite se na server vaše web stranice koristeći FTP klijent (npr. FileZilla) ili File Manager dostupan u vašem hosting kontrolnom panelu.5  
2. **Pronalaženje i brisanje .maintenance datoteke:** Navigirajte do korijenskog direktorija vaše WordPress instalacije (gdje se nalaze mape wp-admin, wp-content, wp-includes). Potražite datoteku pod nazivom .maintenance.5  
3. **Izbrišite .maintenance datoteku**.7  
4. **Provjerite stranicu:** Nakon brisanja datoteke, osvježite svoju web stranicu u pregledniku. Trebala bi se normalno učitati.  
5. **Ponovno pokretanje ažuriranja (ako je potrebno):** Ako je ažuriranje bilo prekinuto, možda ćete ga morati ponovno pokrenuti iz WordPress administratorskog sučelja.

Ova greška zorno ilustrira kako čak i jednostavan mehanizam, dizajniran za poboljšanje korisničkog iskustva tijekom ažuriranja, može postati izvor problema ako se temeljni proces ne dovrši kako je predviđeno. Datoteka .maintenance je samo privremeni "signal".7 Njena svrha je spriječiti posjetitelje da vide potencijalno nedovršenu ili neispravnu stranicu dok se ažuriranje odvija. Međutim, ako se taj signal ne ukloni automatski, stranica ostaje blokirana. Ovo naglašava važnost stabilne internetske veze i dovoljno serverskih resursa tijekom procesa ažuriranja WordPressa, tema ili pluginova, kako bi se smanjila vjerojatnost prekida koji bi mogli dovesti do ovakvog zaglavljivanja. Korisnici bi također trebali biti svjesni postojanja ove datoteke i znati kako je ručno ukloniti ako dođe do problema, jer je rješenje često brzo i lako primjenjivo.

### **10\. Greška Prekoračenja Memorijskog Limita (Allowed Memory Size Exhausted / Memory Limit Error)**

Detaljan Opis:  
Ova fatalna greška javlja se kada PHP skripta na vašoj WordPress stranici pokuša alocirati više memorije nego što joj je dodijeljeno konfiguracijom servera ili WordPressa. Poruka o grešci obično izgleda ovako: "Fatal error: Allowed memory size of XXXXXX bytes exhausted (tried to allocate YYYYYY bytes) in /path/to/some/file.php on line ZZZ".2 To može dovesti do djelomično učitane stranice ili potpunog prekida njenog rada.  
**Najčešći Uzroci:**

* **Nedovoljan PHP memorijski limit:** Zadana vrijednost PHP memorijskog limita na serveru ili unutar WordPress konfiguracije može biti preniska za potrebe vaše stranice, posebno ako koristite mnogo pluginova ili resursno zahtjevnu temu.2  
* **Loše kodiran ili resursno zahtjevan plugin ili tema:** Neki pluginovi ili teme mogu biti neefikasno napisani i trošiti prekomjernu količinu memorije.2  
* **Obrada velikih slika ili podataka:** Operacije poput učitavanja vrlo velikih slika, generiranja kompleksnih izvještaja ili obrade velikih skupova podataka mogu zahtijevati više memorije.  
* **Dijeljeni (shared) hosting s niskim ograničenjima resursa:** Na jeftinijim hosting paketima, dostupni resursi, uključujući PHP memoriju, često su strogo ograničeni.6

Koraci za Rješavanje:  
Primarno rješenje je povećanje PHP memorijskog limita. To se može učiniti na nekoliko načina:

1. **Uređivanje wp-config.php datoteke:** Dodajte ili izmijenite sljedeću liniju u wp-config.php datoteci, prije retka /\* That's all, stop editing\! Happy publishing. \*/ 1:  
   PHP  
   define('WP\_MEMORY\_LIMIT', '256M');  
   Možete pokušati i s većim vrijednostima poput 512M ako je potrebno.  
2. **Uređivanje php.ini datoteke:** Ako imate pristup php.ini datoteci na vašem serveru (obično kod VPS ili dediciranih servera), možete izmijeniti vrijednost direktive memory\_limit 2: memory\_limit \= 256M;  
3. **Uređivanje .htaccess datoteke:** U korijensku .htaccess datoteku možete dodati sljedeću liniju 5: php\_value memory\_limit 256M  
4. **Preko kontrolnog panela hostinga:** Neki hosting provideri omogućuju promjenu PHP memorijskog limita direktno kroz njihov kontrolni panel (npr. cPanel, Plesk, ili prilagođeni paneli poput InstaWP spomenutog u 6).  
5. **Deaktivacija pluginova:** Ako povećanje limita ne pomogne ili ako sumnjate na određeni plugin, pokušajte deaktivirati sve pluginove, a zatim ih aktivirajte jedan po jedan kako biste identificirali onaj koji troši previše memorije.2  
6. **Prebacivanje na lakšu, zadanu temu:** Kompleksne teme mogu biti memorijski zahtjevne. Privremeno prebacivanje na zadanu WordPress temu može pomoći u dijagnostici.5  
7. **Optimizacija slika:** Koristite optimizirane slike manjih dimenzija i veličina datoteka.  
8. **Kontaktiranje hosting providera:** Ako ne možete sami povećati limit ili ako sumnjate da je problem u ograničenjima vašeg hosting paketa, obratite se podršci hostinga.5

WordPress stranice, pogotovo one s većim brojem instaliranih pluginova, kompleksnim temama i dinamičnim sadržajem, mogu postati prilično "gladne" serverskih resursa.2 Greška prekoračenja memorijskog limita jasno ističe stalnu potrebu za usklađivanjem funkcionalnosti web stranice s dostupnim resursima servera. Lakoća kojom se u WordPressu dodaju nove funkcionalnosti putem pluginova može navesti korisnike da instaliraju velik broj dodataka bez potpunog razumijevanja njihovog utjecaja na performanse i potrošnju memorije. Ova greška služi kao podsjetnik da postoji granica koliko se funkcionalnosti može dodati prije nego što se dosegnu limiti servera, posebno na cjenovno pristupačnijim dijeljenim hosting planovima. Stoga je važno da korisnici budu selektivni pri odabiru pluginova, da biraju dobro optimizirane teme i da razmotre hosting paket koji nudi adekvatne resurse za njihove trenutne i buduće potrebe.

### **11\. Greška Prekoračenja Maksimalnog Vremena Izvršavanja (Maximum Execution Time Exceeded)**

Detaljan Opis:  
Ova fatalna greška javlja se kada PHP skripta na vašoj WordPress stranici traje duže od maksimalno dopuštenog vremena izvršavanja koje je postavljeno na serveru. Umjesto da se skripta uspješno završi, WordPress prikazuje poruku o grešci, npr. "Fatal error: Maximum execution time of 30 seconds exceeded in /path/to/script.php on line X".2 Zadano vrijeme izvršavanja na mnogim serverima je 30 ili 60 sekundi.  
**Najčešći Uzroci:**

* **Neefikasan ili loše optimiziran kod u temi ili pluginu:** Dugačke petlje, kompleksni upiti u bazu podataka ili općenito loše napisan kod mogu uzrokovati da skripta traje predugo.2  
* **Obrada velikih datoteka ili podataka:** Operacije poput uvoza/izvoza velikih CSV datoteka, generiranja velikih sigurnosnih kopija ili obrade velikog broja slika odjednom mogu prekoračiti vremenski limit.  
* **Problemi s vanjskim API-jima:** Ako vaša stranica komunicira s vanjskim servisima putem API-ja, a ti servisi sporo odgovaraju, to može produžiti vrijeme izvršavanja vaše skripte.  
* **Nisko postavljeno maksimalno vrijeme izvršavanja na serveru:** Ponekad je zadani max\_execution\_time na serveru jednostavno prenizak za određene legitimne, ali dugotrajne WordPress operacije.2

**Koraci za Rješavanje:**

1. **Povećanje maksimalnog vremena izvršavanja:**  
   * **U php.ini datoteci:** Ako imate pristup, pronađite i povećajte vrijednost max\_execution\_time. Na primjer: max\_execution\_time \= 300 (za 300 sekundi).2  
   * **U .htaccess datoteci:** Dodajte liniju: php\_value max\_execution\_time 300\.2  
   * **U wp-config.php datoteci:** Ponekad se može koristiti set\_time\_limit(300); na početku wp-config.php ili unutar problematične skripte, ali ovo ne funkcionira uvijek ovisno o konfiguraciji servera i PHP safe modu.  
   * **Kontaktiranje hosting providera:** Mnogi hosting provideri (poput Kinsta, kako je navedeno u 2) mogu vam pomoći povećati ovaj limit ili to možete učiniti sami putem njihovog kontrolnog panela.  
2. **Deaktivacija pluginova i prebacivanje na zadanu temu:** Kao i kod drugih grešaka, ovo pomaže identificirati je li problematičan kod u nekom pluginu ili temi.2 Deaktivirajte sve pluginove, pa ih aktivirajte jedan po jedan.  
3. **Optimizacija koda ili pronalaženje alternative:** Ako je problem u specifičnom pluginu ili temi, provjerite postoji li ažurirana verzija, kontaktirajte autora za podršku ili potražite bolje optimiziranu alternativu.  
4. **Korištenje WP-CLI za dugotrajne operacije:** Za zadatke poput velikih uvoza podataka, korištenje WP-CLI (WordPress Command Line Interface) može zaobići HTTP vremenska ograničenja jer se skripte izvršavaju direktno na serveru.2

Slično grešci prekoračenja memorijskog limita, i ova greška često ukazuje na skrivene probleme s performansama koda ili na operacije koje su prezahtjevne za trenutnu konfiguraciju servera.2 Dok povećanje max\_execution\_time može biti nužno i privremeno riješiti problem, omogućujući skripti da se dovrši, važno je razumjeti zašto skripta uopće traje toliko dugo. Ako se radi o redovitoj operaciji ili o ključnoj funkcionalnosti plugina ili teme, a skripta je neefikasna, to može nepotrebno opterećivati server, usporavati cjelokupno iskustvo za sve korisnike i trošiti dragocjene serverske resurse. Stoga, iako je povećanje limita ponekad neizbježno (npr. za jednokratni veliki uvoz podataka), dugoročno je preporučljivije istražiti mogućnosti optimizacije problematičnog koda, pronalaženje efikasnije alternative za plugin ili temu, ili razbijanje dugotrajnih procesa na manje, upravljivije dijelove.

### **12\. 403 Forbidden (Pristup Zabranjen)**

Detaljan Opis:  
Greška 403 Forbidden znači da web server razumije zahtjev koji je klijent (preglednik) poslao, ali odbija odobriti pristup traženom resursu (stranici, datoteci, direktoriju).2 Za razliku od 404 greške gdje server ne može pronaći resurs, kod 403 greške server pronalazi resurs, ali namjerno blokira pristup.  
**Najčešći Uzroci:**

* **Neispravne dozvole za datoteke i mape:** Ovo je vrlo čest uzrok. Ako datoteke ili mape nemaju ispravno postavljene dozvole, server može spriječiti pristup radi sigurnosti.2  
* **Oštećena ili neispravno konfigurirana .htaccess datoteka:** .htaccess datoteka može sadržavati sigurnosna pravila (npr. Deny from all) ili pravila za IP blokiranje koja pogrešno blokiraju pristup.2  
* **Problem s pluginom:** Sigurnosni pluginovi ili pluginovi za vatrozid mogu identificirati određene IP adrese ili obrasce ponašanja kao sumnjive i blokirati pristup, ponekad i greškom.2  
* **Problemi s CDN-om (Content Delivery Network):** Neispravna konfiguracija CDN-a ili problemi u komunikaciji između CDN-a i servera mogu rezultirati 403 greškom.2  
* **Hotlink zaštita:** Ako je hotlink zaštita (sprječavanje drugih stranica da direktno linkaju na vaše slike/resurse) pogrešno konfigurirana, može blokirati i legitiman pristup.2  
* **Problemi s vlasništvom datoteka (file ownership) na serveru:** Ako datoteke ne pripadaju ispravnom korisniku na serveru, pristup može biti odbijen.  
* **Nedostaje index datoteka:** Ako direktorij nema index.php ili index.html datoteku, a listanje sadržaja direktorija je onemogućeno na serveru (što je dobra sigurnosna praksa), pokušaj pristupa tom direktoriju može rezultirati 403 greškom.

**Koraci za Rješavanje:**

1. **Resetiranje dozvola za datoteke i mape:** Putem FTP klijenta, postavite dozvole za mape na 755 i za datoteke na 644\.2 Za wp-config.php preporučuje se 600\.  
2. **Generiranje nove .htaccess datoteke:** Preimenujte postojeću .htaccess datoteku (npr. u .htaccess\_old). Zatim idite u WordPress admin na Postavke \> Trajne veze i kliknite "Spremi promjene" kako biste generirali novu.2  
3. **Deaktivacija svih pluginova:** Posebno obratite pažnju na sigurnosne pluginove ili one koji upravljaju pristupom. Preimenujte mapu plugins putem FTP-a da ih sve deaktivirate, pa provjerite rješava li to problem. Ako da, aktivirajte ih jedan po jedan.2  
4. **Privremeno onemogućavanje CDN-a:** Ako koristite CDN, privremeno ga deaktivirajte da vidite je li on uzrok.2  
5. **Provjera konfiguracije hotlink zaštite:** Ako ste je nedavno omogućili, provjerite njene postavke.2  
6. **Kontaktiranje hosting providera:** Ako sumnjate na probleme s vlasništvom datoteka, serverskim vatrozidom ili drugim serverskim konfiguracijama, obratite se podršci hostinga.2

Greške 403 Forbidden često proizlaze iz sigurnosnih mehanizama koji su postavljeni da štite web stranicu, bilo da su ti mehanizmi ispravno ili pogrešno konfigurirani.2 Postoji osjetljiva ravnoteža između osiguravanja stranice od neovlaštenog pristupa i potencijalnog slučajnog blokiranja legitimnih korisnika ili čak samog administratora. Dozvole datoteka, pravila u .htaccess datoteci, te funkcionalnosti sigurnosnih pluginova svi služe kao slojevi kontrole pristupa. Međutim, ako su ti slojevi previše restriktivni ili ako dođe do greške u njihovoj konfiguraciji (npr. sigurnosni plugin pogrešno identificira vašu IP adresu kao sumnjivu), može doći do 403 greške. Ovo naglašava važnost pažljivog postavljanja i testiranja bilo kakvih sigurnosnih mjera. Korisnici bi trebali razumjeti kako te mjere funkcioniraju kako bi izbjegli nenamjerno zaključavanje dijelova svoje stranice ili cijele stranice, te znati kako dijagnosticirati problem ako do njega dođe.

### **13\. "Sorry, You Are Not Allowed to Access This Page" (Žao nam je, nemate dopuštenje za pristup ovoj stranici)**

Detaljan Opis:  
Ova poruka o grešci pojavljuje se unutar WordPress administratorskog sučelja i sprječava korisnika da pristupi određenim stranicama ili izvrši određene radnje, čak i ako bi prema svojoj korisničkoj ulozi trebao imati ta dopuštenja.2 Može se pojaviti prilikom pokušaja pristupa postavkama, pluginovima, temama ili drugim dijelovima nadzorne ploče.  
**Najčešći Uzroci:**

* **Neispravne dozvole za datoteke:** Iako slično 403 grešci, ovdje se problem može manifestirati unutar WordPressa zbog problema s pristupom određenim skriptama.2  
* **Netočna korisnička uloga ili oštećene korisničke sposobnosti (capabilities):** Korisnička uloga (npr. Administrator, Editor) možda je pogrešno postavljena ili su podaci o sposobnostima tog korisnika u bazi podataka oštećeni.2  
* **Neispravan prefiks baze podataka:** Ako je prefiks tablica u wp-config.php datoteci (varijabla $table\_prefix) različit od stvarnog prefiksa tablica u bazi podataka (npr. nakon migracije ili neuspjelog ažuriranja), WordPress neće moći ispravno čitati korisničke podatke i dozvole.2  
* **Konflikt s pluginom ili temom:** Sigurnosni pluginovi, pluginovi za upravljanje korisničkim ulogama ili čak loše kodirane teme mogu ometati sustav dozvola.2  
* **Problem s wp-config.php datotekom:** Greške u wp-config.php, posebno nakon ručnih izmjena, ažuriranja ili migracije.  
* **Problemi s Multisite konfiguracijom:** U WordPress Multisite instalacijama, problemi s mrežnim postavkama ili dodjelom uloga mogu dovesti do ove greške.  
* **Ažuriranje PHP verzije:** Ponekad, nakon ažuriranja PHP verzije na serveru, može doći do nekompatibilnosti koja uzrokuje ovu grešku ako neki plugin ili tema nisu usklađeni s novom verzijom.

**Koraci za Rješavanje:**

1. **Provjera i resetiranje dozvola za datoteke:** Kao i kod 403 greške, provjerite i postavite dozvole za mape na 755 i datoteke na 644 putem SFTP/FTP-a.2  
2. **Provjera korisničke uloge putem phpMyAdmina:** Pristupite svojoj WordPress bazi podataka putem phpMyAdmina (ili sličnog alata). Provjerite tablicu wp\_users (ili \<prefiks\>\_users) da biste pronašli svoj korisnički ID. Zatim u tablici wp\_usermeta (ili \<prefiks\>\_usermeta) pronađite redak gdje je user\_id jednak vašem ID-u, a meta\_key je wp\_capabilities (ili \<prefiks\>\_capabilities). Vrijednost (meta\_value) bi trebala izgledati otprilike ovako za administratora: a:1:{s:13:"administrator";b:1;}. Ako je neispravna, možda ćete je morati ručno ispraviti ili vratiti iz sigurnosne kopije.2  
3. **Provjera i ispravljanje prefiksa baze podataka:** Otvorite wp-config.php i provjerite vrijednost $table\_prefix. Zatim u phpMyAdminu provjerite koriste li vaše WordPress tablice taj isti prefiks. Ako se ne podudaraju, morate ih uskladiti (obično se mijenja $table\_prefix u wp-config.php da odgovara stvarnom prefiksu u bazi).2 **Napravite sigurnosnu kopiju prije bilo kakvih izmjena\!**  
4. **Deaktivacija pluginova i prebacivanje na zadanu temu:** Standardni korak za provjeru konflikata. Preimenujte mapu plugins i mapu aktivne teme putem FTP-a.2  
5. **Provjera wp-config.php datoteke:** Pažljivo pregledajte wp-config.php na bilo kakve nedavne izmjene ili očite greške.  
6. **Vraćanje sigurnosne kopije:** Ako ništa drugo ne uspije, vraćanje na nedavnu, ispravnu sigurnosnu kopiju može biti rješenje.2  
7. **Ako je problem nakon ažuriranja PHP-a:** Pokušajte se vratiti na prethodnu, stabilnu PHP verziju putem hosting kontrolnog panela da vidite rješava li to problem. Ako da, neki plugin ili tema vjerojatno nisu kompatibilni.

Ova greška, za razliku od općenitije 403 Forbidden greške koja je često vezana uz serverske postavke, ukazuje na probleme unutar samog WordPress sustava korisničkih uloga i dozvola, često na razini baze podataka.2 WordPress pohranjuje informacije o korisničkim ulogama (Administrator, Editor, Author, itd.) i njihovim specifičnim sposobnostima (npr. publish\_posts, edit\_themes) u tablicama baze podataka, prvenstveno u wp\_usermeta (ili tablici s odgovarajućim prefiksom). Ako su ti podaci oštećeni, ili ako WordPress zbog problema s prefiksom tablica u wp-config.php ne može ispravno pročitati te podatke, neće moći točno identificirati što određeni korisnik smije, a što ne smije raditi unutar admin sučelja. Rješavanje ovog problema stoga često zahtijeva direktnu interakciju s bazom podataka putem alata kao što je phpMyAdmin, što može biti zastrašujuće i rizično za korisnike koji nisu tehnički potkovani. Stoga je iznimno važno postupati s oprezom i uvijek imati svježu sigurnosnu kopiju baze podataka prije bilo kakvih ručnih izmjena.

### **14\. "Installation Failed: Could Not Create Directory" (Instalacija Nije Uspjela: Nije Moguće Stvoriti Direktorij)**

Detaljan Opis:  
Ova poruka o grešci pojavljuje se kada WordPress pokuša instalirati novu temu ili plugin, ili ažurirati postojeći, ali ne uspijeva stvoriti potrebne direktorije (mape) na serveru.2 Proces instalacije ili ažuriranja se prekida.  
**Najčešći Uzroci:**

* **Neispravne dozvole za pisanje (Write permissions):** Ovo je glavni uzrok. WordPress procesu (koji se izvršava pod određenim korisnikom na serveru) nedostaje dozvola za stvaranje novih mapa unutar ključnih WordPress direktorija, najčešće unutar wp-content (gdje se nalaze plugins i themes mape), ali ponekad i za wp-admin ili wp-includes.2  
* **Problem s vlasništvom datoteka (file ownership) na serveru:** Ako datoteke i mape WordPress instalacije ne pripadaju korisniku pod kojim se web server izvršava, mogu se pojaviti problemi s dozvolama čak i ako su numeričke vrijednosti dozvola (npr. 755\) ispravne.  
* **Nedostatak prostora na disku:** Ako je hosting račun dosegao svoj limit prostora na disku, nove datoteke i mape se ne mogu stvoriti.  
* **Ograničenja od strane hosting providera:** Neki hosting provideri mogu imati specifična ograničenja ili sigurnosne postavke koje sprječavaju stvaranje direktorija putem PHP skripti.

**Koraci za Rješavanje:**

1. **Provjera i postavljanje ispravnih dozvola za direktorije:** Putem FTP klijenta, provjerite dozvole za mape wp-content, wp-admin i wp-includes. One bi trebale biti postavljene na 755\. Ako nisu, promijenite ih. Unutar wp-content, mape plugins i themes također trebaju imati dozvolu 755\.2  
2. **Kontaktiranje hosting providera:** Ako sumnjate na problem s vlasništvom datoteka ili serverskim ograničenjima, obratite se tehničkoj podršci vašeg hostinga. Oni mogu provjeriti i ispraviti vlasništvo ili vas obavijestiti o eventualnim ograničenjima.2  
3. **Provjera dostupnog prostora na disku:** U kontrolnom panelu vašeg hostinga provjerite koliko prostora na disku koristite i imate li dovoljno slobodnog prostora.  
4. **Pokušajte s ručnom instalacijom:** Ako automatska instalacija ne uspije, možete pokušati ručno instalirati temu ili plugin. Preuzmite.zip datoteku teme/plugina, raspakirajte je na svom računalu, a zatim putem FTP-a prenesite mapu teme/plugina u odgovarajući direktorij (wp-content/themes ili wp-content/plugins).

WordPressu je za mnoge osnovne operacije, poput instalacije i ažuriranja tema i pluginova, te za učitavanje medijskih datoteka, neophodna sposobnost pisanja po vlastitom datotečnom sustavu na serveru.2 Greška "Could Not Create Directory" direktan je pokazatelj da ta fundamentalna sposobnost nedostaje ili je ograničena. Kada instalirate plugin, WordPress treba stvoriti novu mapu unutar wp-content/plugins i u nju smjestiti datoteke plugina. Ako PHP proces pod kojim WordPress radi nema dozvolu od servera da stvori tu mapu, instalacija ne može uspjeti. Ovo naglašava da ispravno postavljene dozvole datotečnog sustava nisu samo pitanje sigurnosti, već i osnovne funkcionalnosti WordPressa. Korisnici moraju osigurati da WordPress ima potrebna prava za pisanje u relevantne direktorije, ali istovremeno paziti da te dozvole ne budu previše permisivne (npr. 777), što bi moglo otvoriti sigurnosne propuste.

### **15\. Greška Neispravnih Dozvola za Datoteke (Incorrect File Permissions)**

Detaljan Opis:  
Ovo je općenitiji problem gdje web server ne može pravilno čitati, pisati ili izvršavati datoteke i mape unutar WordPress instalacije zbog pogrešno postavljenih dozvola (permissions). Može se manifestirati na mnogo različitih načina, uključujući nemogućnost ažuriranja WordPressa, tema ili pluginova, probleme s učitavanjem slika, prikazivanje grešaka poput "Sorry, You Are Not Allowed to Access This Page" ili "Installation Failed: Could Not Create Directory", pa čak i sigurnosne ranjivosti ako su dozvole previše labave.2  
**Najčešći Uzroci:**

* **Pogrešna primjena dozvola:** Tijekom ručne instalacije WordPressa, migracije stranice na novi server, ili čak od strane nekih loše konfiguriranih skripti ili hosting panela, dozvole mogu biti pogrešno postavljene.2  
* **Sigurnosni propusti ili hakerski napadi:** Ako napadači dobiju pristup serveru, mogu promijeniti dozvole kako bi si olakšali daljnje djelovanje ili oštetili stranicu.2  
* **Problemi s hosting providerom:** U rijetkim slučajevima, konfiguracijske promjene na serveru od strane hosting providera mogu utjecati na dozvole.2  
* **Konflikti s pluginima ili temama:** Iako rjeđe, neki loše napisani pluginovi ili teme mogu pokušati promijeniti dozvole datoteka na neispravan način.2

Koraci za Rješavanje:  
Ispravljanje neispravnih dozvola obično se vrši putem FTP ili SFTP klijenta (npr. FileZilla). Preporučene numeričke vrijednosti dozvola za WordPress su 2:

* **Mape (direktoriji):** 755  
  * Vlasnik (Owner): Čitanje, Pisanje, Izvršavanje (Read, Write, Execute)  
  * Grupa (Group): Čitanje, Izvršavanje (Read, Execute)  
  * Ostali (Public/Others): Čitanje, Izvršavanje (Read, Execute)  
* **Datoteke (files):** 644  
  * Vlasnik: Čitanje, Pisanje (Read, Write)  
  * Grupa: Čitanje (Read)  
  * Ostali: Čitanje (Read)  
* **wp-config.php datoteka:** 600 (ili 440, 400 za dodatnu sigurnost)  
  * Vlasnik: Čitanje, Pisanje (Read, Write)  
  * Grupa: Nema dozvola  
  * Ostali: Nema dozvola

**Postupak promjene dozvola (npr. koristeći FileZilla):**

1. Povežite se na svoj server putem FTP/SFTP klijenta.  
2. Navigirajte do korijenskog direktorija vaše WordPress instalacije.  
3. Za **mape**: Odaberite sve mape (npr. wp-admin, wp-content, wp-includes i njihove podmape). Desni klik \> File permissions... Unesite 755\. Označite "Recurse into subdirectories" i odaberite "Apply to directories only". Kliknite OK.  
4. Za **datoteke**: Odaberite sve datoteke u korijenskom direktoriju i unutar svih mapa. Desni klik \> File permissions... Unesite 644\. Označite "Recurse into subdirectories" i odaberite "Apply to files only". Kliknite OK.  
5. Za **wp-config.php**: Pronađite wp-config.php u korijenskom direktoriju. Desni klik \> File permissions... Unesite 600 (ili 440/400). Kliknite OK.

Ako niste sigurni u vezi vlasništva datoteka (file ownership), kontaktirajte svog hosting providera.

Ispravne dozvole za datoteke i mape predstavljaju temelj kako sigurnosti tako i funkcionalnosti WordPress web stranice.2 One diktiraju tko (vlasnik datoteke/mape, grupa kojoj vlasnik pripada, i svi ostali korisnici na serveru) može čitati sadržaj, mijenjati ga (pisati) ili ga izvršavati (ako se radi o skripti ili programu). Ako su dozvole postavljene previše labavo (npr. 777 za mape ili 666 za datoteke), to stvara značajan sigurnosni rizik jer omogućuje potencijalno zlonamjernim procesima ili korisnicima da lakše modificiraju vaše datoteke ili ubace štetan kod. S druge strane, ako su dozvole previše restriktivne, sam WordPress (koji se na serveru izvršava kao određeni korisnički proces, npr. www-data) neće moći obavljati svoje osnovne zadatke, poput pisanja u wp-content mapu prilikom instalacije plugina, učitavanja slika, ili kreiranja cache datoteka. Preporučene vrijednosti (755 za mape, 644 za datoteke, te strože 600 za osjetljivu wp-config.php datoteku) predstavljaju optimalan balans između omogućavanja WordPressu da normalno funkcionira i zaštite datotečnog sustava od neovlaštenih promjena. Stoga je ključno da korisnici razumiju osnove sustava dozvola i redovito provjeravaju jesu li one ispravno postavljene, posebno nakon migracija, promjena na serveru, ili ako postoji sumnja na sigurnosni incident.

### **16\. Upozorenja o Miješanom Sadržaju (Mixed Content Warnings \- SSL related)**

Detaljan Opis:  
Upozorenja o miješanom sadržaju javljaju se kada je vaša WordPress stranica učitana preko sigurnog HTTPS protokola (što označava da imate instaliran SSL certifikat), ali neki od resursa na toj stranici (poput slika, videozapisa, CSS stilskih datoteka, JavaScript datoteka, fontova itd.) i dalje se učitavaju preko nesigurnog HTTP protokola.2 Preglednici poput Chromea, Firefoxa i drugih će u takvim slučajevima prikazati upozorenje u adresnoj traci (npr. ikona lokota može biti prekrižena ili će pisati "Not Secure") jer miješani sadržaj kompromitira sigurnost inače sigurne HTTPS veze.2  
**Najčešći Uzroci:**

* **Tvrdo kodirani HTTP URL-ovi:** Prilikom izrade teme, plugina ili unosa sadržaja, developeri ili korisnici su možda izravno unijeli URL-ove s http:// prefiksom umjesto relativnih putanja ili https://.2  
* **Sadržaj učitan prije instalacije SSL-a:** Ako su slike i druge medijske datoteke učitane na stranicu dok je ona još koristila HTTP, njihovi URL-ovi u WordPress bazi podataka ostat će s http:// prefiksom čak i nakon instalacije SSL certifikata.2  
* **Vanjski resursi učitani putem HTTP-a:** Ako vaša stranica koristi skripte, fontove, iframeove ili druge resurse s vanjskih web stranica koje se poslužuju putem HTTP-a, to će uzrokovati upozorenje o miješanom sadržaju.2  
* **CSS ili JavaScript datoteke koje pozivaju HTTP resurse:** Ponekad stilske datoteke (CSS) ili skripte (JavaScript) unutar sebe mogu sadržavati linkove na druge resurse (npr. pozadinske slike, fontove) putem HTTP-a.

**Koraci za Rješavanje:**

1. **Identifikacija HTTP resursa pomoću alata za razvojne programere:** U većini preglednika (Chrome, Firefox, Edge), otvorite svoju stranicu, desnom tipkom miša kliknite bilo gdje i odaberite "Inspect" ili "Inspect Element". Idite na karticu "Console". Preglednik će ovdje prikazati upozorenja o miješanom sadržaju, navodeći točne HTTP URL-ove koji uzrokuju problem.2  
2. **Ažuriranje URL-ova u WordPress bazi podataka:** Za sadržaj (poput slika u objavama) čiji su URL-ovi pohranjeni u bazi s HTTP-om, potrebno ih je ažurirati na HTTPS. To se može učiniti:  
   * **Pomoću plugina:** Plugini poput "Better Search Replace" omogućuju jednostavno pretraživanje i zamjenu svih instanci http://vasadomena.com s https://vasadomena.com u bazi podataka.2 Budite oprezni i napravite sigurnosnu kopiju baze prije korištenja.  
   * **Ručno putem phpMyAdmina:** Ovo zahtijeva oprez. Možete koristiti SQL upite za pronalaženje i zamjenu URL-ova u relevantnim tablicama (npr. wp\_posts, wp\_postmeta).  
3. **Provjera i ispravljanje URL-ova u datotekama teme i plugina:** Pregledajte datoteke vaše aktivne teme i instaliranih pluginova na tvrdo kodirane HTTP URL-ove i zamijenite ih s HTTPS ili koristite relativne putanje ili WordPress funkcije za generiranje URL-ova (npr. get\_stylesheet\_directory\_uri()).  
4. **Ažuriranje WordPress adrese i adrese web-mjesta:** U WordPress admin sučelju, idite na Postavke \> Općenito i provjerite jesu li "WordPress adresa (URL)" i "Adresa web-mjesta (URL)" postavljene na HTTPS verziju vaše domene.2  
5. **Provjera vanjskih resursa:** Ako učitavate skripte, fontove ili druge elemente s vanjskih stranica, provjerite nude li ti servisi HTTPS verzije i ažurirajte linkove. Ako ne, razmislite o pronalaženju alternative ili hostiranju tih resursa lokalno (ako je moguće i dopušteno).  
6. **Konfiguracija CDN-a za HTTPS:** Ako koristite Content Delivery Network (CDN), osigurajte da je konfiguriran za isporuku sadržaja putem HTTPS-a.2  
7. **Korištenje Content-Security-Policy zaglavlja:** Napredniji korisnici mogu konfigurirati Content-Security-Policy (CSP) HTTP zaglavlje s direktivom upgrade-insecure-requests koja nalaže pregledniku da automatski pokuša učitati HTTP resurse preko HTTPS-a.

Posjedovanje SSL certifikata i prelazak na HTTPS samo je prvi korak prema osiguravanju web stranice. Da bi stranica bila istinski sigurna i da bi se izbjegla upozorenja o miješanom sadržaju koja mogu narušiti povjerenje posjetitelja, apsolutno je nužno da se *svi* resursi koje stranica učitava također poslužuju putem HTTPS protokola.2 Mnogi korisnici previde ovaj korak, misleći da je instalacija certifikata dovoljna. Međutim, ako slike, skripte ili stilovi – posebno oni dodani prije implementacije SSL-a ili oni koji su tvrdo kodirani s HTTP linkovima – i dalje koriste nesigurni protokol, cjelokupna sigurnost HTTPS veze je kompromitirana. Preglednici ovo signaliziraju jer miješani (HTTP) sadržaj na HTTPS stranici može biti presretnut ili izmijenjen od strane napadača (tzv. "man-in-the-middle" napad), čime se poništavaju prednosti SSL enkripcije. Stoga, nakon implementacije SSL-a, slijedi ključan, često zanemaren, korak temeljite provjere i ažuriranja svih internih i eksternih URL-ova na HTTPS.

### **17\. ERR\_TOO\_MANY\_REDIRECTS (Previše Preusmjeravanja)**

Detaljan Opis:  
Greška "ERR\_TOO\_MANY\_REDIRECTS" (ili slična poruka ovisno o pregledniku, npr. "Stranica se ne preusmjerava pravilno" u Firefoxu) javlja se kada preglednik zaglavi u beskonačnoj petlji preusmjeravanja.2 To znači da URL A preusmjerava na URL B, koji zatim preusmjerava natrag na URL A, ili se stvara duži lanac preusmjeravanja koji se vrti u krug, sprječavajući učitavanje stranice.  
**Najčešći Uzroci:**

* **Pogrešna konfiguracija preusmjeravanja na serveru ili u WordPressu:** Ovo je najčešći uzrok. Neispravno postavljena pravila preusmjeravanja u .htaccess datoteci (za Apache servere) ili u konfiguraciji Nginx servera mogu stvoriti petlju.2 Također, WordPress pluginovi za upravljanje preusmjeravanjima mogu biti pogrešno konfigurirani.  
* **Neispravne WordPress adrese (Site URL, Home URL):** Neslaganje između WordPress adrese (URL) i Adrese web-mjesta (URL) u WordPress postavkama (Postavke \> Općenito), posebno ako postoji razlika između http:// i https:// verzija, ili između www. i ne-www. verzija domene, može dovesti do petlje preusmjeravanja.2  
* **Problemi s SSL certifikatom ili HTTPS postavkama:** Ako SSL certifikat nije ispravno instaliran, ili ako postoje konfliktne postavke koje forsiraju HTTPS i HTTP istovremeno, može doći do petlje.  
* **Konflikti s pluginovima:** Cache pluginovi, sigurnosni pluginovi ili SEO pluginovi koji upravljaju URL-ovima ili forsiraju SSL mogu ponekad uzrokovati sukobe koji rezultiraju prekomjernim preusmjeravanjima.2  
* **Problemi s CDN-om (Content Delivery Network) ili postavkama proxy servera:** Neispravna konfiguracija CDN-a ili proxyja (npr. Cloudflare) može uzrokovati petlje preusmjeravanja, posebno vezano uz SSL postavke (npr. Flexible SSL mod na Cloudflareu ako server nije konfiguriran za HTTPS).2  
* **Problemi s kolačićima:** Ponekad oštećeni ili neispravni kolačići u pregledniku mogu doprinijeti problemu.

**Koraci za Rješavanje:**

1. **Brisanje kolačića i cachea preglednika:** Ovo je prvi korak koji treba pokušati. Obrišite kolačiće i cache za vašu web stranicu u postavkama preglednika.2  
2. **Provjera i ispravljanje WordPress adresa (Site URL, Home URL):** Provjerite jesu li WordPress adresa (URL) i Adresa web-mjesta (URL) u Postavke \> Općenito ispravno i konzistentno postavljene (npr. obje na https://www.vasadomena.com ili obje na https://vasadomena.com). Ako ne možete pristupiti admin sučelju, ove vrijednosti možete pokušati definirati u wp-config.php datoteci 2:  
   PHP  
   define('WP\_HOME','https://www.vasadomena.com');  
   define('WP\_SITEURL','https://www.vasadomena.com');

3. **Provjera .htaccess datoteke:** Preimenujte .htaccess datoteku (npr. u .htaccess\_old) putem FTP-a da vidite rješava li to problem. Ako da, generirajte novu odlaskom na Postavke \> Trajne veze i spremanjem promjena.2 Pažljivo pregledajte staru .htaccess datoteku na sumnjiva pravila preusmjeravanja.  
4. **Deaktivacija pluginova:** Deaktivirajte sve pluginove preimenovanjem mape plugins putem FTP-a. Ako problem nestane, aktivirajte ih jedan po jedan kako biste pronašli krivca. Posebno obratite pažnju na pluginove za preusmjeravanje, cache, SSL i sigurnost.2  
5. **Provjera SSL certifikata i HTTPS postavki:** Osigurajte da je SSL certifikat ispravno instaliran i da su postavke na serveru i unutar WordPressa (ili plugina koji forsiraju SSL) konzistentne.  
6. **Privremeno onemogućavanje CDN-a:** Ako koristite CDN poput Cloudflarea, privremeno ga pauzirajte ili prebacite u "Development Mode" da vidite utječe li na problem.2 Provjerite SSL postavke unutar CDN-a (npr. na Cloudflareu, ako koristite Flexible SSL, osigurajte da vaša stranica ne forsira HTTPS preusmjeravanje koje bi stvorilo petlju).  
7. **Kontaktiranje hosting providera:** Ako ništa od navedenog ne pomogne, problem može biti u konfiguraciji servera, te je potrebno kontaktirati podršku hostinga.2

Greška "ERR\_TOO\_MANY\_REDIRECTS" često je rezultat složene interakcije ili sukoba između različitih razina konfiguracije koje utječu na URL-ove i preusmjeravanja.2 Preusmjeravanja se mogu definirati na više mjesta: na razini servera (putem .htaccess datoteke na Apacheu ili Nginx konfiguracijskih datoteka), unutar same WordPress aplikacije (kroz postavke Site URL/Home URL ili putem specijaliziranih pluginova za preusmjeravanje), te na razini vanjskih servisa poput CDN-a ili proxy servera koji mogu imati vlastita pravila preusmjeravanja. Ako postoji neusklađenost, konflikt ili pogrešna logika u tim pravilima – na primjer, ako server preusmjerava sav promet na HTTPS verziju stranice, ali WordPress URL je postavljen na HTTP i pokušava preusmjeriti natrag, ili ako jedan plugin forsira www verziju, a drugi ne-www verziju – može doći do beskonačne petlje. Rješavanje ovog problema stoga zahtijeva holistički pristup, gdje se sustavno provjeravaju sve lokacije na kojima se URL-ovi i pravila preusmjeravanja mogu konfigurirati, umjesto fokusiranja na samo jedan izolirani dio sustava.

### **18\. DNS\_PROBE\_FINISHED\_NXDOMAIN**

Detaljan Opis:  
DNS\_PROBE\_FINISHED\_NXDOMAIN je greška koju prikazuje web preglednik (najčešće Google Chrome) kada sustav domenskih imena (DNS) ne može razriješiti (prevesti) uneseno ime domene (npr. vasastranica.com) u odgovarajuću IP adresu servera na kojem se web stranica nalazi.2 NXDOMAIN označava "Non-Existent Domain" (nepostojeća domena), što znači da DNS upit nije uspio pronaći zapis za traženu domenu.  
Najčešći Uzroci:  
Ova greška obično nije specifična za WordPress, već je problem na razini DNS-a ili mrežne povezanosti, ali sprječava pristup WordPress stranici.

* **Domena nije ispravno registrirana ili je istekla:** Ako domena nije kupljena, ako je registracija istekla ili ako je suspendirana, DNS zapisi neće postojati.2  
* **DNS zapisi nisu ispravno konfigurirani ili se još nisu propagirali:** A zapis (koji usmjerava domenu na IP adresu servera) ili CNAME zapis možda nisu točno uneseni kod registrara domene ili DNS hosting providera. Također, nakon promjene DNS zapisa, potrebno je određeno vrijeme (do 24-48 sati) da se promjene propagiraju kroz globalni DNS sustav.2  
* **Problemi s DNS serverima korisnika ili ISP-a:** DNS serveri koje koristi korisnikov uređaj (obično dodijeljeni od strane Internet Service Providera \- ISP-a) mogu biti privremeno nedostupni ili imati problema.2  
* **Problemi s lokalnom mrežnom konfiguracijom korisnika:** Lokalni DNS cache na računalu može sadržavati zastarjele informacije. Vatrozid (firewall), antivirusni softver ili VPN klijent na korisnikovom računalu također mogu ometati DNS upite.2  
* **Problemi s hosting providerom:** Iako rjeđe, server na kojem je stranica hostana može biti nedostupan, što DNS ne može razriješiti.

Koraci za Rješavanje:  
Rješavanje ove greške uključuje korake koje može poduzeti vlasnik web stranice i korake koje može poduzeti posjetitelj (koji su korisni i za dijagnostiku od strane vlasnika):

* **Sa strane vlasnika stranice:**  
  1. **Provjeriti status registracije domene:** Uvjerite se da je vaša domena aktivna i da nije istekla kod vašeg registrara domena.  
  2. **Provjeriti DNS zapise:** Prijavite se na sučelje vašeg registrara domene ili DNS hosting providera i provjerite jesu li A zapisi (i CNAME ako ih koristite) ispravno usmjereni na IP adresu vašeg web servera. Točnu IP adresu servera trebali biste dobiti od svog hosting providera.  
  3. **Pričekati DNS propagaciju:** Ako ste nedavno mijenjali DNS zapise, pričekajte da se promjene propagiraju. Status propagacije možete provjeriti pomoću online alata poput dnschecker.org.  
  4. **Kontaktirati hosting providera:** Ako sumnjate da je problem s vašim serverom ili ako trebate pomoć oko DNS postavki, obratite se podršci hostinga.  
* **Sa strane posjetitelja (ili za dijagnostiku od strane vlasnika):**  
  1. **Osvježiti stranicu i očistiti cache preglednika**.2  
  2. **Isprazniti lokalni DNS cache:** Na Windowsima, otvorite Command Prompt kao administrator i unesite ipconfig /flushdns. Na macOS-u, naredba ovisi o verziji OS-a (npr. sudo killall \-HUP mDNSResponder). Na Linuxu, može biti sudo systemd-resolve \--flush-caches ili slično.2  
  3. **Promijeniti DNS servere na računalu:** Privremeno promijenite DNS servere vašeg računala na javne DNS servere poput Google Public DNS (8.8.8.8 i 8.8.4.4) ili Cloudflare DNS (1.1.1.1 i 1.0.0.1) kako biste vidjeli rješava li to problem.2  
  4. **Ponovno pokrenuti ruter/modem**.2  
  5. **Privremeno onemogućiti vatrozid, antivirusni softver i VPN:** Testirajte pristup stranici s privremeno onemogućenim ovim programima.2  
  6. **Pokušati pristupiti s druge mreže ili uređaja:** Ovo pomaže utvrditi je li problem lokaliziran na vaš uređaj/mrežu ili je širi.

Iako DNS\_PROBE\_FINISHED\_NXDOMAIN greška izravno utječe na dostupnost WordPress web stranice, važno je razumjeti da njen korijen leži izvan same WordPress instalacije.2 DNS (Domain Name System) je fundamentalni dio internetske infrastrukture koji prethodi bilo kakvoj interakciji s web serverom na kojem se nalazi WordPress. Ako DNS sustav ne može ispravno prevesti ime domene u IP adresu, preglednik korisnika nikada neće ni uspostaviti vezu s serverom, pa samim time ni s WordPressom. Uzroci su najčešće vezani uz administrativne aspekte domene (registracija, istek), konfiguraciju DNS zapisa (koja se obavlja kod registrara domene ili specijaliziranog DNS providera), ili probleme s mrežnom infrastrukturom i DNS serverima koje koristi krajnji korisnik. To znači da vlasnici web stranica ovu grešku ne mogu riješiti unutar WordPress administratorskog sučelja. Umjesto toga, rješavanje zahtijeva provjeru i potencijalne izmjene postavki kod registrara domene, razumijevanje osnova DNS-a i, u nekim slučajevima, strpljivo čekanje da se DNS promjene propagiraju globalno.

### **19\. "Destination Folder Already Exists" (Odredišna Mapa Već Postoji)**

Detaljan Opis:  
Greška "Destination Folder Already Exists" (Odredišna mapa već postoji) javlja se u WordPressu kada pokušavate instalirati temu ili plugin, a WordPress detektira da mapa s istim nazivom kao tema ili plugin koji instalirate već postoji na serveru unutar odgovarajućeg direktorija (wp-content/themes/ ili wp-content/plugins/).2 Ova greška prekida proces instalacije.  
**Najčešći Uzroci:**

* **Prekinuta prethodna instalacija ili ažuriranje:** Ako je prethodni pokušaj instalacije ili ažuriranja iste teme ili plugina bio prekinut (npr. zbog problema s vezom, isteka vremena servera, ili ručnog otkazivanja), mapa je možda ostala djelomično stvorena na serveru.6  
* **Neispravno uklanjanje prethodne verzije:** Ako je tema ili plugin prethodno bio instaliran pa zatim uklonjen putem WordPress sučelja, ponekad proces uklanjanja ne izbriše u potpunosti mapu s servera.6  
* **Ručno preimenovanje ili kopiranje mape:** Ako ste ručno putem FTP-a prenijeli ili preimenovali mapu teme/plugina, a zatim pokušavate instalirati istu komponentu putem WordPress administratorskog sučelja, sustav će detektirati postojeću mapu.6  
* **Vraćanje iz sigurnosne kopije:** Ako ste vratili datoteke iz sigurnosne kopije koja je sadržavala tu temu/plugin, a zatim pokušavate "čistu" instalaciju.

Koraci za Rješavanje:  
Rješenje je obično jednostavno i uključuje uklanjanje ili preimenovanje postojeće mape:

1. **Pristupite datotekama vaše stranice putem FTP-a ili File Managera:** Povežite se na svoj server koristeći FTP klijent ili File Manager u vašem hosting kontrolnom panelu.6  
2. **Navigirajte do odgovarajućeg direktorija:**  
   * Ako instalirate **temu**, idite u mapu wp-content/themes/.  
   * Ako instalirate **plugin**, idite u mapu wp-content/plugins/.6  
3. **Pronađite postojeću mapu:** Unutar themes ili plugins direktorija, pronađite mapu koja ima isti naziv kao tema ili plugin koji pokušavate instalirati. Naziv mape obično odgovara "slug-u" teme/plugina (npr. akismet za Akismet plugin).  
4. **Preimenujte ili izbrišite postojeću mapu:**  
   * **Preporučeni prvi korak je preimenovanje:** Desnom tipkom miša kliknite na mapu i odaberite opciju za preimenovanje. Dodajte \_old ili \_backup na kraj naziva mape (npr. naziv-teme postaje naziv-teme\_old).6 Ovo čuva datoteke ako vam zatrebaju.  
   * **Alternativno, možete izbrisati mapu:** Ako ste sigurni da vam sadržaj mape ne treba, možete je izbrisati. **Budite oprezni prilikom brisanja\!**  
5. **Ponovni pokušaj instalacije:** Vratite se u WordPress administratorsko sučelje i ponovno pokušajte instalirati temu ili plugin. Sada bi instalacija trebala proći bez greške jer više ne postoji mapa koja bi uzrokovala konflikt.6  
6. **Brisanje preimenovane mape (opcionalno):** Ako je instalacija uspjela i sve radi ispravno s novom verzijom, možete se vratiti putem FTP-a i izbrisati staru, preimenovanu mapu (npr. naziv-teme\_old) kako biste oslobodili prostor na disku.6

WordPress, prilikom instalacije novih komponenti poput tema ili pluginova, očekuje "čist" prostor, odnosno da ne postoji već direktorij s istim imenom u koji bi trebao smjestiti datoteke.6 Greška "Destination Folder Already Exists" zapravo je sigurnosna mjera koja sprječava WordPress da automatski prebriše sadržaj postojeće mape, što bi moglo dovesti do gubitka podataka ili neočekivanog ponašanja ako je postojeća mapa bila dio druge, možda modificirane, instalacije. Međutim, ova mjera postaje problem kada je postojeća mapa ostatak neuspjele ili nepotpune prethodne instalacije ili ažuriranja. U takvim situacijama, WordPress ne čisti uvijek automatski za sobom, te je potrebna ručna intervencija korisnika putem FTP-a ili File Managera kako bi se uklonila konfliktna mapa i oslobodio put za novu instalaciju. Ovo služi kao podsjetnik da, iako WordPress automatizira mnoge procese, ponekad je direktan pristup datotečnom sustavu neophodan za rješavanje specifičnih problema.

### **20\. Greška Nedostajuće Stilske Datoteke Teme (Theme Stylesheet Missing Error)**

Detaljan Opis:  
Greška "Theme Stylesheet Missing" (ili slična poruka poput "The parent theme is missing. Please install the parent theme \[...\]" ako se radi o child temi čiji roditelj nedostaje) javlja se kada pokušavate instalirati ili aktivirati WordPress temu, a WordPress ne može pronaći ključnu datoteku style.css na očekivanom mjestu unutar arhive ili mape teme.2 Ova datoteka je esencijalna jer sadrži ne samo CSS stilove, već i informacijsko zaglavlje koje WordPressu govori o temi (naziv, autor, verzija itd.). Bez nje, WordPress ne može prepoznati paket kao valjanu temu.  
**Najčešći Uzroci:**

* **Datoteka style.css zaista nedostaje:** Najjednostavniji uzrok – datoteka style.css nije prisutna u korijenskoj mapi teme.2  
* **Pogrešno ime datoteke:** Datoteka se možda zove drugačije, npr. Style.css (s velikim slovom) ili stylesheet.css. WordPress očekuje točno style.css (sva mala slova).2  
* **style.css nije u korijenskoj mapi teme:** Datoteka style.css mora biti smještena izravno unutar glavne mape teme, a ne u nekoj podmapi (npr. ne u css/style.css unutar mape teme).2  
* **Pogrešno strukturirana.zip arhiva teme:** Ovo je vrlo čest uzrok. Korisnik preuzme.zip datoteku teme, ali ta arhiva unutar sebe sadrži još jednu.zip datoteku ili mapu koja zapravo predstavlja temu. Ako se takva "vanjska" arhiva pokuša instalirati, WordPress neće pronaći style.css na očekivanoj razini.2 Na primjer, preuzmete tema-paket.zip, a unutra je tema.zip ili mapa tema/ koja sadrži style.css. Treba instalirati tema.zip ili sadržaj mape tema/.  
* **Neuspješan ili nepotpun prijenos datoteka putem FTP-a:** Ako se tema prenosi ručno putem FTP-a, prijenos možda nije bio potpun, pa style.css nedostaje ili je oštećena.2  
* **Pokušaj instalacije plugina kao teme:** Korisnik je greškom pokušao instalirati.zip datoteku plugina putem sučelja za instalaciju tema.

**Koraci za Rješavanje:**

1. **Provjerite strukturu.zip arhive teme:** Ako ste preuzeli temu kao.zip datoteku, prvo je raspakirajte na svom lokalnom računalu. Provjerite strukturu mapa. Glavna mapa teme (ona koja sadrži style.css, index.php, functions.php itd.) trebala bi biti na najvišoj razini unutar arhive koju prenosite u WordPress, ili bi arhiva trebala sadržavati samo te datoteke i mape bez dodatne vanjske mape.2 Ako pronađete da je tema unutar dodatne mape u arhivi, trebate zipati samo tu unutarnju mapu ili je prenijeti putem FTP-a.  
2. **Provjerite postojanje i naziv style.css datoteke:** Ako ručno prenosite temu putem FTP-a, ili ako sumnjate na problem, provjerite da li datoteka style.css postoji u korijenskoj mapi teme na serveru (wp-content/themes/naziv-teme/) i da se točno tako zove (sva mala slova).2  
3. **Provjerite lokaciju style.css:** Uvjerite se da style.css nije smještena u neku podmapu unutar mape teme (npr. css/, styles/).2  
4. **Ponovno preuzmite temu:** Preuzmite temu ponovno iz pouzdanog izvora (npr. službeni WordPress repozitorij tema, ThemeForest, web stranica autora teme) kako biste bili sigurni da arhiva nije oštećena ili nepotpuna.2  
5. **Provjerite sadržaj zaglavlja u style.css:** Otvorite style.css datoteku u tekstualnom editoru. Na samom početku datoteke trebao bi biti komentirani blok s informacijama o temi, minimalno 2:  
   CSS  
   /\*  
   Theme Name: Naziv Vase Teme  
   Author: Ime Autora  
   \*/  
   Ako ovo zaglavlje nedostaje ili je neispravno, WordPress možda neće prepoznati temu.  
6. **Ako se radi o child temi:** Provjerite je li roditeljska (parent) tema instalirana i aktivna. Child tema zahtijeva prisutnost roditeljske teme da bi funkcionirala. Poruka o grešci može ukazivati na nedostajuću roditeljsku temu.

Ova greška je direktan pokazatelj da temeljna struktura WordPress teme nije ispoštovana ili da je došlo do problema prilikom pakiranja ili prijenosa teme.2 Datoteka style.css smještena u korijenskom direktoriju mape teme nije samo obična stilska datoteka; ona služi kao "osobna iskaznica" teme za WordPress. Unutar komentara na početku te datoteke nalaze se ključni meta-podaci – poput naziva teme, autora, verzije, opisa, oznaka – koje WordPress čita kako bi identificirao temu, prikazao je u popisu dostupnih tema i omogućio njenu aktivaciju. Ako WordPress ne može pronaći style.css na očekivanom mjestu (korijen mape teme) ili ako ta datoteka ne sadrži minimalno potrebno informacijsko zaglavlje, WordPress jednostavno ne može prepoznati dani skup datoteka kao valjanu temu. Vrlo čest scenarij, posebno s komercijalnim temama, jest da korisnici preuzmu.zip paket koji, osim same teme, sadrži i dokumentaciju, plugine, demo sadržaj itd. Ako korisnik pokuša instalirati cijeli taj paket umjesto samo.zip datoteke koja sadrži isključivo temu, doći će do ove greške. Stoga je ključno da korisnici razumiju osnovnu strukturu WordPress tema i budu pažljivi prilikom rukovanja.zip arhivama i prijenosa datoteka.

## **II. Opći Koraci za Dijagnostiku Problema u WordPressu**

Kada se suočite s WordPress greškom čiji uzrok nije odmah očit, potreban je sustavan i metodičan pristup dijagnostici. Umjesto nasumičnog isprobavanja rješenja, primjena općih tehnika za izoliranje problema može značajno ubrzati proces i dovesti do ispravnog rješenja. Ovi koraci pomažu eliminirati potencijalne krivce i suziti potragu za uzrokom greške.

1\. Omogućavanje WP\_DEBUG Moda  
WP\_DEBUG je PHP konstanta koja se može koristiti za pokretanje WordPress debug (otklanjanje grešaka) moda. Kada je omogućen, WordPress će prikazivati sve PHP greške, obavijesti i upozorenja koja se inače ne bi vidjela.2 Ovo je izuzetno korisno jer "bijeli ekran smrti" ili generičke poruke o grešci (poput Greške 500\) može pretvoriti u konkretne informacije o tome koja datoteka ili funkcija uzrokuje problem.  
Za omogućavanje, potrebno je urediti wp-config.php datoteku koja se nalazi u korijenskom direktoriju vaše WordPress instalacije. Pronađite liniju define( 'WP\_DEBUG', false ); i promijenite false u true. Za bolje rezultate, preporučuje se dodati i sljedeće linije ispod nje 2:

PHP

define( 'WP\_DEBUG\_LOG', true ); // Sprema greške u debug.log datoteku unutar wp-content mape  
define( 'WP\_DEBUG\_DISPLAY', false ); // Ne prikazuje greške direktno na stranici (dobro za produkcijske stranice)  
@ini\_set( 'display\_errors', 0 ); // Dodatno osigurava da se greške ne prikazuju

Nakon spremanja promjena, greške će se bilježiti u wp-content/debug.log datoteci. Ne zaboravite vratiti WP\_DEBUG na false kada završite s dijagnostikom na produkcijskoj stranici. Alternativno, postoje i plugini poput "WP Debugging" 6 ili "Debug This" 6 koji olakšavaju uključivanje i isključivanje debug moda bez ručnog uređivanja datoteka.

2\. Deaktivacija Svih Pluginova  
Pluginovi su čest uzrok problema u WordPressu zbog mogućih konflikata među njima, loše napisanog koda ili nekompatibilnosti s trenutnom verzijom WordPressa ili PHP-a.1

* **Preko administratorskog sučelja:** Ako imate pristup, idite na stranicu Pluginovi, označite sve pluginove, odaberite "Deaktiviraj" iz padajućeg izbornika Masovne radnje i kliknite "Primijeni".3  
* **Preko FTP-a ili File Managera:** Ako ne možete pristupiti admin sučelju, povežite se na server putem FTP-a, navigirajte do mape wp-content i preimenujte mapu plugins u nešto poput plugins\_old ili plugins.stop.1 Ovo će efektivno deaktivirati sve pluginove. Nakon deaktivacije, provjerite je li problem riješen. Ako jest, znači da je jedan od pluginova bio uzrok. Vratite originalni naziv mape plugins (ako ste je preimenovali putem FTP-a), a zatim kroz admin sučelje aktivirajte pluginove jedan po jedan, testirajući stranicu nakon svake aktivacije, dok ne pronađete onaj koji uzrokuje problem.1

3\. Prebacivanje na Zadanu WordPress Temu  
Slično pluginovima, i aktivna tema može biti izvor problema zbog lošeg koda, konflikata s pluginovima ili nekompatibilnosti.1

* **Preko administratorskog sučelja:** Ako imate pristup, idite na Izgled \> Teme i aktivirajte jednu od zadanih WordPress tema (npr. Twenty Twenty-Four, Twenty Twenty-Three).7  
* **Preko FTP-a ili File Managera:** Ako ne možete pristupiti admin sučelju, navigirajte do mape wp-content/themes i preimenujte mapu vaše trenutno aktivne teme (npr. moja-tema u moja-tema\_old).5 WordPress će se automatski pokušati vratiti na zadanu temu ako je dostupna. Ako problem nestane nakon prebacivanja na zadanu temu, onda je vaša originalna tema uzrok problema.

4\. Provjera .htaccess Datoteke  
Datoteka .htaccess (na Apache serverima) je moćna konfiguracijska datoteka koja upravlja permalinkovima, preusmjeravanjima i drugim serverskim postavkama. Ako je oštećena ili sadrži pogrešna pravila, može uzrokovati razne greške, najčešće 500 Internal Server Error ili 404 Not Found.1  
Za provjeru/resetiranje:

* Pristupite korijenskom direktoriju vaše WordPress instalacije putem FTP-a.  
* Pronađite .htaccess datoteku i preimenujte je (npr. u .htaccess\_old).1  
* Pokušajte pristupiti svojoj stranici. Ako radi, problem je bio u .htaccess datoteci.  
* Da biste generirali novu, ispravnu .htaccess datoteku, idite u WordPress admin sučelje na Postavke \> Trajne veze (Permalinks) i jednostavno kliknite gumb "Spremi promjene" (čak i ako niste ništa mijenjali).1 Možete također ručno stvoriti novu .htaccess datoteku s osnovnim WordPress kodom.3

5\. Brisanje Cachea (Predmemorije)  
Zastarjela ili oštećena predmemorija (cache) može uzrokovati da vaša stranica prikazuje stare informacije ili se ponaša neočekivano.5 Postoji nekoliko razina cachea:

* **Cache preglednika:** Obrišite cache i kolačiće u svom web pregledniku (obično putem postavki preglednika ili kombinacijom tipki poput Ctrl+Shift+R ili Cmd+Shift+R za tvrdo osvježavanje).5  
* **Cache WordPress pluginova:** Ako koristite plugin za cacheiranje (npr. WP Rocket, LiteSpeed Cache), pronađite opciju za brisanje cachea unutar postavki tog plugina.  
* **Serverski cache:** Neki hosting provideri implementiraju cacheiranje na razini servera. Opciju za brisanje ovog cachea možete pronaći u svom hosting kontrolnom panelu ili ćete morati kontaktirati podršku.  
* **CDN cache:** Ako koristite Content Delivery Network (CDN) poput Cloudflarea, također ćete morati isprazniti cache putem njihovog korisničkog sučelja.

6\. Provjera PHP Verzije  
Nekompatibilnost između verzije PHP-a na vašem serveru i WordPressa, tema ili pluginova može dovesti do grešaka.1 Preporučuje se korištenje najnovije stabilne verzije PHP-a koju podržava vaša verzija WordPressa. PHP verziju obično možete provjeriti i promijeniti putem kontrolnog panela vašeg hosting računa. Ako sumnjate na problem s PHP verzijom, pokušajte se prebaciti na drugu (preporučenu) verziju.  
7\. Vraćanje Sigurnosne Kopije (Backup)  
Ako ste nedavno napravili promjenu koja je uzrokovala problem (npr. instalirali novi plugin, ažurirali temu) ili ako drugi koraci dijagnostike ne daju rezultate, vraćanje stranice iz nedavne, ispravne sigurnosne kopije može biti najbrže rješenje.2 Ovo naglašava važnost redovitog pravljenja sigurnosnih kopija.  
8\. Provjera Dozvola za Datoteke i Mape  
Kao što je već spomenuto u kontekstu specifičnih grešaka, neispravne dozvole za datoteke i mape čest su uzrok problema.2 Preporučene dozvole su 755 za mape i 644 za datoteke, te 600 za wp-config.php. Provjeru i izmjenu možete izvršiti putem FTP klijenta.  
9\. Čitanje Serverskih Logova Grešaka (Error Logs)  
Serverski logovi grešaka (PHP error log, Apache error log) mogu sadržavati detaljnije informacije o greškama koje WordPress sam ne prikazuje.6 Pristup ovim logovima obično je moguć putem hosting kontrolnog panela (npr. cPanel ima "Errors" ikonu) ili možete zatražiti od hosting podrške da vam ih dostavi. Neki alati, poput InstaWP, također nude lakši pristup logovima.6  
Opći koraci za dijagnostiku WordPress problema rijetko predstavljaju strogo linearan proces. Često je potrebno kombinirati više navedenih metoda i iterativno testirati kako bi se problem izolirao. Na primjer, ako deaktivacija svih pluginova ne riješi problem 1, sljedeći korak može biti provjera aktivne teme, zatim .htaccess datoteke, i tako dalje, uz stalno testiranje stranice nakon svake promjene. Ovaj iterativni pristup, gdje se sustavno eliminiraju potencijalne varijable, ključan je. Ne postoji univerzalan "čarobni štapić" koji rješava sve probleme odjednom. Mnoge greške, poput već spomenute Greške 500, mogu imati višestruke potencijalne uzroke. Stoga, korisnik mora biti spreman na proces koji može zahtijevati strpljenje, metodičnost i više koraka testiranja, umjesto da očekuje trenutno rješenje nakon prve poduzete akcije.

## **III. Preventivne Mjere i Najbolje Prakse za Održavanje WordPress Stranice**

Najbolji način borbe protiv WordPress grešaka jest njihova prevencija. Redovito i pravilno održavanje web stranice ne samo da značajno smanjuje rizik od pojave tehničkih problema, već osigurava i dugoročnu stabilnost, sigurnost i optimalne performanse. Proaktivan pristup održavanju štedi vrijeme, smanjuje stres i čuva reputaciju vaše online prisutnosti.

1\. Redovita Ažuriranja (Core, Teme, Plugini)  
Održavanje WordPress jezgre, svih instaliranih tema i pluginova ažurnima jedna je od najvažnijih preventivnih mjera.2 Ažuriranja često sadrže:

* **Sigurnosne zakrpe:** Ispravljaju poznate ranjivosti koje bi napadači mogli iskoristiti.  
* **Ispravke bugova:** Rješavaju probleme u funkcionalnosti i performansama.  
* **Nove značajke:** Unapređuju mogućnosti softvera.  
* **Poboljšanja kompatibilnosti:** Osiguravaju bolju suradnju s drugim komponentama i novijim verzijama PHP-a. Prije primjene bilo kakvih ažuriranja na produkcijskoj (živoj) stranici, izuzetno je preporučljivo testirati ih na staging (testnoj) okolini, ako je dostupna.10 Ovo omogućuje provjeru kompatibilnosti i sprječava da eventualni problemi s ažuriranjem utječu na vašu aktivnu stranicu. Alati za automatsko ažuriranje, poput onih koje nudi Kinsta 2 ili neki plugini, mogu biti korisni, ali ih treba koristiti s oprezom i razumijevanjem potencijalnih rizika.

2\. Redovite Sigurnosne Kopije (Backups)  
Sigurnosne kopije su vaša najvažnija zaštita od gotovo svih vrsta katastrofa – bilo da se radi o grešci uzrokovanoj ažuriranjem, hakerskom napadu, problemu sa serverom ili ljudskoj pogrešci.2

* **Što uključiti:** Uvijek radite potpunu sigurnosnu kopiju koja uključuje sve WordPress datoteke (jezgra, teme, plugini, medijske datoteke) i cijelu bazu podataka.  
* **Učestalost:** Učestalost ovisi o tome koliko često ažurirate sadržaj na svojoj stranici. Za dinamične stranice preporučuju se dnevne kopije, dok za statičnije stranice tjedne kopije mogu biti dovoljne.10  
* **Pohrana:** Nikada nemojte držati sigurnosne kopije samo na istom serveru gdje je i vaša stranica. Koristite više lokacija, uključujući vanjske (off-site) servise za pohranu (npr. Google Drive, Dropbox, Amazon S3).  
* **Alati:** Mnogi hosting provideri nude vlastita rješenja za backup. Također, postoji mnogo pouzdanih WordPress backup pluginova poput UpdraftPlus, BackupBuddy ili BlogVault.6  
* **Testiranje:** Periodično testirajte proces vraćanja iz sigurnosne kopije kako biste bili sigurni da su kopije ispravne i da znate kako ih koristiti u slučaju potrebe.11

3\. Odabir Pouzdanih Tema i Pluginova  
Ekosustav tema i pluginova velika je snaga WordPressa, ali i potencijalni izvor problema ako se ne bira pažljivo.

* **Izvori:** Preuzimajte teme i pluginove isključivo iz službenog WordPress repozitorija (wordpress.org) ili od renomiranih komercijalnih developera i tržišta (npr. ThemeForest, CodeCanyon, ali uz provjeru autora).2  
* **Provjera:** Prije instalacije, provjerite recenzije korisnika, ocjene

