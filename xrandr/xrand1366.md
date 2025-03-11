Para agregar una resolución personalizada de **1366x768** a la salida `VGA-0`, sigue estos pasos:

---

### ✅ **1. Generar el modelo de la resolución**
Usa el comando `cvt` para crear los parámetros de la resolución:

```bash
cvt 1366 768 60
```

📊 **Salida esperada:**
```bash
# 1366x768 60.00 Hz (CVT 1.02) hsync: 47.71 kHz; pclk: 85.25 MHz
Modeline "1366x768_60.00" 85.25 1366 1434 1566 1766 768 771 781 798 -hsync +vsync
```

---

### ✅ **2. Crear el nuevo modo con `xrandr`**
Copia la línea que empieza con `Modeline` (después de ejecutarlo) y agrégala al sistema:

```bash
xrandr --newmode "1366x768_60.00" 85.25 1366 1434 1566 1766 768 771 781 798 -hsync +vsync
```

---

### ✅ **3. Asignar el nuevo modo a la salida `VGA-0`**
Agrega el modo recién creado a la salida `VGA-0`:

```bash
xrandr --addmode VGA-0 1366x768_60.00
```

---

### ✅ **4. Aplicar la nueva resolución**
Ahora, cambia a la nueva resolución:

```bash
xrandr --output VGA-0 --mode 1366x768_60.00
```

---

### ✅ **5. Guardar la configuración (Opcional)**
Si quieres que la resolución se mantenga después de reiniciar el sistema:

1. Edita el archivo de configuración:
   
```bash
sudo nano /etc/X11/xorg.conf.d/10-monitor.conf
```

2. Agrega lo siguiente (si el archivo no existe, créalo):

```bash
Section "Monitor"
    Identifier "VGA-0"
    Modeline "1366x768_60.00" 85.25 1366 1434 1566 1766 768 771 781 798 -hsync +vsync
    Option "PreferredMode" "1366x768_60.00"
EndSection
```

3. Guarda (Ctrl + O), cierra (Ctrl + X) y reinicia:

```bash
sudo reboot
```

---

¿Funcionó correctamente? 😊
