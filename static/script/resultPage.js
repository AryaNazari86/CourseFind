document.getElementById("filters-btn").addEventListener("click", () => {
  $("#filters-popup").css("display", "flex").fadeIn(100);
});

function showCourseDetails(url) {
  $("#course-url").attr("src", url);
  $("#course-details-popup").css("display", "flex").fadeIn(100);
}
document.getElementById("page-shadow").addEventListener("click", () => {
  $("#filters-popup").fadeOut(100);
});
var courseTitles = document.getElementsByClassName("course-title");
for (let index = 0; index < courseTitles.length; index++) {
  const courseTitle = courseTitles[index];
  if (courseTitle.innerHTML.length > 50) {
    courseTitle.innerHTML = courseTitle.innerHTML.slice(0, 50) + "...";
  }
}
