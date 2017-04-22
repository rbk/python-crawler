# README.md

- Python 3.5.2
- Flask
- BeautifulSoup

### SQL to create first table

```
create table submissions (
	id int auto_increment primary key,
	url varchar(255) not null,
	html longtext not null
);
```