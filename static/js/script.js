const toggleBtn = document.querySelector('.navbar_toggleBtn');
const mainNav = document.querySelector('.main_nav');

toggleBtn.addEventListener('click', () => {
    mainNav.classList.toggle('active');
});

console.log(toggleBtn)
