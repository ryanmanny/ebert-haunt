const bylines = document.getElementsByClassName("blog-stack--byline");
for (let byline of bylines) {
  const link = byline.getElementsByTagName("a").item(0);
  if (link.textContent.trim() !== "Roger Ebert") {
    byline.textContent = "Roger Ebert's Ghost";
  }
}
