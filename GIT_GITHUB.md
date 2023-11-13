# Subiendo un proyecto a GitHub con GIT

1. Iniciar GIT
```zsh
git init
```

2. Seleccionar todos los cambios
```zsh
git add .
```

3. Relizar un commit con GIT
```zsh
git commit -m "comentario"
```

4. Crear un repositorio
```zsh
git remote add origin https://github.com/NOMBRE_USUARIO/NOMBRE_PROYECTO.git
```

5. Subir los cambios a GitHub
```zsh
git push -u origin main (nombre_rama)
```

---
* Cambiar de nombre a la rama 'master'
```zsh 
git branch -m main
```
