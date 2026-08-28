document.addEventListener("DOMContentLoaded", () => {
    const nav = document.querySelector("nav");
    const navLinks = document.querySelectorAll("nav a");
    const currentPath = window.location.pathname;
    
    // 1. Crear e inyectar la píldora que se desliza
    const indicator = document.createElement("div");
    indicator.classList.add("nav-indicator");
    nav.appendChild(indicator);
    
    let activeLink = null;

    // 2. Buscar el enlace activo según la URL actual
    navLinks.forEach(link => {
        const linkPath = link.getAttribute("href");
        if (currentPath === linkPath || currentPath === linkPath + "/") {
            activeLink = link;
            link.classList.add("active");
        }
    });

    // Función para calcular y mover el indicador a la posición de un enlace
    const moveIndicator = (element) => {
        if (!element) return;
        indicator.style.width = `${element.offsetWidth}px`;
        indicator.style.height = `${element.offsetHeight}px`;
        indicator.style.left = `${element.offsetLeft}px`;
        indicator.style.top = `${element.offsetTop}px`;
    };

    // 3. Posicionar el indicador en la opción actual al cargar la página
    if (activeLink) {
        // Un ligero retraso para asegurar que el CSS y las fuentes ya renderizaron sus tamaños
        setTimeout(() => moveIndicator(activeLink), 50);
    }

    // 4. Interceptar los clics para animar antes de navegar
    navLinks.forEach(link => {
        link.addEventListener("click", (e) => {
            e.preventDefault(); // Pausamos la navegación nativa
            
            // Quitar clase al anterior y asignarla al nuevo
            if (activeLink) activeLink.classList.remove("active");
            link.classList.add("active");
            activeLink = link;

            // Deslizar el indicador
            moveIndicator(link);

            // Obtener a dónde quiere ir el usuario
            const href = link.getAttribute("href");
            
            // Redirigir después de que termine la animación (350ms, igual que en el CSS)
            setTimeout(() => {
                window.location.href = href;
            }, 350); 
        });
    });
});