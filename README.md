![example workflow](https://github.com/glebkarl/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)
1. Автор-один из студентов Яндекс.Практикума;
2. Применялись Python, Django, Django REST Framework, Docker, nginx, GitHub, GitHub Actions;
3. Примеры запросов к API:
   -Произведения, к которым пишут отзывы: http://158.160.29.115/api/v1/titles/
   -Получить список всех отзывов: http://158.160.29.115/api/v1/titles/{title_id}/reviews/
4. Документация к API по адресу http://158.160.29.115/redoc/
5. Создать юзера для админки: python manage.py createsuperuser