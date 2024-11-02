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
  
**Wymagania**
Baza danych: Projekt korzysta z domyślnej bazy danych SQLite, więc nie wymaga dodatkowej konfiguracji.

1. Sklonuj repozytorium:
   ```
   git clone https://github.com/Domikaf456/Recipes_project
   ```
2. Zainstaluj zależności:
   ```
   pip install -r requirements.txt

3. Wykonaj makemigrations recipe
   ```
   Przy pierwszej i drugiej migracji należy zahaszować w admin.py admin.site.register(Recipe, RecipeAdmin) i klasę class RecipeCollection w models.py
   
4. Utwórz bazę danych SQLite i wykonaj migracje:
   ```
   python manage.py migrate

5. Uruchom serwer:
   ```
   python manage.py runserver
