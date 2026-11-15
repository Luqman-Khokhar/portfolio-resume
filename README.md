# Muhammad Luqman Khokhar — Portfolio

Personal portfolio of **Muhammad Luqman Khokhar**, a React Native, React.js and MERN stack developer who builds and ships web apps and iOS/Android apps.

**Live site:** [muhammadluqmankhokhar.vercel.app](https://muhammadluqmankhokhar.vercel.app/)
**CV:** [Download (PDF)](https://muhammadluqmankhokhar.vercel.app/CV/Muhammad_Luqman_Khokhar_Universal_CV.pdf)

## Overview

A single-page portfolio built with Vite, React and TypeScript. It presents services, ten shipped products with case-study detail, work experience, an interactive tech-stack keyboard and a contact form. Most of the projects are live on the App Store, Google Play or the web.

### Highlights

- **3D hero.** Floating tech symbols rendered with React Three Fiber, lazy-loaded so the three.js bundle never blocks first paint.
- **Purposeful motion.** Framer Motion animations run on compositor-friendly properties and respect `prefers-reduced-motion`.
- **Crawlable without JavaScript.** At build time a Vite plugin writes the full portfolio content and JSON-LD into `index.html`, so search engines and AI crawlers can read the page without running JavaScript.
- **Single source of truth.** Every section, the crawler-readable snapshot, the structured data and the sitemap are all generated from `src/data/portfolio.ts`.
- **Accessible.** Semantic landmarks, keyboard-operable navigation and project list, visible focus states, and labelled form fields with inline errors.
- **Working contact form.** Submissions are delivered through Web3Forms, with client-side validation.

## Tech stack

| Area | Tools |
|---|---|
| Framework | React 18, TypeScript, Vite |
| Styling | Tailwind CSS, shadcn/ui (Radix UI primitives), lucide-react |
| Motion & 3D | Framer Motion, three.js, React Three Fiber, drei |
| Routing | React Router |
| SEO | Build-time HTML snapshot, JSON-LD (`Person`, `WebSite`, `ProfilePage`), generated `sitemap.xml`, `robots.txt` |
| Hosting | Vercel |

## Getting started

**Requirements:** Node.js 20.19+ or 22.12+, npm.

```sh
git clone https://github.com/Luqman-Khokhar/portfolio-resume.git
cd portfolio-resume
npm install
cp .env.example .env.local   # then add your Web3Forms access key
npm run dev                  # http://localhost:8080
```

### Scripts

| Command | Description |
|---|---|
| `npm run dev` | Start the development server on port 8080 |
| `npm run build` | Production build to `dist/`, including the SEO snapshot and `sitemap.xml` |
| `npm run preview` | Serve the production build locally |
| `npm run lint` | Run ESLint |

### Environment variables

| Variable | Purpose |
|---|---|
| `VITE_WEB3FORMS_KEY` | Web3Forms access key for the contact form. Without it the form shows its error state instead of sending. |

## Project structure

```text
src/
├── data/portfolio.ts      # All site content: identity, services, projects, experience, skills
├── pages/Index.tsx        # Page composition and section order
├── components/site/       # Section components (hero, projects, experience, stack keyboard, contact)
├── components/ui/         # shadcn/ui primitives
├── seo/snapshot.ts        # Crawler-readable HTML, JSON-LD and sitemap generation
└── lib/                   # Smooth scrolling and canvas helpers
public/
├── CV/                    # Downloadable CV PDFs
├── Projects/covers/       # Project screenshots (WebP)
├── fonts/                 # Self-hosted Melodrama, General Sans and JetBrains Mono
└── robots.txt             # Search and AI crawler rules
cv-source/                 # Editable CV sources and the PDF build script
info.md                    # Plain-text content reference that mirrors portfolio.ts
```

## Editing content

1. Update the content in `info.md`, then make the same change in `src/data/portfolio.ts`.
2. Run `npm run build`. The page, the crawler-readable snapshot, the JSON-LD and the sitemap all update together.

## CVs

Three role-specific CVs are generated from one source:

- **Universal:** Full-Stack Software Developer (linked from the site)
- **React Native:** React Native Developer
- **React.js:** React.js / Next.js Developer

To regenerate them, edit `cv-source/build.py` and run the command below. It needs Python 3 and Google Chrome, which prints the PDFs headlessly into `public/CV/`.

```sh
python3 cv-source/build.py
```

## Deployment

The site deploys to Vercel as a static Vite build (`npm run build`, output `dist/`). Set `VITE_WEB3FORMS_KEY` in the Vercel project's environment variables.

## Contact

- **Email:** [mluqmangn@gmail.com](mailto:mluqmangn@gmail.com)
- **LinkedIn:** [linkedin.com/in/mluqmangn](https://www.linkedin.com/in/mluqmangn/)
- **GitHub:** [github.com/Luqman-Khokhar](https://github.com/Luqman-Khokhar)

---

© Muhammad Luqman Khokhar. Content, images and CVs are personal and not licensed for reuse.
