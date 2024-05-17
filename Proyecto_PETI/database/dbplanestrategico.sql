-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         10.4.24-MariaDB - mariadb.org binary distribution
-- SO del servidor:              Win64
-- HeidiSQL Versión:             12.4.0.6659
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Volcando estructura de base de datos para dbplanestrategico
CREATE DATABASE IF NOT EXISTS `dbplanestrategico` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;
USE `dbplanestrategico`;

-- Volcando estructura para tabla dbplanestrategico.plan_estrategico
CREATE TABLE IF NOT EXISTS `plan_estrategico` (
  `IdPlanEstrategico` int(11) NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(50) DEFAULT NULL,
  `Empresa` varchar(50) DEFAULT NULL,
  `Mision` text DEFAULT NULL,
  `Vision` text DEFAULT NULL,
  `FKIdUsuario` int(11) DEFAULT NULL,
  PRIMARY KEY (`IdPlanEstrategico`),
  KEY `FK_plan_estrategico_usuario` (`FKIdUsuario`),
  CONSTRAINT `FK_plan_estrategico_usuario` FOREIGN KEY (`FKIdUsuario`) REFERENCES `usuario` (`IdUsuario`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

-- Volcando datos para la tabla dbplanestrategico.plan_estrategico: ~2 rows (aproximadamente)
INSERT INTO `plan_estrategico` (`IdPlanEstrategico`, `Nombre`, `Empresa`, `Mision`, `Vision`, `FKIdUsuario`) VALUES
	(1, 'ProyectoU1', 'UPT', 'Mision de proyecto', 'Vision de proyecto', 1),
	(2, 'Proyecto empresa A', 'UPT A', 'Mision de proyecto empresa A', 'Vision de proyecto empresa A', 1);

-- Volcando estructura para tabla dbplanestrategico.usuario
CREATE TABLE IF NOT EXISTS `usuario` (
  `IdUsuario` int(11) NOT NULL AUTO_INCREMENT,
  `NombreUsuario` varchar(50) DEFAULT NULL,
  `Contrasena` varchar(50) DEFAULT NULL,
  `Email` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`IdUsuario`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

-- Volcando datos para la tabla dbplanestrategico.usuario: ~2 rows (aproximadamente)
INSERT INTO `usuario` (`IdUsuario`, `NombreUsuario`, `Contrasena`, `Email`) VALUES
	(1, 'mayanahua', '123', 'mayanahua@upt.pe'),
	(2, 'may', '123', 'may@upt.pe');

-- Volcando estructura para tabla dbplanestrategico.valor
CREATE TABLE IF NOT EXISTS `valor` (
  `IdValor` int(11) NOT NULL AUTO_INCREMENT,
  `Descripcion` text DEFAULT NULL,
  `FKIdPlanEstrategico` int(11) DEFAULT NULL,
  PRIMARY KEY (`IdValor`),
  KEY `FK__plan_estrategico` (`FKIdPlanEstrategico`),
  CONSTRAINT `FK__plan_estrategico` FOREIGN KEY (`FKIdPlanEstrategico`) REFERENCES `plan_estrategico` (`IdPlanEstrategico`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;

-- Volcando datos para la tabla dbplanestrategico.valor: ~3 rows (aproximadamente)
INSERT INTO `valor` (`IdValor`, `Descripcion`, `FKIdPlanEstrategico`) VALUES
	(1, 'Descripcion de valores de la empresa 1', 1),
	(2, 'Descripcion de valores de la empresa 2', 1),
	(3, 'Descripcion de valores de la empresa 3', 1);

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
