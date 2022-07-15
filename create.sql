drop table `Wiki`.`Entity_en4`;

create database Wiki2;

CREATE TABLE `Wiki2`.`Entity_mr2018` (
  `entityId` BIGINT NOT NULL,
  `entityName` VARCHAR(750) NOT NULL)
  #PRIMARY KEY (`entityId`))  
COMMENT = 'Ename is the title of the Wikipedia page\nThis table will list all distinct entities in Wikipedia\n';
 alter table `Wiki2`.`Entity_mr2018` add constraint pk1 PRIMARY KEY(`entityId`,`entityName`);

drop table `Wiki2`.`surfaceNames_en2018`;
CREATE TABLE `Wiki2`.`surfaceNames_mr2018` (
  `surfaceNamesId` BIGINT NOT NULL,
  `surfaceName` VARCHAR(1500) NOT NULL);
  #PRIMARY KEY (`surfaceNamesId`)
 alter table `Wiki2`.`surfaceNames_mr2018` add constraint PRIMARY KEY(`surfaceNamesId`);  

CREATE TABLE `Wiki2`.`entitySurfaceNames_mr2022` (
  `SNo` bigint NOT NULL,
  `entityId` bigint NOT NULL,
  `surfaceNamesId` bigint NOT NULL,
  `frequency` bigint DEFAULT NULL,
  `label` bigint DEFAULT NULL
)  COMMENT 'This table will tell us  how many times each surface name is used for each entity in Wikipedia';
 alter table `Wiki2`.`entitySurfaceNames_mr2018` add unique(`entityId`,`surfaceNamesId`);

CREATE TABLE `Wiki2`.`Mention_mr2018` (
  `instanceId`     bigint NOT NULL,
  `dest_eid`        bigint NOT NULL,
  `mention_sid`       bigint NOT NULL,
  `source_eid`     bigint DEFAULT NULL,
  `editDistance`     bigint DEFAULT NULL,
  `editSuggest`       bigint DEFAULT NULL,
  `isCorrectSubString` bigint DEFAULT NULL,
  `subSuggest`          bigint DEFAULT NULL,
  `isCorrectSuperString` bigint DEFAULT NULL,
  `superSuggest`          bigint DEFAULT NULL,
  `sentence`         varchar(600) DEFAULT NULL)
  COMMENT 'This table will store details of all erroneous surface name usage';

alter table `Wiki2`.`Mention_mr2018` add unique(dest_eid, mention_sid, instanceId);






SET GLOBAL  innodb_buffer_pool_size=1360777216;
CREATE TABLE `best_case_hi` (
  `lower` varchar(105) COLLATE `utf8_general_ci` NOT NULL, 
  `suggest` varchar(105) COLLATE `utf8_general_ci` DEFAULT NULL 
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `Wiki`.`UserVoteTable` (
  `id` BIGINT NOT NULL,
  `uid` VARCHAR(100) NOT NULL,
  `instanceid`  bigint NOT NULL,
  `agreeornot` bigint NOT NULL,
  `datetimeofvote` DATETIME,
  PRIMARY KEY (`id`));
  
alter table `Wiki`.`UserVoteTable` add unique(id,uid,instanceId);