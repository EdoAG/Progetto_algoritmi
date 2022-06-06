
# ESAME FINALE UFS04 - Algoritmi di Machine Learning

Il seguente report è stato redatto in quanto è stata richiesto lo sviluppo di un sito di e-commerce con l’implementazione di algoritmi di machine learning, 
la richiesta fa fronte all’esame finale del modulo UFS04 - Algoritmi di Machine Learning svolto presso l’ITS Angelo Rizzoli. 
Viste le nozioni apprese durante lo svolgimento del corso abbiamo imparato come si sviluppano, funzionano e implementano gli algoritmi che fanno utilizzo 
delle tecniche di Machine Learning per effettuare previsioni sui dati. Il Report e il programma sono stati svolti in gruppo, dove ogni partecipante ha contribuito 
allo svolgimento della prova d’esame. Il gruppo è attualmente composto da Edoardo Andrea Giacomin, Samuele Parma, Stefano Perdicchia, Marco Tosi e Alessandro Benzi. 
Abbiamo deciso di dare a questo report una struttura suddivisa in sei parti, inizialmente abbiamo l’introduzione al lavoro svolto e la relativa consegna, 
successivamente seguirà una spiegazione del lavoro svolto, così da poter capire al meglio il funzionamento del programma, andando avanti avremo una spiegazione con immagini, di come funziona il programma che è stato sviluppato, quindi mediante la sua interfaccia, il meccanismo di registrazione e di login, 
i database che sono stati utilizzati e come funziona l’algoritmo di machine learning sviluppato. Successivamente andremo ad analizzare i risultati che abbiamo 
ottenuto con relative immagini di output e infine una breve conclusione al lavoro svolto con i nostri commenti personali. In fondo al report saranno presenti i link utili e quelli utilizzati per poter sviluppare al meglio il programma finale, con il relativo link a GitHub nel quale è presente il codice in formato completo.

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
Il lavoro che è stato affidato alla classe del Machine Learning al primo anno del 2021/2022 come esame finale del modulo di Algoritmi è quello di sviluppare 
mediante le nozioni apprese all’interno del corso un sito che funga da e-commerce, così da poter successivamente implementare quelli che sono gli algoritmi 
di Machine Learning per poter andare a prevedere i dati. Durante il corso abbiamo avuto la possibilità di poter svolgere questo lavoro in gruppi, 
così abbiamo deciso di dividere i diversi compiti all’interno del gruppo che abbiamo formato per rendere più efficiente il tempo investito nello sviluppo del 
programma. Inizialmente abbiamo scelto che tipo di lavoro svolgere, visto che la consegna era molto ampia, e potevamo sviluppare dunque questo progetto come più 
ci aggradava, il nostro approccio è stato quello di creare in maniera semplice un interfaccia grafica che si possa aprire sul proprio localhost del computer 
così da poter gestire meglio i diversi dati. Inizialmente la nostra idea era quella di sviluppare un sito simil-Amazon nel quale poter inserire i prodotti di nostro 
interesse all’interno di un carrello, cosi da poterli acquistare e tramite un algoritmo di machine learning poter ricevere in output i diversi prodotti correlati. 
Successivamente abbiamo invece deciso di sviluppare un prototipo di sito che possa consigliare all’utente che si registra dei film, in base ai titoli dei film che 
si vanno a selezionare come “preferiti”. Questo tipo di programma utilizza un algoritmo di KNN che permette di calcolare la distanza tra punti, verrà comunque 
spiegato maggiormente nel capitolo dedicato. 

# **LAVORO SVOLTO**
Il nostro progetto è strutturato in due parti, la prima parte integra un programma scritto in linguaggio Python e l'algoritmo di machine learning, la seconda parte integra un'interfaccia grafica attraverso un codice in HTML e css, e la libreria Flask di Python.
Questa sezione sarà divisa in due parti, la prima parte andrà a spiegare come abbiamo lavorato il linguaggio python, mentre la seconda riguarderà l'interfaccia presente nel localhost.
# 1. Python
Inizialmente abbiamo trovato online tre dataset per far fronte alla richiesta dell'esame, erano tre dataset separati tra di loro:  “movies_metadata.csv”, ”credits” e ”keyword”, abbiamo iniziato lavorando sull'unione dei dati, e la creazione di un unico dataset su cui poi lavorare. Abbiamo dunque sistemato gli indici, verificato l'integrità del file ed eliminato le righe non idonee, per esempio le vecchie righe 19730,29503,35587, che sono state eliminate in quante erano delle copie di altre righe. Fatto questi passaggi abbiamo ultimato i preparativi e quindi creato un dataset unico con tutti i dati che ci servivano per proseguire all'esame.
Successivamente abbiamo importato in Python la libreria **ast(Abstract Syntax Tree)** per utilizzare la funzione **literal_eval** all'interno di un ciclo for per convertire i valori di features (cast, crew, keywords e genres) da delle stringhe a delle liste di dizionari. A questo punto da crew abbiamo estratto il direttore, mentre se era assente gli abbiamo attribuito un valore di ritorno Nan. Successivamente abbiamo estratto da cast, crew e genres i valori dai dizionari e abbiamo salvato i primi quattro, visto che questo valore va ad influenzare la prezisione del nostro modello.



# 2. Interfaccia
.
