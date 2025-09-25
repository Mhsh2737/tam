

create table lessons
(
    id       integer primary key autoincrement,
    title    text,
    teacher  text,
    unit     integer
);


insert into lessons (title, teacher, unit) values ( 'python', 'ali', 3);
insert into lessons (title, teacher, unit) values ( 'c', 'morteza', 2);


update lessons set title='java', teacher='amir' where id=1;

delete from lessons where id=1;

select title,teacher from lessons;
