SET SQL_SAFE_UPDATES = 0;
use test ;

create table user (
	id int(11) not null auto_increment,
    name varchar(20) not null,
    sex varchar(20) default null,
    age int(11) default null,
    phone varchar(20) default null,
    primary key(id)
);

#delete from user; 

insert into user values(1,'wang wu','male',23,'123');
insert into user values(2,'li si','male',26,'123');
insert into user values(3,'zhang wei','male',18,'123');
insert into user values(4,'li wu','male',34,'123');
insert into user values(5,'chen er','male',23,'123');
insert into user values(6,'zhang wei','male',29,'123');
insert into user values(7,'zhang zhi','male',25,'123');

#delete from user where name like '%wang%';

select avg(age) avg_age from user;

select name,age from user where  age between 20 and 30 and name like '%zhang%' order by age;

create table team (
	id int(11) not null auto_increment,
    teamName varchar(20) default null,
    primary key(id)
);

insert into team values (1,'ECNU');
insert into team values (2,'SEI');

select teamName from team;

create table score (
	id int(11) not null auto_increment,
    teamid int(11) not null,
    userid int(11) not null,
    score int(11) default null,
    primary key(id)
);

insert into score values (1,2,1,1);
insert into score values (2,1,2,2);
insert into score values (3,1,5,3);
insert into score values (4,1,3,4);
insert into score values (5,1,4,12);
insert into score values (6,2,7,12);
insert into score values (7,1,6,4);

select name from user usr join score sc on usr.id=sc.userid join team tm on sc.teamid=tm.id and tm.teamName='ECNU' where age<20;

select sum(score) from score join team on team.id=score.teamid and team.teamName='ECNU';

drop table user;
drop table team;
drop table score;

