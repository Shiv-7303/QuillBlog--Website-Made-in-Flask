-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 03, 2024 at 12:31 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `quillblog`
--

-- --------------------------------------------------------

--
-- Table structure for table `contact`
--

CREATE TABLE `contact` (
  `sno` int(11) NOT NULL,
  `Name` varchar(30) NOT NULL,
  `Email` varchar(30) NOT NULL,
  `Message` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `contact`
--

INSERT INTO `contact` (`sno`, `Name`, `Email`, `Message`) VALUES
(1, 'First-Post', 'firstpost@gmail.com', 'This is my First Post'),
(33, 'Shivansh Rajbhar', 'shivraj7303@gmail.com', 'hii'),
(34, 'Shivansh Rajbhar', 'nanki@bito.com', 'gt'),
(35, 'Shivansh Rajbhar', 'shivrai7303@gmail.com', 'srg'),
(36, 'Shivansh Rajbhar', 'sirojes930@rdluxe.com', 'fgh'),
(37, 'Shivansh Rajbhar', 'shivraj7303@gmail.com', 'sd'),
(38, 'Shivansh Rajbhar', 'sirojes930@rdluxe.com', 'fsff'),
(39, 'Shivansh Rajbhar', 'raishiv7303@gmail.com', 'ds'),
(40, 'Shivansh Rajbhar', 'kabar26942@avidapro.com', 'sdd');

-- --------------------------------------------------------

--
-- Table structure for table `post`
--

CREATE TABLE `post` (
  `sno` int(11) NOT NULL,
  `Title` varchar(30) NOT NULL,
  `slug` varchar(40) NOT NULL,
  `sub_title` varchar(200) NOT NULL,
  `img_file` varchar(50) NOT NULL,
  `Content` text NOT NULL,
  `Date` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `post`
--

INSERT INTO `post` (`sno`, `Title`, `slug`, `sub_title`, `img_file`, `Content`, `Date`) VALUES
(1, 'First Post ', 'first-post', 'dfbgh', '', 'ghfhhgfh', '2024-01-02 14:57:18'),
(3, 'sfsdf', 'sfsdf', 'rwtrertg', '', 'eyteyrgrt', '2024-01-02 14:44:09'),
(4, 'gdfs', 'juyok', 'yj7xhjhghd', '', 'yri57rsxtf', '2024-01-02 11:20:18');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `contact`
--
ALTER TABLE `contact`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `post`
--
ALTER TABLE `post`
  ADD PRIMARY KEY (`sno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `contact`
--
ALTER TABLE `contact`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- AUTO_INCREMENT for table `post`
--
ALTER TABLE `post`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
