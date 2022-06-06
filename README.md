
# ESAME FINALE UFS04 - Algoritmi di Machine Learning

Il seguente report è stato redatto in modo da illustrare il codice per lo sviluppo di un sito di e-commerce e giustificare le scelte fatto rispetto l’implementazione di algoritmi di machine learning. L'intero progetto è il risultato di un lavoro svolto con il fine di completare la parte pratica dell'esame finale del modulo UFS04 - Algoritmi di Machine Learning, svolto presso l’ITS Angelo Rizzoli.

Questo lavoro è la dimostrazione delle competenze acquisite negli ultimi mesi di corso: nello specifico abbiamo appreso tecniche e metodi di implementazione di algoritmi di Machine Learning per effettuare previsioni sui dati.
Il Report e il programma sono stati svolti in gruppo, il quale è composto da: Edoardo Andrea Giacomin, Samuele Parma, Stefano Perdicchia, Marco Tosi ed Alessandro Benzi.

Il report si costituisce di cinque parti, le quali seguono il seguente ordine: 
Introduzione al lavoro svolto e relativa consegna, 
spiegazione del lavoro svolto per capire al meglio il funzionamento del programma, 
spiegazione con immagini di come funziona il programma che è stato sviluppato (quindi mediante la sua interfaccia, il meccanismo di registrazione e di login, i database che sono stati utilizzati, come funziona l’algoritmo di machine learning sviluppato e l'analisi dei risultati che abbiamo ottenuto con relative immagini di output)
ed infine una breve conclusione sul lavoro svolto con i nostri commenti personali.
In fondo al report saranno anche presenti i link utili e quelli utilizzati per poter sviluppare al meglio il programma finale, con il relativo link a GitHub nel quale è presente il codice in formato completo.

INDICE

1.	Introduzione
  a.	Consegna del lavoro
2.	Lavoro svolto
  a.	Fase di elaborazione dei dati
3.	Funzionamento
  a.	Machine Learning
4.	Analisi dei Risultati
5.	Conclusione 
6.	Link utili

# INTRODUZIONE
Come esame finale del modulo di Algoritmi ci è stato richiesto lo sviluppo di un sito e-commerce, per poi implementarvi successivamente algoritmi di Machine Learning.
Lavorando in gruppo, abbiamo stabilito che considerata la libertà progettuale data nella consegna, avremmo sviluppato il progetto con un approccio 'semplice e lineare', e abbiamo quindi sviluppato un'interfaccia grafica con la quale sia possibile interagire dal proprio localhost. 
L'idea originale prevedeva lo sviluppo di un sito simile ad Amazon nel quale poter inserire i prodotti da acquistare all’interno di un carrello e quindi ordinarli (l'algoritmo di machine learning avrebbe poi suggerito i prodotti correlati agli acquisti). 
Nel progetto finale abbiamo invece deciso di sviluppare un prototipo di sito che possa consigliare all’utente che si registra dei film, in base ai titoli di film che l'utente indica inizialmente come “preferiti” (in modo quindi da individuare film simili a quelli che piacciono). 
Il programma sviluppato utilizza nello specifico un algoritmo di KNN (verrà poi spiegato più avanti). 

# **LAVORO SVOLTO**
Il progetto si avvale di linguaggio Python soprattutto per l'algoritmo di machine learning mentre per l'interfaccia grafica abbiamo fatto uso di codice in HTML, CSS, e della libreria Flask di Python.
Ora andremo a spiegare come abbiamo lavorato python;

# 1. Python
Per sviluppare il lavoro ci siamo avvalsi di tre dataset trovati online:  “movies_metadata.csv”, ”credits” e ”keyword”.
Ci siamo quindi occupati di unire i dataset, così da avere un unico dataset su cui poi lavorare.
Successivamente abbiamo sistemato gli indici e verificato l'integrità del file ed eliminato le righe non idonee (per esempio le vecchie righe 19730,29503,35587, che sono state eliminate in quante erano delle copie di altre righe). 
Abbiamo poi importato in Python la libreria **ast(Abstract Syntax Tree)** per utilizzare la funzione **literal_eval** all'interno di un ciclo f'or' per convertire i valori di features (cast, crew, keywords e genres) da delle stringhe a delle liste di dizionari. 
A questo punto da 'crew' abbiamo estratto il direttore, mentre se era assente gli abbiamo attribuito un valore di ritorno Nan. Dopodichè abbiamo estratto da 'cast', 'crew' e 'genres' i valori dai dizionari e abbiamo salvato i primi tre, visto che questo valore va ad influenzare la precisione del nostro modello che andremo ad applicare.
Una volta fatto ciò abbiamo pulito il dataset, e abbiamo impostato tutto lo scritto in formato minuscolo, per non incorrere in successivi errori.
Abbiamo poi creato e aggiunto al dataset una colonna "soup" per concatenare tutto in una colonna che potesse contenere una stringa di valori estratti in precedenza dalle altre colonne (direttore, cast, keyword e genres).
Abbiamo utilizzato il metodo **sklearn.feature_extraction.text.CountVectorize** per andare a convertire la colonna soup da una stringa in una matrice di token (in sostanza va a creare una matrice che ha come indici la diverse parole presenti nella colonna mentre nelle righe è presente quante volte la parola compare).
Andando poi a utilizzare il metodo **sklearn.metrics.pairwise.cosine_similarity** per calcolare quanto simili sono i film rispetto alla matrice che è stata creata precedentemente, mentre **cosine_similarity** va a rappresentare tutti i film sullo stesso piano cartesiano in base alla matrice e va a calcolare la distranza tra i film (minore è la distanza maggiore è la similarità).
Infine attraverso la funzione **get_reccomendation** l'utente da in input il titolo di un film, che attraverso la matrice di similarità va a trovare l'indice rispetto al dato del titolo (nel nostro caso i titoli uguali/simili), va a trovare la distanza tra il film dato in input e tutti gli altri presenti al'interno del dataset utilizzato, vengono quindi ordinati e poi restituiti in output i primi 11 titoli correlati (il primo è il nome di se stesso) .

