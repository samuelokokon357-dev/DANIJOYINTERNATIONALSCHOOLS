#!/usr/bin/env python3
"""Generates the static Danijoy site. Run: python3 build.py
Pages: index.html (one-page site), admissions/, portal/login/"""
import os

OUT = os.path.dirname(os.path.abspath(__file__))
PHONE1, PHONE2 = "0808 824 8176", "0810 364 9175"
EMAIL = "danijoyinternationalschooluyo@gmail.com"
ADDRESS = "After Ibom Icon Hotel & Golf Resort, Nwaniba (before the Police Station), Ifiayong, Uruan L.G.A., Uyo, Akwa Ibom State"
SCHOOL = "Danijoy International Schools"

NAV = [("#about", "About"), ("#academics", "Academics"), ("#student-life", "Student life"),
       ("#gallery", "Gallery"), ("admissions/", "Admissions"), ("#contact", "Contact")]

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link href="https://fonts.googleapis.com/css2?family=Figtree:wght@400;500;600;700;800&family=Young+Serif&display=swap" rel="stylesheet">')

ICON_USER = '<svg class="ico" viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="8" r="4"/><path d="M4 21c0-4.4 3.6-8 8-8s8 3.6 8 8"/></svg>'
ICON_ARROW = '<svg class="ico arrow" viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'


def portal_btn(href, light=False, sm=False):
    cls = "btn btn-portal" + (" btn-line-light" if light else " btn-line") + (" btn-sm" if sm else "")
    return f'<a class="{cls}" href="{href}">{ICON_USER}<span>Portal Login</span></a>'


def apply_btn(href, sm=False, label="Apply Now"):
    cls = "btn btn-apply btn-gold" + (" btn-sm" if sm else "")
    return f'<a class="{cls}" href="{href}"><span>{label}</span>{ICON_ARROW}</a>'


def layout(path, title, desc, body, current=None, home=False):
    depth = path.count("/")
    root = "../" * depth
    nav = "".join(
        f'<a href="{root}{href}"{" aria-current=\"page\"" if href == current else ""}>{label}</a>' for href, label in NAV)
    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#0f1a52">
<link rel="icon" href="{root}assets/img/logo.jpg">
{FONTS}
<link rel="stylesheet" href="{root}assets/css/style.css">
</head>
<body{' class="is-home"' if home else ''}>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <div class="wrap">
    <a class="brand" href="{root}index.html" aria-label="{SCHOOL}, home">
      <img src="{root}assets/img/logo.jpg" alt="">
      <span><b>Danijoy</b><small>International Schools · Uyo</small></span>
    </a>
    <nav class="nav" aria-label="Main">{nav}
      <div class="nav-cta">{portal_btn(root + "portal/login/", sm=True)}{apply_btn(root + "admissions/", sm=True)}</div>
    </nav>
    <div class="header-cta">
      {portal_btn(root + "portal/login/", sm=True)}
      {apply_btn(root + "admissions/", sm=True)}
    </div>
    <button class="menu-btn" aria-expanded="false" aria-label="Menu"><span></span><span></span><span></span></button>
  </div>
</header>
<main id="main">
{body.replace("__ROOT__", root)}
</main>
<footer class="site-footer">
  <div class="wrap">
    <div>
      <div class="fbrand"><img src="{root}assets/img/logo.jpg" alt=""><b style="font-family:var(--display);font-weight:400;font-size:1.3rem;color:#fff">{SCHOOL}</b></div>
      <p>Full boarding secondary school in Uyo, Akwa Ibom State, teaching the Cambridge curriculum.</p>
      <p><i>Honesty in learning is our legacy.</i></p>
    </div>
    <div><h3>School</h3>
      <a href="{root}#about">About us</a><a href="{root}#academics">Academics</a><a href="{root}#student-life">Student life</a><a href="{root}#gallery">Gallery</a></div>
    <div><h3>Join us</h3>
      <a href="{root}admissions/">Apply now</a><a href="{root}portal/login/">Portal login</a><a href="{root}#contact">Contact</a></div>
    <div><h3>Visit or call</h3>
      <p style="margin:0 0 .6rem">{ADDRESS}</p>
      <a href="tel:+2348088248176">{PHONE1}</a><a href="tel:+2348103649175">{PHONE2}</a>
      <a href="mailto:{EMAIL}" style="word-break:break-all">{EMAIL}</a></div>
  </div>
  <div class="wrap legal"><span style="grid-column:1/-1">© 2026 {SCHOOL}, Uyo Campus. All rights reserved.</span></div>
