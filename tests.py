import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.books_genre) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_add_new_book_in_book_genre_success(self): #добавляем новую книгу в словарь books_genre, проверяем добавилась ли
        collector = BooksCollector()

        collector.add_new_book('Евгений Онегин')

        assert 'Евгений Онегин' in collector.books_genre

    def test_add_new_book_in_book_genre_twice_fail(self): #добавляем одну и ту же новую книгу в словарь books_genre 2 раза, проверяем, что добавлена 1 раз
        collector = BooksCollector()

        collector.add_new_book('Евгений Онегин')
        collector.add_new_book('Евгений Онегин')

        assert len(collector.books_genre) == 1

    @pytest.mark.parametrize ("book_name, genre, expected_genre",   #проверяем соответствие жанра ожидаемому жанру
            [
        ("Евгений Онегин", "Фантастика", "Фантастика"),
        ("Евгений Онегин", "Кулинария", "Фантастика")
            ]
                              )

    def test_set_book_genre_valid_and_invalid(self, book_name, genre, expected_genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, "Фантастика")
        collector.set_book_genre(book_name, genre)
        assert collector.books_genre[book_name] == expected_genre

    def test_get_book_genre_for_valid_book_name_with_valid_genre(self): #устанавливаем валидный жанр книге, запрашиваем жанр по названию, сравниваем с ранее установленным
        collector = BooksCollector()

        collector.add_new_book('Евгений Онегин')
        collector.set_book_genre('Евгений Онегин', 'Фантастика')

        assert collector.get_book_genre('Евгений Онегин') == 'Фантастика'

    def test_get_book_genre_with_not_valid_book_name_with_none_genre(self): #пытаемся установить жанр у книги по названию, которой жанр до этого не присвоили
        collector = BooksCollector()

        assert collector.get_book_genre('Старик и море') is None

    def test_get_books_with_specific_genre_valid_genre(self): #обавляем книги с валидным жанром, пытаемся получить книгу по одному из этих жанров
        collector = BooksCollector()

        collector.add_new_book( 'Как снимали "Простоквашино"' )
        collector.set_book_genre( 'Как снимали "Простоквашино"', 'Мультфильмы')
        collector.add_new_book('Евгений Онегин')
        collector.set_book_genre('Евгений Онегин', 'Фантастика')

        books_with_genre_fiction = collector.get_books_with_specific_genre('Фантастика')

        assert books_with_genre_fiction == ['Евгений Онегин']


    def test_get_books_genre_empty(self): #проверяем, что метод вернет пустой словарь, если не добавляли книги
        collector = BooksCollector()

        assert collector.get_books_genre() == {}


    def test_get_books_for_children_check__for_not_children_book_genre(self): #проверяем, что книга с жанром имеющим возрастное ограничение не попадает в детский список(его длина 0)
        collector = BooksCollector()

        collector.add_new_book('Вампиры!')
        collector.set_book_genre('Вампиры!', 'Ужасы')

        assert len(collector.get_books_for_children()) == 0

    def test_add_book_in_favorites_check_favorites_after(self): #добавляем книгу в избранное, проверяем оказалась ли она в избранном
        collector = BooksCollector()

        collector.add_new_book('Евгений Онегин')
        collector.add_book_in_favorites('Евгений Онегин')

        assert 'Евгений Онегин' in collector.favorites

    def test_delete_book_from_favorites_check_favorites_after(self): #проверяем, что книга удаленная из избранного не отображается в избранном
        collector = BooksCollector()

        collector.add_new_book('Евгений Онегин')
        collector.add_book_in_favorites('Евгений Онегин')
        collector.delete_book_from_favorites('Евгений Онегин')

        assert 'Евгений Онегин' not in collector.favorites

    def test_get_list_of_favorites_books_after_adding_book(self): #добавляем книгу в избранное, проверяем что эта книга есть в списке избранных
        collector = BooksCollector()

        collector.add_new_book('Евгений Онегин')
        collector.add_book_in_favorites('Евгений Онегин')

        assert collector.get_list_of_favorites_books() == ['Евгений Онегин']










