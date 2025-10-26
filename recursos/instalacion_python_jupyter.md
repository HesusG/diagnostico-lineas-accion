# Guía de Instalación: Python y Jupyter Notebook

## 🎯 Objetivo

Instalar Python, Jupyter Notebook y todas las librerías necesarias para el curso CD2001B.

**Tiempo estimado:** 30-45 minutos

---

## 📋 Requisitos Previos

- **Sistema operativo:** Windows 10/11, macOS, o Linux
- **Espacio en disco:** Mínimo 5 GB libres
- **Conexión a internet:** Estable para descargas (~500 MB)
- **Permisos:** Administrador en tu computadora

---

## ✅ Opción 1: Anaconda (Recomendada para Principiantes)

**Ventajas:**
- ✅ Todo en uno (Python + Jupyter + librerías científicas)
- ✅ Gestor de paquetes incluido (conda)
- ✅ Gestión de entornos virtuales fácil
- ✅ Interfaz gráfica (Anaconda Navigator)

### Paso 1: Descargar Anaconda

1. Ve a: https://www.anaconda.com/products/distribution
2. Haz clic en **"Download"**
3. Selecciona tu sistema operativo (Windows, macOS, Linux)
4. Descarga la versión de **Python 3.11** o superior (64-bit)

**Tamaño de descarga:** ~500-700 MB

---

### Paso 2: Instalar Anaconda

#### Windows:

1. Ejecuta el archivo descargado (`Anaconda3-202X.XX-Windows-x86_64.exe`)
2. Haz clic en **"Next"**
3. Lee y acepta los términos de licencia
4. Tipo de instalación:
   - **Recomendado:** "Just Me" (solo para tu usuario)
   - Si necesitas instalación para todos los usuarios, selecciona "All Users" (requiere admin)
5. Ubicación de instalación:
   - Deja la ruta por defecto: `C:\Users\<TuUsuario>\anaconda3`
   - O elige una ruta sin espacios ni caracteres especiales
6. **Opciones avanzadas:**
   - ❌ NO marques "Add Anaconda to my PATH" (puede causar conflictos)
   - ✅ SÍ marca "Register Anaconda as my default Python 3.11"
7. Haz clic en **"Install"** (tomará 10-15 minutos)
8. Al finalizar, haz clic en **"Finish"**

#### macOS:

1. Abre el archivo descargado (`Anaconda3-202X.XX-MacOSX-x86_64.pkg`)
2. Sigue el asistente de instalación
3. Acepta los términos de licencia
4. Selecciona el disco de instalación (por defecto)
5. Haz clic en **"Install"**
6. Puede pedir tu contraseña de administrador
7. Al finalizar, cierra el instalador

#### Linux:

```bash
# Navega a la carpeta de descargas
cd ~/Downloads

# Da permisos de ejecución al instalador
chmod +x Anaconda3-202X.XX-Linux-x86_64.sh

# Ejecuta el instalador
bash Anaconda3-202X.XX-Linux-x86_64.sh

# Sigue las instrucciones en pantalla
# Presiona ENTER para revisar la licencia
# Escribe "yes" para aceptar
# Confirma la ubicación de instalación (por defecto: ~/anaconda3)
# Escribe "yes" cuando pregunte si deseas inicializar Anaconda

# Reinicia la terminal
source ~/.bashrc
```

---

### Paso 3: Verificar la Instalación

#### Windows:

1. Abre el **Menú Inicio**
2. Busca **"Anaconda Prompt"**
3. Ejecuta:

```bash
python --version
```

Deberías ver algo como: `Python 3.11.5`

```bash
conda --version
```

Deberías ver algo como: `conda 23.7.4`

#### macOS / Linux:

Abre la **Terminal** y ejecuta:

```bash
python --version
conda --version
```

---

### Paso 4: Crear Entorno Virtual para el Curso

**¿Por qué un entorno virtual?**
- Aísla las librerías del curso
- Evita conflictos con otros proyectos
- Facilita reproducibilidad

```bash
# Abre Anaconda Prompt (Windows) o Terminal (macOS/Linux)

# Crea el entorno con Python 3.11
conda create -n diagnostico python=3.11 -y

# Activa el entorno
conda activate diagnostico

# Verifica que estás en el entorno correcto
# Deberías ver (diagnostico) al inicio de la línea de comando
```

---

### Paso 5: Instalar Librerías del Curso

Con el entorno `diagnostico` activado:

```bash
# Instala pandas, numpy, matplotlib, seaborn
conda install pandas numpy matplotlib seaborn -y

# Instala scipy y statsmodels
conda install scipy statsmodels -y

# Instala scikit-learn
conda install scikit-learn -y

# Instala plotly (visualización interactiva)
conda install plotly -c plotly -y

# Instala jupyter
conda install jupyter notebook -y

# (Opcional) Instala jupyterlab (versión moderna de Jupyter)
conda install jupyterlab -y
```