</footer>
<script src="{root}assets/js/site.js"></script>
</body>
</html>"""
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(html)


def page_hero(title, lead, img):
    return f"""<div class="page-hero"><img src="__ROOT__assets/img/{img}.jpg" alt=""><div class="wrap"><h1>{title}</h1><p>{lead}</p></div></div>"""


CTA = f"""<section class="cta-band"><div class="wrap">
  <div><h2>Admissions are open for a full boarding place</h2>
  <p>Sit our entrance exam and tour the campus. Call {PHONE1} or {PHONE2}.</p></div>
  <div class="acts">{apply_btn("__ROOT__admissions/")}<a class="btn btn-line-light" href="__ROOT__#contact"><span>Book a visit</span></a></div>
</div></section>"""

# ---------------------------------------------------------------- GALLERY DATA
gal_items = [
    ("choir", "events", "Students singing at the awards ceremony"),
    ("lab", "classroom", "Science practical in the laboratory"),
    ("dance-front", "events", "Cultural dance performance"),
    ("violins", "music", "Violin players at a school event"),
    ("exam-hall", "classroom", "Students writing an exam"),
    ("basketball", "sports", "A basketball game"),
    ("award-2", "events", "Best Oratory Award winner"),
    ("classroom", "classroom", "Students in class"),
    ("dance-back", "events", "Dancers in colourful costume"),
    ("drums", "music", "Student on the drums"),
    ("volleyball", "sports", "A student ready for the ball on court"),
    ("books", "classroom", "Students carrying their books across campus"),
    ("painting", "events", "A student painting at an event"),
    ("quiz", "events", "A student speaking at a quiz"),
    ("football", "sports", "Football on the pitch"),
    ("primary-class", "classroom", "Younger students writing in class"),
    ("podium", "events", "A student speaking at the podium"),
    ("keys", "music", "Student at the keyboard"),
    ("netball", "sports", "Court game in action"),
    ("assembly", "events", "Students seated at a school event"),
    ("maths-medal", "events", "National Mathematics Festival medallist"),
    ("radio-1", "radio", "Students in the radio studio"),
    ("cert-3", "events", "Certificate of Excellence presentation"),
    ("group-uniform", "events", "Students in uniform on the balcony"),
    ("dance-group", "events", "The cultural dance troupe in orange costume outside the school"),
    ("radio-laugh", "radio", "A student laughing during a live radio show"),
    ("radio-side", "radio", "Students on air at the radio studio"),
    ("radio-guest", "radio", "Students and a guest at the studio microphones"),
    ("radio-girl", "radio", "A student speaking on the radio"),
    ("radio-kente", "radio", "Two students in kente uniform at the radio studio"),
    ("radio-pair", "radio", "Two students about to go on air"),
]
gal_html = "".join(
    f'<button data-tag="{t}"><img loading="lazy" src="__ROOT__assets/img/{n}.jpg" alt="{a}"></button>' for n, t, a in gal_items)

# ---------------------------------------------------------------- HOME (one page)
home = f"""
<section class="hero" id="top" style="padding:0">
  <div class="hero-slides" aria-hidden="true">
    <img class="on" src="assets/img/choir.jpg" alt="">
    <img src="assets/img/lab.jpg" alt="" loading="lazy">
    <img src="assets/img/dance-front.jpg" alt="" loading="lazy">
    <img src="assets/img/classroom.jpg" alt="" loading="lazy">
  </div>
  <div class="wrap">
    <span class="badge"><i></i> Admissions open · Full boarding secondary school</span>
    <h1>Where honest learning becomes a legacy</h1>
    <p class="lead">A Cambridge secondary school in Uyo where students learn, lead and create in a calm, well-equipped boarding community.</p>
    <div class="actions">
      {apply_btn("admissions/")}
      {portal_btn("portal/login/", light=True)}
    </div>
  </div>
  <div class="hero-motto">Probitas et eruditio legatum est</div>
