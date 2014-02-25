crawler
=======

1. Устанавливаем git:
	sudo apt-get install git
2. Клонируем репозиторий: 
	git clone https://github.com/alex-icez/crawler
3. Устанавливаем Java: 
	sudo apt-get install openjdk-6-jdk
4. Запускаем ElasticSearch и ждем пару-минут:
	./elasticsearch-0.90.5/bin/elasticsearch
5. Устанавливаем автоматический сборщик проектов maven:
	sudo apt-get install maven2
6. Пересобираем роботов:
	mvn clean install
7. Ставим утилиту curl для запросов:
	sudo apt-get install curl
7. Выполняем инциализацию индекса и типа в эластике:
	python init.py
9. Запускаем роботов:
	java -jar target/crawler-0.0.1.jar

Пункты 5-6 можно пропустить.