**Alternativa (más rápida):** Instalar todo de una vez:

```bash
conda install pandas numpy scipy statsmodels scikit-learn matplotlib seaborn plotly jupyter notebook jupyterlab -y
```

---

### Paso 6: Verificar Instalación de Librerías

```bash
# Abre Python
python

# Dentro de Python, ejecuta:
>>> import pandas as pd
>>> import numpy as np
>>> import matplotlib.pyplot as plt
>>> import seaborn as sns
>>> import scipy.stats as stats
>>> import statsmodels.api as sm
>>> from sklearn import linear_model
>>> import plotly.express as px

# Si no hay errores, todo está instalado correctamente

# Sal de Python
>>> exit()
```

---

### Paso 7: Lanzar Jupyter Notebook

```bash
# Asegúrate de estar en el entorno diagnostico
conda activate diagnostico

# Navega a la carpeta donde tienes el repositorio del curso
cd C:\Users\<TuUsuario>\Documents\Github\diagnostico-lineas-accion

# Lanza Jupyter Notebook
jupyter notebook

# O lanza JupyterLab (interfaz moderna)
jupyter lab
```

Se abrirá una ventana del navegador con Jupyter.

---

## ✅ Opción 2: Python Nativo + pip (Para Usuarios Avanzados)

**Ventajas:**
- Instalación más ligera
- Control total sobre paquetes
- No incluye librerías innecesarias

**Desventajas:**
- Más pasos de configuración
- Puede requerir compiladores en Windows para algunas librerías

### Paso 1: Instalar Python

#### Windows:

1. Ve a: https://www.python.org/downloads/
2. Descarga **Python 3.11** o superior
3. Ejecuta el instalador
4. **IMPORTANTE:** Marca ✅ **"Add Python to PATH"**
5. Haz clic en **"Install Now"**

#### macOS:

```bash
# Opción 1: Usando Homebrew (recomendado)
# Instala Homebrew si no lo tienes
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Instala Python
brew install python@3.11

# Opción 2: Descarga desde python.org
# Ve a https://www.python.org/downloads/macos/
```

#### Linux (Ubuntu/Debian):

```bash
sudo apt update
sudo apt install python3.11 python3-pip python3-venv -y
```

---

### Paso 2: Verificar Instalación

```bash
python --version
# o
python3 --version

pip --version
# o
pip3 --version
```

---

### Paso 3: Crear Entorno Virtual

```bash
# Navega a la carpeta del curso
cd C:\Users\<TuUsuario>\Documents\Github\diagnostico-lineas-accion

# Crea el entorno virtual
python -m venv venv

# Activa el entorno
# Windows:
venv\Scripts\activate

# macOS/Linux:
source venv/bin/activate

# Deberías ver (venv) al inicio de la línea de comando
```

---

### Paso 4: Instalar Librerías con pip

Con el entorno activado:

```bash
# Actualiza pip
python -m pip install --upgrade pip

# Instala todas las librerías desde requirements.txt
pip install -r requirements.txt

# O instala manualmente:
pip install pandas numpy scipy statsmodels scikit-learn matplotlib seaborn plotly jupyter notebook jupyterlab
```

---

### Paso 5: Lanzar Jupyter

```bash
# Asegúrate de que el entorno venv está activado
# Deberías ver (venv) al inicio

# Lanza Jupyter Notebook
jupyter notebook

# O JupyterLab
jupyter lab
```

---

## ✅ Opción 3: Google Colab (Sin Instalación Local)

**Ventajas:**
- ✅ No requiere instalar nada en tu computadora
- ✅ Acceso a GPUs gratuitas
- ✅ Guarda notebooks en Google Drive
- ✅ Colaboración en tiempo real

**Desventajas:**
- ❌ Requiere conexión a internet
- ❌ Sesión se cierra después de inactividad
- ❌ Menos control sobre el entorno

### Cómo Usar Google Colab:

1. Ve a: https://colab.research.google.com/
2. Inicia sesión con tu cuenta de Google
3. Haz clic en **"Archivo"** → **"Nuevo notebook"**
4. Listo! Ya puedes ejecutar código Python

**Instalar librerías en Colab:**

```python
# Las librerías básicas (pandas, numpy, matplotlib, scipy, scikit-learn)
# ya están instaladas en Colab

# Si necesitas instalar algo adicional:
!pip install statsmodels plotly
```

**Subir archivos de datos:**

