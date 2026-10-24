"use strict";

const previewControls = document.querySelector(".preview-controls");
previewControls.hidden = false;
for (const input of previewControls.querySelectorAll("input")) {
  input.addEventListener("change", () => {
    for (const answer of document.querySelectorAll(".preview-answer")) {
      answer.hidden = answer.id !== `preview-${input.value}`;
    }
  });
}

const copyStatus = document.querySelector("#copy-status");
for (const button of document.querySelectorAll("[data-copy]")) {
  button.hidden = false;
  const label = button.textContent;
  button.addEventListener("click", async () => {
    try {
      await navigator.clipboard.writeText(button.dataset.copy);
      copyStatus.textContent = "In die Zwischenablage kopiert.";
      button.textContent = "Kopiert";
    } catch {
      copyStatus.textContent = "Kopieren nicht möglich. Bitte den sichtbaren Befehl markieren und manuell kopieren.";
      button.textContent = "Bitte Text markieren";
    }
    setTimeout(() => { button.textContent = label; }, 2500);
  });
}

const mobileMenu = document.querySelector(".mobile-nav");
for (const link of mobileMenu.querySelectorAll("a")) {
  link.addEventListener("click", () => { mobileMenu.open = false; });
}
mobileMenu.addEventListener("keydown", (event) => {
  if (event.key === "Escape" && mobileMenu.open) {
    mobileMenu.open = false;
    mobileMenu.querySelector("summary").focus();
  }
});