</section>

<div class="creds"><div class="wrap">
  <span class="lbl">Recognised pathways</span>
  <b>Cambridge Assessment International Education</b><span class="sep"></span><b>IELTS</b><span class="sep"></span><b>SAT</b>
</div></div>

<!-- ABOUT -->
<section id="about">
  <div class="wrap split">
    <div class="media"><img src="assets/img/podium.jpg" alt="A student speaking at the podium during a school event"></div>
    <div>
      <h2>A school built on honesty and learning</h2>
      <p>Danijoy International Schools, Uyo Campus, is a full boarding secondary school in Ifiayong, Uruan L.G.A., Akwa Ibom State. Our students follow the Cambridge curriculum, take part in music, sport, art and public speaking, and live and study on a quiet campus.</p>
      <div class="motto-card"><b>Probitas et eruditio legatum est</b><span>Honesty and learning is our legacy</span></div>
      <ul class="checks">
        <li><b>Integrity.</b> We teach students to be honest in their work and in their words.</li>
        <li><b>Excellence.</b> We expect strong results and we celebrate them.</li>
        <li><b>Leadership.</b> Students lead, speak and mentor others.</li>
        <li><b>Creativity.</b> Music, dance and art are part of the school week.</li>
      </ul>
    </div>
  </div>
</section>

<section class="bg-paper">
  <div class="wrap">
    <div class="section-head"><h2>What every Danijoy student receives</h2>
    <p>Six commitments that shape the school day, from the first lesson to lights out in the boarding house.</p></div>
    <div class="features">
      <div class="feature"><h3>Value-based, holistic education</h3><p>Integrity sits beside grades. Students are taught to do the right thing when no one is watching.</p></div>
      <div class="feature"><h3>Creative and vocational training</h3><p>Music, art, dance and practical skills sit alongside the core subjects.</p></div>
      <div class="feature"><h3>International certifications</h3><p>Cambridge qualifications, with preparation for IELTS and SAT.</p></div>
      <div class="feature"><h3>Leadership and mentorship</h3><p>Students take on responsibility and are guided by teachers who know them by name.</p></div>
      <div class="feature"><h3>World-class learning and boarding</h3><p>Science laboratories, a computer room, interactive boards and comfortable dormitories.</p></div>
      <div class="feature"><h3>A serene environment</h3><p>A calm campus away from the noise of the city, made for focus.</p></div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head"><h2>Our people</h2><p>Teachers and staff who guide students in class and in the boarding house.</p></div>
    <img loading="lazy" src="assets/img/staff.jpg" alt="Danijoy teachers and staff in a group photo on the school grounds" style="width:100%;border-radius:var(--radius);box-shadow:var(--shadow)">
  </div>
</section>

<!-- ACADEMICS -->
<section id="academics" class="bg-paper">
  <div class="wrap">
    <div class="section-head"><h2>Academics</h2>
    <p>We are a Cambridge school. Students work towards internationally recognised qualifications and prepare for the IELTS and SAT.</p></div>
    <div class="cards">
      <div class="card"><img loading="lazy" src="assets/img/lab.jpg" alt="Students working in the science laboratory"><div><h3>Sciences</h3><p>Hands-on practicals in our laboratory, from chemistry to physics and biology.</p></div></div>
      <div class="card"><img loading="lazy" src="assets/img/teacher.jpg" alt="A teacher working through chemistry corrections on a whiteboard"><div><h3>Core subjects</h3><p>English, mathematics and the subjects every student needs, taught by qualified teachers.</p></div></div>
      <div class="card"><img loading="lazy" src="assets/img/exam-hall.jpg" alt="Students writing an exam in a bright hall"><div><h3>Assessment</h3><p>Regular tests and exams show every student where they stand and what to work on next.</p></div></div>
    </div>
  </div>
