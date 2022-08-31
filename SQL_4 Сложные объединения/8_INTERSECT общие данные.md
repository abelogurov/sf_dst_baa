### INTERSECT выбираем общие данные

А что если нам надо вывести общие записи — те, что существуют в нескольких таблицах?

Предположим, нам надо вывести совпадающие по названию города и штаты.

### ПОПРОБУЙТЕ В METABASE!

1. SELECT 
2.          c.city_name object_name /*выбираем столбец city_name, задаём ему алиас object_name*/
3. FROM 
4.          sql.city c /*из схемы sql и таблицы city, задаём таблице алиас с*/

5. INTERSECT /*оператор присоединения*/

6. SELECT 
         cc.state /*выбираем столбец state*/
7. FROM 
8.          sql.city cc /*из схемы sql и таблицы city, задаём таблице алиас с*/
9. ORDER BY 1

Как видим, с помощью оператора INTERSECT мы вывели названия городов и штатов, которые совпадают: New York, Washington и Wyoming. Присмотримся к нему внимательнее.

* [Чтобы лучше понять, как работает этот оператор, вновь обратимся к диаграмме Венна: INTERSECT оставляет из результатов первого запроса все строки, которые совпали с результатом выполнения второго запроса.](https://drive.google.com/file/d/1XbVUpKplPLW9w4ZratbEYWsOv_eAx3FT/view?usp=sharing)

Синтаксис запроса с оператором INTERSECT выглядит следующим образом:

1. SELECT 
2.          n columns
3. FROM 
4.          table_1
 
5. INTERSECT

6. SELECT 
7.          n columns
8. FROM 
9.          table_2

Вернёмся к нашему примеру с продажами канцтоваров.

* [С помощью оператора INTERSECT мы можем вывести те позиции, которые продавались и в мае, и в июне. Визуализировать это действие можно примерно так:](https://drive.google.com/file/d/16hOzVds9YU6mHNn4k5bkxfMYIP-rSLO2/view?usp=sharing)

Оператор INTERSECT оставляет только те строки, которые являются общими для двух запросов (в нашем примере это Тетрадь).

Как EXCEPT, так и INTERSECT убирают дубликаты, если они имеются.

### Задание 8.1

Напишите запрос, который выведет список id городов, в которых есть и клиенты, и доставки, и водители.

1. SELECT s.city_id
2. FROM sql.shipment s 
3. INTERSECT
4. SELECT c.city_id
5. FROM sql.customer c
6. INTERSECT
7. SELECT d.city_id
8. FROM sql.driver d

### Задание 8.2

Выведите zip-код, который есть как в таблице с клиентами, так и в таблице с водителями.

1. SELECT c.zip
2. FROM sql.customer c
3. INTERSECT 
4. SELECT d.zip_code
5. FROM sql.driver d