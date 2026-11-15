// Build-time HTML for crawlers that do not run JavaScript. Everything here is read from
// src/data/portfolio.ts, so it never drifts from what the React app renders. React's
// createRoot replaces it on mount; without JavaScript it is the readable page.
import {
  about,
  contact,
  experience,
  hero,
  identity,
  navItems,
  platformLabel,
  process,
  projectLinks,
  projects,
  projectsIntro,
  services,
  servicesIntro,
  skills,
} from "../data/portfolio.ts";

const ESCAPES: Record<string, string> = { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" };
const esc = (value: string) => value.replace(/[&<>"']/g, (c) => ESCAPES[c]);

const list = (items: string[]) => `<ul>${items.map((item) => `<li>${esc(item)}</li>`).join("")}</ul>`;
const link = (href: string, label: string, external = false) =>
  `<a href="${esc(href)}"${external ? ' rel="noopener" target="_blank"' : ""}>${esc(label)}</a>`;

const absolute = (path: string) => new URL(path, identity.site).href;

function projectArticle(project: (typeof projects)[number]) {
  const links = projectLinks(project);
  return `<article>
<h3>${esc(project.title)}</h3>
<p><strong>${esc(project.type)}</strong> · ${esc(platformLabel[project.platform])} · ${esc(project.context)}</p>
<p>${esc(project.description)}</p>
${project.featured ? `<p><strong>Problem:</strong> ${esc(project.featured.problem)}</p><p><strong>Solution:</strong> ${esc(project.featured.solution)}</p><p><strong>Outcome:</strong> ${esc(project.featured.outcome)}</p>` : ""}
${project.contribution ? `<p><strong>My role:</strong> ${esc(project.contribution)}</p>` : ""}
<h4>Features</h4>
${list(project.features)}
<p><strong>Built with:</strong> ${esc(project.tech.join(", "))}</p>
${links.length ? `<p>${links.map((l) => link(l.href, `${project.title}: ${l.label}`, true)).join(" · ")}</p>` : ""}
${project.note ? `<p>${esc(project.note)}</p>` : ""}
<img src="${esc(project.cover)}" alt="${esc(project.coverAlt)}" width="1600" height="1000" loading="lazy" decoding="async">
</article>`;
}

export function renderSnapshot() {
  return `<div class="seo-snapshot">
<header>
<p><a href="/">${esc(identity.fullName)}</a> · ${esc(identity.role)}</p>
<nav aria-label="Sections"><ul>${navItems.map((item) => `<li>${link(item.href, item.name)}</li>`).join("")}</ul></nav>
</header>
<main>
<section id="home">
<p>${esc(hero.heading)}</p>
<p>${esc(hero.eyebrow)}</p>
<h1>${esc(hero.headline)}</h1>
<p>${esc(hero.sub)}</p>
<p>${esc(hero.proof)} · ${esc(identity.availability)}</p>
<p>${link(hero.primaryCta.href, hero.primaryCta.label)} · ${link(hero.secondaryCta.href, hero.secondaryCta.label)}</p>
<img src="${esc(identity.portrait)}" alt="Illustrated portrait of ${esc(identity.fullName)} in a denim jacket" width="777" height="907">
</section>
<section id="about">
<h2>About</h2>
<p>${esc(about.statement)}</p>
${about.paragraphs.map((p) => `<p>${esc(p)}</p>`).join("")}
<ul>${about.facts.map((f) => `<li>${esc(f.label)}: ${esc(f.value)}</li>`).join("")}</ul>
</section>
<section id="services">
<h2>${esc(servicesIntro.heading)}</h2>
<p>${esc(servicesIntro.sub)}</p>
${services
  .map(
    (s) => `<article>
<h3>${esc(s.title)}</h3>
<p>${esc(s.line)}</p>
<h4>What I deliver</h4>
${list(s.deliver)}
<h4>What it solves</h4>
<p>${esc(s.solves)}</p>
<h4>What to expect</h4>
<p>${esc(s.expect)}</p>
</article>`,
  )
  .join("")}
</section>
<section id="projects">
<h2>${esc(projectsIntro.title)}</h2>
<p>${esc(projectsIntro.sub)}</p>
${projects.map(projectArticle).join("")}
</section>
<section id="process">
<h2>How a project runs</h2>
<ol>${process.map((step) => `<li><strong>${esc(step.title)}:</strong> ${esc(step.text)}</li>`).join("")}</ol>
</section>
<section id="experience">
<h2>Experience</h2>
${experience
  .map(
    (job) => `<article>
<h3>${esc(job.role)}, ${esc(job.company)}</h3>
<p>${esc(job.period)}</p>
<p>${esc(job.summary)}</p>
${list(job.points)}
</article>`,
  )
  .join("")}
</section>
<section id="skills">
<h2>Technical skills</h2>
${skills.map((group) => `<h3>${esc(group.category)}</h3><p>${esc(group.items.join(", "))}</p>`).join("")}
</section>
<section id="contact">
<h2>${esc(contact.heading)}</h2>
<p>${esc(contact.intro)}</p>
<ul>
<li>Email: ${link(`mailto:${identity.email}`, identity.email)}</li>
<li>Phone: ${link(identity.phoneHref, identity.phone)}</li>
<li>Location: ${esc(identity.location)} (${esc(identity.availability)})</li>
<li>GitHub: ${link(identity.github, "Luqman-Khokhar", true)}</li>
<li>LinkedIn: ${link(identity.linkedin, "mluqmangn", true)}</li>
<li>Resume: ${link(identity.cv, `Download ${identity.fullName}'s CV (PDF)`)}</li>
</ul>
</section>
</main>
</div>`;
}

/** Schema.org graph: the site, the profile page it is, and the person it is about. */
export function structuredData() {
  const site = identity.site;
  const person = `${site}#person`;
  const current = experience[0];
  return {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "WebSite",
        "@id": `${site}#website`,
        url: site,
        name: identity.fullName,
        description: hero.sub,
        inLanguage: "en",
        publisher: { "@id": person },
      },
      {
        "@type": "ProfilePage",
        "@id": `${site}#profile`,
        url: site,
        name: `${identity.fullName}, ${identity.role}`,
        isPartOf: { "@id": `${site}#website` },
        mainEntity: { "@id": person },
        inLanguage: "en",
      },
      {
        "@type": "Person",
        "@id": person,
        name: identity.fullName,
        alternateName: "Luqman Khokhar",
        jobTitle: identity.role,
        description: `${about.statement} ${about.paragraphs[0]}`,
        url: site,
        image: absolute(identity.portrait),
        email: `mailto:${identity.email}`,
        telephone: identity.phone.replace(/\s/g, ""),
        address: { "@type": "PostalAddress", addressLocality: "Daska", addressCountry: "PK" },
        worksFor: { "@type": "Organization", name: current.company },
        sameAs: [identity.github, identity.linkedin],
        knowsAbout: [...new Set(skills.filter((g) => g.category !== "UI / UX").flatMap((g) => g.items))],
        makesOffer: services.map((s) => ({
          "@type": "Offer",
          itemOffered: { "@type": "Service", name: s.title, description: s.line },
        })),
      },
    ],
  };
}

/** Pages listed in sitemap.xml. The site is a single page; the CV is the one other document worth indexing. */
export const sitemapPaths = ["/", identity.cv];

export function renderSitemap(lastmod: string) {
  const urls = sitemapPaths
    .map((path) => `  <url>\n    <loc>${esc(absolute(path))}</loc>\n    <lastmod>${lastmod}</lastmod>\n  </url>`)
    .join("\n");
  return `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n${urls}\n</urlset>\n`;
}
