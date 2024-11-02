**Opis aplikacji**
Aplikacja z przepisami kulinarnymi, która umożliwia zalogowanym użytkownikom na przeglądanie przepisów, dodawanie, filtrowanie oraz tworzenie i zarządzanie kolekcjami.
W zależności od uprawnień, administrator i użytkownik posiadają zróżnicowany dostęp do funkcjonalności aplikacji.

Administrator ma możliwość:
- przeglądania przepisów
- tworzenia przepisów
- edycji przepisów
- oceniania przepisów
- tworzenia osobistych kolekcji
- dodawania przepisów do osobistych kolekcji
- filtrowania przepisów według kryteriów, takich jak poziom trudności i nazwa posiłku

Użytkownik ma możliwość:
- przeglądania przepisów
- tworzenia osobistych kolekcji
- dodawania przepisów do osobistych kolekcji
- filtrowania przepisów według kryteriów, takich jak poziom trudności i nazwa posiłku

Główny katalog aplikacji Django: recipes
Aplikacje: recipe

**Wymagania**
Aplikacja korzysta z bazy danych SQLite (db.sqlite3), która jest domyślnie skonfigurowana w pliku settings.py, więc nie wymaga dodatkowej konfiguracji.

1. Sklonuj repozytorium:
   ```
   git clone https://github.com/Domikaf456/recipes
   ```
2. Zainstaluj zależności:
   ```
   pip install -r requirements.txt
   
3. Utwórz bazę danych SQLite i wykonaj migracje danych:
   ```
   python manage.py migrate
   
4. Stwórz superużytkownika, aby mieć dostęp do panelu administratora:
     ```
     python manage.py createsuperuser

5. Uruchom serwer:
   ```
   python manage.py runserver
