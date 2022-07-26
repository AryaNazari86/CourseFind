document.getElementById("filters-btn").addEventListener("click", () => {
  $("#filters-popup").css("display", "flex").fadeIn(100);
});

function showCourseDetails(url) {
  $("#course-url").attr("src", url);
  $("#course-details-popup").css("display", "flex").fadeIn(100);
}
