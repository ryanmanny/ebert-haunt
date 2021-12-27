const byline = document.getElementsByClassName('byline').item(0);
if (byline.textContent.trim() !== "Roger Ebert") {
    byline.textContent = "\nRoger Ebert's Ghost\n";
};
