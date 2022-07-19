document.getElementById("filters-btn").addEventListener('click', () => {
    $("#filters-popup").css("display", "flex").fadeIn(100);
});
document.getElementById("page-shadow").addEventListener('click', () => {
    $("#filters-popup").fadeOut(100);
});