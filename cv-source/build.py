"""Builds the three CV variants as standalone HTML, then prints each to PDF with headless Chrome.

Run:  python3 cv-source/build.py
Edit content here (single source of truth), or edit a generated .html directly and re-print it.
"""
import os
import subprocess
from html import escape

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(os.path.dirname(HERE), "public", "CV")
STYLE = open(os.path.join(HERE, "style.css.part")).read()

CONTACT = """<div class="contact">
    <span>Daska, Pakistan · Open to remote (PKT, UTC+5)</span>
    <a href="tel:+923147551262">+92 314 7551262</a>
    <a href="mailto:mluqmangn@gmail.com">mluqmangn@gmail.com</a>
    <a href="https://muhammadluqmankhokhar.vercel.app/">muhammadluqmankhokhar.vercel.app</a>
    <a href="https://github.com/Luqman-Khokhar">github.com/Luqman-Khokhar</a>
    <a href="https://www.linkedin.com/in/mluqmangn/">linkedin.com/in/mluqmangn</a>
  </div>"""

EDUCATION = """<h2>Education</h2>
<div class="head"><div><span class="title">BS Information Technology</span> · <span class="org">University of the Punjab</span> · CGPA 3.1</div><span class="meta">Sep 2018 – Aug 2022</span></div>
<p style="margin-top:3px"><span class="label">Languages:</span> English, Urdu</p>"""

# ---------------------------------------------------------------- experience
JOBS = {
    "contrive": ("MERN Stack &amp; React Native Developer", "Contrive Solutions", "Feb 2026 – Present"),
    "adroid": ("React.js &amp; React Native Developer", "Adroid IT Solutions", "Feb 2025 – Feb 2026"),
    "appcrates": ("React Native Developer", "AppCrates", "Jul 2024 – Feb 2025"),
    "alsalam": ("React.js &amp; React Native Developer", "Al-Salam Tech House", "Mar 2023 – Mar 2024"),
}