</section>
<section>
  <div class="wrap split flip">
    <div class="media"><img loading="lazy" src="assets/img/primary-class.jpg" alt="Students writing in a classroom with green desks"></div>
    <div>
      <h2>Rooms made for learning</h2>
      <ul class="checks">
        <li>Bright, ordered classrooms with proper desks</li>
        <li>A science laboratory for practical lessons</li>
        <li>A computer room</li>
        <li>Interactive boards for visual teaching</li>
        <li>Boarding houses for rest and prep</li>
      </ul>
    </div>
  </div>
</section>

<!-- STUDENT LIFE -->
<section id="student-life" class="bg-paper">
  <div class="wrap">
    <div class="section-head"><h2>Student life</h2><p>Music, sport, art, public speaking and broadcasting. There's a place for every talent.</p></div>
    <div class="life">
      <figure class="a"><img loading="lazy" src="assets/img/dance-front.jpg" alt="Students in cultural dance costume"><figcaption>Cultural dance</figcaption></figure>
      <figure class="b"><img loading="lazy" src="assets/img/violin-solo.jpg" alt="A student playing the violin"><figcaption>Strings</figcaption></figure>
      <figure class="c"><img loading="lazy" src="assets/img/drums.jpg" alt="A student playing the drums"><figcaption>Drums</figcaption></figure>
      <figure class="d"><img loading="lazy" src="assets/img/keys.jpg" alt="A student playing a keyboard"><figcaption>Keys</figcaption></figure>
      <figure class="e"><img loading="lazy" src="assets/img/painting.jpg" alt="A student painting on a canvas"><figcaption>Art</figcaption></figure>
      <figure class="f"><img loading="lazy" src="assets/img/basketball.jpg" alt="Students playing basketball"><figcaption>Basketball</figcaption></figure>
      <figure class="g"><img loading="lazy" src="assets/img/netball.jpg" alt="Students playing a game on the sports court"><figcaption>Court games</figcaption></figure>
      <figure class="h"><img loading="lazy" src="assets/img/football.jpg" alt="A football under a student's boot on the pitch"><figcaption>Football</figcaption></figure>
    </div>
  </div>
</section>
<section>
  <div class="wrap">
    <div class="section-head"><h2>Live on the radio</h2><p>Students visit a local radio studio to present, interview and speak live on air.</p></div>
    <div class="cards four">
      <div class="card"><img loading="lazy" src="assets/img/radio-laugh.jpg" alt="A student laughing during a live radio show" style="aspect-ratio:4/3"></div>
      <div class="card"><img loading="lazy" src="assets/img/radio-side.jpg" alt="Students on air at the radio studio" style="aspect-ratio:4/3"></div>
      <div class="card"><img loading="lazy" src="assets/img/radio-girl.jpg" alt="A student speaking on the radio" style="aspect-ratio:4/3"></div>
      <div class="card"><img loading="lazy" src="assets/img/radio-pair.jpg" alt="Two students ready to go on air" style="aspect-ratio:4/3"></div>
    </div>
  </div>
</section>
<section class="bg-paper">
  <div class="wrap split flip">
    <div class="media"><img loading="lazy" src="assets/img/dance-group.jpg" alt="The Danijoy cultural dance troupe in orange costume outside the school"></div>
    <div>
      <h2>Culture on stage</h2>
      <p>Our dance troupe performs traditional dances in hand-made costume, with painted faces, beads and ankle rattles. They perform at school events and bring local culture into school life.</p>
    </div>
  </div>
</section>

