# bashion_ktv
1.数据库和Django工程的同步命令:
    刪除数据库中的所有表包括bashion_ktv这个库，执行django1.9之前的版本python manage.py migrate
2.
CREATE TABLE `room`(
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `type` varchar(255) NOT NULL,
    `room_number` int(11) NOT NULL,
    `name` varchar(255) NOT NULL,
    PRIMARY KEY(`id`),
    UNIQUE KEY(`room_number`)
    )ENGINE=InnoDB DEFAULT CHARSET=UTF8;


CREATE TABLE `room_use_time`(
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `room_number` int(11) NOT NULL,
    `start_time` datetime(6) NOT NULL,
    `end_time` datetime(6) NOT NULL,
    PRIMARY KEY(`id`)
    )ENGINE=InnoDB DEFAULT CHARSET=UTF8;


CREATE TABLE `staff`(
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `staff_number` int(11) NOT NULL,
    `name` varchar(255) NOT NULL,
    `gender` int(1) NOT NULL,
    `age` int(11) NOT NULL ,
    `status` int(11) NOT NULL ,
    `join_time` datetime(6) NOT NULL,
    PRIMARY KEY(`id`)
    )ENGINE=InnoDB DEFAULT CHARSET=UTF8;


CREATE TABLE `order`(
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `room_number` int(11) NOT NULL,
    `fee` int(11) NOT NULL,
    `finish_time` datetime(6) NOT NULL,
    PRIMARY KEY(`id`)
    )ENGINE=InnoDB DEFAULT CHARSET=UTF8;
