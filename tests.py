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
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_add_new_book_rating_is_equal_to_one(self): # Добавляем книгу. Её рейтинг по умолчанию 1
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        # добавляем новую книгу
        collector.add_new_book('Гордость и предубеждение и зомби')
        # проверяем, что рейтинг у книги равен 1
        assert collector.get_book_rating('Гордость и предубеждение и зомби') == 1

    def test_add_two_books_with_the_same_title(self): # Добавить книгу. Добавить книгу с таким же название. В словаре только 1 книга
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        # добавляем новые книги с одинаковым названием
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')
        # проверяем, что добавиласт только одна
        assert len(collector.get_books_rating()) == 1

    def test_set_book_rating_the_rating_of_the_book_is_changing(self): # Добавить книгу. Поменять ей рейтинг на 5
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        # добавляем новую книгу
        collector.add_new_book('Гордость и предубеждение и зомби')
        # меняем рейтинг на 5
        collector.set_book_rating('Гордость и предубеждение и зомби', 5)
        # проверяем, что рейтинг равен 5
        assert collector.get_book_rating('Гордость и предубеждение и зомби') == 5

    def test_set_book_rating_set_an_inappropriate_rating_it_will_remain_unit(self): #Добавим книгу. Поменяем ей рейтинг на 5.5
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        # добавляем новую книгу
        collector.add_new_book('Гордость и предубеждение и зомби')
        # меняем рейтинг на 5.5
        collector.set_book_rating('Гордость и предубеждение и зомби', 5.5)
        # проверяем, что рейтинг равен 1
        assert collector.get_book_rating('Гордость и предубеждение и зомби') == 1

    def test_set_book_rating_set_rating_of_more_than_ten_it_will_remain_a_unit(self):  # Добавим книгу. Поменяем ей рейтинг на 11
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        # добавляем новую книгу
        collector.add_new_book('Гордость и предубеждение и зомби')
        # меняем рейтинг на 11
        collector.set_book_rating('Гордость и предубеждение и зомби', 11)
        # проверяем, что рейтинг равен 1
        assert collector.get_book_rating('Гордость и предубеждение и зомби') == 1
    def test_set_book_rating_set_rating_to_less_than_one_it_will_remain_a_unit(self):  # Добавим книгу. Поменяем ей рейтинг на 0
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        # добавляем новую книгу
        collector.add_new_book('Гордость и предубеждение и зомби')
        # меняем рейтинг на 0
        collector.set_book_rating('Гордость и предубеждение и зомби', 0)
        # проверяем, что рейтинг равен 1
        assert collector.get_book_rating('Гордость и предубеждение и зомби') == 1

    def test_get_book_rating_to_find_out_the_rating_book_that_has_not_been_added_to_the_dictionary_there_is_no_rating(self):  #Добавляем книгу. Выводим рейтинг у недобавленной в словарь книги. Рейтинга нет.
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        # добавляем новую книгу
        collector.add_new_book('Гордость и предубеждение и зомби')
        # проверяем, что рейтинг равен None у недобавленноей книги
        assert collector.get_book_rating('Как правильно кушать тортик') == None

    def test_set_book_rating_set_rating_for_book_that_has_not_been_added_to_the_dictionary_there_is_no_rating(self):  # Добавляем 2 книги. Меняем рейтинг другой книге(ее не добавляли в список). Рейтинг не поменяется у несуществующей книги.
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        # добавляем новые книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        # меняем рейтинг на 5
        collector.set_book_rating('Как правильно кушать тортик', 5)
        # проверяем, что рейтинг равен None у недобавленноей книги
        assert collector.get_book_rating('Как правильно кушать тортик') == None
    def test_get_books_with_specific_rating_all_books_with_rating_of_one_will_be_displayed(self):  # Добавить 3 книги. Выводим список книг с рейтингом 1. Выведутся 3 книги
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        # добавляем новые книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_new_book('Как правильно кушать тортик')
        # проверяем, что книг с рейтингом равным единице 3
        assert len(collector.get_books_with_specific_rating(1)) == 3

    def test_get_books_with_specific_rating_change_the_rating_of_one_book_only_book_with_rating_of_five_will_be_displayed(self):  # Добавить 3 книги. Установить 2 книге рейтинг 5. Вывести книги с рейтингом 5. Выведется одна книга.
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        # добавляем новые книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_new_book('Как правильно кушать тортик')
        # меняем рейтинг на 5
        collector.set_book_rating('Что делать, если ваш кот хочет вас убить', 5)
        # проверяем, что книг с рейтингом равным пяти 1
        assert len(collector.get_books_with_specific_rating(5)) == 1
    def test_get_books_with_specific_change_the_rating_of_books_books_with_rating_of_six_will_not_be_displayed(self):  # Добавить 3 книги. Установить 1 книге рейтинг 2, второй 3, третей 7. Вывести книги с рейтингом 6. Не выведутся книги.
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        # добавляем новые книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_new_book('Как правильно кушать тортик')
        # меняем рейтинг на 2
        collector.set_book_rating('Гордость и предубеждение и зомби', 2)
        # меняем рейтинг на 3
        collector.set_book_rating('Что делать, если ваш кот хочет вас убить', 3)
        # меняем рейтинг на 7
        collector.set_book_rating('Как правильно кушать тортик', 7)
        # проверяем, что книг с рейтингом равным шести 0
        assert len(collector.get_books_with_specific_rating(5)) == 0

    def test_add_book_in_favorites_the_book_is_added_to_favorites(self): #Добавляем 1 книгу. Добавляем ее в избранное. В избранном 1 книга.
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        # добавляем книгу
        collector.add_new_book('Гордость и предубеждение и зомби')
        # добавляем книгу в избранное
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        # список favorites содержит 1 книгу
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_add_book_in_favorites_only_one_book_has_been_added_to_favorites(self): #Добавляем 2 книги. Добавляем одну в избранное. В избранном 1 книга.
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        # добавляем книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        # добавляем книгу в избранное
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        # список favorites содержит 1 книгу
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_add_book_in_favorites_add_a_nonexistent_book_to_favorites_there_are_no_books_favorites(self): #Добавляем 1 книгу. Добавляем другую книгу(ее не добавляли в список) в избранное. В избранном нет книг.
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        # добавляем книгу
        collector.add_new_book('Гордость и предубеждение и зомби')
        # добавляем несуществующую книгу в избранное
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        # список favorites содержит 0 книг
        assert len(collector.get_list_of_favorites_books()) == 0

    def test_add_book_in_favorites_the_same_book_will_not_be_added_to_favorites_twice(self): #Добавляем 2 книги. Добавляем одну в избранное. Добавляем ее же в избранное. В избранном 1 книга.
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        # добавляем книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        # добавляем книгу в избранное
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        # добавляем эту же книгу еще раз в избранное
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        # список favorites содержит 1 книгу
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites_the_book_is_being_deleted(self): #Добавляем 2 книги. Добавляем их в избранное. В избранном 2 книги. Удаляем одну из избранного. В избранном 1 книга.
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        # добавляем книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        # добавляем книги в избранное
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        # удаляем книгу из избранного
        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')
        # список favorites содержит 1 книгу, список get_books_rating содержит 2 книги
        assert len(collector.get_list_of_favorites_books()) == 1 and len(collector.get_books_rating()) == 2

    def test_delete_book_from_favorites_delete_all_books_from_favorites_there_are_no_books_in_favorites(self): #Добавляем 2 книги. Добавляем их в избранное. В избранном 2 книги. Удаляем их из избранного. В избранном нет книг.
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        # добавляем книгу
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        # добавляем книги в избранное
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        # удаляем книги из избранного
        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')
        collector.delete_book_from_favorites('Что делать, если ваш кот хочет вас убить')
        # список favorites содержит 0 книг, список get_books_rating содержит 2 книги
        assert len(collector.get_list_of_favorites_books()) == 0 and len(collector.get_books_rating()) == 2