<section class="bg-navy">
  <div class="wrap">
    <div class="section-head"><h2>Proud moments</h2><p>Our students were recognised at the 2025/2026 end-of-session awards and at the National Mathematics Festival.</p></div>
    <div class="ach">
      <figure><img loading="lazy" src="assets/img/maths-medal.jpg" alt="A student with a medal and Certificate of Merit from the National Mathematics Festival"><figcaption><b>National Mathematics Festival</b>Certificate of Merit, May 2026</figcaption></figure>
      <figure><img loading="lazy" src="assets/img/award-1.jpg" alt="A student holding an Outstanding Legacy Award"><figcaption><b>Outstanding Legacy Award</b>End-of-session awards</figcaption></figure>
      <figure><img loading="lazy" src="assets/img/award-2.jpg" alt="A student holding a Best Oratory Award"><figcaption><b>Best Oratory Award</b>2025/2026 session</figcaption></figure>
      <figure><img loading="lazy" src="assets/img/cert-2.jpg" alt="A student holding two Certificates of Excellence in the sciences"><figcaption><b>Certificates of Excellence</b>Highest cumulative average in sciences</figcaption></figure>
    </div>
  </div>
</section>

<!-- GALLERY -->
<section id="gallery">
  <div class="wrap">
    <div class="section-head"><h2>Gallery</h2><p>A look at classes, performances, sport and celebrations.</p></div>
    <div class="filters" role="group" aria-label="Filter photos">
      <button data-tag="all" aria-pressed="true">All</button><button data-tag="classroom" aria-pressed="false">Classroom</button>
      <button data-tag="events" aria-pressed="false">Events</button><button data-tag="music" aria-pressed="false">Music</button>
      <button data-tag="sports" aria-pressed="false">Sports</button><button data-tag="radio" aria-pressed="false">Radio</button>
    </div>
    <div class="gallery">{gal_html}</div>
    <dialog class="lightbox" aria-label="Photo viewer"><button class="lb-close" aria-label="Close photo">Close</button><img alt=""></dialog>
  </div>
</section>

<section class="bg-paper">
  <div class="wrap">
    <div class="section-head"><h2>How to join</h2><p>Three steps from first call to first day.</p></div>
    <ol class="steps">
      <li><h3>Make an enquiry</h3><p>Call, message on WhatsApp or send the form on our admissions page.</p></li>
      <li><h3>Sit the entrance exam</h3><p>We assess your child on our entrance exam. Ask the school office for the next date.</p></li>
      <li><h3>Register and settle in</h3><p>Complete registration with the school office and prepare for boarding.</p></li>
    </ol>
  </div>
</section>
{CTA}

<!-- CONTACT -->
<section id="contact">
  <div class="wrap two-col">
    <div>
      <h2>Contact us</h2>
      <p>Call, message or come and see the campus.</p>
      <ul class="checks">
        <li><b>Phone:</b> <a href="tel:+2348088248176">{PHONE1}</a> · <a href="tel:+2348103649175">{PHONE2}</a></li>
        <li><b>WhatsApp:</b> <a href="https://wa.me/2348088248176">+234 808 824 8176</a></li>
        <li><b>Email:</b> <a href="mailto:{EMAIL}">{EMAIL}</a></li>
        <li><b>Address:</b> {ADDRESS}</li>
      </ul>
      <p style="margin-top:1.6rem">{apply_btn("admissions/")}</p>
    </div>
    <div class="side-card"><h3>Finding us</h3>
      <p>We are on the road after Ibom Icon Hotel &amp; Golf Resort, in Nwaniba, just before the Police Station.</p>
      <p><a href="https://www.google.com/maps/search/?api=1&amp;query=Danijoy+International+Schools+Uyo">Open in Google Maps</a></p></div>
  </div>
</section>
"""

# ---------------------------------------------------------------- ADMISSIONS
admissions = page_hero("Admissions", "Apply for a full boarding place at Danijoy International Schools, Uyo.", "exam-hall") + f"""
<section><div class="wrap">
  <div class="section-head"><h2>How admission works</h2></div>
  <ol class="steps">
    <li><h3>Send your enquiry</h3><p>Fill in the form below. It opens WhatsApp so the school office gets your details straight away.</p></li>
    <li><h3>Take the entrance exam</h3><p>The office will confirm the next exam date and what to bring.</p></li>
    <li><h3>Register your child</h3><p>Once your child is offered a place, the office guides you through registration and boarding needs.</p></li>
  </ol>
