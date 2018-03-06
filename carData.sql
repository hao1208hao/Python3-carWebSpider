/*
Navicat MySQL Data Transfer

Source Server         : 本机电脑
Source Server Version : 50717
Source Host           : localhost:3306
Source Database       : test

Target Server Type    : MYSQL
Target Server Version : 50717
File Encoding         : 65001

Date: 2017-09-28 16:08:36
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for cardata
-- ----------------------------
DROP TABLE IF EXISTS `cardata`;
CREATE TABLE `cardata` (
  `catid` int(10) DEFAULT NULL COMMENT '车大类ID',
  `brandid` int(10) DEFAULT NULL COMMENT '品牌ID',
  `brandsn` int(10) DEFAULT NULL COMMENT '车型ID',
  `itemid` int(10) DEFAULT NULL COMMENT '最终详细ID',
  `carname` varchar(255) DEFAULT NULL COMMENT '车大类名',
  `brandshortname` varchar(255) DEFAULT NULL COMMENT '品牌首字母',
  `brandname` varchar(255) DEFAULT NULL COMMENT '品牌名',
  `cartypename` varchar(255) DEFAULT NULL COMMENT '车型名',
  `cartype` varchar(255) DEFAULT NULL COMMENT '车型小类名',
  `detailcarname` varchar(255) DEFAULT NULL COMMENT '具体车型名',
  `engine` varchar(255) DEFAULT NULL COMMENT '发动机型号'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


