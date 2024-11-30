document.addEventListener('DOMContentLoaded', () => {
    const toggleButton = document.getElementById('toggleButton');
    const sendForm = document.getElementById('sendForm');

    toggleButton.addEventListener('click', () => {
        if (sendForm.classList.contains('show')) {
            sendForm.classList.remove('show');
        } else {
            const buttonRect = toggleButton.getBoundingClientRect();
            sendForm.style.top = `${buttonRect.top + window.scrollY - 400}px`;
            sendForm.style.left = `${buttonRect.left + window.scrollX - (sendForm.offsetWidth / 2) + (toggleButton.offsetWidth / 2 - 100)}px`;
            sendForm.classList.add('show');
        }
    });

    document.addEventListener('keydown', (event) => {
        if (event.ctrlKey && event.key == 'm') {
            event.preventDefault();
            toggleButton.click();
        }
    })
})