
const toggleBtn = document.getElementById('tgb1');
const mainNav = document.getElementById('mn1');

toggleBtn.addEventListener('click', () => {
    mainNav.classList.toggle('active');
});

console.log(toggleBtn)
console.log(mainNav)