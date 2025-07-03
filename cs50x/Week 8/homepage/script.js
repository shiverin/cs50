document.addEventListener('DOMContentLoaded', () => {
    const clickArea = document.getElementById('click');
    const bullet = document.getElementById('bullet');

    clickArea.addEventListener('click', (event) => {
        bullet.append("<THIS IS CS50>");
    });
});
