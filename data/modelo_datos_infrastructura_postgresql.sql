

-- MODELO DE DATOS / ABASTECIMIENTO INFRAESTUCTURA / MOTOR: POSTGRESQL

-- INGENIERÍA DE SISTEMAS E INFORMÁTICA - TÓPICOS AVANZADOS EN BASES DE DATOS (TADB)

-- ESTUDIANTE N°1: THOMAS CAMILO VANEGAS ACEVEDO - ID:000287437 - THOMAS.VANEGASA@UPB.EDU.CO
-- ESTUDIANTE N°2: ELIANA GIRALDO DUQUE - ID: 000321721 - ELIANA.GIRALDOD@UPB.EDU.CO

-- CREACION DE LA BASE DE DATOS
create database db_gestion_utilizacion_buses_cargadores;

-- CREACION DEL USUARIO CON PERMISOS
create user dba_gestion_movilidad_medellin with encrypted password 'UnaClav3';

-- DATA CONTROL LANGUAGE: ASIGNACION DE PERMISOS AL USUARIO (GRANTS AND REVOKES) PARA EL DBA
GRANT CONNECT ON DATABASE db_gestion_utilizacion_buses_cargadores TO dba_gestion_movilidad_medellin;

-- SE OTORGAN PRIVILEGIOS DE ACCESO AL SCHEMA PÚBLICO AL DBA
GRANT USAGE ON SCHEMA public TO dba_gestion_movilidad_medellin;

-- SE OTORGAN PRIVILEGIOS DE CREACION EN EL SCHEMA PÚBLICO AL DBA
GRANT CREATE ON SCHEMA public TO dba_gestion_movilidad_medellin;

-- SE OTORGAN PRIVILEGIOS DE LECTURA EN EL SCHEMA PÚBLICO AL DBA
GRANT SELECT ON ALL TABLES IN SCHEMA public TO dba_gestion_movilidad_medellin;

-- SE OTORGAN PRIVILEGIOS DE MODIFICACION DE TABLAS EN EL SCHEMA PÚBLICO AL DBA
GRANT INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO dba_gestion_movilidad_medellin;


-- CREACIÓN DEL MODELO DE DATOS RELACIONAL (TABLAS)

-- LAS TABLAS SE CREAN EN PLURAL INDICANDO QUE ES UNA COLECCIÓN Y POR TANTO CADA REGISTRO UNA INSTANCIA DE DICHA COLECCION

-- LAS TABLAS SE CREAN UTILIZANDO EL ESTÁNDAR snake_lower_case

-- INICIO TABLA ESTADOS_BUSES --- --- ---
DROP TABLE IF EXISTS estados_buses;

CREATE TABLE estados_buses (
    id INT SERIAL PRIMARY KEY,
    descripcion VARCHAR(20) NOT NULL UNIQUE
);

CREATE INDEX ix_descripcion_est_buses ON estados_buses(descripcion);
-- FIN TABLA ESTADOS_BUSES --- --- ---


-- INICIO TABLA BUSES --- --- ---
DROP TABLE IF EXISTS buses;

CREATE TABLE buses (
    id INT SERIAL PRIMARY KEY,
    placa VARCHAR(6) NOT NULL UNIQUE,
    estado_id INT,

    CONSTRAINT fk_buses_estados_buses FOREIGN KEY (estado_id) REFERENCES estados_buses(id)
);

CREATE INDEX ix_placa_buses ON buses(placa);

ALTER TABLE buses
ADD CONSTRAINT verificar_placa
CHECK (placa ~ '^[A-Z]{3}[0-9]{3}$'); 
-- SE VERIFICA QUE LA PLACA TENGA COMO ORDEN LOS 3 PRIMEROS CARACTERES LETRAS MAYUSCULAS Y LOS ÚLTIMOS 3 CARACTERES DIGITOS
-- FIN TABLA BUSES --- --- ---


-- INICIO TABLA ESTADOS_CARGADORES --- --- ---
DROP TABLE IF EXISTS estados_cargadores;

CREATE TABLE estados_cargadores (
    id INT SERIAL PRIMARY KEY,
    descripcion VARCHAR(20) NOT NULL UNIQUE
);

CREATE INDEX ix_descripcion_est_cargadores ON estados_cargadores(descripcion);
-- FIN TABLA ESTADOS_CARGADORES --- --- ---



-- INICIO TABLA CARGADORES --- --- ---
DROP TABLE IF EXISTS cargadores;

CREATE TABLE cargadores (
    id INT SERIAL PRIMARY KEY,
    estado_id INT,

    CONSTRAINT fk_cargadores_estados_cargadores FOREIGN KEY (estado_id) REFERENCES estados_cargadores(id)
);
-- FIN TABLA CARGADORES --- --- ---



-- INICIO TABLA HORAS --- --- ---
DROP TABLE IF EXISTS horas;

CREATE TABLE horas (
    id  INT SERIAL PRIMARY KEY,
    descripcion VARCHAR(4) UNIQUE NOT NULL,
    hora_pico BOOLEAN NOT NULL
);

CREATE INDEX ix_descripcion_horas ON horas(descripcion);

COMMENT ON COLUMN horas.hora_pico IS 'Indica si es una hora pico, es decir, [5AM-8AM] y [4PM-7PM]';
COMMENT ON COLUMN horas.descripcion IS 'Indica la hora, se usaran, AM Y PM, por tanto, la máxima longitud de hora es DDAM or DDPM'
-- FIN TABLA HORAS --- --- ---



-- INICIO TABLA HISTORIAL_UTILIZACION_CARGADORES_HORA --- --- ---
DROP TABLE IF EXISTS historial_utilizacion_cargadores_hora;

CREATE TABLE historial_utilizacion_cargadores_hora (
    id INT SERIAL PRIMARY KEY,
    cargador_id INT NOT NULL,
    hora_id INT NOT NULL,
    bus_id INT DEFAULT NULL,

    CONSTRAINT fk_historial_util_carg_hora_cargadores FOREIGN KEY (cargador_id) REFERENCES cargadores(id),
    CONSTRAINT fk_historial_util_carg_hora_buses FOREIGN KEY (bus_id) REFERENCES buses(id),
    CONSTRAINT fk_historial_util_carg_hora_horas FOREIGN KEY (hora_id) REFERENCES horas(id)
);
-- FIN TABLA UTILIZACION_CARGADORES_BUSES --- --- ---



-- INICIO TABLA HISTORIAL_UTILIZACION_CARGADORES_HORA --- --- ---
DROP TABLE IF EXISTS historial_utilizacion_buses_hora;

CREATE TABLE historial_utilizacion_buses_hora (
    id INT SERIAL PRIMARY KEY,
    bus_id INT NOT NULL,
    hora_id INT NOT NULL,

    CONSTRAINT fk_historial_util_buses_hora_buses FOREIGN KEY (bus_id) REFERENCES buses(id),
    CONSTRAINT fk_historial_util_buses_hora_horas FOREIGN KEY (hora_id) REFERENCES horas(id)
);
-- FIN TABLA UTILIZACION_CARGADORES_BUSES --- --- ---



-- CREACION DE STORED PROCEDURES PARA EL USO POSTERIOR EN EL CRUD DEL REPOSITORY PATTERN