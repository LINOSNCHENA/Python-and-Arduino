-- Create the table
Drop table if exists audz;
create table audz (
        id serial primary key,
        namex text,
        namey text,
        namez text
    );
insert into audz (namex,namey,namez)
values ('Auduino', 'xy-axis', 'ab-axis');
select * from audz;
