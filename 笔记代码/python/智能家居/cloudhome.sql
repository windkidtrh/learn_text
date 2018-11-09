-- phpMyAdmin SQL Dump
-- version 3.4.10.1
-- http://www.phpmyadmin.net
--
-- 主机: localhost
-- 生成日期: 2017 年 08 月 04 日 12:25
-- 服务器版本: 5.5.20
-- PHP 版本: 5.3.10

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- 数据库: `cloudhome`
--

-- --------------------------------------------------------

--
-- 表的结构 `log`
--

CREATE TABLE IF NOT EXISTS `log` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `user_id` int(10) NOT NULL,
  `the_time` datetime NOT NULL,
  `info` text NOT NULL,
  PRIMARY KEY (`id`,`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='用户使用功能日志' AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- 表的结构 `log_drive`
--

CREATE TABLE IF NOT EXISTS `log_drive` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_type` varchar(8) NOT NULL,
  `second_type` varchar(8) NOT NULL,
  `device_nums` int(11) NOT NULL,
  `the_time` datetime NOT NULL,
  `current_status` varchar(20) NOT NULL,
  `info` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=44 ;

--
-- 转存表中的数据 `log_drive`
--

INSERT INTO `log_drive` (`id`, `first_type`, `second_type`, `device_nums`, `the_time`, `current_status`, `info`) VALUES
(1, 'AABC', 'AADG', 2, '2017-04-14 20:15:19', '01_00_01', '00013345'),
(2, 'AAKG', 'AASX', 1, '2017-04-14 20:15:20', '00_00_00', '0'),
(3, 'AAKG', 'AASX', 1, '2017-04-14 20:15:21', '00_00_00', '0'),
(4, 'AAKG', 'AASX', 1, '2017-04-14 20:15:23', '00_00_00', '0'),
(5, 'AABC', 'AADG', 1, '2017-04-14 20:15:24', '01_00_01', '00013393'),
(6, 'AAKG', 'AASX', 1, '2017-04-14 20:15:25', '00_00_00', '0'),
(7, 'AAKG', 'AASX', 1, '2017-04-14 20:15:27', '00_00_00', '0'),
(8, 'AAKG', 'AASX', 1, '2017-04-14 20:15:28', '00_00_00', '0'),
(9, 'AABC', 'AAFS', 3, '2017-04-14 20:15:30', '00_00_00', '00013226'),
(10, 'AAKG', 'AASX', 1, '2017-04-14 20:15:30', '00_00_00', '0'),
(11, 'AABC', 'AADG', 2, '2017-04-14 20:15:30', '01_00_01', '00013345'),
(12, 'AAKG', 'AASX', 1, '2017-04-14 20:15:32', '00_00_00', '0'),
(13, 'AAKG', 'AASX', 1, '2017-04-14 20:15:33', '00_00_00', '0'),
(14, 'AABC', 'AADG', 1, '2017-04-14 20:15:35', '01_00_01', '00013393'),
(15, 'AAKG', 'AASX', 1, '2017-04-14 20:15:35', '00_00_00', '0'),
(16, 'AABC', 'AAFS', 1, '2017-04-14 20:15:36', '00_00_01', '00013221'),
(17, 'AAKG', 'AASX', 1, '2017-04-14 20:15:37', '00_00_00', '0'),
(18, 'AAKG', 'AASX', 1, '2017-04-14 20:15:39', '00_00_00', '0'),
(19, 'AAKG', 'AASX', 1, '2017-04-14 20:15:40', '00_00_00', '0'),
(20, 'AABC', 'AADG', 2, '2017-04-14 20:15:41', '01_00_01', '00013345'),
(21, 'AAKG', 'AASX', 1, '2017-04-14 20:15:42', '00_00_00', '0'),
(22, 'AAKG', 'AASX', 1, '2017-04-14 20:15:44', '00_00_00', '0'),
(23, 'AABC', 'AACL', 2, '2017-04-14 20:15:45', '00_10_01', '00013435'),
(24, 'AAKG', 'AASX', 1, '2017-04-14 20:15:46', '00_00_00', '0'),
(25, 'AABC', 'AADG', 1, '2017-04-14 20:15:46', '01_00_01', '00013393'),
(26, 'AABC', 'AACL', 3, '2017-04-14 20:15:46', '00_10_01', '00013436'),
(27, 'AABC', 'AAFS', 2, '2017-04-14 20:15:46', '00_00_00', '00013223'),
(28, 'AAKG', 'AASX', 1, '2017-04-14 20:15:47', '00_00_00', '0'),
(29, 'AAKG', 'AASX', 1, '2017-04-14 20:15:49', '00_00_00', '0'),
(30, 'AAKG', 'AASX', 1, '2017-04-14 20:15:51', '00_00_00', '0'),
(31, 'AABC', 'AADG', 2, '2017-04-14 20:15:52', '01_00_01', '00013345'),
(32, 'AAKG', 'AASX', 1, '2017-04-14 20:15:53', '00_00_00', '0'),
(33, 'AAKG', 'AASX', 1, '2017-04-14 20:15:54', '00_00_00', '0'),
(34, 'AAKG', 'AASX', 1, '2017-04-14 20:15:56', '00_00_00', '0'),
(35, 'AABC', 'AAFS', 4, '2017-04-14 20:15:57', '00_00_00', '00013227'),
(36, 'AABC', 'AADG', 1, '2017-04-14 20:15:57', '01_00_01', '00013393'),
(37, 'AAKG', 'AASX', 1, '2017-04-14 20:15:58', '00_00_00', '0'),
(38, 'AAKG', 'AASX', 1, '2017-04-14 20:15:59', '00_00_00', '0'),
(39, 'AAKG', 'AASX', 1, '2017-04-14 20:16:01', '00_00_00', '0'),
(40, 'AABC', 'AADG', 2, '2017-04-14 20:16:03', '01_00_01', '00013345'),
(41, 'AAKG', 'AASX', 1, '2017-04-14 20:16:03', '00_00_00', '0'),
(42, 'AAKG', 'AASX', 1, '2017-04-14 20:16:05', '00_00_00', '0'),
(43, 'AAKG', 'AASX', 1, '2017-04-14 20:16:06', '00_00_00', '0');

-- --------------------------------------------------------

--
-- 表的结构 `log_scene`
--

CREATE TABLE IF NOT EXISTS `log_scene` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `scene_id` int(11) NOT NULL,
  `answer_time` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=62 ;

--
-- 转存表中的数据 `log_scene`
--

INSERT INTO `log_scene` (`id`, `user_id`, `scene_id`, `answer_time`) VALUES
(1, 1, 3, '2017.04.14 21.31'),
(2, 1, 3, '2017.04.14 21.31'),
(3, 1, 3, '2017.04.14 21.31'),
(4, 1, 3, '2017.04.14 21.31'),
(5, 1, 3, '2017.04.14 21.31'),
(6, 1, 3, '2017.04.14 21.31'),
(7, 1, 3, '2017.04.14 21.32'),
(8, 1, 3, '2017.04.14 21.32'),
(9, 1, 3, '2017.04.14 21.33'),
(10, 1, 3, '2017.04.14 21.33'),
(11, 1, 3, '2017.04.14 21.34'),
(12, 1, 3, '2017.04.14 21.34'),
(13, 1, 3, '2017.04.14 21.35'),
(14, 1, 3, '2017.04.14 21.36'),
(15, 1, 3, '2017.04.14 21.36'),
(16, 1, 3, '2017.04.14 21.37'),
(17, 1, 3, '2017.04.14 21.37'),
(18, 1, 3, '2017.04.14 21.38'),
(19, 1, 3, '2017.04.14 21.38'),
(20, 1, 3, '2017.04.14 21.46'),
(21, 1, 3, '2017.04.14 21.46'),
(22, 1, 3, '2017.04.14 21.51'),
(23, 1, 3, '2017.04.14 21.51'),
(24, 1, 3, '2017.04.14 21.54'),
(25, 1, 3, '2017.04.14 21.54'),
(26, 1, 3, '2017.04.14 22.01'),
(27, 1, 3, '2017.04.14 22.01'),
(28, 1, 3, '2017.04.14 22.03'),
(29, 1, 3, '2017.04.14 22.03'),
(30, 1, 3, '2017.04.14 22.04'),
(31, 1, 3, '2017.04.14 22.04'),
(32, 1, 3, '2017.04.14 22.04'),
(33, 1, 3, '2017.04.14 22.04'),
(34, 1, 3, '2017.04.14 22.05'),
(35, 1, 3, '2017.04.14 22.05'),
(36, 1, 3, '2017.04.14 22.06'),
(37, 1, 3, '2017.04.14 22.06'),
(38, 1, 3, '2017.04.14 22.07'),
(39, 1, 3, '2017.04.14 22.07'),
(40, 1, 3, '2017.04.14 22.08'),
(41, 1, 3, '2017.04.14 22.08'),
(42, 1, 3, '2017.04.14 22.12'),
(43, 1, 3, '2017.04.14 22.12'),
(44, 1, 3, '2017.04.14 22.17'),
(45, 1, 3, '2017.04.14 22.17'),
(46, 1, 3, '2017.04.14 22.18'),
(47, 1, 3, '2017.04.14 22.18'),
(48, 1, 3, '2017.04.14 22.19'),
(49, 1, 3, '2017.04.14 22.19'),
(50, 1, 3, '2017.04.14 23.26'),
(51, 1, 3, '2017.04.14 23.26'),
(52, 1, 3, '2017.04.14 23.26'),
(53, 1, 3, '2017.04.14 23.26'),
(54, 1, 3, '2017.04.14 23.27'),
(55, 1, 3, '2017.04.14 23.27'),
(56, 1, 3, '2017.04.14 23.28'),
(57, 1, 3, '2017.04.14 23.28'),
(58, 1, 3, '2017.04.14 23.29'),
(59, 1, 3, '2017.04.14 23.29'),
(60, 1, 3, '2017.04.16 21.15'),
(61, 1, 3, '2017.04.16 21.15');

-- --------------------------------------------------------

--
-- 表的结构 `log_switch`
--

CREATE TABLE IF NOT EXISTS `log_switch` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_type` varchar(4) NOT NULL,
  `second_type` varchar(4) NOT NULL,
  `product_num` int(11) NOT NULL,
  `the_time` datetime NOT NULL,
  `info` text NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=4 ;

--
-- 转存表中的数据 `log_switch`
--

INSERT INTO `log_switch` (`id`, `first_type`, `second_type`, `product_num`, `the_time`, `info`) VALUES
(1, 'AAKG', 'AACL', 2, '2017-04-14 20:15:13', 'online'),
(2, 'AAKG', 'AACL', 3, '2017-04-14 20:15:34', 'online'),
(3, 'AAKG', 'AACL', 2, '2017-04-14 20:15:45', 'online');

-- --------------------------------------------------------

--
-- 表的结构 `log_timer`
--

CREATE TABLE IF NOT EXISTS `log_timer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `timer_id` int(11) NOT NULL,
  `first_type` varchar(20) NOT NULL,
  `second_type` varchar(20) NOT NULL,
  `product_num` int(11) NOT NULL,
  `state` varchar(20) NOT NULL,
  `set_time` varchar(20) NOT NULL,
  `answer_time` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=18 ;

--
-- 转存表中的数据 `log_timer`
--

INSERT INTO `log_timer` (`id`, `user_id`, `timer_id`, `first_type`, `second_type`, `product_num`, `state`, `set_time`, `answer_time`) VALUES
(1, 1, 1, 'AABC', 'AADG', 1, '00_00_11', '14.48', ''),
(2, 1, 6, 'AABC', 'AASX', 1, '01_10_01', '21.13', '2017.03.14 21.13'),
(3, 1, 7, 'AABC', 'AASX', 1, '00_00_00', '21.14', '2017.03.14 21.14'),
(4, 1, 8, 'AABC', 'AASX', 1, '00_10_01', '21.15', '2017.03.14 21.15'),
(5, 1, 6, 'AABC', 'AASX', 1, '01_10_01', '21.16', '2017.03.14 21.16'),
(6, 1, 7, 'AABC', 'AASX', 1, '00_00_00', '21.17', '2017.03.14 21.17'),
(7, 1, 8, 'AABC', 'AASX', 1, '00_10_01', '21.18', '2017.03.14 21.18'),
(8, 1, 6, 'AABC', 'AASX', 1, '01_10_01', '21.20', '2017.03.14 21.20'),
(9, 1, 7, 'AABC', 'AASX', 1, '00_00_00', '21.21', '2017.03.14 21.21'),
(10, 1, 8, 'AABC', 'AASX', 1, '00_10_01', '21.21', '2017.03.14 21.21'),
(11, 1, 7, 'AABC', 'AASX', 1, '00_00_00', '21.22', '2017.03.14 21.22'),
(12, 1, 6, 'AABC', 'AASX', 1, '01_10_01', '21.23', '2017.03.14 21.23'),
(13, 1, 6, 'AABC', 'AASX', 1, '01_10_01', '20.24', '2017.04.14 20.24'),
(14, 1, 7, 'AABC', 'AACL', 2, '00_00_01', '20.27', '2017.04.14 20.27'),
(15, 1, 6, 'AABC', 'AACL', 3, '01_10_01', '23.38', '2017.04.14 23.38'),
(16, 1, 7, 'AABC', 'AACL', 2, '00_00_01', '23.38', '2017.04.14 23.38'),
(17, 1, 8, 'AABC', 'AACL', 2, '00_10_01', '23.39', '2017.04.14 23.39');

-- --------------------------------------------------------

--
-- 表的结构 `manage_request`
--

CREATE TABLE IF NOT EXISTS `manage_request` (
  `first_type` varchar(4) NOT NULL,
  `second_type` varchar(4) NOT NULL,
  `product_num` int(11) NOT NULL,
  `life` int(1) NOT NULL,
  `request_value` int(8) NOT NULL,
  `return_value` int(8) NOT NULL,
  `state` text NOT NULL,
  PRIMARY KEY (`first_type`,`second_type`,`product_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `product`
--

CREATE TABLE IF NOT EXISTS `product` (
  `first_type` varchar(4) NOT NULL,
  `second_type` varchar(4) NOT NULL,
  `product_num` int(11) NOT NULL,
  `regist_num` varchar(5) NOT NULL,
  `mac` varchar(12) NOT NULL,
  `product_state` tinyint(1) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`first_type`,`second_type`,`product_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `product`
--

INSERT INTO `product` (`first_type`, `second_type`, `product_num`, `regist_num`, `mac`, `product_state`, `user_id`) VALUES
('AABC', 'AACL', 1, '12345', '123413411331', 1, 1),
('AABC', 'AACL', 2, '12345', '12313132131', 1, 1),
('AABC', 'AACL', 3, '12345', '123123213131', 1, 1),
('AABC', 'AADG', 1, '12345', '123456789123', 1, 1),
('AABC', 'AADG', 2, '12345', '12421424', 1, 1),
('AABC', 'AADG', 3, '12345', '12414512412', 1, 1),
('AABC', 'AADG', 4, '12345', '12312412541', 1, 1),
('AABC', 'AAFS', 1, '12345', '123456789123', 1, 1),
('AABC', 'AAFS', 2, '12345', '123456789123', 1, 1),
('AABC', 'AAFS', 3, '12345', '123456789123', 1, 1),
('AABC', 'AAFS', 4, '12345', '123456789123', 1, 1),
('AABC', 'AASX', 1, '12345', '112233445566', 0, 1),
('AABC', 'AASX', 2, '12345', '123456789123', 0, 1),
('AABC', 'AASX', 3, '12345', '112233445566', 1, 1),
('AABC', 'AASX', 4, '12345', '112233445566', 1, 1),
('AABC', 'AASX', 5, '12345', '112233445566', 1, 1),
('AABC', 'AASX', 6, '12345', '112233445566', 0, 0),
('AABC', 'AATC', 1, '12345', '123456789123', 1, 1),
('AABC', 'LIPK', 1, '12345', '123456789123', 1, 1),
('AAKG', 'AACT', 1, '12345', '123456789123', 1, 1),
('AAKG', 'AADG', 1, '12345', '123456789123', 1, 1),
('AAKG', 'AASX', 1, '12345', '123456789123', 1, 1),
('AAKG', 'AASX', 2, '12345', '123456789123', 1, 1),
('AAKG', 'AASX', 3, '12345', '123456789123', 1, 1),
('GABC', 'AASX', 1, '41243', '23532532', 127, 1),
('JFBS', 'JFBS', 1, '12345', '123456789123', 1, 1);

-- --------------------------------------------------------

--
-- 表的结构 `product_belong_to`
--

CREATE TABLE IF NOT EXISTS `product_belong_to` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `first_type` varchar(4) NOT NULL,
  `second_type` varchar(4) NOT NULL,
  `product_num` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `pro_name` varchar(22) NOT NULL,
  PRIMARY KEY (`product_num`,`first_type`,`second_type`,`user_id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=37 ;

--
-- 转存表中的数据 `product_belong_to`
--

INSERT INTO `product_belong_to` (`id`, `first_type`, `second_type`, `product_num`, `user_id`, `pro_name`) VALUES
(22, 'AABC', 'AASX', 0, 44, ''),
(26, 'AAKG', 'A', 0, 58, ''),
(23, ' AAB', 'AATC', 1, 1, '停车位模型'),
(30, 'AABC', 'AACL', 1, 1, ''),
(25, 'AABC', 'AADG', 1, 1, ''),
(33, 'AABC', 'AAFS', 1, 1, ''),
(17, 'AABC', 'AASX', 1, 1, '窗帘'),
(8, 'AABC', 'AASX', 1, 3, ''),
(19, 'AAKG', 'AACT', 1, 1, '乌璐'),
(24, 'AAKG', 'AADG', 1, 1, ''),
(18, 'AAKG', 'AASX', 1, 1, '四向测'),
(12, 'AAKG', 'LIPK', 1, 1, ''),
(1, 'GABC', 'AASX', 1, 1, ''),
(31, 'AABC', 'AACL', 2, 1, ''),
(27, 'AABC', 'AADG', 2, 1, '123'),
(34, 'AABC', 'AAFS', 2, 1, ''),
(11, 'AABC', 'AASX', 2, 1, ''),
(20, 'AAKG', 'AASX', 2, 1, 'asd'),
(32, 'AABC', 'AACL', 3, 1, ''),
(28, 'AABC', 'AADG', 3, 1, '123'),
(35, 'AABC', 'AAFS', 3, 1, ''),
(4, 'AABC', 'AASX', 3, 1, ''),
(21, 'AAKG', 'AASX', 3, 1, ''),
(29, 'AABC', 'AADG', 4, 1, '123'),
(36, 'AABC', 'AAFS', 4, 1, ''),
(5, 'AABC', 'AASX', 4, 1, ''),
(6, 'AABC', 'AABB', 5, 1, '');

-- --------------------------------------------------------

--
-- 表的结构 `product_current_state`
--

CREATE TABLE IF NOT EXISTS `product_current_state` (
  `first_type` varchar(4) NOT NULL,
  `second_type` varchar(4) NOT NULL,
  `product_num` int(11) NOT NULL,
  `current_state` text NOT NULL,
  `request_state` text,
  `ip_address` varchar(16) NOT NULL,
  `net_port` int(6) NOT NULL,
  `online_value` int(1) NOT NULL,
  `belong_id` int(10) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`first_type`,`second_type`,`product_num`),
  UNIQUE KEY `belong_id` (`belong_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=459 ;

--
-- 转存表中的数据 `product_current_state`
--

INSERT INTO `product_current_state` (`first_type`, `second_type`, `product_num`, `current_state`, `request_state`, `ip_address`, `net_port`, `online_value`, `belong_id`) VALUES
('AABC', 'AACL', 2, '00_10_01', NULL, '113.107.163.197', 1406, 2, 448),
('AABC', 'AACL', 3, '00_10_01', NULL, '113.107.163.197', 1375, 2, 447),
('AABC', 'AADG', 1, '01_00_01', NULL, '113.107.163.197', 12000, 2, 445),
('AABC', 'AADG', 2, '01_00_01', NULL, '113.107.163.197', 1334, 2, 446),
('AABC', 'AAFS', 1, '00_00_01', NULL, '113.107.163.197', 1463, 2, 458),
('AABC', 'AAFS', 2, '00_00_00', NULL, '113.107.163.197', 1464, 2, 450),
('AABC', 'AAFS', 3, '00_00_00', NULL, '113.107.163.197', 1453, 2, 449),
('AABC', 'AAFS', 4, '00_00_00', NULL, '113.107.163.197', 1466, 2, 451),
('AAKG', 'AASX', 1, '00_00_00', NULL, '223.73.106.140', 21436, 2, 452);

-- --------------------------------------------------------

--
-- 表的结构 `product_description`
--

CREATE TABLE IF NOT EXISTS `product_description` (
  `first_type` varchar(4) NOT NULL,
  `second_type` varchar(4) NOT NULL,
  `property` text,
  PRIMARY KEY (`first_type`,`second_type`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `product_description`
--

INSERT INTO `product_description` (`first_type`, `second_type`, `property`) VALUES
('GABC', 'AASX', 'rwgebteb');

-- --------------------------------------------------------

--
-- 表的结构 `room`
--

CREATE TABLE IF NOT EXISTS `room` (
  `room_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `f_id` int(11) NOT NULL DEFAULT '0' COMMENT '父级ID',
  `f_room_id` int(11) NOT NULL DEFAULT '0',
  `room_name` varchar(20) NOT NULL COMMENT '房间名',
  PRIMARY KEY (`room_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='物体对应的房间表' AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- 表的结构 `room_product`
--

CREATE TABLE IF NOT EXISTS `room_product` (
  `rp_id` int(11) NOT NULL AUTO_INCREMENT,
  `room_id` int(11) NOT NULL,
  `product_id` int(11) NOT NULL,
  PRIMARY KEY (`rp_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='房间与设备对应表' AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- 表的结构 `save_tmp_value`
--

CREATE TABLE IF NOT EXISTS `save_tmp_value` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `last_value` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=3 ;

--
-- 转存表中的数据 `save_tmp_value`
--

INSERT INTO `save_tmp_value` (`id`, `last_value`) VALUES
(1, 13504),
(2, 13504);

-- --------------------------------------------------------

--
-- 表的结构 `scene`
--

CREATE TABLE IF NOT EXISTS `scene` (
  `scene_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `scene_name` char(20) NOT NULL,
  PRIMARY KEY (`scene_id`),
  UNIQUE KEY `user_id` (`user_id`,`scene_name`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=6 ;

--
-- 转存表中的数据 `scene`
--

INSERT INTO `scene` (`scene_id`, `user_id`, `scene_name`) VALUES
(4, 1, 'gaga'),
(3, 1, 'haha'),
(5, 2, 'haha');

-- --------------------------------------------------------

--
-- 表的结构 `scene_product`
--

CREATE TABLE IF NOT EXISTS `scene_product` (
  `scene_id` int(11) NOT NULL,
  `first_type` char(4) NOT NULL,
  `second_type` char(4) NOT NULL,
  `product_num` int(11) NOT NULL,
  `state` char(20) NOT NULL,
  PRIMARY KEY (`scene_id`,`first_type`,`second_type`,`product_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `scene_product`
--

INSERT INTO `scene_product` (`scene_id`, `first_type`, `second_type`, `product_num`, `state`) VALUES
(3, 'AABC', 'AACL', 2, '11_22_11'),
(3, 'AABC', 'AACL', 3, '11_22_11');

-- --------------------------------------------------------

--
-- 表的结构 `set_timer`
--

CREATE TABLE IF NOT EXISTS `set_timer` (
  `timer_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `first_type` char(20) NOT NULL,
  `second_type` char(20) NOT NULL,
  `product_num` int(11) NOT NULL,
  `state` char(20) NOT NULL,
  `set_time` char(20) NOT NULL,
  `set_day` char(20) NOT NULL,
  PRIMARY KEY (`timer_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=9 ;

--
-- 转存表中的数据 `set_timer`
--

INSERT INTO `set_timer` (`timer_id`, `user_id`, `first_type`, `second_type`, `product_num`, `state`, `set_time`, `set_day`) VALUES
(6, 1, 'AABC', 'AACL', 3, '01_10_01', '23.38', '0123456'),
(7, 1, 'AABC', 'AACL', 2, '00_00_01', '23.38', '0123456'),
(8, 1, 'AABC', 'AACL', 2, '00_10_01', '23.39', '0123456');

-- --------------------------------------------------------

--
-- 表的结构 `switch_join_device`
--

CREATE TABLE IF NOT EXISTS `switch_join_device` (
  `first_type` varchar(4) NOT NULL,
  `second_type` varchar(4) NOT NULL,
  `product_num` int(11) NOT NULL,
  `target_first_type` varchar(4) NOT NULL,
  `target_second_type` varchar(4) NOT NULL,
  `target_product_num` varchar(11) NOT NULL,
  PRIMARY KEY (`first_type`,`second_type`,`product_num`,`target_first_type`,`target_second_type`,`target_product_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='??ҪԼ??һ????Ʒ????Ϊָ??ֵ';

--
-- 转存表中的数据 `switch_join_device`
--

INSERT INTO `switch_join_device` (`first_type`, `second_type`, `product_num`, `target_first_type`, `target_second_type`, `target_product_num`) VALUES
('AAAA', 'BBBB', 1, 'GABC', 'AASX', '1'),
('AABC', 'AADG', 1, 'AABC', 'AADG', '1'),
('AABC', 'AADG', 2, 'AABC', 'AADG', '2'),
('AAKG', 'AACL', 1, 'AABC', 'AACL', '1'),
('AAKG', 'AACL', 2, 'AABC', 'AACL', '2'),
('AAKG', 'AACL', 3, 'AABC', 'AACL', '3'),
('AAKG', 'AACT', 1, 'AABC', 'AASX', '1'),
('AAKG', 'AASX', 1, 'AABC', 'AASX', '1'),
('AAKG', 'AASX', 1, 'AABC', 'AASX', '3'),
('AAKG', 'AASX', 1, 'AABC', 'AASX', '4'),
('AAKG', 'AASX', 1, 'AAKG', 'AASX', '1'),
('AAKG', 'AASX', 2, 'AABC', 'AASX', '2'),
('AAKG', 'AASX', 3, 'AABC', 'AASX', '3');

-- --------------------------------------------------------

--
-- 表的结构 `user`
--

CREATE TABLE IF NOT EXISTS `user` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `phone` varchar(11) NOT NULL,
  `user_name` varchar(20) NOT NULL,
  `user_pwd` varchar(20) NOT NULL,
  `user_set` text,
  `last_set_time` datetime DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=62 ;

--
-- 转存表中的数据 `user`
--

INSERT INTO `user` (`user_id`, `phone`, `user_name`, `user_pwd`, `user_set`, `last_set_time`) VALUES
(1, '13929718507', '13929718507', '123456', '123', '2017-03-26 08:34:56'),
(3, '15910103707', '15910103707', '123456', NULL, NULL),
(41, '13709641376', '13709641376', '123456', NULL, NULL),
(44, '13620453854', '13620453854', 'tommego940703', NULL, NULL),
(45, '15917103707', '15917103707', '13543381597myc', NULL, NULL),
(48, '13714926977', '13714926977', '123456', NULL, NULL),
(58, '18719125879', '18719125879', 'abcd644934', NULL, NULL),
(59, '13929709806', 'zhang', 'meng', NULL, NULL),
(60, '13929709223', 'zhang234', 'meng23', NULL, NULL),
(61, '13437564131', 'Kscn99', '123456', NULL, NULL);

-- --------------------------------------------------------

--
-- 表的结构 `user_membership`
--

CREATE TABLE IF NOT EXISTS `user_membership` (
  `member_id` int(10) NOT NULL AUTO_INCREMENT,
  `user_id` int(10) NOT NULL,
  `f_id` int(10) NOT NULL DEFAULT '0',
  ` alias` varchar(22) NOT NULL COMMENT '别名备注',
  PRIMARY KEY (`member_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='关系表' AUTO_INCREMENT=1 ;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
