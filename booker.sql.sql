-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 05-05-2022 a las 17:32:09
-- Versión del servidor: 10.4.22-MariaDB
-- Versión de PHP: 8.1.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `booker`
--
CREATE schema booker; 
USE booker;

--
-- Estructura de tabla para la tabla `administradores`
--

CREATE TABLE `administradores` (
  `id_administrador` int(11) NOT NULL,
  `tipodoc` varchar(5) DEFAULT NULL,
  `nombres` varchar(50) NOT NULL,
  `apellidos` varchar(50) NOT NULL,
  `telefono` varchar(20) DEFAULT NULL,
  `direccion` varchar(100) DEFAULT NULL,
  `doc` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `api_usuario`
--

CREATE TABLE `api_usuario` (
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `doc` varchar(20) NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `email` varchar(60) DEFAULT NULL,
  `imagen` varchar(200) DEFAULT NULL,
  `usuario_activo` tinyint(1) NOT NULL,
  `usuario_administrador` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `api_usuario`
--

INSERT INTO `api_usuario` (`password`, `last_login`, `doc`, `name`, `email`, `imagen`, `usuario_activo`, `usuario_administrador`) VALUES
('pbkdf2_sha256$260000$aL7CiIOS2XYg6xAdD7XaUh$SbmXSy7Z9eycBUmlYW1LV5Dlki+aE+ZK24V1bq3tTG8=', '2022-04-04 01:28:36.859677', '1', 'Booker', 'eamendez85@misena.edu.co', '', 1, 1),
('pbkdf2_sha256$260000$ozypWDJvZ8ETD88LMsPMdL$+omNUF6Nr1+s/BVY7dOi4WpCwpLxy3dl31gsDlKy9FE=', '2022-04-04 01:27:06.000000', '2', 'prueba2', NULL, '', 1, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `authtoken_token`
--

CREATE TABLE `authtoken_token` (
  `key` varchar(40) NOT NULL,
  `created` datetime(6) NOT NULL,
  `user_id` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add content type', 4, 'add_contenttype'),
(14, 'Can change content type', 4, 'change_contenttype'),
(15, 'Can delete content type', 4, 'delete_contenttype'),
(16, 'Can view content type', 4, 'view_contenttype'),
(17, 'Can add session', 5, 'add_session'),
(18, 'Can change session', 5, 'change_session'),
(19, 'Can delete session', 5, 'delete_session'),
(20, 'Can view session', 5, 'view_session'),
(21, 'Can add usuario', 6, 'add_usuario'),
(22, 'Can change usuario', 6, 'change_usuario'),
(23, 'Can delete usuario', 6, 'delete_usuario'),
(24, 'Can view usuario', 6, 'view_usuario'),
(25, 'Can add estudiantes', 7, 'add_estudiantes'),
(26, 'Can change estudiantes', 7, 'change_estudiantes'),
(27, 'Can delete estudiantes', 7, 'delete_estudiantes'),
(28, 'Can view estudiantes', 7, 'view_estudiantes'),
(29, 'Can add favoritos', 8, 'add_favoritos'),
(30, 'Can change favoritos', 8, 'change_favoritos'),
(31, 'Can delete favoritos', 8, 'delete_favoritos'),
(32, 'Can view favoritos', 8, 'view_favoritos'),
(33, 'Can add de prestamos', 9, 'add_deprestamos'),
(34, 'Can change de prestamos', 9, 'change_deprestamos'),
(35, 'Can delete de prestamos', 9, 'delete_deprestamos'),
(36, 'Can view de prestamos', 9, 'view_deprestamos'),
(37, 'Can add prestados', 10, 'add_prestados'),
(38, 'Can change prestados', 10, 'change_prestados'),
(39, 'Can delete prestados', 10, 'delete_prestados'),
(40, 'Can view prestados', 10, 'view_prestados'),
(41, 'Can add infracciones', 11, 'add_infracciones'),
(42, 'Can change infracciones', 11, 'change_infracciones'),
(43, 'Can delete infracciones', 11, 'delete_infracciones'),
(44, 'Can view infracciones', 11, 'view_infracciones'),
(45, 'Can add idiomas', 12, 'add_idiomas'),
(46, 'Can change idiomas', 12, 'change_idiomas'),
(47, 'Can delete idiomas', 12, 'delete_idiomas'),
(48, 'Can view idiomas', 12, 'view_idiomas'),
(49, 'Can add reservas', 13, 'add_reservas'),
(50, 'Can change reservas', 13, 'change_reservas'),
(51, 'Can delete reservas', 13, 'delete_reservas'),
(52, 'Can view reservas', 13, 'view_reservas'),
(53, 'Can add categorias', 14, 'add_categorias'),
(54, 'Can change categorias', 14, 'change_categorias'),
(55, 'Can delete categorias', 14, 'delete_categorias'),
(56, 'Can view categorias', 14, 'view_categorias'),
(57, 'Can add editoriales', 15, 'add_editoriales'),
(58, 'Can change editoriales', 15, 'change_editoriales'),
(59, 'Can delete editoriales', 15, 'delete_editoriales'),
(60, 'Can view editoriales', 15, 'view_editoriales'),
(61, 'Can add grupos', 16, 'add_grupos'),
(62, 'Can change grupos', 16, 'change_grupos'),
(63, 'Can delete grupos', 16, 'delete_grupos'),
(64, 'Can view grupos', 16, 'view_grupos'),
(65, 'Can add tipo infraccion', 17, 'add_tipoinfraccion'),
(66, 'Can change tipo infraccion', 17, 'change_tipoinfraccion'),
(67, 'Can delete tipo infraccion', 17, 'delete_tipoinfraccion'),
(68, 'Can view tipo infraccion', 17, 'view_tipoinfraccion'),
(69, 'Can add autores', 18, 'add_autores'),
(70, 'Can change autores', 18, 'change_autores'),
(71, 'Can delete autores', 18, 'delete_autores'),
(72, 'Can view autores', 18, 'view_autores'),
(73, 'Can add ejemplares', 19, 'add_ejemplares'),
(74, 'Can change ejemplares', 19, 'change_ejemplares'),
(75, 'Can delete ejemplares', 19, 'delete_ejemplares'),
(76, 'Can view ejemplares', 19, 'view_ejemplares'),
(77, 'Can add libros', 20, 'add_libros'),
(78, 'Can change libros', 20, 'change_libros'),
(79, 'Can delete libros', 20, 'delete_libros'),
(80, 'Can view libros', 20, 'view_libros'),
(81, 'Can add administradores', 21, 'add_administradores'),
(82, 'Can change administradores', 21, 'change_administradores'),
(83, 'Can delete administradores', 21, 'delete_administradores'),
(84, 'Can view administradores', 21, 'view_administradores'),
(85, 'Can add grados', 22, 'add_grados'),
(86, 'Can change grados', 22, 'change_grados'),
(87, 'Can delete grados', 22, 'delete_grados'),
(88, 'Can view grados', 22, 'view_grados'),
(89, 'Can add Token', 23, 'add_token'),
(90, 'Can change Token', 23, 'change_token'),
(91, 'Can delete Token', 23, 'delete_token'),
(92, 'Can view Token', 23, 'view_token'),
(93, 'Can add token', 24, 'add_tokenproxy'),
(94, 'Can change token', 24, 'change_tokenproxy'),
(95, 'Can delete token', 24, 'delete_tokenproxy'),
(96, 'Can view token', 24, 'view_tokenproxy');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `autores`
--

CREATE TABLE `autores` (
  `id_autor` int(11) NOT NULL,
  `nombres` varchar(50) NOT NULL,
  `apellidos` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `autores`
--

INSERT INTO `autores` (`id_autor`, `nombres`, `apellidos`) VALUES
(1, 'Clive', 'Barker'),
(2, 'Stephen', 'King'),
(3, 'Patricia', 'Nieto'),
(4, 'María Fernanda', 'Heredia'),
(5, 'Ana María', 'Shua'),
(6, 'María Luisa', 'Balseiro'),
(7, 'Bernard', 'Torelló López'),
(8, 'Anne', 'Frank'),
(9, 'Michael', 'Ende'),
(10, 'John', 'Boyne');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `categorias`
--

CREATE TABLE `categorias` (
  `id_categoria` int(11) NOT NULL,
  `nombre` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `categorias`
--

INSERT INTO `categorias` (`id_categoria`, `nombre`) VALUES
(1, 'Terror'),
(2, 'Aventura'),
(3, 'Infantil'),
(4, 'Escolar'),
(5, 'Novela');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `de_prestamos`
--

CREATE TABLE `de_prestamos` (
  `id_de_prestamo` int(11) NOT NULL,
  `fec_prestamo` datetime(6) NOT NULL,
  `fec_devolucion` datetime(6) NOT NULL,
  `estado` varchar(3) NOT NULL,
  `id_administrador` int(11) NOT NULL,
  `id_estudiante` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `de_prestamos_ejemplares`
--

CREATE TABLE `de_prestamos_ejemplares` (
  `id` bigint(20) NOT NULL,
  `deprestamos_id` int(11) NOT NULL,
  `ejemplares_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2022-04-04 01:26:53.418150', '2', 'prueba2,  doc: 2', 2, '[{\"changed\": {\"fields\": [\"Usuario administrador\"]}}]', 6, '1'),
(2, '2022-04-04 01:28:45.586415', '3', 'prueba2,  doc: 3', 3, '', 6, '1'),
(3, '2022-04-04 01:28:57.329950', '2', 'prueba2,  doc: 2', 2, '[]', 6, '1');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(21, 'api', 'administradores'),
(18, 'api', 'autores'),
(14, 'api', 'categorias'),
(9, 'api', 'deprestamos'),
(15, 'api', 'editoriales'),
(19, 'api', 'ejemplares'),
(7, 'api', 'estudiantes'),
(8, 'api', 'favoritos'),
(22, 'api', 'grados'),
(16, 'api', 'grupos'),
(12, 'api', 'idiomas'),
(11, 'api', 'infracciones'),
(20, 'api', 'libros'),
(10, 'api', 'prestados'),
(13, 'api', 'reservas'),
(17, 'api', 'tipoinfraccion'),
(6, 'api', 'usuario'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(23, 'authtoken', 'token'),
(24, 'authtoken', 'tokenproxy'),
(4, 'contenttypes', 'contenttype'),
(5, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2022-04-04 01:15:48.958670'),
(2, 'api', '0001_initial', '2022-04-04 01:15:49.277665'),
(3, 'admin', '0001_initial', '2022-04-04 01:15:51.367509'),
(4, 'admin', '0002_logentry_remove_auto_add', '2022-04-04 01:15:51.427645'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2022-04-04 01:15:51.480612'),
(6, 'contenttypes', '0002_remove_content_type_name', '2022-04-04 01:15:52.122725'),
(7, 'auth', '0001_initial', '2022-04-04 01:16:00.705089'),
(8, 'auth', '0002_alter_permission_name_max_length', '2022-04-04 01:16:02.301114'),
(9, 'auth', '0003_alter_user_email_max_length', '2022-04-04 01:16:02.374066'),
(10, 'auth', '0004_alter_user_username_opts', '2022-04-04 01:16:02.472011'),
(11, 'auth', '0005_alter_user_last_login_null', '2022-04-04 01:16:02.522972'),
(12, 'auth', '0006_require_contenttypes_0002', '2022-04-04 01:16:02.639898'),
(13, 'auth', '0007_alter_validators_add_error_messages', '2022-04-04 01:16:02.767815'),
(14, 'auth', '0008_alter_user_username_max_length', '2022-04-04 01:16:02.892117'),
(15, 'auth', '0009_alter_user_last_name_max_length', '2022-04-04 01:16:02.978059'),
(16, 'auth', '0010_alter_group_name_max_length', '2022-04-04 01:16:03.240021'),
(17, 'auth', '0011_update_proxy_permissions', '2022-04-04 01:16:03.368467'),
(18, 'auth', '0012_alter_user_first_name_max_length', '2022-04-04 01:16:03.472938'),
(19, 'sessions', '0001_initial', '2022-04-04 01:16:04.443550'),
(20, 'api', '0002_auto_20220403_2019', '2022-04-04 01:20:02.945799'),
(21, 'api', '0002_libros_imagen', '2022-05-05 12:15:24.176299'),
(22, 'api', '0003_rename_imagen_libros_imagen_libro', '2022-05-05 12:15:24.197299'),
(23, 'api', '0004_rename_imagen_libro_libros_imagen', '2022-05-05 12:15:24.217298'),
(24, 'api', '0005_rename_imagen_usuario_imagen_libro', '2022-05-05 12:15:24.228299'),
(25, 'api', '0006_rename_imagen_libros_imagen_libro_and_more', '2022-05-05 12:15:24.255298'),
(26, 'api', '0007_alter_tipoinfraccion_id_tipo_infraccion', '2022-05-05 12:15:24.393073'),
(27, 'api', '0008_alter_libros_imagen_libro', '2022-05-05 12:15:24.407071'),
(28, 'authtoken', '0001_initial', '2022-05-05 12:15:24.459020'),
(29, 'authtoken', '0002_auto_20160226_1747', '2022-05-05 12:15:24.483616'),
(30, 'authtoken', '0003_tokenproxy', '2022-05-05 12:15:24.486546');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('zvf3ii9djom5sgjk0o6g6bfnm09jpwkv', '.eJxVjMsOwiAQRf-FtSEMb1y69xvIAINUDU1KuzL-uzbpQrf3nHNfLOK2trgNWuJU2JkBO_1uCfOD-g7KHftt5nnu6zIlviv8oINf50LPy-H-HTQc7Vv7YCVI7bWu4J0CZ0gLJQQJsM6jAxDVVR-qDcoqmbKwaKSpQSEEQ569P4hJNdI:1nbBWG:80Vs1RO-Y2Mb_CRFQXdIqjZvnTqHtP0aijBrB00Asvc', '2022-04-18 01:28:36.901686');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `editoriales`
--

CREATE TABLE `editoriales` (
  `id_editorial` int(11) NOT NULL,
  `nombre` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `editoriales`
--

INSERT INTO `editoriales` (`id_editorial`, `nombre`) VALUES
(1, 'Factoría de ideas'),
(2, 'Debolsillo'),
(3, 'Tusquets'),
(4, 'Norma'),
(5, 'Lo que leo'),
(6, 'Siruela'),
(7, 'Minotauro'),
(8, 'Definitions');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ejemplares`
--

CREATE TABLE `ejemplares` (
  `id_ejemplar` int(11) NOT NULL,
  `num_ejemplar` varchar(3) DEFAULT NULL,
  `estado` varchar(3) DEFAULT NULL,
  `id_libro` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `estudiantes`
--

CREATE TABLE `estudiantes` (
  `id_estudiante` int(11) NOT NULL,
  `tipodoc` varchar(5) DEFAULT NULL,
  `nombres` varchar(50) NOT NULL,
  `apellidos` varchar(50) NOT NULL,
  `telefono` varchar(20) DEFAULT NULL,
  `direccion` varchar(100) DEFAULT NULL,
  `doc` varchar(20) NOT NULL,
  `id_grado` int(11) DEFAULT NULL,
  `id_grupo` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `favoritos`
--

CREATE TABLE `favoritos` (
  `id_favorito` int(11) NOT NULL,
  `id_estudiante` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `favoritos_libros`
--

CREATE TABLE `favoritos_libros` (
  `id` bigint(20) NOT NULL,
  `favoritos_id` int(11) NOT NULL,
  `libros_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `grados`
--

CREATE TABLE `grados` (
  `id_grado` int(11) NOT NULL,
  `nombre` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `grupos`
--

CREATE TABLE `grupos` (
  `id_grupo` int(11) NOT NULL,
  `letra_grupo` varchar(3) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `idiomas`
--

CREATE TABLE `idiomas` (
  `id_idioma` int(11) NOT NULL,
  `nombre` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `idiomas`
--

INSERT INTO `idiomas` (`id_idioma`, `nombre`) VALUES
(1, 'Español'),
(2, 'Ingles');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `infracciones`
--

CREATE TABLE `infracciones` (
  `id_infraccion` int(11) NOT NULL,
  `descripcion` longtext DEFAULT NULL,
  `estado` varchar(3) DEFAULT NULL,
  `id_administrador` int(11) DEFAULT NULL,
  `id_estudiante` int(11) DEFAULT NULL,
  `id_tipo_infraccion` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `infracciones_ejemplares`
--

CREATE TABLE `infracciones_ejemplares` (
  `id` bigint(20) NOT NULL,
  `infracciones_id` int(11) NOT NULL,
  `ejemplares_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `libros`
--

CREATE TABLE `libros` (
  `id_libro` int(11) NOT NULL,
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
  `imagen_libro` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `libros`
--

INSERT INTO `libros` (`id_libro`, `isbn`, `nombre`, `edicion`, `descripcion`, `numero_paginas`, `alto`, `ancho`, `peso`, `presentacion`, `anexos`, `palabras_clave`, `estado`, `id_editorial`, `id_idioma`, `imagen_libro`) VALUES
(1, '8498005671', 'Cabal : Razas de noche', '', 'Aaron Boone lleva un tiempo sufriendo espantosas pesadillas, en las que se ve cometiendo los crímenes más atroces. Su psicólogo, el doctor Decker, termina de convencerlo de que esos asesinatos han ocurrido realmente. Ahora Boone sabe que en el mundo no hay lugar para él, y deja que el infierno lo llame, quiere que la Muerte lo lleve hasta allí. Pero hasta la mismísima Muerte parece retroceder ante él. Parece que el único refugio para Boone es Midian, aquel terrible y legendario lugar que estrecha entre sus monstruosos brazos a los medio muertos, las razas de noche?', 249, '20 cm', '12 cm', '', 'Tapa blanda', '', '', 'A', 1, 1, 'images/libros/cabal-razas-de-noche_AYBnxxk.jpg'),
(2, '8497595696', 'Carrie (Best Seller)', '', 'El escalofriante caso de una joven de apariencia insignificante que se transformó en un ser de poderes anormales, sembrando el terror en toda la ciudad.\r\n\r\nCon pulso mágico para mantener la tensión a lo largo de todo el libro, Stephen King narra la atormentada adolescencia de Carrie, y nos envuelve en una atmósfera sobrecogedora cuando la muchacha realiza una serie de descubrimientos hasta llegar al terrible momento de la venganza.', 256, '19 cm', '12 cm', '', 'Libro de bolsillo', '', '', 'A', 2, 1, 'images/libros/carrie-best-seller_jHhUwu2.jpg'),
(3, '9789584299413', 'Crónicas del paraíso', '', 'Este libro reúne buena parte del trabajo de una de las grandes cronistas de la  Colombia contemporánea. Desde los años 90, Patricia Nieto ha observado con compasión y cuidado la guerra y sus efectos sobre personajes anónimos que no aparecen en las primeras planas de los diarios o revistas. Se ha ocupado de las víctimas, de los sobrevivientes, de personas que merecen ser reconocidas por su tozudez y la valentía de asumir que, a pesar de la tragedia, es importante seguir insistiendo en que se oiga la voz de ese país que no figura en el imaginario de muchos. La escritura de Patricia Nieto está atada a la vida así se ocupe de terribles hechos como el desplazamiento o el asesinato de seres humanos que, como todos, merecen ser recordados. Este es un libro definitivo para entender un país que necesita reconciliarse consigo mismo.', 457, '23 cm', '14 cm', '', 'Tapa rústica', '', '', 'A', 3, 1, 'images/libros/cronicas-del-paraiso_l4hhSwV.jpg'),
(4, '9789580009658', 'Cuando despierte el viento', '', 'Novela escrita en tercera persona. Los protagonistas son Josefina y Leo, dos adolescentes que se conocen en la escuela y se convierten en amigos, a pesar de los problemas que enfrenta cada uno. Desde que su hermana Analuisa se suicidó porque no logró que se castigara a su agresor y fue acusada de difamar al hijo de un político famoso, Josefina y su familia no son felices: cargan con una gran pena. Debido a que un compañero insulta la memoria de su hermana, Josefina lo golpea y es expulsada de su primera escuela. Leo vive con Norberto, su padre, un escritor fracasado que maltrata a su madre, Beatriz.', 256, '21 cm', '13 cm', '', 'Tapa blanda', '', '', 'A', 4, 1, 'images/libros/cuando-despierte-el-viento_KPhn3yM.jpg'),
(5, '9789587434750', 'Dioses y héroes de la mitologia griega', '', 'En esta obra, Shua narra con un estilo magistral los relatos míticos más bellos. En sus páginas se encuentran el mito de la creación del Universo, el origen de los dioses del Olimpo, y las aventuras de los héroes más valientes como Heracles, Teseo y Odiseo, quienes deberán luchar contra terribles monstruos y, sobre todo, contra su propio destino.\r\n\r\nLos mitos griegos continúan cautivando a Los lectores de todas las edades porque tienen el poder de la fantasía y de las pasiones humanas.', 250, '20 cm', '13 cm', '', 'Tapa rústica', '', '', 'A', 5, 1, 'images/libros/dioses-y-heroes-de-la-mitologia-griega_aMxe4Ah.jpg'),
(6, '9788417041571', 'El bucanero de bombay', '', 'Un recorrido animado y colorista por las costumbres de la India, lleno de imaginación y humor, de la mano de un detective tan original como excéntrico. Siruela recupera en este volumen una colección de cuatro historias del afamado cineasta y narrador', 290, '23 cm', '15 cm', '', 'Tapa blanda', '', '', 'A', 6, 1, 'images/libros/el-bucanero-de-bombay_NTysjuA.jpg'),
(7, '8445009672', 'El demonio de arbennios', '', 'Kai es un antiguo soldado de élite que reside en Arbennios, capital del reino de Lénoda, cuya monótona vida se sustenta en tres pilares: un trabajo en la guardia del noble señor Nárenwal, la compañía de su leal grupo de amigos y las furtivas visitas de su amante secreta.\r\n\r\nPor desgracia, durante un caluroso día de verano tendrá lugar un ataque inesperado que dará un giro a su vida. Condenado por la misma sociedad a la que había defendido durante años, Kai se verá arrastrado por un torbellino de emociones y violencia que lo llevarán por el oscuro camino de la venganza.', 304, '23 cm', '15 cm', '', 'Tapa blanda', '', '', 'A', 7, 1, 'images/libros/el-demonio-de-arbennios_wmtK5tM.jpg'),
(8, '9788497593069', 'El diario de Ana Frank', '', 'Oculta con su familia y otra familia judía (los Van Daan), en una buhardilla de unos almacenes de Ámsterdam durante la ocupación nazi de Holanda. Ana Frankcon trece años, cuenta en su diario, al que llamó «Kitty», la vida del grupo. Ayudados por varios empleados de la oficina, permanecieron durante más de dos años en el achterhuis (conocido como «el anexo secreto») hasta que, finalmente, fueron delatados y detenidos. Ana escribió un diario entre el 12 de junio de 1942 y el 1 de agosto de 1944.', 384, '19 cm', '12 cm', '', 'Tapa blanda', '', '', 'A', 2, 1, 'images/libros/el-diario-de-ana-frank_DMmZlAn.jpg'),
(9, '9789585939301', 'La historia interminable', '', 'La Emperatriz Infantil está mortalmente enferma y su reino corre un grave peligro. La salvación depende de Atreyu, un valiente guerrero de la tribu de los pieles verdes, y Bastián, un niño tímido que lee con pasión un libro mágico. Mil aventuras les llevarán a reunirse y a conocer una fabulosa galería de personajes, y juntos dar forma a una de las grandes creaciones de la literatura de todos los tiempos.', 540, '23 cm', '14 cm', '', 'Tapa rústica', '', '', 'A', 5, 1, 'images/libros/la-historia-interminable.jpg'),
(10, '1909531197', 'The boy in the striped pyjamas', '', 'La historia de El niño con el pijama de rayas es muy difícil de describir. Normalmente damos algunas pistas sobre el libro en la portada, pero en este caso pensamos que estropearía la lectura del libro. Creemos que es importante que empieces a leer sin saber de qué se trata.', 256, '19 cm', '12 cm', '', 'Tapa blanda', '', '', 'A', 8, 2, 'images/libros/the-boy-in-the-striped-pyjamas.jpg');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `libros_autores`
--

CREATE TABLE `libros_autores` (
  `id` bigint(20) NOT NULL,
  `libros_id` int(11) NOT NULL,
  `autores_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `libros_autores`
--

INSERT INTO `libros_autores` (`id`, `libros_id`, `autores_id`) VALUES
(1, 1, 1),
(2, 2, 2),
(3, 3, 3),
(4, 4, 4),
(5, 5, 5),
(6, 6, 6),
(7, 7, 7),
(8, 8, 8),
(9, 9, 9),
(10, 10, 10);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `libros_categorias`
--

CREATE TABLE `libros_categorias` (
  `id` bigint(20) NOT NULL,
  `libros_id` int(11) NOT NULL,
  `categorias_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `libros_categorias`
--

INSERT INTO `libros_categorias` (`id`, `libros_id`, `categorias_id`) VALUES
(1, 1, 1),
(2, 2, 1),
(3, 3, 4),
(4, 4, 4),
(5, 5, 4),
(6, 6, 3),
(7, 7, 1),
(8, 8, 4),
(9, 9, 3),
(10, 10, 5);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `prestados`
--

CREATE TABLE `prestados` (
  `id_prestado` int(11) NOT NULL,
  `estado` varchar(3) DEFAULT NULL,
  `id_ejemplar` int(11) NOT NULL,
  `id_estudiante` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `reservas`
--

CREATE TABLE `reservas` (
  `id_reserva` int(11) NOT NULL,
  `estado` varchar(3) DEFAULT NULL,
  `id_estudiante` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `reservas_ejemplares`
--

CREATE TABLE `reservas_ejemplares` (
  `id` bigint(20) NOT NULL,
  `reservas_id` int(11) NOT NULL,
  `ejemplares_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipo_infraccion`
--

CREATE TABLE `tipo_infraccion` (
  `id_tipo_infraccion` int(11) NOT NULL,
  `nombre` varchar(15) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `administradores`
--
ALTER TABLE `administradores`
  ADD PRIMARY KEY (`id_administrador`),
  ADD KEY `administradores_doc_127e967f_fk_api_usuario_doc` (`doc`);

--
-- Indices de la tabla `api_usuario`
--
ALTER TABLE `api_usuario`
  ADD PRIMARY KEY (`doc`);

--
-- Indices de la tabla `authtoken_token`
--
ALTER TABLE `authtoken_token`
  ADD PRIMARY KEY (`key`),
  ADD UNIQUE KEY `user_id` (`user_id`);

--
-- Indices de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indices de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indices de la tabla `autores`
--
ALTER TABLE `autores`
  ADD PRIMARY KEY (`id_autor`);

--
-- Indices de la tabla `categorias`
--
ALTER TABLE `categorias`
  ADD PRIMARY KEY (`id_categoria`);

--
-- Indices de la tabla `de_prestamos`
--
ALTER TABLE `de_prestamos`
  ADD PRIMARY KEY (`id_de_prestamo`),
  ADD KEY `de_prestamos_id_administrador_03aa9a0a_fk_administr` (`id_administrador`),
  ADD KEY `de_prestamos_id_estudiante_97000d86_fk_estudiantes_id_estudiante` (`id_estudiante`);

--
-- Indices de la tabla `de_prestamos_ejemplares`
--
ALTER TABLE `de_prestamos_ejemplares`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `de_prestamos_ejemplares_deprestamos_id_ejemplare_4836c5ec_uniq` (`deprestamos_id`,`ejemplares_id`),
  ADD KEY `de_prestamos_ejempla_ejemplares_id_8d30c0bc_fk_ejemplare` (`ejemplares_id`);

--
-- Indices de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_api_usuario_doc` (`user_id`);

--
-- Indices de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indices de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indices de la tabla `editoriales`
--
ALTER TABLE `editoriales`
  ADD PRIMARY KEY (`id_editorial`);

--
-- Indices de la tabla `ejemplares`
--
ALTER TABLE `ejemplares`
  ADD PRIMARY KEY (`id_ejemplar`),
  ADD KEY `ejemplares_id_libro_792b7445_fk_libros_id_libro` (`id_libro`);

--
-- Indices de la tabla `estudiantes`
--
ALTER TABLE `estudiantes`
  ADD PRIMARY KEY (`id_estudiante`),
  ADD KEY `estudiantes_id_grado_c1f574c6_fk_grados_id_grado` (`id_grado`),
  ADD KEY `estudiantes_id_grupo_0cbc96d9_fk_grupos_id_grupo` (`id_grupo`),
  ADD KEY `estudiantes_doc_08258e00_fk_api_usuario_doc` (`doc`);

--
-- Indices de la tabla `favoritos`
--
ALTER TABLE `favoritos`
  ADD PRIMARY KEY (`id_favorito`),
  ADD KEY `favoritos_id_estudiante_f80a6f61_fk_estudiantes_id_estudiante` (`id_estudiante`);

--
-- Indices de la tabla `favoritos_libros`
--
ALTER TABLE `favoritos_libros`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `favoritos_libros_favoritos_id_libros_id_97baf293_uniq` (`favoritos_id`,`libros_id`),
  ADD KEY `favoritos_libros_libros_id_02bbbc7c_fk_libros_id_libro` (`libros_id`);

--
-- Indices de la tabla `grados`
--
ALTER TABLE `grados`
  ADD PRIMARY KEY (`id_grado`);

--
-- Indices de la tabla `grupos`
--
ALTER TABLE `grupos`
  ADD PRIMARY KEY (`id_grupo`);

--
-- Indices de la tabla `idiomas`
--
ALTER TABLE `idiomas`
  ADD PRIMARY KEY (`id_idioma`);

--
-- Indices de la tabla `infracciones`
--
ALTER TABLE `infracciones`
  ADD PRIMARY KEY (`id_infraccion`),
  ADD KEY `infracciones_id_administrador_290921d7_fk_administr` (`id_administrador`),
  ADD KEY `infracciones_id_estudiante_c7a587ad_fk_estudiantes_id_estudiante` (`id_estudiante`),
  ADD KEY `infracciones_id_tipo_infraccion_da040f2e_fk_tipo_infr` (`id_tipo_infraccion`);

--
-- Indices de la tabla `infracciones_ejemplares`
--
ALTER TABLE `infracciones_ejemplares`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `infracciones_ejemplares_infracciones_id_ejemplar_7fc277c6_uniq` (`infracciones_id`,`ejemplares_id`),
  ADD KEY `infracciones_ejempla_ejemplares_id_17c56869_fk_ejemplare` (`ejemplares_id`);

--
-- Indices de la tabla `libros`
--
ALTER TABLE `libros`
  ADD PRIMARY KEY (`id_libro`),
  ADD KEY `libros_id_editorial_ee987fee_fk_editoriales_id_editorial` (`id_editorial`),
  ADD KEY `libros_id_idioma_a39a8bd6_fk_idiomas_id_idioma` (`id_idioma`);

--
-- Indices de la tabla `libros_autores`
--
ALTER TABLE `libros_autores`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `libros_autores_libros_id_autores_id_3f872055_uniq` (`libros_id`,`autores_id`),
  ADD KEY `libros_autores_autores_id_1d242f7e_fk_autores_id_autor` (`autores_id`);

--
-- Indices de la tabla `libros_categorias`
--
ALTER TABLE `libros_categorias`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `libros_categorias_libros_id_categorias_id_7d7bedc4_uniq` (`libros_id`,`categorias_id`),
  ADD KEY `libros_categorias_categorias_id_5aafa82d_fk_categoria` (`categorias_id`);

--
-- Indices de la tabla `prestados`
--
ALTER TABLE `prestados`
  ADD PRIMARY KEY (`id_prestado`),
  ADD KEY `prestados_id_ejemplar_577cf4a2_fk_ejemplares_id_ejemplar` (`id_ejemplar`),
  ADD KEY `prestados_id_estudiante_7fd1ff6a_fk_estudiantes_id_estudiante` (`id_estudiante`);

--
-- Indices de la tabla `reservas`
--
ALTER TABLE `reservas`
  ADD PRIMARY KEY (`id_reserva`),
  ADD KEY `reservas_id_estudiante_c860c3b0_fk_estudiantes_id_estudiante` (`id_estudiante`);

--
-- Indices de la tabla `reservas_ejemplares`
--
ALTER TABLE `reservas_ejemplares`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `reservas_ejemplares_reservas_id_ejemplares_id_ad3b2c81_uniq` (`reservas_id`,`ejemplares_id`),
  ADD KEY `reservas_ejemplares_ejemplares_id_76771f24_fk_ejemplare` (`ejemplares_id`);

--
-- Indices de la tabla `tipo_infraccion`
--
ALTER TABLE `tipo_infraccion`
  ADD PRIMARY KEY (`id_tipo_infraccion`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `administradores`
--
ALTER TABLE `administradores`
  MODIFY `id_administrador` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=97;

--
-- AUTO_INCREMENT de la tabla `autores`
--
ALTER TABLE `autores`
  MODIFY `id_autor` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `categorias`
--
ALTER TABLE `categorias`
  MODIFY `id_categoria` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `de_prestamos`
--
ALTER TABLE `de_prestamos`
  MODIFY `id_de_prestamo` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `de_prestamos_ejemplares`
--
ALTER TABLE `de_prestamos_ejemplares`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;

--
-- AUTO_INCREMENT de la tabla `editoriales`
--
ALTER TABLE `editoriales`
  MODIFY `id_editorial` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `ejemplares`
--
ALTER TABLE `ejemplares`
  MODIFY `id_ejemplar` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `estudiantes`
--
ALTER TABLE `estudiantes`
  MODIFY `id_estudiante` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `favoritos`
--
ALTER TABLE `favoritos`
  MODIFY `id_favorito` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `favoritos_libros`
--
ALTER TABLE `favoritos_libros`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `grados`
--
ALTER TABLE `grados`
  MODIFY `id_grado` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `grupos`
--
ALTER TABLE `grupos`
  MODIFY `id_grupo` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `idiomas`
--
ALTER TABLE `idiomas`
  MODIFY `id_idioma` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `infracciones`
--
ALTER TABLE `infracciones`
  MODIFY `id_infraccion` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `infracciones_ejemplares`
--
ALTER TABLE `infracciones_ejemplares`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `libros`
--
ALTER TABLE `libros`
  MODIFY `id_libro` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `libros_autores`
--
ALTER TABLE `libros_autores`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `libros_categorias`
--
ALTER TABLE `libros_categorias`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `prestados`
--
ALTER TABLE `prestados`
  MODIFY `id_prestado` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `reservas`
--
ALTER TABLE `reservas`
  MODIFY `id_reserva` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `reservas_ejemplares`
--
ALTER TABLE `reservas_ejemplares`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `tipo_infraccion`
--
ALTER TABLE `tipo_infraccion`
  MODIFY `id_tipo_infraccion` int(11) NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `administradores`
--
ALTER TABLE `administradores`
  ADD CONSTRAINT `administradores_doc_127e967f_fk_api_usuario_doc` FOREIGN KEY (`doc`) REFERENCES `api_usuario` (`doc`);

--
-- Filtros para la tabla `authtoken_token`
--
ALTER TABLE `authtoken_token`
  ADD CONSTRAINT `authtoken_token_user_id_35299eff_fk_api_usuario_doc` FOREIGN KEY (`user_id`) REFERENCES `api_usuario` (`doc`);

--
-- Filtros para la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Filtros para la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Filtros para la tabla `de_prestamos`
--
ALTER TABLE `de_prestamos`
  ADD CONSTRAINT `de_prestamos_id_administrador_03aa9a0a_fk_administr` FOREIGN KEY (`id_administrador`) REFERENCES `administradores` (`id_administrador`),
  ADD CONSTRAINT `de_prestamos_id_estudiante_97000d86_fk_estudiantes_id_estudiante` FOREIGN KEY (`id_estudiante`) REFERENCES `estudiantes` (`id_estudiante`);

--
-- Filtros para la tabla `de_prestamos_ejemplares`
--
ALTER TABLE `de_prestamos_ejemplares`
  ADD CONSTRAINT `de_prestamos_ejempla_deprestamos_id_d2e67f2d_fk_de_presta` FOREIGN KEY (`deprestamos_id`) REFERENCES `de_prestamos` (`id_de_prestamo`),
  ADD CONSTRAINT `de_prestamos_ejempla_ejemplares_id_8d30c0bc_fk_ejemplare` FOREIGN KEY (`ejemplares_id`) REFERENCES `ejemplares` (`id_ejemplar`);

--
-- Filtros para la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_api_usuario_doc` FOREIGN KEY (`user_id`) REFERENCES `api_usuario` (`doc`);

--
-- Filtros para la tabla `ejemplares`
--
ALTER TABLE `ejemplares`
  ADD CONSTRAINT `ejemplares_id_libro_792b7445_fk_libros_id_libro` FOREIGN KEY (`id_libro`) REFERENCES `libros` (`id_libro`);

--
-- Filtros para la tabla `estudiantes`
--
ALTER TABLE `estudiantes`
  ADD CONSTRAINT `estudiantes_doc_08258e00_fk_api_usuario_doc` FOREIGN KEY (`doc`) REFERENCES `api_usuario` (`doc`),
  ADD CONSTRAINT `estudiantes_id_grado_c1f574c6_fk_grados_id_grado` FOREIGN KEY (`id_grado`) REFERENCES `grados` (`id_grado`),
  ADD CONSTRAINT `estudiantes_id_grupo_0cbc96d9_fk_grupos_id_grupo` FOREIGN KEY (`id_grupo`) REFERENCES `grupos` (`id_grupo`);

--
-- Filtros para la tabla `favoritos`
--
ALTER TABLE `favoritos`
  ADD CONSTRAINT `favoritos_id_estudiante_f80a6f61_fk_estudiantes_id_estudiante` FOREIGN KEY (`id_estudiante`) REFERENCES `estudiantes` (`id_estudiante`);

--
-- Filtros para la tabla `favoritos_libros`
--
ALTER TABLE `favoritos_libros`
  ADD CONSTRAINT `favoritos_libros_favoritos_id_0e9b7b01_fk_favoritos_id_favorito` FOREIGN KEY (`favoritos_id`) REFERENCES `favoritos` (`id_favorito`),
  ADD CONSTRAINT `favoritos_libros_libros_id_02bbbc7c_fk_libros_id_libro` FOREIGN KEY (`libros_id`) REFERENCES `libros` (`id_libro`);

--
-- Filtros para la tabla `infracciones`
--
ALTER TABLE `infracciones`
  ADD CONSTRAINT `infracciones_id_administrador_290921d7_fk_administr` FOREIGN KEY (`id_administrador`) REFERENCES `administradores` (`id_administrador`),
  ADD CONSTRAINT `infracciones_id_estudiante_c7a587ad_fk_estudiantes_id_estudiante` FOREIGN KEY (`id_estudiante`) REFERENCES `estudiantes` (`id_estudiante`),
  ADD CONSTRAINT `infracciones_id_tipo_infraccion_da040f2e_fk` FOREIGN KEY (`id_tipo_infraccion`) REFERENCES `tipo_infraccion` (`id_tipo_infraccion`);

--
-- Filtros para la tabla `infracciones_ejemplares`
--
ALTER TABLE `infracciones_ejemplares`
  ADD CONSTRAINT `infracciones_ejempla_ejemplares_id_17c56869_fk_ejemplare` FOREIGN KEY (`ejemplares_id`) REFERENCES `ejemplares` (`id_ejemplar`),
  ADD CONSTRAINT `infracciones_ejempla_infracciones_id_90de9bf5_fk_infraccio` FOREIGN KEY (`infracciones_id`) REFERENCES `infracciones` (`id_infraccion`);

--
-- Filtros para la tabla `libros`
--
ALTER TABLE `libros`
  ADD CONSTRAINT `libros_id_editorial_ee987fee_fk_editoriales_id_editorial` FOREIGN KEY (`id_editorial`) REFERENCES `editoriales` (`id_editorial`),
  ADD CONSTRAINT `libros_id_idioma_a39a8bd6_fk_idiomas_id_idioma` FOREIGN KEY (`id_idioma`) REFERENCES `idiomas` (`id_idioma`);

--
-- Filtros para la tabla `libros_autores`
--
ALTER TABLE `libros_autores`
  ADD CONSTRAINT `libros_autores_autores_id_1d242f7e_fk_autores_id_autor` FOREIGN KEY (`autores_id`) REFERENCES `autores` (`id_autor`),
  ADD CONSTRAINT `libros_autores_libros_id_d5b7ceef_fk_libros_id_libro` FOREIGN KEY (`libros_id`) REFERENCES `libros` (`id_libro`);

--
-- Filtros para la tabla `libros_categorias`
--
ALTER TABLE `libros_categorias`
  ADD CONSTRAINT `libros_categorias_categorias_id_5aafa82d_fk_categoria` FOREIGN KEY (`categorias_id`) REFERENCES `categorias` (`id_categoria`),
  ADD CONSTRAINT `libros_categorias_libros_id_38521506_fk_libros_id_libro` FOREIGN KEY (`libros_id`) REFERENCES `libros` (`id_libro`);

--
-- Filtros para la tabla `prestados`
--
ALTER TABLE `prestados`
  ADD CONSTRAINT `prestados_id_ejemplar_577cf4a2_fk_ejemplares_id_ejemplar` FOREIGN KEY (`id_ejemplar`) REFERENCES `ejemplares` (`id_ejemplar`),
  ADD CONSTRAINT `prestados_id_estudiante_7fd1ff6a_fk_estudiantes_id_estudiante` FOREIGN KEY (`id_estudiante`) REFERENCES `estudiantes` (`id_estudiante`);

--
-- Filtros para la tabla `reservas`
--
ALTER TABLE `reservas`
  ADD CONSTRAINT `reservas_id_estudiante_c860c3b0_fk_estudiantes_id_estudiante` FOREIGN KEY (`id_estudiante`) REFERENCES `estudiantes` (`id_estudiante`);

--
-- Filtros para la tabla `reservas_ejemplares`
--
ALTER TABLE `reservas_ejemplares`
  ADD CONSTRAINT `reservas_ejemplares_ejemplares_id_76771f24_fk_ejemplare` FOREIGN KEY (`ejemplares_id`) REFERENCES `ejemplares` (`id_ejemplar`),
  ADD CONSTRAINT `reservas_ejemplares_reservas_id_b6a6cd59_fk_reservas_id_reserva` FOREIGN KEY (`reservas_id`) REFERENCES `reservas` (`id_reserva`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
