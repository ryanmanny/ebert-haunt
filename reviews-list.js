function updateBylines() {
  const bylines = document.getElementsByClassName('review-stack--byline');
  for (let byline of bylines) {
    if (byline.textContent.trim() !== "Roger Ebert") {
      byline.textContent = "\nRoger Ebert's Ghost\n";
    }
  };
  setTimeout(updateBylines, 1000);
}

updateBylines();
