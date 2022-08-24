### UNION и дополнительные условия

UNION также может быть использован для разделения существующей выборки по критерию «выполнение определённого условия».

Например, с помощью UNION можно отобразить, у кого из водителей заполнен столбец с номером телефона.

### ПОПРОБУЙТЕ В METABASE!

1. SELECT
2.          d.first_name,
3.          d.last_name,
4.          'телефон заполнен' phone_info /*выбираем столбцы first_name, last_name, сами выводим объект ‘телефон заполнен’*/
5. FROM
6.          sql.driver d /*из схемы sql и таблицы driver, задаём алиас d*/
7. WHERE d.phone IS NOT NULL /*условие, что телефон заполнен*/

8. UNION /*оператор присоединения (уникальные значения)*/

9. SELECT
10.          d.first_name,
11.          d.last_name,
12.          'телефон не заполнен' phone_info /*выбираем столбцы first_name, last_name, сами выводим объект ‘телефон не заполнен’*/
13. FROM
14.          sql.driver d /*из схемы sql и таблицы driver, задаём алиас d*/
15. WHERE d.phone IS NULL /*условие, что телефон не заполнен*/

### Задание 5.1

Напишите запрос, который выведет все города и штаты, в которых они расположены, а также информацию о том, была ли осуществлена доставка в этот город:

- если в город была осуществлена доставка, то выводим 'доставка осуществлялась';
- если нет — выводим 'доставка не осуществлялась'.

Столбцы к выводу: city_name, state, shipping_status.
Отсортируйте в алфавитном порядке по городу, а затем — по штату.

1. SELECT
2.     city_name city_name,
3.     state state,
4.     'доставка осуществлялась' shipping_status
5. FROM
6.     sql.city c
7.     LEFT JOIN sql.shipment s ON c.city_id = s.city_id
8. WHERE s.city_id IS NOT NULL
9. union
10. SELECT
11.     city_name city_name,
12.     state state,
13.     'доставка не осуществлялась' shipping_status
14. FROM
15.     sql.city c
16.     LEFT JOIN sql.shipment s ON c.city_id = s.city_id
17. WHERE s.city_id IS NULL

### Задание 5.2

Напишите запрос, который выводит два столбца: city_name и shippings_fake. Выведите города, куда совершались доставки.

Пусть первый столбец содержит название города, а второй формируется так:

если в городе было более десяти доставок, вывести количество доставок в этот город как есть;
иначе — вывести количество доставок, увеличенное на пять.
Отсортируйте по убыванию получившегося «нечестного» количества доставок, а затем — по имени в алфавитном порядке.

1. SELECT
2.     city_name city_name,
3.     count(s.city_id) shippings_fake
4. FROM 
5.     sql.city c
6. JOIN sql.shipment s on c.city_id = s.city_id
7. GROUP BY 1
8. HAVING count(s.city_id) > 10
9. UNION
10. SELECT
11.     city_name city_name,
12.     count(s.city_id) + 5 shippings_fake
13. FROM 
14.     sql.city c
15. JOIN sql.shipment s on c.city_id = s.city_id
16. GROUP BY 1
17. HAVING count(s.city_id) <= 10
18. ORDER BY 2 DESC, 1