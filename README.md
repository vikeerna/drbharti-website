# Dr. Bharti Surgery website

Static HTML/CSS/JavaScript website hosted on Hostinger at https://drbhartisurgery.com/.

## Source and deployment

The September 2026 baseline was imported from the owner's Hostinger download. GitHub's earlier single-page version was dated May 2026. The original backup is retained privately by the owner; no private records belong in this repository.

The repository has no GitHub Actions deployment workflow and GitHub Pages is disabled. Hostinger-side Git/webhook configuration has not been verified. A commit or merge is not proof of deployment.

Deploy only the website files: root HTML, CSS, JavaScript, favicon, robots.txt, sitemap.xml, `.htaccess`, and `images/`. Do not upload `.git`, documentation or tests into the public web root. Keep a Hostinger backup before replacing live files. Preserve unrelated subdomains, application folders and hosting configuration. Verify the live home page, Bariatu page, contact routes and Garhwa confirmation message after deployment.

## Editing

Read `AGENTS.md` and `.ai/CURRENT.md`. Preserve existing treatment URLs. Keep content, metadata and structured data consistent. The Bariatu hours are carried forward from the supplied website; do not invent fees or changes to hours. Garhwa attendance requires explicit confirmation; do not generate guaranteed future dates from a calendar rule.

## Analytics

The existing GA4 property is retained. `site.js` records contact clicks without form contents or destination query strings. The consultation form emits one `whatsapp_click`, not a second form key event. Local preview does not send events. GA4 admin settings, enhanced-measurement behaviour and key-event definitions require a separate account audit. Clicks are not confirmed bookings. Automated form-interaction collection should be reviewed/disabled in GA4 before using sensitive forms; clinical content must never be included in analytics parameters.

## Local preview

Serve this folder with a local static HTTP server, then open `index.html` and `bariatu-surgery-clinic-ranchi.html`. Run `python tests/check_site.py` for local link, schema, sitemap and contact checks. JavaScript contact-event tests use `node tests/contact-events.test.cjs`.
