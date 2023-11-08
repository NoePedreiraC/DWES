-- MariaDB dump 10.19  Distrib 10.11.3-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: mysitedb
-- ------------------------------------------------------
-- Server version	10.11.3-MariaDB-1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `tCanciones`
--

DROP TABLE IF EXISTS `tCanciones`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tCanciones` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) DEFAULT NULL,
  `url_imagen` varchar(200) DEFAULT NULL,
  `genero` varchar(50) DEFAULT NULL,
  `duracion` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tCanciones`
--

LOCK TABLES `tCanciones` WRITE;
/*!40000 ALTER TABLE `tCanciones` DISABLE KEYS */;
INSERT INTO `tCanciones` VALUES
(1,'Suave','https://geo-media.beatsource.com/image_size/500x500/8/1/6/81612ff6-a285-469c-a7ac-b5515c5a3c77.jpg','Urbano latino',136),
(2,'Purple Widow','https://is1-ssl.mzstatic.com/image/thumb/Music125/v4/ad/6e/5e/ad6e5ed0-43b3-c10b-bab0-0d22e3c98256/cover.jpg/600x600bf-60.jpg','Techno',382),
(3,'Weltschmerz','https://i1.sndcdn.com/artworks-MCsFdaITqg1fqb7e-eMOydg-t500x500.jpg','Techno',385),
(4,'Suave','https://geo-media.beatsource.com/image_size/500x500/8/1/6/81612ff6-a285-469c-a7ac-b5515c5a3c77.jpg','Urbano latino',136),
(5,'Purple Widow','https://is1-ssl.mzstatic.com/image/thumb/Music125/v4/ad/6e/5e/ad6e5ed0-43b3-c10b-bab0-0d22e3c98256/cover.jpg/600x600bf-60.jpg','Techno',382),
(6,'Weltschmerz','https://i1.sndcdn.com/artworks-MCsFdaITqg1fqb7e-eMOydg-t500x500.jpg','Techno',385),
(7,'Suave','https://geo-media.beatsource.com/image_size/500x500/8/1/6/81612ff6-a285-469c-a7ac-b5515c5a3c77.jpg','Urbano latino',136),
(8,'Purple Widow','https://is1-ssl.mzstatic.com/image/thumb/Music125/v4/ad/6e/5e/ad6e5ed0-43b3-c10b-bab0-0d22e3c98256/cover.jpg/600x600bf-60.jpg','Techno',382),
(9,'Weltschmerz','https://i1.sndcdn.com/artworks-MCsFdaITqg1fqb7e-eMOydg-t500x500.jpg','Techno',385);
/*!40000 ALTER TABLE `tCanciones` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tComentarios`
--

DROP TABLE IF EXISTS `tComentarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tComentarios` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `comentario` varchar(2000) DEFAULT NULL,
  `cancion_id` int(11) NOT NULL,
  `usuario_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `cancion_id` (`cancion_id`),
  KEY `usuario_id` (`usuario_id`),
  CONSTRAINT `tComentarios_ibfk_1` FOREIGN KEY (`cancion_id`) REFERENCES `tCanciones` (`id`),
  CONSTRAINT `tComentarios_ibfk_2` FOREIGN KEY (`usuario_id`) REFERENCES `tUsuarios` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tComentarios`
--

LOCK TABLES `tComentarios` WRITE;
/*!40000 ALTER TABLE `tComentarios` DISABLE KEYS */;
INSERT INTO `tComentarios` VALUES
(1,'Me encanta esta canción',1,1),
(2,'Me encanta esta canción',2,2),
(3,'Temardoooooo',3,3),
(4,'Me encanta el techno',4,4),
(5,'Me gusta mas el Remix',5,5);
/*!40000 ALTER TABLE `tComentarios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tUsuarios`
--

DROP TABLE IF EXISTS `tUsuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tUsuarios` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) DEFAULT NULL,
  `apellidos` varchar(100) DEFAULT NULL,
  `email` varchar(200) DEFAULT NULL,
  `contraseña` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tUsuarios`
--

LOCK TABLES `tUsuarios` WRITE;
/*!40000 ALTER TABLE `tUsuarios` DISABLE KEYS */;
INSERT INTO `tUsuarios` VALUES
(1,'Jose','Perez','joseperez69@email.com','abc123..'),
(2,'Segundo','Ocaña','segundoocana69@email.com','abc123..'),
(3,'Benigno',' Martín','benignomartin69@email.com','abc123..'),
(4,'Elsa','Porico','elsaporico69@email.com','abc123..'),
(5,'Meardel','Peson','meardelpeson69@email.com','abc123..');
/*!40000 ALTER TABLE `tUsuarios` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-10-18 14:32:45
