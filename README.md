README.md

### SQL to create first table

```
create table submissions (
	id int auto_increment primary key,
	url varchar(255) not null,
	html longtext not null
);
```