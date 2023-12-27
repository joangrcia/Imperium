// JavaScript to handle sidebar toggle
const openSidebarBtn = document.getElementById('openSidebarBtn');
const sidebar = document.getElementById('sidebar');

openSidebarBtn.addEventListener('click', function () {
  sidebar.style.display = (sidebar.style.display === 'none' || sidebar.style.display === '') ? 'block' : 'none';
  openSidebarBtn.classList.toggle("mdi-close");
  openSidebarBtn.classList.toggle("mdi-menu");
});