crawler
=======


1. Клонируем репозиторий: 
	git clone https://github.com/alex-ice/crawler
2. Устанавливаем Java(можно так же 6-ую): 
	sudo apt-get install openjdk-7-jdk
3. Запускаем ElasticSearch
	./elasticsearch-0.90.5/bin/elasticsearch
и ждем пару-минут.

[4,5, если хочется пересобрать проект]
4. Устанавливаем автоматический сборщик проектов maven:
sudo apt-get install maven3

5. Пересобираем роботов:
mvn clean install

6. Запускаем роботов:
Java -jar target/crawler-0.0.1.jar

7. Ставим утилиту curl
sudo apt-get install curl

Скачивание всех статей и индексация с хабра заняло около 8 часов(я сделал своеобразный timeout что бы не забанили). Там примерно 55'000 статей. Их чуть меньше чем на самом деле, это связано с тем что роботы "шли" к статьям через "хабы". Если их пустить через "посты", то их будет немного больше.

Размер индекса получился порядка 2,2 Гб.

В процессе работы в консоль выводятся следующие сообщения:

queue size : 1326 http://habrahabr.ru/post/212305/
это означет, что в очереди на скачивание стоят уже 1326 статей, и добавлена новая по адресу http://habrahabr.ru/post/212305/

count : 12745
это означает что обработано уже 12745 статей.


Примеры некоторых запросов с elastic:

Получить 10 статей:
curl -GET localhost:9200/habr/document/_search | python view.py

Получить 10 статьей автора shulyndina
curl -GET localhost:9200/habr/document/_search?q=author:shulyndina | python view.py

Кол-во отдаваемый результатов можно задать следующим образом, через параметр size:

curl -GET 'http://localhost:9200/habr/document/_search' -d '{
    "query" : {
        "term" : { "author" : "shulyndina" }
    },
	"size" : 1
}' | python view.py

Вывести только тексты статей, автора, релевантность, и просортить по релевантности:

curl -GET 'http://localhost:9200/habr/document/_search' -d '{
	"sort" : [
		{ "score" : "desc" }        
    ],
	"fields" : ["text", "author", "score"],
	"size" : 5
}' | python view.py

Полнотекстовый поиск:
curl -GET 'http://localhost:9200/habr/document/_search' -d '{
	"sort" : [
		{ "score" : "desc" }        
    ],
	"fields" : ["text", "author", "score"],
	"size" : 5,
	"query" : {
		"query_string" : {
			"default_operator" : "AND",
        	"query" : "фонда планируется потратить 38,7 млн руб."
   	 	}
	}
}' | python view.py

В общем, вот мануал по эластику где описываются всевозможные к нему запросы:
http://www.elastic search.org/guide/en/elastic search/reference/current/query-dsl-queries.html

В принципе, я сделал открытым свой эластик, который находится у меня на компьютере, и Вы сможете удаленно посмотреть запросы.
замените localhost 95.31.222.171 (но он не всегда будет доступен)

Так же запросы можно делать через некоторые плагины к браузерам, позволяющие конфигурировать POST запросы.








