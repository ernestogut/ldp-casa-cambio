# Casa de Cambio - Lenguajes de Programación

Aplicación de consola para la gestión de cambio de divisas y usuarios, simulando una casa de cambio. Permite registrar usuarios, iniciar sesión, realizar cambios de moneda, consultar tasas de cambio y ver transacciones, con roles de administrador y usuario.

## Características principales

- Registro e inicio de sesión de usuarios.
- Gestión de roles (Administrador, Usuario).
- Cambio de divisas entre diferentes monedas.
- Consulta y mantenimiento de tasas de cambio (solo administrador).
- Visualización de transacciones por usuario.
- Métodos de depósito configurables.

## Estructura del proyecto

```
src/
  main.py                  # Punto de entrada de la aplicación
  application/             # Lógica de negocio (servicios)
  domain/                  # Modelos y puertos (interfaces)
  infrastructure/          # Implementaciones en memoria de los repositorios
  utils/                   # Utilidades y validaciones
```

## Requisitos

- Python 3.10 o superior
- Git

## Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/ernestogut/ldp-casa-cambio.git
cd ldp-casa-cambio
```

### 2. Ejecutar la aplicación

#### En Linux/MacOS

```bash
python -m src.main
```

#### En Windows

```cmd
python -m src.main
```

## Uso

Sigue las instrucciones en consola para:

- Registrarte o iniciar sesión.
- Si eres administrador, podrás gestionar usuarios y tasas de cambio.
- Si eres usuario, podrás realizar cambios de moneda y ver tus transacciones.

## Notas

- Todos los datos se almacenan en memoria (no hay base de datos).
- Para restablecer los datos, reinicia la aplicación.
- El usuario administrador por defecto es:
  - **Email:** sistema@gmail.com
  - **Contraseña:** root

---
