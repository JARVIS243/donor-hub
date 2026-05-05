console.log("Blood Bank Website Loaded Successfully 🩸");

document.addEventListener("DOMContentLoaded", function () {
    const cards = document.querySelectorAll(".card");

    cards.forEach((card, index) => {
        card.style.animation = `fadeUp 0.8s ease ${index * 0.2}s both`;
    });
});