```python
from google.colab import files

# Subir archivo
uploaded = files.upload()

# O conectar con Google Drive
from google.colab import drive
drive.mount('/content/drive')
```

---

## 🐛 Solución de Problemas Comunes

### Problema 1: "conda: command not found" (macOS/Linux)

**Solución:**

```bash
# Añade Anaconda al PATH
echo 'export PATH="$HOME/anaconda3/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc

# O para macOS con zsh:
echo 'export PATH="$HOME/anaconda3/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

---

### Problema 2: "Jupyter command not found"

**Solución:**

```bash
# Asegúrate de estar en el entorno correcto
conda activate diagnostico

# Reinstala jupyter
conda install jupyter notebook -y
```

---

### Problema 3: Error al importar librerías en Jupyter

**Problema:** `ModuleNotFoundError: No module named 'pandas'`

**Solución:**

```bash
# Asegúrate de que el kernel de Jupyter usa el entorno correcto

# Instala ipykernel
conda install ipykernel -y

# Registra el entorno como un kernel de Jupyter
python -m ipykernel install --user --name=diagnostico --display-name "Python (diagnostico)"

# Reinicia Jupyter y selecciona el kernel "Python (diagnostico)"
```

---

### Problema 4: Jupyter se abre pero no muestra archivos

**Solución:**

```bash
# Inicia Jupyter desde la carpeta correcta
cd C:\Users\<TuUsuario>\Documents\Github\diagnostico-lineas-accion
jupyter notebook

# O navega manualmente en la interfaz de Jupyter
```

---

### Problema 5: Error de permisos en Windows

**Solución:**

```bash
# Ejecuta Anaconda Prompt como Administrador
# Botón derecho → "Ejecutar como administrador"
```

---

## 🔄 Actualizar Librerías

```bash
# Anaconda
conda activate diagnostico
conda update --all -y

# pip
pip install --upgrade pandas numpy scipy statsmodels scikit-learn matplotlib seaborn plotly jupyter
```

---

## 🗑️ Desinstalar

### Anaconda:

**Windows:**
1. Panel de Control → Programas → Desinstalar
2. Busca "Anaconda3" y desinstala

**macOS/Linux:**
```bash
# Elimina la carpeta de Anaconda
rm -rf ~/anaconda3

# Elimina referencias en .bashrc o .zshrc
# Abre el archivo y elimina líneas que contengan "anaconda"
nano ~/.bashrc
```

### Entorno virtual (venv):

```bash
# Simplemente elimina la carpeta
rm -rf venv
```

---

## 📚 Próximos Pasos

Una vez instalado:

1. ✅ Clona o descarga el repositorio del curso
2. ✅ Abre `Semana1/notebooks/01_introduccion_estadistica.ipynb` en Jupyter
3. ✅ Ejecuta la primera celda para verificar que todo funciona

---

## 💡 Tips de Uso

### Atajos de Teclado en Jupyter:

**Modo Comando (presiona Esc):**
- `A`: Insertar celda arriba
- `B`: Insertar celda abajo
- `D, D`: Eliminar celda
- `M`: Convertir a Markdown
- `Y`: Convertir a código

**Modo Edición (presiona Enter):**
- `Ctrl + Enter`: Ejecutar celda
- `Shift + Enter`: Ejecutar celda y avanzar
- `Tab`: Autocompletar
- `Shift + Tab`: Ver documentación de función

---

### Mejores Prácticas:

1. **Siempre activa el entorno antes de trabajar:**
   ```bash
   conda activate diagnostico
   ```

2. **Guarda frecuentemente:** Jupyter autosave cada 2 min, pero guarda manualmente con `Ctrl + S`

3. **Reinicia el kernel si algo falla:** `Kernel → Restart & Clear Output`

4. **Versionamiento:** Usa Git para hacer commit de tus notebooks

5. **No ejecutes celdas fuera de orden:** Los notebooks deben ejecutarse secuencialmente

---

## 📧 Soporte

Si tienes problemas con la instalación:

1. Revisa esta guía completa
2. Busca el error en Google/Stack Overflow
3. Pregunta en el foro del curso
4. Contacta al instructor en horario de oficina

---

## ✅ Checklist de Instalación Completa

- [ ] Python 3.11+ instalado
- [ ] Entorno virtual creado (`diagnostico`)
- [ ] Todas las librerías instaladas sin errores
- [ ] Jupyter Notebook lanza correctamente
- [ ] Puedes importar pandas, numpy, scipy, matplotlib, seaborn, statsmodels, sklearn, plotly
- [ ] Navegas a la carpeta del curso en Jupyter
- [ ] Puedes abrir y ejecutar el notebook de prueba

---

**¡Estás listo para empezar el curso!** 🎓🐍📊