</div></section>
<section class="bg-paper" id="apply"><div class="wrap two-col">
  <div class="form-card">
    <h2 style="font-size:1.8rem">Admission enquiry</h2>
    <form id="enquiry-form" novalidate>
      <div class="form-grid">
        <div><label for="child">Child's full name</label><input id="child" name="child" required autocomplete="off"></div>
        <div><label for="dob">Date of birth</label><input id="dob" name="dob" type="date" required></div>
        <div><label for="class">Class applying for</label>
          <select id="class" name="class" required><option value="">Choose a class</option>
            <option>JSS 1</option><option>JSS 2</option><option>JSS 3</option><option>SS 1</option><option>SS 2</option><option>SS 3</option><option>Not sure yet</option></select></div>
        <div><label for="prev">Previous school</label><input id="prev" name="prev"></div>
        <div><label for="parent">Parent or guardian's name</label><input id="parent" name="parent" required autocomplete="name"></div>
        <div><label for="phone">Phone number</label><input id="phone" name="phone" type="tel" required autocomplete="tel"></div>
        <div class="full"><label for="email">Email</label><input id="email" name="email" type="email" autocomplete="email"></div>
        <div class="full"><label for="note">Anything we should know?</label><textarea id="note" name="note"></textarea></div>
      </div>
      <p style="margin-top:1.2rem"><button class="btn btn-apply btn-gold" type="submit"><span>Send enquiry on WhatsApp</span>{ICON_ARROW}</button></p>
      <div id="enquiry-note" class="notice" role="status"></div>
    </form>
  </div>
  <aside class="side-card">
    <h3>Prefer to talk?</h3>
    <p>Call the school office:</p>
    <p><a href="tel:+2348088248176">{PHONE1}</a><br><a href="tel:+2348103649175">{PHONE2}</a></p>
    <h3 style="margin-top:1.4rem">Visit the campus</h3>
    <p>{ADDRESS}</p>
    <h3 style="margin-top:1.4rem">Already enrolled?</h3>
    <p>{portal_btn("__ROOT__portal/login/", light=True, sm=True)}</p>
  </aside>
</div></section>
"""

# ---------------------------------------------------------------- PORTAL LOGIN
portal = f"""
<div class="portal-wrap">
  <div class="portal-card">
    <img src="__ROOT__assets/img/logo.jpg" alt="Danijoy crest">
    <h1>Portal login</h1>
    <p class="sub">Students, parents and staff sign in here.</p>
    <form id="portal-form" novalidate>
      <div class="who" role="radiogroup" aria-label="I am a">
        <span><input type="radio" id="w1" name="who" value="parent" checked><label for="w1">Parent</label></span>
        <span><input type="radio" id="w2" name="who" value="student"><label for="w2">Student</label></span>
        <span><input type="radio" id="w3" name="who" value="staff"><label for="w3">Staff</label></span>
      </div>
      <div class="field"><label for="pe">Email or ID</label><input id="pe" name="id" required autocomplete="username"></div>
      <div class="field"><label for="pp">Password</label><input id="pp" name="password" type="password" required autocomplete="current-password"></div>
      <button class="btn btn-apply btn-gold" type="submit"><span>Sign in</span>{ICON_ARROW}</button>
      <div id="portal-note" class="notice" role="status"></div>
    </form>
    <p style="text-align:center;margin:1.2rem 0 0;font-size:.95rem">New here? <a href="__ROOT__admissions/"><b>Apply for admission</b></a></p>
  </div>
</div>
"""

if __name__ == "__main__":
    layout("index.html", "Danijoy International Schools, Uyo | Full boarding secondary school", "Cambridge full boarding secondary school in Uyo, Akwa Ibom State. Admissions open.", home, home=True)
    layout("admissions/index.html", "Admissions | Danijoy International Schools", "Apply for a full boarding place in Uyo.", admissions, "admissions/")
    layout("portal/login/index.html", "Portal login | Danijoy International Schools", "Sign in to the school portal.", portal)
    print("built")
