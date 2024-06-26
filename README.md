# qa_python
# Тесты для BooksCollector

Класс `BooksCollector` предоставляет функционал для управления коллекцией книг, включая добавление книг, установку и получение жанров, работу со списком избранных книг и фильтрацию книг по определенным критериям. Ниже приведены описания тестов, покрывающих основные функции этого класса.

## Тесты на добавление книг

### `test_add_new_book_add_two_books`

- **Цель**: Проверить, что в коллекцию можно добавить две различные книги.
- **Шаги**:
  1. Создается экземпляр `BooksCollector`.
  2. Добавляются две различные книги.
- **Ожидаемый результат**: В коллекции присутствуют обе добавленные книги.

### `test_add_new_book_in_book_genre_success`

- **Цель**: Проверить успешное добавление новой книги в словарь `books_genre`.
- **Шаги**:
  1. Создается экземпляр `BooksCollector`.
  2. Добавляется новая книга.
- **Ожидаемый результат**: Новая книга присутствует в словаре `books_genre`.

### `test_add_new_book_in_book_genre_twice_fail`

- **Цель**: Проверить, что повторное добавление одной и той же книги не увеличивает количество элементов в словаре `books_genre`.
- **Шаги**:
  1. Создается экземпляр `BooksCollector`.
  2. Добавляется одна и та же книга дважды.
- **Ожидаемый результат**: В словаре `books_genre` присутствует только одна запись для добавленной книги.

## Тесты на установку жанра книги

### `test_set_book_genre_valid_and_invalid`

- **Цель**: Проверить, что жанр книги корректно обновляется на допустимый жанр, и не изменяется при попытке установить невалидный жанр.
- **Шаги**:
  1. Создается экземпляр `BooksCollector`.
  2. Добавляется книга и устанавливается валидный жанр "Фантастика".
  3. Пытаемся установить жанр "Кулинария" (предполагаемый невалидный).
- **Ожидаемый результат**: Жанр книги остается "Фантастика".

## Тесты на получение жанра книги

### `test_get_book_genre_for_valid_book_name_with_valid_genre`

- **Цель**: Проверить, что можно получить установленный жанр для книги.
- **Шаги**:
  1. Создается экземпляр `BooksCollector`.
  2. Добавляется книга и устанавливается её жанр.
- **Ожидаемый результат**: Метод `get_book_genre` возвращает корректный жанр для книги.

### `test_get_book_genre_with_not_valid_book_name_with_none_genre`

- **Цель**: Проверить, что метод `get_book_genre` возвращает `None` для книги, жанр которой не был установлен.
- **Шаги**:
  1. Создается экземпляр `BooksCollector`.
- **Ожидаемый результат**: Для несуществующей книги метод `get_book_genre` возвращает `None`.

## Тесты на избранные книги

### `test_add_book_in_favorites_check_favorites_after`

- **Цель**: Проверить, что книга добавляется в список избранных.
- **Шаги**:
  1. Создать экземпляр `BooksCollector`.
  2. Добавить книгу в коллекцию.
  3. Добавить ту же книгу в список избранных.
- **Ожидаемый результат**: Книга появляется в списке избранных.

### `test_delete_book_from_favorites_check_favorites_after`

- **Цель**: Убедиться, что книга удаляется из списка избранных.
- **Шаги**:
  1. Создать экземпляр `BooksCollector`.
  2. Добавить книгу в коллекцию и в список избранных.
  3. Удалить книгу из списка избранных.
- **Ожидаемый результат**: Книга больше не присутствует в списке избранных.

### `test_get_list_of_favorites_books_after_adding_book`

- **Цель**: Проверить, что метод возвращает актуальный список избранных книг после добавления в него книги.
- **Шаги**:
  1. Создать экземпляр `BooksCollector`.
  2. Добавить книгу в коллекцию и в список избранных.
- **Ожидаемый результат**: Список избранных книг содержит добавленную книгу.

## Тесты на получение книг по жанру

### `test_get_books_with_specific_genre_valid_genre`

- **Цель**: Проверить, что метод корректно возвращает книги заданного жанра.
- **Шаги**:
  1. Создать экземпляр `BooksCollector`.
  2. Добавить несколько книг разных жанров.
  3. Запросить книги одного из жанров.
- **Ожидаемый результат**: Возвращается только список книг запрошенного жанра.

## Дополнительные тесты

### `test_get_books_genre_empty`

- **Цель**: Проверить, что метод возвращает пустой словарь, если не было добавлено ни одной книги.
- **Шаги**:
  1. Создать экземпляр `BooksCollector`.
- **Ожидаемый результат**: Метод возвращает пустой словарь.

### `test_get_books_for_children_check__for_not_children_book_genre`

- **Цель**: Убедиться, что книги с жанром, имеющим возрастное ограничение, не попадают в список книг для детей.
- **Шаги**:
  1. Создать экземпляр `BooksCollector`.
  2. Добавить книгу с жанром, предполагающим возрастное ограничение.
- **Ожидаемый результат**: Список книг для детей остается пустым.

## Заключение

Тесты для `BooksCollector` позволяют проверить корректность работы основного функционала приложения, включая управление коллекцией книг, работу со списком избранных и фильтрацию книг по жанрам и другим критериям.