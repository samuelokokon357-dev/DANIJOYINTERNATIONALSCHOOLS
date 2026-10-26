// Danijoy site scripts: mobile menu, hero slideshow, gallery filter + lightbox, forms.
(function () {
  // Settings the school can change in one place
  var CFG = window.DANIJOY || {
    whatsapp: "2348088248176",
    // When the portal / admissions backend (e.g. Supabase) is ready, set these:
    supabaseUrl: "",
    supabaseAnonKey: ""
  };

  // Mobile menu
  var header = document.querySelector(".site-header");
  var menuBtn = document.querySelector(".menu-btn");
  if (header && menuBtn) {
    menuBtn.addEventListener("click", function () {
      var open = header.classList.toggle("open");
      menuBtn.setAttribute("aria-expanded", open ? "true" : "false");
      var nav = header.querySelector(".nav");
      if (open && nav) header.style.setProperty("--navh", nav.offsetHeight + "px");
    });
  }

  // Close the mobile menu after choosing a link
  document.querySelectorAll(".nav a").forEach(function (a) {
    a.addEventListener("click", function () {
      if (header) { header.classList.remove("open"); if (menuBtn) menuBtn.setAttribute("aria-expanded", "false"); }
    });
  });

  // Shadow under the header once the page scrolls
  function onScroll() { if (header) header.classList.toggle("scrolled", window.scrollY > 8); }
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  // Highlight the nav link for the section on screen (home page only)
  if (document.body.classList.contains("is-home") && "IntersectionObserver" in window) {
    var links = {};
    document.querySelectorAll('.nav>a[href^="#"]').forEach(function (a) { links[a.getAttribute("href").slice(1)] = a; });
    var spy = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) {
          Object.keys(links).forEach(function (k) { links[k].removeAttribute("aria-current"); });
          if (links[en.target.id]) links[en.target.id].setAttribute("aria-current", "true");
        }
      });
    }, { rootMargin: "-45% 0px -50% 0px" });
    Object.keys(links).forEach(function (k) { var el = document.getElementById(k); if (el) spy.observe(el); });
  }

  // Hero slideshow (respects reduced motion)
  var slides = document.querySelectorAll(".hero-slides img");
  if (slides.length > 1 && !window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
    var i = 0;
    setInterval(function () {
      slides[i].classList.remove("on");
      i = (i + 1) % slides.length;
      slides[i].classList.add("on");
    }, 5500);
  }

  // Gallery filter + lightbox
  var gal = document.querySelector(".gallery");
  if (gal) {
    var items = gal.querySelectorAll("button");
    document.querySelectorAll(".filters button").forEach(function (b) {
      b.addEventListener("click", function () {
        document.querySelectorAll(".filters button").forEach(function (x) { x.setAttribute("aria-pressed", "false"); });
        b.setAttribute("aria-pressed", "true");
        var tag = b.dataset.tag;
        items.forEach(function (it) { it.hidden = tag !== "all" && it.dataset.tag !== tag; });
      });
    });
    var dlg = document.querySelector("dialog.lightbox");
    var big = dlg.querySelector("img");
    items.forEach(function (it) {
      it.addEventListener("click", function () {
        var im = it.querySelector("img");
        big.src = im.dataset.full || im.src;
        big.alt = im.alt;
        dlg.showModal();
      });
    });
    dlg.addEventListener("click", function (e) { if (e.target === dlg || e.target.classList.contains("lb-close")) dlg.close(); });
  }

  // Admissions enquiry: opens WhatsApp with the details until the admissions backend is connected
  var enq = document.getElementById("enquiry-form");
  if (enq) {
    enq.addEventListener("submit", function (e) {
      e.preventDefault();
      var d = new FormData(enq);
      var msg = [
        "Admission enquiry — Danijoy International Schools, Uyo",
        "Child's name: " + d.get("child"),
        "Date of birth: " + d.get("dob"),
        "Class applying for: " + d.get("class"),
        "Previous school: " + (d.get("prev") || "-"),
        "Parent/guardian: " + d.get("parent"),
        "Phone: " + d.get("phone"),
        "Email: " + (d.get("email") || "-"),
        "Note: " + (d.get("note") || "-")
      ].join("\n");
      var note = document.getElementById("enquiry-note");
      note.textContent = "Opening WhatsApp with your details. Send the message to complete your enquiry.";
      note.classList.add("show");
      window.open("https://wa.me/" + CFG.whatsapp + "?text=" + encodeURIComponent(msg), "_blank", "noopener");
    });
  }

  // Portal login: front end only until the portal backend is connected
  var login = document.getElementById("portal-form");
  if (login) {
    login.addEventListener("submit", function (e) {
      e.preventDefault();
      var note = document.getElementById("portal-note");
      note.textContent = CFG.supabaseUrl
        ? "Signing in…"
        : "The portal isn't connected yet, so sign-in is switched off. Please contact the school office for help.";
      note.classList.add("show");
    });
  }
})();