# 2. Interfaccia
 
Lo sviluppo dell'interfaccia grafica è stato più complicato soprattutto per il collegamento che dovevamo fare con il dataset importato e il codice python.
Per riassumere il lavoro che abbiamo svolto, possiamo dire che abbiamo iniziato attraverso la liberia Flask di python che ci ha permesso di andare a creare nel nostro localhost una breve interfaccia di login e registrazione, che permette in locale di memorizzare username e password (ovviamente nascosta), in un piccolo database SQLlite che inserisce e salva i dati di registrazione per fare il login.
Attraverso la nostra interfaccia possiamo dunque registrare un nuovo utente, attraverso username e una pasword, che verranno successivamente richiesti per fare il login al nostro local-site. 
Tutto questo avviene attraverso il run di flask dal cmd, cosi da poter avviare in locale il nostro sito. 
Dall'interfaccia si può quindi andare a cercare un film, cosi da poter leggere la descrizione, e i film correlati, che possono uscire attraverso il linguaggio python e che utilizza un algoritmo di machine learning (nel codice python possiamo farlo con tutti i film possibili, visto la grande quantità di dati presenti all'interno del dataset, mentre all'interno dell'interfaccia possiamo solamente salvare un file txt preso in locale con un film).


# MACHINE LEARNING

Vista la richiesta dell'esame abbiamo implementato dunque al nostro codice un algoritmo di machine learning tra quelli studiati. Quello che abbiamo deciso di utilizzare è l'algoritmo K-Nearest Neighbors (KNN) che, oltre alla sua semplicità, produce buoni risultati in un gran numero di domini. L'obbiettivo è quello di andare a calcolare la distanza euclidea tra il titolo inserito in input dall'utente che fa la richiesta di film, e i dati dei film presenti all'interno del dataset. Abbiamo deciso di impostare la variabile k al valore 10, così che a schermo esca come output atteso i primi 11 valori trovati (il primo titolo stesso cercato dall'utente mentre i successivi 10 alla nostra k di risultati).
In output otterremo quindi dei film con caratteristiche simili all'input (esempio: se cerco un film fantasy restituirà il film fantasy con caratteristiche più simili).

# ANALISI DEI RISULTATI

Il programma suggerisce con successo film con caratteristiche simili, infatti dato un titolo restituisce film titoli della stessa serie o dello stesso genere. 
Le caratteristice considerate sono regista e cast ma volendo possiamo basarci esclusivamente su genere o dare più peso alle parole chiave che meglio descrivono il film. Il programma funziona solo con titoli già presenti nel dataset ma una futura implementazione potrebbe essere di chiedere all’utente le caratteristiche del film cercato e trovare quali film sono più vicini ai gusti dell’utente.

# CONCLUSIONI

Possiamo notare come il programma funzioni tramite l'algoritmo che abbiamo scelto, la nostra interfaccia grafica inoltre ci permette di caricare noi stessi i film online, in maniera tale da poter averne sempre di nuovi e di ingrandire il nostro dataset.
Siamo soddisfatti dei risultati che abbiamo ottenuto, visto che nel tempo che abbiamo avuto a disposizione siamo riusciti a sviluppare un programma funzionante e abbastanza ottimizzato, nonostante alcune complicazioni classiche nel lavoro del progrmmatore. 
Nel complesso dunque il programma che abbiamo sviluppato funziona come avevamo pensato che avrebbe dovuto funzionare e siamo felici del lavoro svolto.

# LINK UTILI
1. https://flask.palletsprojects.com/en/2.1.x/
2. https://www.datacamp.com/tutorial/recommender-systems-python
3. https://github.com/EdoAG/Progetto_algoritmi
4. https://flask.palletsprojects.com/en/2.1.x/tutorial/blog/
