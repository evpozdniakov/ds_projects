# EDA + Feature engineering

*Проект по курсу [«Профессия Data Science»](https://lms.skillfactory.ru/courses/course-v1:Skillfactory+DST-PRO+15APR2020/about)\
от школы [SkillFactory](https://skillfactory.ru)*

## Цель проекта

- Создать свою первую модель, основанную на алгоритмах машинного обучения.
- Принять участие в соревновании на Kaggle.
- Разобраться, как правильно «подготовить» данные, чтобы модель работала лучше.

## Формулировка задания

Представьте, что вы работаете дата-сайентистом в компании Booking. Одна из проблем компании — это нечестные отели, которые накручивают себе рейтинг. Одним из способов обнаружения таких отелей является построение модели, которая предсказывает рейтинг отеля. Если предсказания модели сильно отличаются от фактического результата, то, возможно, отель ведёт себя нечестно, и его стоит проверить.

## Поля датасета

- `hotel_address` — адрес отеля;
- `review_date` — дата, когда рецензент разместил соответствующий отзыв;
- `average_score` — средний балл отеля, рассчитанный на основе последнего комментария за последний год;
- `hotel_name` — название отеля;
- `reviewer_nationality` — страна рецензента;
- `negative_review` — отрицательный отзыв, который рецензент дал отелю;
- `review_total_negative_word_counts` — общее количество слов в отрицательном отзыв;
- `positive_review` — положительный отзыв, который рецензент дал отелю;
- `review_total_positive_word_counts` — общее количество слов в положительном отзыве.
- `reviewer_score` — оценка, которую рецензент поставил отелю на основе своего опыта;
- `total_number_of_reviews_reviewer_has_given` — количество отзывов, которые рецензенты дали в прошлом;
- `total_number_of_reviews` — общее количество действительных отзывов об отеле;
- `tags` — теги, которые рецензент дал отелю;
- `days_since_review` — количество дней между датой проверки и датой очистки;
- `additional_number_of_scoring` — есть также некоторые гости, которые просто поставили оценку сервису, но не оставили отзыв. Это число указывает, сколько там действительных оценок без проверки.
- `lat` — географическая широта отеля;
- `lng` — географическая долгота отеля.