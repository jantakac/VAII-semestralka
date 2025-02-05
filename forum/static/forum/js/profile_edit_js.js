document.addEventListener('DOMContentLoaded', () => {
    const toggleButton = document.getElementById('toggleConfirmation');
    const confirmationBox = document.getElementById('confirmationBox');
    const cancelButton = document.getElementById('cancelConfirmation');

    // Zobraz/Skry
    toggleButton.addEventListener('click', () => {
        confirmationBox.classList.toggle('d-none');
    });

    // Skry
    cancelButton.addEventListener('click', () => {
        confirmationBox.classList.add('d-none');
    });
});