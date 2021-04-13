var collapseCard = document.getElementsByClassName("card-header-link");
for (let i = 0; i < collapseCard.length; i++) {
  let firstLoad = true;
  collapseCard[i].addEventListener("click", function () {
    if (firstLoad) {
      collapseCard[i]
        .getElementsByClassName("arrow-icon")[0]
        .classList.add("down");
    }
    if (collapseCard[i].classList.contains("collapsed")) {
      collapseCard[i]
        .getElementsByClassName("arrow-icon")[0]
        .classList.add("down");
    } else {
      if (!firstLoad) {
        collapseCard[i]
          .getElementsByClassName("arrow-icon")[0]
          .classList.remove("down");
      }
    }
    firstLoad = false;
  });
}