# ---------------------------------------------------------------- projects
P = {}
P["saleem"] = dict(
    name="Saleem Mosque Finder", type="Mosque &amp; prayer location app (iOS, Android)", role="Sole mobile engineer · Contrive Solutions",
    desc="Helps Muslims who are travelling or new to an area find nearby mosques and prayer areas, and see who is about to pray there.",
    links=[("Google Play", "https://play.google.com/store/apps/details?id=com.akhie.saleem&amp;hl=en"), ("App Store", "https://apps.apple.com/us/app/saleem-mosque-finder/id6760958351")],
    bullets=[
        "Built the Expo React Native app in TypeScript with Redux, including map-based discovery of nearby mosques and prayer areas.",
        "Implemented user-submitted locations and edits, and start/join flows for a congregation at the next prayer.",
        "Integrated the Ruby on Rails API and Firebase; manage builds and releases to Google Play and the App Store.",
    ],
    tech="Expo, React Native, TypeScript, Redux, Firebase, Ruby on Rails API",
    compact="Built the Expo React Native app solo in TypeScript with Redux, integrated the Ruby on Rails API and Firebase, and manage its releases to Google Play and the App Store.",
)
P["chirpbyte"] = dict(
    name="Chirpbyte", type="Customer support &amp; engagement app", role="React Native developer · team project",
    desc="Lets businesses chat with website and social-media visitors (WhatsApp, Facebook, Instagram) from one inbox and schedule meetings.",
    links=[("App Store", "https://apps.apple.com/us/app/chirpbyte/id6670273736"), ("chirpbyte.com", "https://chirpbyte.com/")],
    bullets=[
        "Developed the live chat modules for the unified multi-platform inbox, with real-time sync over Socket.io and Pusher.",
        "Implemented live visitor tracking and push notifications with Notifee; managed app state with Redux Toolkit.",
    ],
    tech="React Native, Redux Toolkit, Socket.io, Pusher, Notifee",
    compact="Developed live chat modules for a multi-platform support inbox, with real-time sync over Socket.io and Pusher, visitor tracking and Notifee push notifications.",
)
P["kroolo"] = dict(
    name="Kroolo", type="Work management &amp; team collaboration app", role="React Native developer · team project",
    desc="A Slack- and Trello-style mobile app for team communication, task tracking and collaboration.",
    links=[("Google Play", "https://play.google.com/store/apps/details?id=com.kroolo.app&amp;hl=en"), ("kroolo.com", "https://kroolo.com/")],
    bullets=[
        "Built the mobile frontend in React Native and TypeScript: task creation, assignment and progress tracking, team spaces and role-based access.",
        "Implemented real-time group and direct chat with Socket.io, and Google, Apple and Facebook sign-in.",
        "Managed asynchronous app state with Redux-Saga, structured with an MVC architecture.",
    ],
    tech="React Native, TypeScript, Redux-Saga, Socket.io, Firebase",
    compact="Built the React Native and TypeScript frontend for tasks, team spaces and role-based access, with Socket.io chat, social sign-in and Redux-Saga state management.",
)
P["tfc"] = dict(
    name="TFC Academy", type="Academy website &amp; certificate platform", role="Solo developer",
    desc="Website and certificate platform for Two Fast Computer College, Daska, with staff tools behind a login.",
    links=[("tfcacademy.vercel.app", "https://tfcacademy.vercel.app/")],
    bullets=[
        "Built the full platform solo in Next.js: public site, course catalogue with fees and durations, staff tools and deployment.",
        "Implemented certificate lookup by ID with print/download and QR verification.",
        "Built bulk certificate management from Excel and PDF files for teachers, and course management for admins.",
    ],
    tech="Next.js, Tailwind CSS",
    compact="Built the full platform solo in Next.js: course catalogue, certificate lookup with QR verification, and bulk certificate management from Excel and PDF files.",
)
P["nexgen"] = dict(
    name="NexGen Tracker", type="GPS vehicle-tracking company website", role="Solo developer",
    desc="Company website for a vehicle-tracking service in Pakistan, linking customers to the separate web app where they track their vehicles.",
    links=[("nexgentracker.com", "https://nexgentracker.com/"), ("app.nexgentracker.com", "https://app.nexgentracker.com/")],
    links_note=" (tracking portal)",
    bullets=[
        "Built and deployed the site solo with Astro, Three.js and Tailwind CSS.",
        "Built service pages for live location, zone alerts, route replay and over-speed alerts, a how-it-works walkthrough and FAQ, and contact via form, phone and WhatsApp.",
    ],
    tech="Astro, Three.js, Tailwind CSS",
    compact="Built and deployed the company website solo: service pages, how-it-works walkthrough, FAQ and contact via form, phone and WhatsApp, linking to the tracking portal.",
)
P["alsalaam"] = dict(
    name="AlSalaam Tourism", type="Tour &amp; event booking web app (Dubai)", role="Next.js frontend · team project",
    desc="A platform for discovering, comparing and booking curated tours and events in Dubai, for families and solo travellers.",
    links=[("alsalaamtourism.com", "https://alsalaamtourism.com/")],
    bullets=[
        "Built the Next.js frontend: category-filtered tour and event booking, family and solo traveller modes, and an admin panel with CRUD operations.",
        "Integrated APIs with Axios and managed state with Redux Toolkit.",
        "Built a responsive UI with Tailwind CSS and Ant Design, with Framer Motion animations.",
    ],
    tech="Next.js, Redux Toolkit, Axios, Tailwind CSS, Ant Design, Framer Motion",
    compact="Built the Next.js frontend: category-filtered tour and event booking, family and solo traveller modes and an admin panel; integrated APIs with Axios and Redux Toolkit.",
)
P["skip2beat"] = dict(
    name="Skip2Beat", type="Social fitness app", role="React Native developer · team project",
    desc="Fitness app with rep counting, music-backed workouts and social features.",
    links=[("Google Play", "https://play.google.com/store/apps/details?id=com.skip2beat.app&amp;hl=en")],
    bullets=[
        "Built the guided workout flows in React Native.",
        "Implemented real-time chat over Socket.io and Google Maps location features for finding nearby users.",
    ],
    tech="React Native, Socket.io, Google Maps",
    compact="Fitness app with rep counting, music-backed workouts and social features. Built the guided workout flows, real-time chat over Socket.io, and Google Maps location features for finding nearby users.",
)
P["health"] = dict(
    name="Health In Mobile", type="Health &amp; habit app", role="React Native developer · team project",
    desc="An app that builds healthy habits to help prevent and manage chronic disease.",
    links=[("Google Play", "https://play.google.com/store/apps/details?id=org.hksr.healthinmobile&amp;hl=en")],
    bullets=[
        "Built the Expo React Native app on a KeystoneJS backend, with habit reminders and passwordless magic-link sign-in.",
    ],
    tech="Expo, React Native, KeystoneJS",
    compact="Built the Expo React Native app on a KeystoneJS backend, with habit reminders and passwordless magic-link sign-in.",
)

