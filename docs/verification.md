# Verification report

17 November 2026

- Production Vite build passed.
- Automated Chromium checks passed for 11 routes at 375, 768 and 1440 px (33 combinations): one h1, no horizontal overflow, all images decoded, no JavaScript page errors.
- Mobile navigation link, Escape dismissal and FAQ expansion passed.
- Desktop and phone full-page screenshots reviewed for design consistency and image placement.
- Old WordPress page IDs tested, including sample-page compatibility. Readable routes and unknown-page view tested.
- Original copy preserved in content data; original editing suffix removed from final FAQ. Contact destinations corrected to Sealteck's displayed details.
- Contact form delivery remains incomplete: no production endpoint or mail credentials supplied; explicit email/phone fallback is shown. No enquiry was sent.
- Image rights are not independently verified; all reused images come from the source site. See image-sources.md.
- These checks are not a full accessibility audit. Screen-reader behavior, actual message delivery and live-domain redirects remain unverified.

Reproduce: npm run build; npm run dev; node scripts/check-browser.mjs (uses installed Chrome on Windows).
