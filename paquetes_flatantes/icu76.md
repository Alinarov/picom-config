Gracias. Si ejecutaste:

```bash
pacman -Q icu
```

Deberías ver algo como:

```
icu 75.1-1
```

Eso confirmaría que **tienes la versión 75**, y por eso **no está disponible `libicui18n.so.76` en tu sistema** actualmente.

---

### 🔧 ¿Cómo puedes instalar la versión 76 en Manjaro?

Lamentablemente, **Manjaro aún no ha actualizado `icu` a la versión 76 en sus repos oficiales**, y **no hay un paquete `icu76` disponible actualmente en el AUR** de manera activa.

---

### ✅ SOLUCIÓN RECOMENDADA (Manual, pero segura)

Si necesitas esa versión para una aplicación específica, puedes instalar **ICU 76 en paralelo sin romper tu sistema**. Aquí va una guía completa para compilar e instalar manualmente ICU 76:

---

### 🛠️ PASO A PASO PARA INSTALAR ICU 76 MANUALMENTE

1. **Descarga ICU 76**:

```bash
wget https://github.com/unicode-org/icu/releases/download/release-76-1/icu4c-76_1-src.tgz
```

2. **Descomprime y entra al directorio**:

```bash
tar -xf icu4c-76_1-src.tgz
cd icu/source
```

3. **Compila e instala en una ruta segura (`/opt/icu76`)**:

```bash
./configure --prefix=/opt/icu76
make -j$(nproc)
sudo make install
```

4. **Verifica que la biblioteca está instalada**:

```bash
ls /opt/icu76/lib/libicui18n.so.76*
```

5. **Ejecuta tu aplicación usando esta versión**:

```bash
LD_LIBRARY_PATH=/opt/icu76/lib:$LD_LIBRARY_PATH ./tu_aplicacion
```

---

### ❓¿Por qué no simplemente actualizas ICU en Manjaro?

Porque ICU es una **dependencia crítica del sistema** y una actualización manual fuera de los repositorios puede **romper muchas aplicaciones** que dependen de la versión actual (75 en tu caso). Por eso, instalarla en paralelo es lo más seguro.

---

¿Quieres que te prepare un script que automatice todo este proceso?