# ---------------------------------------------------------------- variants
VARIANTS = {
    "Universal": dict(
        title="Full-Stack Software Developer",
        headline="Full-Stack Software Developer | React.js · Next.js · React Native · Node.js · MongoDB",
        keywords="Full-Stack Developer, MERN, React.js, Next.js, React Native, TypeScript, Node.js, Express.js, MongoDB, Socket.io",
        summary="Full-stack JavaScript developer with 3+ years of experience shipping production web and mobile apps with React.js, Next.js, React Native and the MERN stack. At Contrive Solutions, builds full-stack web features with MongoDB, Express.js, React.js and Node.js, and is the sole mobile engineer on a live Expo app on Google Play and the App Store. Experienced in real-time features, including live chat, push notifications and maps, using Socket.io, Pusher and Firebase, and in integrating front ends with Node.js, KeystoneJS, Laravel and Ruby on Rails backends.",
        jobs={
            "contrive": [
                "Build and maintain full-stack web features with MongoDB, Express.js, React.js and Node.js; joined as a React.js developer and moved into full-stack and mobile ownership.",
                "Sole mobile engineer on Saleem Mosque Finder, an Expo React Native and TypeScript app live on Google Play and the App Store.",
                "Own the mobile release cycle end to end: feature planning, Ruby on Rails API integration, builds and store submissions.",
            ],
            "adroid": [
                "Led front-end development of multiple client web and mobile products in React.js and React Native.",
                "Integrated an AI chatbot and real-time notification features into client products.",
                "Connected front ends to Node.js, KeystoneJS and Laravel backends, working directly with backend teams on API integration and data flow.",
            ],
            "appcrates": [
                "Built and maintained responsive UI components for production React Native and React.js apps.",
                "Restructured state management and component architecture to reduce code complexity and speed up feature delivery.",
            ],
            "alsalam": [
                "Developed CRM web applications in React.js.",
                "Built a ride-booking mobile app in React Native.",
                "Optimized performance and state management, and refined the UI/UX across both products.",
            ],
        },
        full=["saleem", "tfc", "chirpbyte", "kroolo", "alsalaam"],
        compact=["nexgen", "skip2beat", "health"],
        skills=[
            ("Frontend", "React.js, Next.js, TypeScript, JavaScript, Tailwind CSS, Ant Design, Material UI, Framer Motion, Formik, Yup"),
            ("Mobile", "React Native, Expo, Expo EAS, Notifee push notifications, App Store and Google Play releases"),
            ("Backend &amp; APIs", "Node.js, Express.js, MongoDB, KeystoneJS, REST APIs, GraphQL"),
            ("State Management", "Redux Toolkit, Redux-Saga, Redux Thunk, React Query, Zustand, Context API"),
            ("Real-time &amp; Cloud", "Socket.io, Pusher, WebSockets, Firebase, Firebase Functions, Supabase, AWS Amplify"),
            ("Integrations", "Ruby on Rails and Laravel APIs, Google Maps, Google / Apple / Facebook sign-in, magic-link sign-in, Stripe, AI chatbot"),
            ("Tools &amp; Platforms", "Git, GitHub, GitLab, Bitbucket, Jira, Trello, Vercel"),
        ],
    ),
    "React_Native": dict(
        title="React Native Developer",
        headline="React Native Developer | Expo · TypeScript · Redux · iOS &amp; Android",
        keywords="React Native Developer, Expo, TypeScript, Redux, iOS, Android, App Store, Google Play, Socket.io, Firebase, Mobile Developer",
        summary="React Native developer with 3+ years of experience building and shipping cross-platform iOS and Android apps. Currently the sole mobile engineer on Saleem Mosque Finder, a live Expo and TypeScript app, responsible for feature delivery, Ruby on Rails API integration, builds and App Store and Google Play submissions. Built real-time mobile features, including live chat, push notifications with Notifee and Google Maps location features, using Socket.io, Pusher and Firebase, with Redux Toolkit and Redux-Saga for state. Supported by web experience in React.js and Next.js and full-stack work on the MERN stack.",
        jobs={
            "contrive": [
                "Sole mobile engineer on Saleem Mosque Finder, an Expo React Native and TypeScript app live on Google Play and the App Store.",
                "Own the mobile release cycle end to end: feature planning, Ruby on Rails API integration, builds and store submissions.",
                "Also build full-stack web features with MongoDB, Express.js, React.js and Node.js; joined as a React.js developer and moved into mobile ownership.",
            ],
            "adroid": [
                "Led front-end development of multiple client mobile and web products in React Native and React.js.",
                "Integrated an AI chatbot and real-time notification features into client products.",
                "Connected front ends to Node.js, KeystoneJS and Laravel backends, working directly with backend teams on API integration and data flow.",
            ],
            "appcrates": [
                "Built and maintained responsive UI components for production React Native and React.js apps.",
                "Restructured state management and component architecture to reduce code complexity and speed up feature delivery.",
            ],
            "alsalam": [
                "Built a ride-booking mobile app in React Native.",
                "Developed CRM web applications in React.js.",
                "Optimized performance and state management, and refined the UI/UX across both products.",
            ],
        },
        full=["saleem", "chirpbyte", "kroolo", "skip2beat", "health"],
        compact=["tfc", "alsalaam", "nexgen"],
        compact_heading="Web Projects",
        skills=[
            ("Mobile", "React Native, Expo, Expo EAS, TypeScript, Notifee push notifications, App Store and Google Play releases"),
            ("State Management", "Redux Toolkit, Redux-Saga, Redux Thunk, React Query, Zustand, Context API"),
            ("Real-time &amp; Cloud", "Socket.io, Pusher, WebSockets, Firebase, Firebase Functions, Supabase, AWS Amplify"),
            ("Integrations", "Ruby on Rails and Laravel APIs, Google Maps, Google / Apple / Facebook sign-in, magic-link sign-in, Stripe, AI chatbot"),
            ("Web Frontend", "React.js, Next.js, JavaScript, Tailwind CSS, Ant Design, Material UI, Framer Motion, Formik, Yup"),
            ("Backend &amp; APIs", "Node.js, Express.js, MongoDB, KeystoneJS, REST APIs, GraphQL"),
            ("Tools &amp; Platforms", "Git, GitHub, GitLab, Bitbucket, Jira, Trello, Vercel"),
        ],
    ),
    "React_JS": dict(
        title="React.js / Next.js Developer",
        headline="React.js / Next.js Developer | TypeScript · Redux · Tailwind CSS · REST APIs",
        keywords="React.js Developer, Next.js Developer, Frontend Developer, TypeScript, JavaScript, Redux Toolkit, Tailwind CSS, REST APIs, MERN, Node.js",
        summary="React.js and Next.js developer with 3+ years of experience building production web applications with TypeScript and JavaScript. Built the TFC Academy certificate platform solo in Next.js and the AlSalaam Tourism booking frontend, and currently builds full-stack web features with React.js, Node.js, Express.js and MongoDB at Contrive Solutions. Works with Redux Toolkit and Redux-Saga for state, Tailwind CSS and Ant Design for UI, and integrates front ends with Node.js, KeystoneJS and Laravel backends. Also ships cross-platform mobile apps in React Native.",
        jobs={
            "contrive": [
                "Build and maintain full-stack web features with React.js, Node.js, Express.js and MongoDB; joined the company as a React.js developer.",
                "Also the sole mobile engineer on Saleem Mosque Finder, an Expo React Native app on Google Play and the App Store, owning its release cycle.",
            ],
            "adroid": [
                "Led front-end development of multiple client web and mobile products in React.js and React Native.",
                "Connected front ends to Node.js, KeystoneJS and Laravel backends, working directly with backend teams on API integration and data flow.",
                "Integrated an AI chatbot and real-time notification features into client products.",
            ],
            "appcrates": [
                "Built and maintained responsive UI components for production React.js and React Native apps.",
                "Restructured state management and component architecture to reduce code complexity and speed up feature delivery.",
            ],
            "alsalam": [
                "Developed CRM web applications in React.js.",
                "Built a ride-booking mobile app in React Native.",
                "Optimized performance and state management, and refined the UI/UX across both products.",
            ],
        },
        full=["tfc", "alsalaam", "nexgen"],
        second_full=["saleem"],
        compact=["chirpbyte", "kroolo"],
        compact_heading="Mobile Projects (React Native)",
        skills=[
            ("Frontend", "React.js, Next.js, TypeScript, JavaScript, responsive UI, reusable component design"),
            ("Styling &amp; UI", "Tailwind CSS, Ant Design, Material UI, Framer Motion, Formik, Yup"),
            ("State Management", "Redux Toolkit, Redux-Saga, Redux Thunk, React Query, Zustand, Context API"),
            ("Backend &amp; APIs", "Node.js, Express.js, MongoDB, KeystoneJS, REST APIs, GraphQL, Axios"),
            ("Real-time &amp; Cloud", "Socket.io, Pusher, WebSockets, Firebase, Firebase Functions, Supabase, AWS Amplify"),
            ("Integrations", "Ruby on Rails and Laravel APIs, Google / Apple / Facebook sign-in, Stripe, AI chatbot"),
            ("Mobile", "React Native, Expo, Expo EAS, App Store and Google Play releases"),
            ("Tools &amp; Platforms", "Git, GitHub, GitLab, Bitbucket, Jira, Trello, Vercel"),
        ],
    ),
}


