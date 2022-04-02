CREATE DATABASE  IF NOT EXISTS `bookerbd` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;
USE `bookerbd`;
-- MariaDB dump 10.19  Distrib 10.4.21-MariaDB, for Win64 (AMD64)
--
-- Host: 127.0.0.1    Database: bookerbd
-- ------------------------------------------------------
-- Server version	10.4.21-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `administradores`
--

DROP TABLE IF EXISTS `administradores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `administradores` (
  `id_administrador` int(11) NOT NULL AUTO_INCREMENT,
  `tipodoc` varchar(5) DEFAULT NULL,
  `nombres` varchar(50) NOT NULL,
  `apellidos` varchar(50) NOT NULL,
  `telefono` varchar(20) DEFAULT NULL,
  `direccion` varchar(100) DEFAULT NULL,
  `doc` varchar(20) NOT NULL,
  PRIMARY KEY (`id_administrador`),
  KEY `administradores_doc_127e967f_fk_api_usuario_doc` (`doc`),
  CONSTRAINT `administradores_doc_127e967f_fk_api_usuario_doc` FOREIGN KEY (`doc`) REFERENCES `api_usuario` (`doc`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `administradores`
--

LOCK TABLES `administradores` WRITE;
/*!40000 ALTER TABLE `administradores` DISABLE KEYS */;
/*!40000 ALTER TABLE `administradores` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `api_usuario`
--

DROP TABLE IF EXISTS `api_usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `api_usuario` (
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `doc` varchar(20) NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `email` varchar(60) DEFAULT NULL,
  `imagen` varchar(200) DEFAULT NULL,
  `usuario_activo` tinyint(1) NOT NULL,
  `usuario_administrador` tinyint(1) NOT NULL,
  PRIMARY KEY (`doc`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `api_usuario`
--

LOCK TABLES `api_usuario` WRITE;
/*!40000 ALTER TABLE `api_usuario` DISABLE KEYS */;
INSERT INTO `api_usuario` VALUES ('pbkdf2_sha256$260000$lB4PlJfy1pnaKcP1Q8N5NI$0U8IIsQjXHqswIlqQW17nK3600S5r5D38NKYvzTdNNA=','2022-04-02 22:36:41.062457','1','Booker','eamendez85@misena.edu.co','',1,1);
/*!40000 ALTER TABLE `api_usuario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=93 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add administradores',7,'add_administradores'),(26,'Can change administradores',7,'change_administradores'),(27,'Can delete administradores',7,'delete_administradores'),(28,'Can view administradores',7,'view_administradores'),(29,'Can add autores',8,'add_autores'),(30,'Can change autores',8,'change_autores'),(31,'Can delete autores',8,'delete_autores'),(32,'Can view autores',8,'view_autores'),(33,'Can add categorias',9,'add_categorias'),(34,'Can change categorias',9,'change_categorias'),(35,'Can delete categorias',9,'delete_categorias'),(36,'Can view categorias',9,'view_categorias'),(37,'Can add editoriales',10,'add_editoriales'),(38,'Can change editoriales',10,'change_editoriales'),(39,'Can delete editoriales',10,'delete_editoriales'),(40,'Can view editoriales',10,'view_editoriales'),(41,'Can add ejemplares',11,'add_ejemplares'),(42,'Can change ejemplares',11,'change_ejemplares'),(43,'Can delete ejemplares',11,'delete_ejemplares'),(44,'Can view ejemplares',11,'view_ejemplares'),(45,'Can add estudiantes',12,'add_estudiantes'),(46,'Can change estudiantes',12,'change_estudiantes'),(47,'Can delete estudiantes',12,'delete_estudiantes'),(48,'Can view estudiantes',12,'view_estudiantes'),(49,'Can add grados',13,'add_grados'),(50,'Can change grados',13,'change_grados'),(51,'Can delete grados',13,'delete_grados'),(52,'Can view grados',13,'view_grados'),(53,'Can add grupos',14,'add_grupos'),(54,'Can change grupos',14,'change_grupos'),(55,'Can delete grupos',14,'delete_grupos'),(56,'Can view grupos',14,'view_grupos'),(57,'Can add idiomas',15,'add_idiomas'),(58,'Can change idiomas',15,'change_idiomas'),(59,'Can delete idiomas',15,'delete_idiomas'),(60,'Can view idiomas',15,'view_idiomas'),(61,'Can add tipo infraccion',16,'add_tipoinfraccion'),(62,'Can change tipo infraccion',16,'change_tipoinfraccion'),(63,'Can delete tipo infraccion',16,'delete_tipoinfraccion'),(64,'Can view tipo infraccion',16,'view_tipoinfraccion'),(65,'Can add usuario',17,'add_usuario'),(66,'Can change usuario',17,'change_usuario'),(67,'Can delete usuario',17,'delete_usuario'),(68,'Can view usuario',17,'view_usuario'),(69,'Can add reservas',18,'add_reservas'),(70,'Can change reservas',18,'change_reservas'),(71,'Can delete reservas',18,'delete_reservas'),(72,'Can view reservas',18,'view_reservas'),(73,'Can add prestados',19,'add_prestados'),(74,'Can change prestados',19,'change_prestados'),(75,'Can delete prestados',19,'delete_prestados'),(76,'Can view prestados',19,'view_prestados'),(77,'Can add libros',20,'add_libros'),(78,'Can change libros',20,'change_libros'),(79,'Can delete libros',20,'delete_libros'),(80,'Can view libros',20,'view_libros'),(81,'Can add infracciones',21,'add_infracciones'),(82,'Can change infracciones',21,'change_infracciones'),(83,'Can delete infracciones',21,'delete_infracciones'),(84,'Can view infracciones',21,'view_infracciones'),(85,'Can add favoritos',22,'add_favoritos'),(86,'Can change favoritos',22,'change_favoritos'),(87,'Can delete favoritos',22,'delete_favoritos'),(88,'Can view favoritos',22,'view_favoritos'),(89,'Can add de prestamos',23,'add_deprestamos'),(90,'Can change de prestamos',23,'change_deprestamos'),(91,'Can delete de prestamos',23,'delete_deprestamos'),(92,'Can view de prestamos',23,'view_deprestamos');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `autores`
--

DROP TABLE IF EXISTS `autores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `autores` (
  `id_autor` int(11) NOT NULL AUTO_INCREMENT,
  `nombres` varchar(50) NOT NULL,
  `apellidos` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id_autor`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `autores`
--

LOCK TABLES `autores` WRITE;
/*!40000 ALTER TABLE `autores` DISABLE KEYS */;
/*!40000 ALTER TABLE `autores` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `categorias`
--

DROP TABLE IF EXISTS `categorias`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `categorias` (
  `id_categoria` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id_categoria`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categorias`
--

LOCK TABLES `categorias` WRITE;
/*!40000 ALTER TABLE `categorias` DISABLE KEYS */;
/*!40000 ALTER TABLE `categorias` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `de_prestamos`
--

DROP TABLE IF EXISTS `de_prestamos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `de_prestamos` (
  `id_de_prestamo` int(11) NOT NULL AUTO_INCREMENT,
  `fec_prestamo` datetime(6) NOT NULL,
  `fec_devolucion` datetime(6) NOT NULL,
  `estado` varchar(3) NOT NULL,
  `id_administrador` int(11) NOT NULL,
  `id_estudiante` int(11) NOT NULL,
  PRIMARY KEY (`id_de_prestamo`),
  KEY `de_prestamos_id_administrador_03aa9a0a_fk_administr` (`id_administrador`),
  KEY `de_prestamos_id_estudiante_97000d86_fk_estudiantes_id_estudiante` (`id_estudiante`),
  CONSTRAINT `de_prestamos_id_administrador_03aa9a0a_fk_administr` FOREIGN KEY (`id_administrador`) REFERENCES `administradores` (`id_administrador`),
  CONSTRAINT `de_prestamos_id_estudiante_97000d86_fk_estudiantes_id_estudiante` FOREIGN KEY (`id_estudiante`) REFERENCES `estudiantes` (`id_estudiante`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `de_prestamos`
--

LOCK TABLES `de_prestamos` WRITE;
/*!40000 ALTER TABLE `de_prestamos` DISABLE KEYS */;
/*!40000 ALTER TABLE `de_prestamos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `de_prestamos_ejemplares`
--

DROP TABLE IF EXISTS `de_prestamos_ejemplares`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `de_prestamos_ejemplares` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `deprestamos_id` int(11) NOT NULL,
  `ejemplares_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `de_prestamos_ejemplares_deprestamos_id_ejemplare_4836c5ec_uniq` (`deprestamos_id`,`ejemplares_id`),
  KEY `de_prestamos_ejempla_ejemplares_id_8d30c0bc_fk_ejemplare` (`ejemplares_id`),
  CONSTRAINT `de_prestamos_ejempla_deprestamos_id_d2e67f2d_fk_de_presta` FOREIGN KEY (`deprestamos_id`) REFERENCES `de_prestamos` (`id_de_prestamo`),
  CONSTRAINT `de_prestamos_ejempla_ejemplares_id_8d30c0bc_fk_ejemplare` FOREIGN KEY (`ejemplares_id`) REFERENCES `ejemplares` (`id_ejemplar`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `de_prestamos_ejemplares`
--

LOCK TABLES `de_prestamos_ejemplares` WRITE;
/*!40000 ALTER TABLE `de_prestamos_ejemplares` DISABLE KEYS */;
/*!40000 ALTER TABLE `de_prestamos_ejemplares` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(7,'api','administradores'),(8,'api','autores'),(9,'api','categorias'),(23,'api','deprestamos'),(10,'api','editoriales'),(11,'api','ejemplares'),(12,'api','estudiantes'),(22,'api','favoritos'),(13,'api','grados'),(14,'api','grupos'),(15,'api','idiomas'),(21,'api','infracciones'),(20,'api','libros'),(19,'api','prestados'),(18,'api','reservas'),(16,'api','tipoinfraccion'),(17,'api','usuario'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2022-04-02 22:31:49.504693'),(2,'auth','0001_initial','2022-04-02 22:32:03.160300'),(3,'admin','0001_initial','2022-04-02 22:32:06.062450'),(4,'admin','0002_logentry_remove_auto_add','2022-04-02 22:32:06.135409'),(5,'admin','0003_logentry_add_action_flag_choices','2022-04-02 22:32:06.242364'),(6,'api','0001_initial','2022-04-02 22:33:00.608140'),(7,'contenttypes','0002_remove_content_type_name','2022-04-02 22:33:02.160287'),(8,'auth','0002_alter_permission_name_max_length','2022-04-02 22:33:03.525568'),(9,'auth','0003_alter_user_email_max_length','2022-04-02 22:33:03.791603'),(10,'auth','0004_alter_user_username_opts','2022-04-02 22:33:03.882887'),(11,'auth','0005_alter_user_last_login_null','2022-04-02 22:33:04.373260'),(12,'auth','0006_require_contenttypes_0002','2022-04-02 22:33:04.420136'),(13,'auth','0007_alter_validators_add_error_messages','2022-04-02 22:33:04.549196'),(14,'auth','0008_alter_user_username_max_length','2022-04-02 22:33:04.891611'),(15,'auth','0009_alter_user_last_name_max_length','2022-04-02 22:33:05.049296'),(16,'auth','0010_alter_group_name_max_length','2022-04-02 22:33:05.244569'),(17,'auth','0011_update_proxy_permissions','2022-04-02 22:33:05.441856'),(18,'auth','0012_alter_user_first_name_max_length','2022-04-02 22:33:05.611699'),(19,'sessions','0001_initial','2022-04-02 22:33:06.190185');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('g2tecogaln1xeb1oj1e1pdczuiql3f91','.eJxVjDsOwjAQBe_iGlkLZv2hpM8ZorV3jQPIluKkQtwdIqWA9s3Me6mR1qWMa5d5nFhd1FEdfrdI6SF1A3ynems6tbrMU9Sbonfa9dBYntfd_Tso1Mu3dhQy8gltziLsz9FaBwFcsp5NBCEAkZCEjEFmQWKHkLzJzjrygur9AQCyOKo:1namML:vyQIeArRLaHAVvPIVrnGE_z6BocPW9a2-vqJn_qysEQ','2022-04-16 22:36:41.097532');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `editoriales`
--

DROP TABLE IF EXISTS `editoriales`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `editoriales` (
  `id_editorial` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id_editorial`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `editoriales`
--

LOCK TABLES `editoriales` WRITE;
/*!40000 ALTER TABLE `editoriales` DISABLE KEYS */;
/*!40000 ALTER TABLE `editoriales` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ejemplares`
--

DROP TABLE IF EXISTS `ejemplares`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ejemplares` (
  `id_ejemplar` int(11) NOT NULL AUTO_INCREMENT,
  `num_ejemplar` varchar(3) DEFAULT NULL,
  `estado` varchar(3) DEFAULT NULL,
  `id_libro` int(11) NOT NULL,
  PRIMARY KEY (`id_ejemplar`),
  KEY `ejemplares_id_libro_792b7445_fk_libros_id_libro` (`id_libro`),
  CONSTRAINT `ejemplares_id_libro_792b7445_fk_libros_id_libro` FOREIGN KEY (`id_libro`) REFERENCES `libros` (`id_libro`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ejemplares`
--

LOCK TABLES `ejemplares` WRITE;
/*!40000 ALTER TABLE `ejemplares` DISABLE KEYS */;
/*!40000 ALTER TABLE `ejemplares` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `estudiantes`
--

DROP TABLE IF EXISTS `estudiantes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `estudiantes` (
  `id_estudiante` int(11) NOT NULL AUTO_INCREMENT,
  `tipodoc` varchar(5) DEFAULT NULL,
  `nombres` varchar(50) NOT NULL,
  `apellidos` varchar(50) NOT NULL,
  `telefono` varchar(20) DEFAULT NULL,
  `direccion` varchar(100) DEFAULT NULL,
  `doc` varchar(20) NOT NULL,
  `id_grado` int(11) DEFAULT NULL,
  `id_grupo` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_estudiante`),
  KEY `estudiantes_doc_08258e00_fk_api_usuario_doc` (`doc`),
  KEY `estudiantes_id_grado_c1f574c6_fk_grados_id_grado` (`id_grado`),
  KEY `estudiantes_id_grupo_0cbc96d9_fk_grupos_id_grupo` (`id_grupo`),
  CONSTRAINT `estudiantes_doc_08258e00_fk_api_usuario_doc` FOREIGN KEY (`doc`) REFERENCES `api_usuario` (`doc`),
  CONSTRAINT `estudiantes_id_grado_c1f574c6_fk_grados_id_grado` FOREIGN KEY (`id_grado`) REFERENCES `grados` (`id_grado`),
  CONSTRAINT `estudiantes_id_grupo_0cbc96d9_fk_grupos_id_grupo` FOREIGN KEY (`id_grupo`) REFERENCES `grupos` (`id_grupo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `estudiantes`
--

LOCK TABLES `estudiantes` WRITE;
/*!40000 ALTER TABLE `estudiantes` DISABLE KEYS */;
/*!40000 ALTER TABLE `estudiantes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `favoritos`
--

DROP TABLE IF EXISTS `favoritos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `favoritos` (
  `id_favorito` int(11) NOT NULL AUTO_INCREMENT,
  `id_estudiante` int(11) NOT NULL,
  PRIMARY KEY (`id_favorito`),
  KEY `favoritos_id_estudiante_f80a6f61_fk_estudiantes_id_estudiante` (`id_estudiante`),
  CONSTRAINT `favoritos_id_estudiante_f80a6f61_fk_estudiantes_id_estudiante` FOREIGN KEY (`id_estudiante`) REFERENCES `estudiantes` (`id_estudiante`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `favoritos`
--

LOCK TABLES `favoritos` WRITE;
/*!40000 ALTER TABLE `favoritos` DISABLE KEYS */;
/*!40000 ALTER TABLE `favoritos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `favoritos_libros`
--

DROP TABLE IF EXISTS `favoritos_libros`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `favoritos_libros` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `favoritos_id` int(11) NOT NULL,
  `libros_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `favoritos_libros_favoritos_id_libros_id_97baf293_uniq` (`favoritos_id`,`libros_id`),
  KEY `favoritos_libros_libros_id_02bbbc7c_fk_libros_id_libro` (`libros_id`),
  CONSTRAINT `favoritos_libros_favoritos_id_0e9b7b01_fk_favoritos_id_favorito` FOREIGN KEY (`favoritos_id`) REFERENCES `favoritos` (`id_favorito`),
  CONSTRAINT `favoritos_libros_libros_id_02bbbc7c_fk_libros_id_libro` FOREIGN KEY (`libros_id`) REFERENCES `libros` (`id_libro`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `favoritos_libros`
--

LOCK TABLES `favoritos_libros` WRITE;
/*!40000 ALTER TABLE `favoritos_libros` DISABLE KEYS */;
/*!40000 ALTER TABLE `favoritos_libros` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `grados`
--

DROP TABLE IF EXISTS `grados`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `grados` (
  `id_grado` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id_grado`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `grados`
--

LOCK TABLES `grados` WRITE;
/*!40000 ALTER TABLE `grados` DISABLE KEYS */;
/*!40000 ALTER TABLE `grados` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `grupos`
--

DROP TABLE IF EXISTS `grupos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `grupos` (
  `id_grupo` int(11) NOT NULL AUTO_INCREMENT,
  `letra_grupo` varchar(3) DEFAULT NULL,
  PRIMARY KEY (`id_grupo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `grupos`
--

LOCK TABLES `grupos` WRITE;
/*!40000 ALTER TABLE `grupos` DISABLE KEYS */;
/*!40000 ALTER TABLE `grupos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `idiomas`
--

DROP TABLE IF EXISTS `idiomas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `idiomas` (
  `id_idioma` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id_idioma`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `idiomas`
--

LOCK TABLES `idiomas` WRITE;
/*!40000 ALTER TABLE `idiomas` DISABLE KEYS */;
/*!40000 ALTER TABLE `idiomas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `infracciones`
--

DROP TABLE IF EXISTS `infracciones`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `infracciones` (
  `id_infraccion` int(11) NOT NULL AUTO_INCREMENT,
  `descripcion` longtext DEFAULT NULL,
  `estado` varchar(3) DEFAULT NULL,
  `id_administrador` int(11) DEFAULT NULL,
  `id_estudiante` int(11) DEFAULT NULL,
  `id_tipo_infraccion` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_infraccion`),
  KEY `infracciones_id_administrador_290921d7_fk_administr` (`id_administrador`),
  KEY `infracciones_id_estudiante_c7a587ad_fk_estudiantes_id_estudiante` (`id_estudiante`),
  KEY `infracciones_id_tipo_infraccion_da040f2e_fk_tipo_infr` (`id_tipo_infraccion`),
  CONSTRAINT `infracciones_id_administrador_290921d7_fk_administr` FOREIGN KEY (`id_administrador`) REFERENCES `administradores` (`id_administrador`),
  CONSTRAINT `infracciones_id_estudiante_c7a587ad_fk_estudiantes_id_estudiante` FOREIGN KEY (`id_estudiante`) REFERENCES `estudiantes` (`id_estudiante`),
  CONSTRAINT `infracciones_id_tipo_infraccion_da040f2e_fk_tipo_infr` FOREIGN KEY (`id_tipo_infraccion`) REFERENCES `tipo_infraccion` (`id_tipo_infraccion`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `infracciones`
--

LOCK TABLES `infracciones` WRITE;
/*!40000 ALTER TABLE `infracciones` DISABLE KEYS */;
/*!40000 ALTER TABLE `infracciones` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `infracciones_ejemplares`
--

DROP TABLE IF EXISTS `infracciones_ejemplares`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `infracciones_ejemplares` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `infracciones_id` int(11) NOT NULL,
  `ejemplares_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `infracciones_ejemplares_infracciones_id_ejemplar_7fc277c6_uniq` (`infracciones_id`,`ejemplares_id`),
  KEY `infracciones_ejempla_ejemplares_id_17c56869_fk_ejemplare` (`ejemplares_id`),
  CONSTRAINT `infracciones_ejempla_ejemplares_id_17c56869_fk_ejemplare` FOREIGN KEY (`ejemplares_id`) REFERENCES `ejemplares` (`id_ejemplar`),
  CONSTRAINT `infracciones_ejempla_infracciones_id_90de9bf5_fk_infraccio` FOREIGN KEY (`infracciones_id`) REFERENCES `infracciones` (`id_infraccion`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `infracciones_ejemplares`
--

LOCK TABLES `infracciones_ejemplares` WRITE;
/*!40000 ALTER TABLE `infracciones_ejemplares` DISABLE KEYS */;
/*!40000 ALTER TABLE `infracciones_ejemplares` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `libros`
--

DROP TABLE IF EXISTS `libros`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `libros` (
  `id_libro` int(11) NOT NULL AUTO_INCREMENT,
  `isbn` varchar(20) NOT NULL,
  `nombre` varchar(150) NOT NULL,
  `edicion` varchar(50) DEFAULT NULL,
  `descripcion` longtext DEFAULT NULL,
  `numero_paginas` int(11) DEFAULT NULL,
  `alto` varchar(5) DEFAULT NULL,
  `ancho` varchar(5) DEFAULT NULL,
  `peso` varchar(7) DEFAULT NULL,
  `presentacion` varchar(30) DEFAULT NULL,
  `anexos` varchar(200) DEFAULT NULL,
  `palabras_clave` longtext DEFAULT NULL,
  `estado` varchar(3) DEFAULT NULL,
  `id_editorial` int(11) DEFAULT NULL,
  `id_idioma` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_libro`),
  KEY `libros_id_editorial_ee987fee_fk_editoriales_id_editorial` (`id_editorial`),
  KEY `libros_id_idioma_a39a8bd6_fk_idiomas_id_idioma` (`id_idioma`),
  CONSTRAINT `libros_id_editorial_ee987fee_fk_editoriales_id_editorial` FOREIGN KEY (`id_editorial`) REFERENCES `editoriales` (`id_editorial`),
  CONSTRAINT `libros_id_idioma_a39a8bd6_fk_idiomas_id_idioma` FOREIGN KEY (`id_idioma`) REFERENCES `idiomas` (`id_idioma`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `libros`
--

LOCK TABLES `libros` WRITE;
/*!40000 ALTER TABLE `libros` DISABLE KEYS */;
/*!40000 ALTER TABLE `libros` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `libros_autores`
--

DROP TABLE IF EXISTS `libros_autores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `libros_autores` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `libros_id` int(11) NOT NULL,
  `autores_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `libros_autores_libros_id_autores_id_3f872055_uniq` (`libros_id`,`autores_id`),
  KEY `libros_autores_autores_id_1d242f7e_fk_autores_id_autor` (`autores_id`),
  CONSTRAINT `libros_autores_autores_id_1d242f7e_fk_autores_id_autor` FOREIGN KEY (`autores_id`) REFERENCES `autores` (`id_autor`),
  CONSTRAINT `libros_autores_libros_id_d5b7ceef_fk_libros_id_libro` FOREIGN KEY (`libros_id`) REFERENCES `libros` (`id_libro`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `libros_autores`
--

LOCK TABLES `libros_autores` WRITE;
/*!40000 ALTER TABLE `libros_autores` DISABLE KEYS */;
/*!40000 ALTER TABLE `libros_autores` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `libros_categorias`
--

DROP TABLE IF EXISTS `libros_categorias`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `libros_categorias` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `libros_id` int(11) NOT NULL,
  `categorias_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `libros_categorias_libros_id_categorias_id_7d7bedc4_uniq` (`libros_id`,`categorias_id`),
  KEY `libros_categorias_categorias_id_5aafa82d_fk_categoria` (`categorias_id`),
  CONSTRAINT `libros_categorias_categorias_id_5aafa82d_fk_categoria` FOREIGN KEY (`categorias_id`) REFERENCES `categorias` (`id_categoria`),
  CONSTRAINT `libros_categorias_libros_id_38521506_fk_libros_id_libro` FOREIGN KEY (`libros_id`) REFERENCES `libros` (`id_libro`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `libros_categorias`
--

LOCK TABLES `libros_categorias` WRITE;
/*!40000 ALTER TABLE `libros_categorias` DISABLE KEYS */;
/*!40000 ALTER TABLE `libros_categorias` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `prestados`
--

DROP TABLE IF EXISTS `prestados`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `prestados` (
  `id_prestado` int(11) NOT NULL AUTO_INCREMENT,
  `estado` varchar(3) DEFAULT NULL,
  `id_ejemplar` int(11) NOT NULL,
  `id_estudiante` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_prestado`),
  KEY `prestados_id_ejemplar_577cf4a2_fk_ejemplares_id_ejemplar` (`id_ejemplar`),
  KEY `prestados_id_estudiante_7fd1ff6a_fk_estudiantes_id_estudiante` (`id_estudiante`),
  CONSTRAINT `prestados_id_ejemplar_577cf4a2_fk_ejemplares_id_ejemplar` FOREIGN KEY (`id_ejemplar`) REFERENCES `ejemplares` (`id_ejemplar`),
  CONSTRAINT `prestados_id_estudiante_7fd1ff6a_fk_estudiantes_id_estudiante` FOREIGN KEY (`id_estudiante`) REFERENCES `estudiantes` (`id_estudiante`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `prestados`
--

LOCK TABLES `prestados` WRITE;
/*!40000 ALTER TABLE `prestados` DISABLE KEYS */;
/*!40000 ALTER TABLE `prestados` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reservas`
--

DROP TABLE IF EXISTS `reservas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `reservas` (
  `id_reserva` int(11) NOT NULL AUTO_INCREMENT,
  `estado` varchar(3) DEFAULT NULL,
  `id_estudiante` int(11) NOT NULL,
  PRIMARY KEY (`id_reserva`),
  KEY `reservas_id_estudiante_c860c3b0_fk_estudiantes_id_estudiante` (`id_estudiante`),
  CONSTRAINT `reservas_id_estudiante_c860c3b0_fk_estudiantes_id_estudiante` FOREIGN KEY (`id_estudiante`) REFERENCES `estudiantes` (`id_estudiante`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reservas`
--

LOCK TABLES `reservas` WRITE;
/*!40000 ALTER TABLE `reservas` DISABLE KEYS */;
/*!40000 ALTER TABLE `reservas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reservas_ejemplares`
--

DROP TABLE IF EXISTS `reservas_ejemplares`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `reservas_ejemplares` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `reservas_id` int(11) NOT NULL,
  `ejemplares_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `reservas_ejemplares_reservas_id_ejemplares_id_ad3b2c81_uniq` (`reservas_id`,`ejemplares_id`),
  KEY `reservas_ejemplares_ejemplares_id_76771f24_fk_ejemplare` (`ejemplares_id`),
  CONSTRAINT `reservas_ejemplares_ejemplares_id_76771f24_fk_ejemplare` FOREIGN KEY (`ejemplares_id`) REFERENCES `ejemplares` (`id_ejemplar`),
  CONSTRAINT `reservas_ejemplares_reservas_id_b6a6cd59_fk_reservas_id_reserva` FOREIGN KEY (`reservas_id`) REFERENCES `reservas` (`id_reserva`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reservas_ejemplares`
--

LOCK TABLES `reservas_ejemplares` WRITE;
/*!40000 ALTER TABLE `reservas_ejemplares` DISABLE KEYS */;
/*!40000 ALTER TABLE `reservas_ejemplares` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tipo_infraccion`
--

DROP TABLE IF EXISTS `tipo_infraccion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tipo_infraccion` (
  `id_tipo_infraccion` int(11) NOT NULL,
  `nombre` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`id_tipo_infraccion`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipo_infraccion`
--

LOCK TABLES `tipo_infraccion` WRITE;
/*!40000 ALTER TABLE `tipo_infraccion` DISABLE KEYS */;
/*!40000 ALTER TABLE `tipo_infraccion` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-04-02 17:39:05
