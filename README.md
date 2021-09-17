# Welcome to Alaska!

This is CRUD service for bears in alaska.
CRUD routes presented with REST naming notation:


|Method|Endpoint|Description|
|---|---|---|
|POST |/bear| create|
|GET |/bear| read all bears|
|GET |/bear/:id| read specific bear|
|PUT |/bear/:id| update specific bear|
|DELETE	|/bear| delete all bears|
|DELETE	 |/bear/:id| delete specific bear|

Example of ber json: 

    {"bear_type":"BLACK",
     "bear_name":"mikhail",
     "bear_age":17.5}
     
Available types for bears are: POLAR, BROWN, BLACK and GUMMY.

## Чек лист

### 1. Создание:
#### 1.1 Создание мишек с разными типами

	1.1.1 С типом POLAR - Automated
	1.1.2 С типом BROWN - Automated
	1.1.3 С типом BLACK - Automated
	1.1.4 С типом GUMMY - Automated
	1.1.5 С типом WRONG (негативный) - Automated
	
#### 1.2 Проверки на обязательность полей (негативные)

	1.2.1 Без поля bear_type
	1.2.2 Без поля bear_name
	1.2.3 Без поля bear_age
	
#### 1.3 Проверки типов данных. При создании мишки использовать:

	1.3.1 bear_age с типом float
	1.3.2 bear_age с типом int
	1.3.4 bear_age с типом str не пустая
	1.3.5 bear_age с типом str пустая
	1.3.6 bear_name с типом str пустая
	1.3.7 bear_name с типом str с учетом регистра
	1.3.8 bear_name с типом str с учетом регистра
	1.3.9 bear_name с типом int
	1.3.10 bear_name с типом int отрицательный

### 2. Получение информации о мишке по id:
	2.1 Получение по корректному id + сравнение полученных данных - Automated
	2.2 Получение по несуществующему id 

### 3. Получение информации по всем мишкам
	3.1 Получение информации по всем мишкам и сравнение с ожидаемой информацией - Automated

### 4. Изменение и проверка информации
	4.1 Изменение поля bear_type на корректное - Automated
	4.2 Изменение поля bear_type на не корректное - Automated
	4.3 Изменение поля bear_name - Automated
	4.4 Изменение поля bear_age
	4.5 Проверка возможности изменения при передаче только bear_type
	4.5 Проверка возможности изменения при передаче только bear_name
	4.5 Проверка возможности изменения при передаче только bear_age
	
### 5. Удаление по id
	5.1 Удаление созданного мишки и получение информации по нему - Automated

### 6. Удаление всех
	6.1 Удаление всех мишек и получение информации по id удаленных мишек и по всем мишкам - Automated


Обнаруженные дефекты (или фичи? :) :
* При добавлении мишки имя всегда в верхнем регистре, но при изменении имени, регистр сохраняется в переданном виде
* Нельзя получить информацию о мишке с типом GUMMY
* Не обновляется тип мишки
* Обновить возраст или выполнить попытку обновления типа мишки можно только вместе с передачей поля "bear_name"