def links_html(p):
    return " · ".join(f'<a href="{u}">{t}</a>' for t, u in p["links"]) + p.get("links_note", "")


def full_project(p):
    lis = "\n".join(f"    <li>{b}</li>" for b in p["bullets"])
    return f"""<div class="item">
  <div class="head"><div><span class="title">{p['name']}</span> <span class="type">– {p['type']}</span></div><span class="meta">{p['role']}</span></div>
  <p>{p['desc']}</p>
  <p class="links">{links_html(p)}</p>
  <ul>
{lis}
  </ul>
  <div class="tech"><span class="label">Tech:</span> {p['tech']}</div>
</div>
"""


def compact_project(p):
    return f"""<div class="compact">
  <div class="head"><div><span class="title">{p['name']}</span> <span class="type">– {p['type']}</span></div><span class="meta">{p['role']}</span></div>
  <p>{p['compact']}</p>
  <p class="links">{links_html(p)} <span class="tech"> · <span class="label">Tech:</span> {p['tech']}</span></p>
</div>
"""


def job_html(key, bullets):
    t, org, date = JOBS[key]
    lis = "\n".join(f"    <li>{b}</li>" for b in bullets)
    return f"""<div class="item">
  <div class="head"><div><span class="title">{t}</span> · <span class="org">{org}</span></div><span class="meta">{date}</span></div>
  <ul>
{lis}
  </ul>
</div>
"""


