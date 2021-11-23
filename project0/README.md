# Алгоритм угадвающий число за минимальное количество попыток

*Проект по курсу [«Профессия Data Science»](https://lms.skillfactory.ru/courses/course-v1:Skillfactory+DST-PRO+15APR2020/about)\
от школы [SkillFactory](https://skillfactory.ru)*

## Описание модуля

Получает целое число от 1 до 100. Делает последовательные предсказания, постепенно приближаясь к искомому числу (на основе подсказок больше/меньше). Возвращает количество попыток потраченное на поиск числа.

## Содержание модуля

Содержит 3 функции:
- [guess_number(number_to_guess: int) -> int](#guess_number)
- [guess_number_user_test()](#guess_number_user_test)
- [guess_number_mean_test() -> float](#guess_number_mean_test)

### guess_number

Основная функция. Содержит алгоритм угадывания числа. Пример использования:

```py
attempts = guess_number(28)

print(attempts) # 5
```

### guess_number_user_test

Можно использовать для тестирования guess_number.

### guess_number_mean_test

Запускает guess_number 10000 раз и возвращает среднее количество попыток
```py
mean_number_of_attempts = guess_number_mean_test()

print(mean_number_of_attempts) # 5.781
```