// Bovi Tiziano Torneria — comportamenti del sito
// Menu mobile, animazioni allo scroll, back-to-top, lightbox galleria, invio form.

document.addEventListener("DOMContentLoaded", () => {
  initYear();
  initMobileMenu();
  initScrollReveal();
  initBackToTop();
  initLightbox();
  initContactForm();
});

function initYear() {
  const el = document.getElementById("year");
  if (el) el.textContent = new Date().getFullYear();
}

function initMobileMenu() {
  const toggle = document.getElementById("menu-toggle");
  const nav = document.getElementById("main-nav");
  if (!toggle || !nav) return;

  toggle.addEventListener("click", () => {
    const isOpen = nav.classList.toggle("open");
    toggle.setAttribute("aria-expanded", String(isOpen));
    toggle.setAttribute("aria-label", isOpen ? "Chiudi menu" : "Apri menu");
  });

  nav.querySelectorAll("a").forEach((link) => {
    link.addEventListener("click", () => {
      nav.classList.remove("open");
      toggle.setAttribute("aria-expanded", "false");
      toggle.setAttribute("aria-label", "Apri menu");
    });
  });
}

function initScrollReveal() {
  const items = document.querySelectorAll(".reveal");
  if (!items.length) return;

  if (!("IntersectionObserver" in window)) {
    items.forEach((el) => el.classList.add("is-visible"));
    return;
  }

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.15, rootMargin: "0px 0px -40px 0px" }
  );

  items.forEach((el) => observer.observe(el));
}

function initBackToTop() {
  const btn = document.getElementById("back-to-top");
  if (!btn) return;

  window.addEventListener("scroll", () => {
    btn.classList.toggle("visible", window.scrollY > 600);
  });

  btn.addEventListener("click", () => {
    window.scrollTo({ top: 0, behavior: "smooth" });
  });
}

function initLightbox() {
  const lightbox = document.getElementById("lightbox");
  const lightboxImg = document.getElementById("lightbox-img");
  const closeBtn = lightbox ? lightbox.querySelector(".lightbox-close") : null;
  if (!lightbox || !lightboxImg || !closeBtn) return;

  document.querySelectorAll(".gallery-item").forEach((btn) => {
    btn.addEventListener("click", () => {
      const full = btn.getAttribute("data-full");
      const alt = btn.querySelector("img")?.getAttribute("alt") || "";
      lightboxImg.src = full;
      lightboxImg.alt = alt;
      lightbox.hidden = false;
      document.body.style.overflow = "hidden";
    });
  });

  function closeLightbox() {
    lightbox.hidden = true;
    lightboxImg.src = "";
    document.body.style.overflow = "";
  }

  closeBtn.addEventListener("click", closeLightbox);
  lightbox.addEventListener("click", (e) => {
    if (e.target === lightbox) closeLightbox();
  });
  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape" && !lightbox.hidden) closeLightbox();
  });
}

function initContactForm() {
  const form = document.getElementById("contact-form");
  const status = document.getElementById("form-status");
  if (!form || !status) return;

  form.addEventListener("submit", async (e) => {
    e.preventDefault();

    // Campo anti-spam nascosto: se un bot lo compila, blocchiamo l'invio.
    if (form.botcheck && form.botcheck.checked) return;

    const accessKey = form.access_key ? form.access_key.value : "";
    if (!accessKey || accessKey === "WEB3FORMS_ACCESS_KEY_QUI") {
      status.textContent =
        "Il modulo non è ancora collegato: manca la chiave di invio (vedi README.md, sezione 2).";
      status.className = "form-status err";
      return;
    }

    const submitBtn = form.querySelector("button[type=submit]");
    submitBtn.disabled = true;
    status.textContent = "Invio in corso…";
    status.className = "form-status";

    try {
      const res = await fetch("https://api.web3forms.com/submit", {
        method: "POST",
        headers: { "Content-Type": "application/json", Accept: "application/json" },
        body: JSON.stringify(Object.fromEntries(new FormData(form))),
      });
      const data = await res.json();

      if (data.success) {
        status.textContent = "Richiesta inviata! Ti risponderemo il prima possibile.";
        status.className = "form-status ok";
        form.reset();
      } else {
        throw new Error(data.message || "Invio non riuscito");
      }
    } catch (err) {
      status.textContent =
        "Invio non riuscito. Puoi scriverci direttamente a torbovi@virgilio.it.";
      status.className = "form-status err";
    } finally {
      submitBtn.disabled = false;
    }
  });
}