def build(name, v):
    jobs = "\n".join(job_html(k, v["jobs"][k]) for k in ("contrive", "adroid", "appcrates", "alsalam"))
    full = "\n".join(full_project(P[k]) for k in v["full"])
    compact = "\n".join(compact_project(P[k]) for k in v["compact"])
    ch = v.get("compact_heading")
    second = "\n".join(full_project(P[k]) for k in v.get("second_full", []))
    compact_block = (f'<h2>{ch}</h2>\n' if ch else "") + second + compact
    skills = "\n".join(f"  <dt>{a}</dt><dd>{b}</dd>" for a, b in v["skills"])
    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Muhammad Luqman Khokhar — {v['title']}</title>
<meta name="author" content="Muhammad Luqman Khokhar">
<meta name="subject" content="CV: {v['title']}">
<meta name="keywords" content="{v['keywords']}">
{STYLE}
</head>
<body>

<header>
  <h1>Muhammad Luqman Khokhar</h1>
  <div class="headline">{v['headline']}</div>
  {CONTACT}
</header>

<h2>Summary</h2>
<p>{v['summary']}</p>

<h2>Professional Experience</h2>

{jobs}
<h2>{'Selected Projects' if not ch else ('Mobile Projects' if name == 'React_Native' else 'Web Projects')}</h2>

{full}
{compact_block}
<h2>Technical Skills</h2>
<dl class="skills">
{skills}
</dl>

{EDUCATION}

</body>
</html>
"""
    src = os.path.join(HERE, f"Muhammad_Luqman_Khokhar_{name}_CV.html")
    open(src, "w").write(html)
    pdf = os.path.join(OUT_DIR, f"Muhammad_Luqman_Khokhar_{name}_CV.pdf")
    subprocess.run(["google-chrome", "--headless=new", "--disable-gpu", "--no-sandbox", "--allow-file-access-from-files",
                    "--no-pdf-header-footer", f"--print-to-pdf={pdf}", f"file://{src}"], check=True, capture_output=True)
    print(pdf)


if __name__ == "__main__":
    for n, v in VARIANTS.items():
        build(n, v)
