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
	java -jar target/crawler-0.0.1.jar

7. Ставим утилиту curl
	sudo apt-get install curl







