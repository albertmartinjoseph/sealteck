# Sealteck corporate redesign

Run `npm install`, then `npm run dev`. Build with `npm run build`; preview with `npm run preview`.

The five business routes, legacy `?page_id=` URLs, sample-page compatibility and a not-found view are implemented. Configure the production host to serve index.html for application routes. The live Sealteck domain has not been changed.

Contact has six fields, accessible client-side validation and a disabled submit button with an explicit availability notice, as requested. No backend integration is active. `src/contact.js` isolates validation and a future submission adapter contract. Do not put service secrets in the client bundle. Email and phone links are available.

See docs/image-sources.md for original asset sources and licence-verification limitations; all imagery is served locally as responsive WebP. See docs/verification.md for QA results. Audit and design-plan documents describe the original research; the current six-field contact form supersedes their earlier four-field implementation plan.
