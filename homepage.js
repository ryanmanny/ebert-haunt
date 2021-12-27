const overlays = document.getElementsByClassName('review-overlay--author');
for (let overlay of overlays) {
  if (overlay.textContent.trim() !== "Roger Ebert") {
    overlay.textContent = "\nRoger Ebert's Ghost\n";
  }
};
