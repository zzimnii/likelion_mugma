const imageInput = document.querySelector("#upload_file");
const imageArea = document.querySelector(".image-area");
const fileBox = document.querySelector(".filebox");
imageInput.addEventListener("change", loadImage);
fileBox.addEventListener("click", () => imageInput.click());

function loadImage(input) {
  if (input.target.files[0]) {
    const imageSrc = URL.createObjectURL(input.target.files[0]);
    imageArea.style.width = "100%";
    imageArea.src = imageSrc;
  }
}

const selectLabel = document.querySelector(".select-label");
const options = document.querySelectorAll(".option-item");
const selectedText = document.querySelector(".selected-text");
const arrowIcons = document.querySelector(".material-symbols-outlined");

const handleSelectOptions = (item) => {
  selectLabel.parentNode.classList.remove("active");
  selectedText.innerHTML = item.textContent;
};

options.forEach((option) => {
  option.addEventListener("click", () => {
    handleSelectOptions(option);
    arrowIcons.innerHTML = "keyboard_arrow_down";
  });
});

// 셀렉트 박스를 클릭하면 옵션 목록이 열리거나 닫힘
selectLabel.addEventListener("click", () => {
  if (selectLabel.parentNode.classList.contains("active")) {
    selectLabel.parentNode.classList.remove("active");
    arrowIcons.innerHTML = "keyboard_arrow_down";
  } else {
    selectLabel.parentNode.classList.add("active");
    arrowIcons.innerHTML = "keyboard_arrow_up";
  }
});
