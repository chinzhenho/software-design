-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- 主机： 127.0.0.1
-- 生成日期： 2025-06-19 09:19:39
-- 服务器版本： 10.4.32-MariaDB
-- PHP 版本： 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 数据库： `recycling_system`
--

-- --------------------------------------------------------

--
-- 表的结构 `categories`
--

CREATE TABLE `categories` (
  `category_id` int(11) NOT NULL,
  `category_name` varchar(255) NOT NULL,
  `category_type` enum('Recyclable','Non-Recyclable') NOT NULL,
  `description` varchar(255) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `tip` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- 转存表中的数据 `categories`
--

INSERT INTO `categories` (`category_id`, `category_name`, `category_type`, `description`, `created_at`, `updated_at`, `tip`) VALUES
(72, 'Paper', 'Recyclable', 'Newspapers, magazines, office paper, cardboard boxes, paper bags.', '2025-06-18 07:58:11', '2025-06-18 07:47:37', 'Keep paper clean and dry, and flatten cardboard boxes.'),
(73, 'Glass', 'Recyclable', 'Glass bottles, food jars, wine bottles, sauce jars, beverage containers.', '2025-06-18 07:58:01', '2025-06-18 07:47:53', 'Rinse glass containers and sort by color if required.'),
(74, 'Metal', 'Recyclable', 'Aluminum cans, tin cans, soda cans, food tins, metal bottle caps.', '2025-06-18 07:57:52', '2025-06-18 07:48:08', 'Rinse metal containers and remove labels if possible.'),
(75, 'Electronics ', 'Recyclable', 'Mobile phones, laptops, keyboards, batteries, chargers.', '2025-06-18 07:57:39', '2025-06-18 07:48:24', 'Bring e-waste to special recycling centers, not regular bins.'),
(76, 'Plastic Bags and Film', 'Non-Recyclable', 'Grocery bags, plastic packaging.', '2025-06-18 07:57:19', '2025-06-18 07:48:43', 'Recycle at special collection points, not in home bins.'),
(77, 'Styrofoam ', 'Non-Recyclable', 'Foam cups, food containers.', '2025-06-18 07:57:04', '2025-06-18 07:48:57', 'Put in trash unless special recycling is available.'),
(78, 'Ceramics and Pyrex', 'Non-Recyclable', 'Coffee mugs, plates, baking dishes.', '2025-06-18 07:55:35', '2025-06-18 07:49:11', 'if in good condition, otherwise dispose in trash carefully.'),
(79, 'Greasy or Contaminated Paper', 'Non-Recyclable', 'Napkins, food wrappers, dirty paper plates.', '2025-06-18 07:55:24', '2025-06-18 07:49:27', 'Compost if possible, otherwise dispose in the trash.'),
(80, 'Clothing and Textiles', 'Non-Recyclable', 'Socks, bedsheets, towels, shoes.', '2025-06-19 07:16:17', '2025-06-18 07:49:45', 'Donate or recycle through textile programs, not home bins.'),
(81, 'Plastic', 'Recyclable', 'Water bottles, milk jugs, shampoo bottles, yogurt containers, detergent bottles.', '2025-06-19 07:16:37', '2025-06-19 07:16:37', NULL);

-- --------------------------------------------------------

--
-- 表的结构 `materials`
--

CREATE TABLE `materials` (
  `material_name` varchar(255) NOT NULL,
  `price` float NOT NULL,
  `center_name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- 转存表中的数据 `materials`
--

INSERT INTO `materials` (`material_name`, `price`, `center_name`) VALUES
('wood ', 2, '123 Recycling Center'),
('plastic', 1, 'Meranti Recycling Center'),
('paper', 0.35, 'Cycberjaya Recycling Center'),
('battery', 5, 'Bukit Bintang Center');

-- --------------------------------------------------------

--
-- 表的结构 `recycle_center_materials`
--

CREATE TABLE `recycle_center_materials` (
  `id` int(11) NOT NULL,
  `center_name` varchar(100) DEFAULT NULL,
  `material_name` varchar(100) DEFAULT NULL,
  `amount_kg` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- 转存表中的数据 `recycle_center_materials`
--

INSERT INTO `recycle_center_materials` (`id`, `center_name`, `material_name`, `amount_kg`) VALUES
(1, '123 Recycling Center', 'wood', 3),
(2, 'Meranti Recycling Center', 'paper', 2),
(3, 'Bukit Bintang Center', 'Battery', 5);

-- --------------------------------------------------------

--
-- 表的结构 `recycling_centers`
--

CREATE TABLE `recycling_centers` (
  `id` int(11) NOT NULL,
  `center_name` varchar(255) NOT NULL,
  `location_name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- 转存表中的数据 `recycling_centers`
--

INSERT INTO `recycling_centers` (`id`, `center_name`, `location_name`) VALUES
(1, '123 Recycling Center', 'Cyberjaya'),
(2, 'Meranti Recycling Center', 'Puchong');

-- --------------------------------------------------------

--
-- 表的结构 `survey`
--

CREATE TABLE `survey` (
  `id` int(11) NOT NULL,
  `email` varchar(255) NOT NULL,
  `q1` varchar(50) NOT NULL,
  `q2` varchar(50) NOT NULL,
  `q3` varchar(50) NOT NULL,
  `q4` varchar(50) NOT NULL,
  `q5` text NOT NULL,
  `submitted_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- 转存表中的数据 `survey`
--

INSERT INTO `survey` (`id`, `email`, `q1`, `q2`, `q3`, `q4`, `q5`, `submitted_at`) VALUES
(1, 'ericteoh@gmail.com', 'Very Useful', 'Very Easy', 'Yes, very helpful', 'Yes', 'Good !', '2025-06-08 10:47:14'),
(2, 'ericteoh@gmail.com', 'Somewhat Useful', 'Very Easy', 'Neutral', 'Yes', 'Well !', '2025-06-08 10:56:43');

-- --------------------------------------------------------

--
-- 表的结构 `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `username` varchar(255) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- 转存表中的数据 `user`
--

INSERT INTO `user` (`id`, `username`, `email`, `password`) VALUES
(1, 'Eric', 'ericteoh@gmail.com', '$2b$12$zJtFsgBFKj1Qmp764ERmDOg41w3CvwTAHopB.PKP5agu0FNlTXFOG'),
(2, 'Bernard', 'bernard@gmail.com', '$2b$12$RPjzP9t32y6uPlqIv/5cy.KsQbfCdtxVAR0or9G925pfvNe1JI7N2'),
(3, 'ZhenHo', 'zhenho@gmail.com', '$2b$12$yGgPKw1XHptifZd53rBheOe6YmhzlVLG3niPIxdCZnrbHCTC2NQay'),
(4, 'Tian You', 'Tianyou@gmail.com', '$2b$12$g1/jVUGXDShpfOlF3uigeuv5vMr8ys.CmB6JChhbVq19u0nQoxIYa');

-- --------------------------------------------------------

--
-- 表的结构 `user_profiles`
--

CREATE TABLE `user_profiles` (
  `email` varchar(255) NOT NULL,
  `name` varchar(100) NOT NULL,
  `phone` varchar(20) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `age` int(11) NOT NULL,
  `address` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- 转存表中的数据 `user_profiles`
--

INSERT INTO `user_profiles` (`email`, `name`, `phone`, `gender`, `age`, `address`) VALUES
('ericteoh@gmail.com', 'Eric Teoh Wei Xiang', '0174063708', 'MALE', 21, '56, Bagan Tiang, 34250, Tanjong Piandang,Perak.');

-- --------------------------------------------------------

--
-- 表的结构 `user_proof`
--

CREATE TABLE `user_proof` (
  `id` int(11) NOT NULL,
  `email` varchar(255) NOT NULL,
  `category` varchar(100) NOT NULL,
  `description` text DEFAULT NULL,
  `image_path` varchar(255) DEFAULT NULL,
  `points` int(11) NOT NULL,
  `submitted_at` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- 转存表中的数据 `user_proof`
--

INSERT INTO `user_proof` (`id`, `email`, `category`, `description`, `image_path`, `points`, `submitted_at`) VALUES
(1, 'ericteoh@gmail.com', 'plastic', '', NULL, 1, '2025-06-08 20:46:40'),
(2, 'ericteoh@gmail.com', 'plastic', 'Today I recycle 1kg of plastic.', NULL, 2, '2025-06-08 20:47:25'),
(3, 'ericteoh@gmail.com', 'paper', 'Today I recycle a lot of paper.', 'ericteoh_gmail.com_20250608204758.png', 3, '2025-06-08 20:47:58'),
(4, 'zhenho@gmail.com', 'plastic', '', NULL, 1, '2025-06-08 21:01:51'),
(5, 'zhenho@gmail.com', 'paper', 'I recycle a lot of paper', NULL, 2, '2025-06-08 21:02:06'),
(6, 'bernard@gmail.com', 'plastic', '', NULL, 1, '2025-06-08 21:02:46'),
(7, 'bernard@gmail.com', 'paper', 'I recycle 10KG of paper', 'bernard_gmail.com_20250608210443.png', 3, '2025-06-08 21:04:43'),
(8, 'tianyou@gmail.com', 'plastic', '', NULL, 1, '2025-06-08 21:05:50'),
(9, 'ericteoh@gmail.com', 'paper', 'I recycle a lot of paper', 'ericteoh_gmail.com_20250608211149.png', 3, '2025-06-08 21:11:49');

--
-- 转储表的索引
--

--
-- 表的索引 `categories`
--
ALTER TABLE `categories`
  ADD PRIMARY KEY (`category_id`);

--
-- 表的索引 `recycle_center_materials`
--
ALTER TABLE `recycle_center_materials`
  ADD PRIMARY KEY (`id`);

--
-- 表的索引 `recycling_centers`
--
ALTER TABLE `recycling_centers`
  ADD PRIMARY KEY (`id`);

--
-- 表的索引 `survey`
--
ALTER TABLE `survey`
  ADD PRIMARY KEY (`id`);

--
-- 表的索引 `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- 表的索引 `user_profiles`
--
ALTER TABLE `user_profiles`
  ADD PRIMARY KEY (`email`);

--
-- 表的索引 `user_proof`
--
ALTER TABLE `user_proof`
  ADD PRIMARY KEY (`id`);

--
-- 在导出的表使用AUTO_INCREMENT
--

--
-- 使用表AUTO_INCREMENT `categories`
--
ALTER TABLE `categories`
  MODIFY `category_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=82;

--
-- 使用表AUTO_INCREMENT `recycle_center_materials`
--
ALTER TABLE `recycle_center_materials`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- 使用表AUTO_INCREMENT `recycling_centers`
--
ALTER TABLE `recycling_centers`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- 使用表AUTO_INCREMENT `survey`
--
ALTER TABLE `survey`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- 使用表AUTO_INCREMENT `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- 使用表AUTO_INCREMENT `user_proof`
--
ALTER TABLE `user_proof`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
