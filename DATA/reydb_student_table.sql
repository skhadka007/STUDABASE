-- MySQL dump 10.13  Distrib 8.0.20, for Win64 (x86_64)
--
-- Host: localhost    Database: reydb
-- ------------------------------------------------------
-- Server version	8.0.20

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `student_table`
--

DROP TABLE IF EXISTS `student_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student_table` (
  `First_Name` varchar(25) NOT NULL,
  `Last_Name` varchar(25) NOT NULL,
  `Student_ID` int NOT NULL,
  `Email` varchar(50) NOT NULL,
  `Department` varchar(25) NOT NULL,
  `Major` varchar(25) NOT NULL,
  `Grad_Date` date NOT NULL,
  PRIMARY KEY (`Student_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student_table`
--

LOCK TABLES `student_table` WRITE;
/*!40000 ALTER TABLE `student_table` DISABLE KEYS */;
INSERT INTO `student_table` VALUES ('Blythe','Kreisel',1,'Blythe.Kreisel@schooll.edu','Engineering','Computer Science','2022-12-30'),('Jani','Bittle',2,'Jani.Bittle@schooll.edu','Business','Finance','2021-12-30'),('Awilda','Betterton',3,'Awilda.Betterton@schooll.edu','Sciences','Chemistry','2023-12-30'),('Tomiko','Mccausland',4,'Tomiko.Mccausland@school.edu','Education','Mathematics','2021-08-30'),('Lucas','Jelks',5,'Lucas.Jelks@school.edu','Engineering','Electrical Engineering','2024-12-30'),('Basil','Bates',6,'Basil.Bates@school.edu','Business','IT','2022-05-30'),('Kristy','Webber',7,'Kristy.Webber@school.edu','Sciences','Geology','2024-05-30'),('Daisey','Staller',8,'Daisey.Staller@school.edu','Education','Counseling','2022-08-30'),('Elane','Chamberlain',9,'Elane.Chamberlain@school.edu','Education','Nutrition','2023-05-30'),('Mira','Holen',10,'Mira.Holen@school.edu','Sciences','Chemistry','2024-08-30'),('Ernie','Hgehrke',11,'Ernie.Hgehrke@school.edu','Business','Finance','2022-05-30'),('Arron','Valente',12,'Arron.Valente@school.edu','Engineering','Mechanical Enginerring','2021-12-30'),('Catherina','Newbill',13,'Catherina.Newbill@school.edu','Business','Accounting','2023-08-30'),('Winnie','Wingert',14,'Winnie.Wingert@school.edu','Engineering','Computer Science','2023-05-30'),('Vena','Conforti',15,'Vena.Conforti@school.edu','Engineering','Computer Science','2024-05-30'),('Tyrone','Neuhaus',16,'Tyrone.Neuhaus@school.edu','Sciences','Physics','2022-08-30'),('Elinore','Kling',17,'Elinore.Kling@school.edu','Business','Finance','2023-08-30'),('Pansy','Bellinger',18,'Pansy.Bellinger@school.edu','Business','Accounting','2022-08-30'),('Maude','Leisinger',19,'Maude.Leisinger@school.edu','Sciences','Chemistry','2021-08-30'),('Myrtie','Keplinger',20,'Myrtie.Keplinger@school.edu','Business','Accounting','2022-05-30'),('Jerald','Woodman',21,'Jerald.Woodman@school.edu','Education','Mathematics','2022-12-30'),('Krysta','Mcmurty',22,'Krysta.Mcmurty@school.edu','Education','Kinesiology','2023-12-30'),('Morgan','Tookers',23,'Morgan.Tookers@school.edu','Business','Marketing','2024-12-30'),('Dewitt','Swanigan',24,'Dewitt.Swanigan@school.edu','Business','Finance','2024-05-30'),('Nan','Best',25,'Nan.Best@school.edu','Engineering','Mechanical Enginerring','2023-12-30'),('Suzanna','Okelley',26,'Suzanna.Okelley@school.edu','Sciences','Biology','2023-05-30'),('Eartha','Baer',27,'Eartha.Baer@school.edu','Engineering','Electrical Engineering','2022-08-30'),('Jonathon','Longoria',28,'Jonathon.Longoria@school.edu','Engineering','Electrical Engineering','2021-12-30'),('Lona','Acklin',29,'Lona.Acklin@school.edu','Sciences','Physics','2022-05-30'),('Agueda','Lyman',30,'Agueda.Lyman@school.edu','Business','Marketing','2023-12-30'),('Marylynn','Nyland',31,'Marylynn.Nyland@school.edu','Education','Kinesiology','2024-08-30'),('Efren','Murakami',32,'Efren.Murakami@school.edu','Sciences','Geology','2021-12-30'),('Eric','Massingill',33,'Eric.Massingill@school.edu','Sciences','Biology','2022-12-30'),('Madison','Johansson',34,'Madison.Johansson@school.edu','Sciences','Biology','2023-12-30'),('Janette','Paredez',35,'Janette.Paredez@school.edu','Engineering','Electrical Engineering','2021-08-30'),('Shawn','Baskerville',36,'Shawn.Baskerville@school.edu','Engineering','Mechanical Enginerring','2023-08-30'),('Carola','Toone',37,'Carola.Toone@school.edu','Education','Mathematics','2023-12-30'),('Eldridge','Manso',38,'Eldridge.Manso@school.edu','Business','Marketing','2022-08-30'),('Shawnna','Corker',39,'Shawnna.Corker@school.edu','Business','Accounting','2021-08-30'),('Hiedi','Slape',40,'Hiedi.Slape@school.edu','Engineering','Computer Science','2021-12-30'),('Ellena','Crooms',41,'Ellena.Crooms@school.edu','Business','Marketing','2021-12-30'),('Analisa','Mccusker',42,'Analisa.Mccusker@school.edu','Engineering','Computer Science','2021-08-30'),('Gregory','Mccrystal',43,'Gregory.Mccrystal@school.edu','Business','Accounting','2024-05-30'),('Lajuana','Calixte',44,'Lajuana.Calixte@school.edu','Business','Accounting','2023-08-30'),('Brook','Hallenbeck',45,'Brook.Hallenbeck@school.edu','Engineering','Computer Science','2023-05-30'),('Dorthy','Diederich',46,'Dorthy.Diederich@school.edu','Sciences','Chemistry','2021-08-30'),('Simona','Thrailkill',47,'Simona.Thrailkill@school.edu','Engineering','Computer Science','2023-12-30'),('Delta','Howse',48,'Delta.Howse@school.edu','Business','IT','2022-12-30'),('Helaine','Sarles',49,'Helaine.Sarles@school.edu','Business','IT','2022-08-30'),('Thurman','Love',50,'Thurman.Love@school.edu','Business','IT','2023-12-30'),('Myesha','Shipe',51,'Myesha.Shipe@school.edu','Education','Nutrition','2022-05-30'),('Inocencia','Hembree',52,'Inocencia.Hembree@school.edu','Business','Finance','2021-08-30'),('Lloyd','Maruin',53,'Lloyd.Maruin@school.edu','Education','Counseling','2022-12-30'),('Merrie','Champine',54,'Merrie.Champine@school.edu','Engineering','Electrical Engineering','2023-05-30'),('Nora','Dunkire',55,'Nora.Dunkire@school.edu','Sciences','Chemistry','2023-12-30'),('Dianna','Melecio',56,'Dianna.Melecio@school.edu','Business','Finance','2022-12-30'),('Orlando','Hartle',57,'Orlando.Hartle@school.edu','Sciences','Biology','2021-12-30'),('Domenic','Kitamura',58,'Domenic.Kitamura@school.edu','Education','Counseling','2024-08-30'),('Pearly','Caivedo',59,'Pearly.Caivedo@school.edu','Engineering','Mechanical Enginerring','2023-08-30'),('Darcel','Shin',60,'Darcel.Shin@school.edu','Sciences','Biology','2021-08-30'),('Melinda','Kinnison',61,'Melinda.Kinnison@school.edu','Business','IT','2021-08-30'),('Samantha','Klippel',62,'Samantha.Klippel@school.edu','Business','IT','2021-12-30'),('Tilda','Gurganus',63,'Tilda.Gurganus@school.edu','Business','Accounting','2024-05-30'),('Andra','Weathersby',64,'Andra.Weathersby@school.edu','Engineering','Mechanical Enginerring','2022-08-30'),('Chantay','Galdamez',65,'Chantay.Galdamez@school.edu','Engineering','Electrical Engineering','2024-05-30'),('Talisha','Multon',66,'Talisha.Multon@school.edu','Sciences','Biology','2022-08-30'),('Annette','Dilbeck',67,'Annette.Dilbeck@school.edu','Sciences','Physics','2022-12-30'),('Zora','Cluff',68,'Zora.Cluff@school.edu','Engineering','Computer Science','2024-05-30'),('Chana','Farraj',69,'Chana.Farraj@school.edu','Sciences','Physics','2021-12-30'),('Estelle','Quijas',70,'Estelle.Quijas@school.edu','Education','Mathematics','2021-08-30'),('Annabell','Cheatam',71,'Annabell.Cheatam@school.edu','Business','Marketing','2024-08-30'),('Kemberly','Abeyta',72,'Kemberly.Abeyta@school.edu','Business','Accounting','2024-12-30'),('Alida','Richman',73,'Alida.Richman@school.edu','Education','Kinesiology','2022-12-30'),('Vanessa','Koerber',74,'Vanessa.Koerber@school.edu','Engineering','Computer Science','2021-08-30'),('Carie','Qualey',75,'Carie.Qualey@school.edu','Engineering','Electrical Engineering','2024-08-30'),('Jonathon','Landi',76,'Jonathon.Landi@school.edu','Business','Marketing','2023-05-30'),('Luciana','Gomer',77,'Luciana.Gomer@school.edu','Sciences','Geology','2022-05-30'),('Lupita','Forbis',78,'Lupita.Forbis@school.edu','Business','Finance','2024-12-30'),('Marc','Pfeifer',79,'Marc.Pfeifer@school.edu','Engineering','Electrical Engineering','2023-05-30'),('Lavone','Rush',80,'Lavone.Rush@school.edu','Engineering','Electrical Engineering','2024-12-30'),('Maximo','Gong',81,'Maximo.Gong@school.edu','Sciences','Physics','2021-08-30'),('Margareta','Fane',82,'Margareta.Fane@school.edu','Sciences','Chemistry','2022-12-30'),('Catina','Mclead',83,'Catina.Mclead@school.edu','Engineering','Mechanical Enginerring','2022-08-30'),('Cherish','Thiessen',84,'Cherish.Thiessen@school.edu','Engineering','Computer Science','2021-12-30'),('Wilbur','Bellin',85,'Wilbur.Bellin@school.edu','Business','IT','2022-05-30'),('Launa','Hardwick',86,'Launa.Hardwick@school.edu','Business','IT','2023-12-30'),('Melodi','Mutchler',87,'Melodi.Mutchler@school.edu','Business','Marketing','2023-08-30'),('Tajuana','Estrella',88,'Tajuana.Estrella@school.edu','Education','Mathematics','2022-08-30'),('Elaina','Stennis',89,'Elaina.Stennis@school.edu','Sciences','Biology','2021-12-30'),('Lyman','Jugh',90,'Lyman.Jugh@school.edu','Sciences','Biology','2021-12-30'),('Omar','Knepp',91,'Omar.Knepp@school.edu','Engineering','Computer Science','2022-12-30'),('Zack','Ferro',92,'Zack.Ferro@school.edu','Business','IT','2023-05-30'),('Domonique','Thaler',93,'Domonique.Thaler@school.edu','Engineering','Computer Science','2022-05-30'),('Sherrie','Wilmore',94,'Sherrie.Wilmore@school.edu','Engineering','Computer Science','2024-12-30'),('Gino','Dennison',95,'Gino.Dennison@school.edu','Sciences','Biology','2022-12-30'),('Sherrill','Culton',96,'Sherrill.Culton@school.edu','Business','Marketing','2021-12-30'),('Ada','Burget',97,'Ada.Burget@school.edu','Business','Marketing','2023-08-30'),('Willetta','Mease',98,'Willetta.Mease@school.edu','Business','Finance','2024-12-30'),('Lesha','Craine',99,'Lesha.Craine@school.edu','Business','Accounting','2022-05-30'),('Kris','Benitez',100,'Kris.Benitez@school.edu','Education','Mathematics','2024-08-30');
/*!40000 ALTER TABLE `student_table` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-06-30 22:06:54
