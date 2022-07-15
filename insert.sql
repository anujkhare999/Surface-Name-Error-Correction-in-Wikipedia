truncate table `Wiki`.`Entity_en10`;
SET GLOBAL local_infile=1;
load data local infile '/home/anuj/Documents/Dump_temp_de_2018/Anuj_Table1.demo(2022)2.txt' into table `Wiki2`.`Entity_mr2018` 
fields terminated by ',' ENCLOSED BY '`'
lines terminated by '\n'
Ignore 1 LINES;


load data local infile '/home/anuj/Documents/Dump_temp_de_2018/Anuj_Table2.demo(2022)2.txt' into table `Wiki2`.`surfaceNames_mr2018` 
fields terminated by ',' ENCLOSED BY '`'
lines terminated by '\n'
Ignore 1 LINES;


load data local infile '/home/anuj/Documents/Dump_temp_de_2018/Anuj_Table5.demo(2022)2.txt' into table `Wiki2`.`entitySurfaceNames_mr2018` 
fields terminated by ',' ENCLOSED BY '`'
ENCLOSED BY '~'
lines terminated by '\n'
Ignore 1 LINES;

-- load data local infile '/home/anuj/Documents/Dump_temp_de_2018/Anuj_Table6.demo(2022)2.txt' into table `Wiki2`.`Mention_mr2018`
-- fields terminated by ',' ENCLOSED BY '`'
-- lines terminated by '\n'
-- Ignore 1 LINES ;

load data local infile '/home/anuj/Documents/Dump_temp_de_2022/Anuj_Table1.demo(2022)2.txt' into table `Wiki2`.`Entity_mr2022` 
fields terminated by ',' ENCLOSED BY '`'
lines terminated by '\n'
Ignore 1 LINES;

load data local infile '/home/anuj/Documents/Dump_temp_de_2022/Anuj_Table2.demo(2022)2.txt' into table `Wiki2`.`surfaceNames_mr2022` 
fields terminated by ',' ENCLOSED BY '`'
lines terminated by '\n'
Ignore 1 LINES;


load data local infile '/home/anuj/Documents/Dump_temp_de_2022/Anuj_Table5.demo(2022)2.txt' into table `Wiki2`.`entitySurfaceNames_mr2022` 
fields terminated by ',' ENCLOSED BY '`'
ENCLOSED BY '~'
lines terminated by '\n'
Ignore 1 LINES;

-- load data local infile '/home/anuj/Documents/Dump_temp_de_2022/Anuj_Table6.demo(2022)2.txt' into table `Wiki2`.`Mention_mr2022`
-- fields terminated by ',' ENCLOSED BY '`'
-- lines terminated by '\n'
-- Ignore 1 LINES ;

show warnings;
show warnings;

select * from `Wiki`.`entitySurfaceNames_en4`;

select count(*) from `Wiki`.`entitySurfaceNames_hi2`;

select * from `Wiki`.`Mention_hi4`;
show warnings;
truncate table `Wiki`.`Mention_hi4`;
load data local infile '/home/anuj/Documents/Dump_temp_hi_2022/Anuj_Table1.demo(2022).txt' into table `Wiki`.`Mention_en10` 
fields terminated by ','  enclosed by '`'
lines terminated by '\n'
Ignore 1 LINES;

show warnings;