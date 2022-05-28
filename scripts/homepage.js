const bylines = document.getElementsByClassName("review-overlay--author");
for (let byline of bylines) {
  if (byline.textContent.trim() !== "Roger Ebert") {
    byline.textContent = "\nRoger Ebert's Ghost\n";
  }
}
