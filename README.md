# Local development

Run `npm install`, then `npm run dev`. Build with `npm run build`; preview with `npm run preview`.

The five business routes, legacy `?page_id=` URLs, sample-page compatibility and a not-found view are implemented. Configure your host to serve index.html for application routes. No live-domain cutover is configured.

## Contact delivery

Copy `.env.example` to `.env.local` and set an owner-controlled HTTPS `VITE_CONTACT_ENDPOINT` accepting JSON `{firstName,lastName,email,message}`. It must allow your deployed origin, validate requests, rate limit and deliver mail server-side. Never put secrets in a VITE variable. Only a successful HTTP response displays submission success. Until configured, the page explicitly offers email/phone contact instead of online delivery. End-to-end delivery remains unverified.

## Images

See docs/image-sources.md for every original source and the rights verification limitation. Original downloads are retained; components use optimized responsive WebP assets. Owner licence confirmation is required before public launch.
