# **Proyecto: App visualización de datos📊🚀**  

Esta aplicación es una herramienta de visualización de datos que fue desarrollada con FastAPI en el Backend, Svelte en el Frontend y eCharts para la representación grafica de datos. 
Tambien se implemento Docker en el proyecto para facilitar su despliegue, mantenimiento y ejecución.

## **Tecnologías Utilizadas:**                    

🔹 Backend: FastAPI

🔹 Frontend: Svelte

🔹 Visualización de Datos: eCharts

🔹 Docker & Docker Compose    

### **Instalación y Ejecución:**


(Para poder ejecutar la APP debes tener instalados Git, Docker y Docker Compose)☑️


### 1- Clonar el Repositorio:

  Para ello debes ejecutar los siguientes comandos en tu terminal: 
  
  (si por ejemplo utilizas sistema operativo Windows, debes hacerlo desde PowerShell o Git Bash.)
- git clone https://github.com/nicolasaurora/project-lucas
- cd project-lucas

### 2- Construir y Ejecutar la Aplicación con Docker:
- docker-compose up --build

### **Acceder a la Aplicación**
- API (FastAPI docs): http://localhost:8000/data
- Frontend (Svelte App): http://localhost:3000

## **Estructura del Proyecto**
```bash
project
│────── backend  
│       ├── __pycache__
│       ├── .gitignore
│       ├── Dockerfile 
│       ├── main.py 
│       └── requirements.txt   
├────── frontend 
│       ├── src
│       │   ├── App.svelte
│       │   ├── Graficos.svelte
│       │   └── main.js
│       ├── .gitignore
│       ├── Dockerfile
│       ├── public
│       ├── package-lock.json
│       ├── package.json
│       ├── README.md
│       └── rollup.config.js     
├── data.json   
├── docker-compose.yml


