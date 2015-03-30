Usługa strumieniowa wyliczająca statystki, odwiedzin serwisów, ilości używanych wulgaryzmów oraz wyświetleń obrazów, podobnych do zadanych,  na podstawie analizy ruchu sieciowego TCP/IP.

TCP port splitter

Opis
moduł filtruje ruch sieciowy TCP względem wybranego portu 
Wejście
przechwycony ruch sieciowy (plik .pcap)
Wyjście
odfiltrowany ruch TCP
Adres interfejsu zarządzania
localhost:11111
Czas przetwarzania
rzeczywisty
Koszt
niski

TCP stream reasembler

Opis
składa ruchu TCP w strumienie
Wejście
odfiltrowanych ruch TCP
Wyjście
strumienie TCP
Adres interfejsu zarządzania
brak
Czas przetwarzania
rzeczywisty
Koszt
wysoki

HTTP page spliter

Opis
moduł filtruje strumienie TCP i wydobywa z nich pliki html
Wejście
strumienie TCP
Wyjście
strumienie TCP Content-Type: text/html;
Adres interfejsu zarządzania
brak
Czas przetwarzania
rzeczywisty
Koszt
niski
HTTP text splitter

Opis
moduł filtruje strumień TCP i wydobywa tekst z zapytań
Wejście
strumienie TCP
Wyjście
odkodowane teksty, JSON
Adres interfejsu zarządzania
brak
Czas przetwarzania
rzeczywisty
Koszt
niski

HTTP graphics splitter

Opis
moduł filtruje strumień TCP i wydobywa przesyłane obrazy
Wejście
strumienie TCP
Wyjście
obrazy
Adres interfejsu zarządzania
brak
Czas przetwarzania
rzeczywisty
Koszt
niski

domain extractor

Opis
wydobywa adres domeny ze strumieni zawierających pliki html
Wejście
strumienie TCP Content-Type: text/html;
Wyjście
nazwy domen, JSON
Adres interfejsu zarządzania
brak
Czas przetwarzania
rzeczywisty
Koszt
niski
vulgarism detector

Opis
wykrywa wulgaryzmy w przetwarzanych tekstach, używająć do tego dostarczonego słownika
Wejście
odkodowane teksty, JSON
Wyjście
wystąpienia w słowniku, JSON
Adres interfejsu zarządzania
localhost:11112
Czas przetwarzania
rzeczywisty
Koszt
średni

object comparator

Opis
porównuje otrzymane obrazki pod względem podobieństwa do zadanych i zgłasza wstąpienia wystarczająco podobnych obrazów
Wejście
obrazy
Wyjście
wystąpienia, JSON
Adres interfejsu zarządzania
localhost:11113
Czas przetwarzania
rzeczywisty
Koszt
wysoki

statistics generator

Opis
generowanie statystyk z wystąpień wszystkich typów
Wejście
wystąpienia, JSON
Wyjście
połączone wystąpienia, JSON
Adres interfejsu zarządzania
localhost:11113
Czas przetwarzania
rzeczywisty
Koszt
średni

per user statistics splitter

opis funkcjonalny
generowanie statystyk w określonym odstępie czasu dla poszczególnych użytkowników
wejście
statystyki JSON
wyjście
pogrupowane statystyki wg użytkownika
adres interfejsu zarządzania
brak
czas przetwarzania
rzeczywisty
koszt
niski

database - zapis wszystkich wystąpień
statistics panel - wizualizacja statystyk na żywo, oraz archiwalnych
