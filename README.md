crawler
=======


1. Клонируем репозиторий: 
	git clone https://github.com/alex-icez/crawler
2. Устанавливаем java(можно так же 6-ую): 
	sudo apt-get install openjdk-7-jdk
3. Скачиваем ElasticSearch
	wget https://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-0.90.5.zip
4. Если не установлен unzip, то ставим
	sudo apt-get install unzip
5. Распаковываем ElasticSearch
	unzip elasticsearch-0.90.5.zip
6. Настраиваем. Добавлем в файл elasticsearch-0.90.5/config/elasticsearch.yml следующие строки:

cluster.name: elasticsearch
node.name: "master"
node.master: true
node.data: true
network.host: localhost
discovery.zen.ping.multicast.enabled: false
discovery.zen.minimum_master_nodes: 1
client.transport.ping_timeout: 180s
http.max_content_length: 10mb
index.number_of_replicas: 1
bootstrap.mlockall: true
gateway.recover_after_nodes: 1
discovery.zen.ping.timeout: 60s

7. Запускаем elastic
./elasticsearch-0.90.5/bin/elasticsearch
и ждем пару-минут.

8. Устанавливаем атоматический сборщик проектов maven:
sudo apt-get install maven3

9. Пересобираем роботов:
mvn clean install

10. Запускаем роботов:
java -jar target/crawler-0.0.1.jar

11. Ставим утилиту curl
sudo apt-get install curl

Скачивание всех статей и индексация с хабра заняла около 10 часов(я сделал некоторый timeout что бы не забанили). Там примерно 70'000 статей.
Размер индекса получился порядка 5 Гб.

В процессе работы в консоль выводятся следующие сообщения:

queue size : 1326 http://habrahabr.ru/post/212305/
это означет, что в очереди на скачивание стоят уже 1326 статей, и добавлена новая по адрессу http://habrahabr.ru/post/212305/

count : 12745
это означает что обработанно уже 12745 статей.


Примеры некоторых запросов с elastic:

Получить 10 статей:
curl -XGET localhost:9200/habr/document/_search | python view.py

Получить 10 статьей автора shulyndina
curl -XGET localhost:9200/habr/document/_search?q=author:shulyndina | python view.py

Кол-во отдаваемый результатов можно задачть следующим образом, через параметр size:

curl -XGET 'http://localhost:9200/habr/document/_search' -d '{
    "query" : {
        "term" : { "author" : "shulyndina" }
    },
	"size" : 1
}' | python view.py

Вывести только тексты статей, автора и релевантность, и просортить по релевантности:

curl -XGET 'http://localhost:9200/habr/document/_search' -d '{
	"sort" : [
		{ "score" : "desc" }        
    ],
	"fields" : ["text", "author", "score"],
	"size" : 5
}' | python view.py

Полнотектовый поиск:















