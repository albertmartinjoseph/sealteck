# Sealteck redesign plan

Status: research and implementation plan. No application has been implemented, built, browser-tested or deployed at this stage.

## Direction

Create a premium industrial corporate website using Sealteck's verified blue `#2E489E`, orange `#F69220`, existing textual wordmark and original business content. Translate the reference's editorial scale, photographic emphasis, spaciousness and restrained motion into an original composition. Do not copy Aramco's layouts, imagery, typography assets, logo or copy.

Lead with the existing infrastructure-protection headline. Explain Sealteck's specialist installation work, then its process and sector applications, and make the route to an enquiry obvious. Avoid statistics, certification badges, customer logos and testimonials because none were verified.

## Design system

- Brand blue `#2E489E`: principal brand surfaces and links. Orange `#F69220`: restrained highlights, decorative rules and suitable dark-text buttons. Check actual color pairs against WCAG AA; do not assume orange supports white body text.
- White and light neutral editorial surfaces with dark charcoal body text. Deep overlays derived from the brand blue may support readable text over photography.
- Preserve the SEALTECK wordmark. Use Oswald selectively for headings/wordmark and a locally served Roboto family for body text if original font licensing/source files are available. System sans-serif fallback; no unverified brand font dependency.
- Large fluid headings, readable body measure around 60–70 characters, consistent line-height and generous vertical space. Use a repeatable spacing scale and shared button, link, field, card and section styles.
- Full-width imagery with deliberate responsive crops. Original industrial images must be individually inspected before hero selection. Avoid fabricated project labels. Decorative imagery receives empty alt text; informative images receive accurate descriptions.
- Hover transitions approximately 150–250 ms; one-time subtle GSAP reveals. Honor `prefers-reduced-motion`; content remains visible if JavaScript animation fails. Use native scrolling and avoid scroll hijacking.

## Information architecture and URL preservation

| Page | Preferred readable route | Compatibility |
| --- | --- | --- |
| Home | `/` | `/?page_id=9`, `/home` |
| About Us | `/about-us` | `/?page_id=111` |
| Services | `/service` | `/?page_id=158`, optional `/services` alias |
| Sectors We Serve | `/sectors-we-serve` | `/?page_id=169` |
| Contact Us | `/contact-us` | `/?page_id=143` |
| Existing Sample Page | `/sample-page` | `/?page_id=2`; no main-navigation placement |

Use explicit query-ID resolution before normal route rendering. Set page-specific titles, descriptions and canonical URLs. Configure production server SPA fallback for direct loads. Do not claim HTTP 301 redirects unless host-level redirects are actually configured; client navigation compatibility is a separate behavior.

Sample Page retains the existing generic content in a compatibility view, marked noindex and excluded from business navigation. No content from it enters business copy.

## Page compositions

### Home

1. Transparent desktop navigation over a full-height industrial photograph, with the existing headline and supporting text. Provide Services and Contact calls to action. Use a compact opaque navigation state after scrolling and a readable mobile menu.
2. Spacious About split section pairing original introduction with original imagery and an About link.
3. Service-process overview with the four verified service stages and links to the complete Services page.
4. Original six Quality Services benefits, presented as a concise editorial grid without losing their text.
5. Image-led overview of all six sector groups, linking to identifiable sections on Sectors We Serve.
6. Original Latest Projects gallery without invented names, outcomes or customer claims; image provenance remains flagged in the audit.
7. Original three FAQs in accessible disclosure elements, with only the stray editing suffix corrected.
8. Existing reliable-sealing enquiry CTA and shared footer with verified contacts and page links.

### About Us

Image-led introduction, full original company narrative and mission, four reasons-to-choose sections, and existing enquiry CTA. Preserve warranty and quality text without adding certification or duration claims.

### Services

Existing service introduction followed by four clearly numbered stages, retaining every measurement, installation and testing detail. Use inspected original imagery where relevant. End with a Contact action.

### Sectors We Serve

Original introduction, six section anchors and six substantial image/text modules. Retain every original application bullet. Alternate layouts selectively for rhythm and use consistent image treatment; do not imply that illustrative images prove delivered projects.

### Contact Us

Verified phone, email and London address with correct `tel:` and `mailto:` targets. Keep the four original form fields, visible labels, accessible validation and useful submit/error states. Render success only after a confirmed backend response. Do not add an unverified office map pin or social profile links.

## Technical architecture

Use React with Vite, Tailwind CSS, React Router, Lucide React and GSAP, as requested. Keep content separate from layout and use a small reusable component set.

```text
src/
  app/                 Router, legacy URL resolution, layout, route metadata
  components/          Header, MobileMenu, Footer, Button, Section, Image,
                       ServiceCard, SectorCard, FAQ, ContactForm
  pages/               Home, About, Services, Sectors, Contact, Sample, NotFound
  content/             Verified copy, navigation, sector/service data, assets
  hooks/               Reduced-motion-aware reveals, route focus/scroll
  styles/              Tailwind entry, design tokens, base and focus styles
public/
  images/              Downloaded, inspected and optimized Sealteck assets
docs/                  Audit, plan, verification notes and source evidence
```

Local implementation should use the supplied workspace. A separately hosted preview may be prepared only after an actual working build; do not replace the live Sealteck domain or assume control of its DNS.

## Form integration dependency

First inspect the existing Elementor submission contract without sending an enquiry. Establish whether the original backend is suitable for cross-origin use and whether access is available to maintain its security and recipient settings. If unsuitable, connect an owner-supplied form service or server endpoint with secrets stored server-side. Never expose mail-service credentials in the Vite bundle.

Until a backend is available and delivery is tested, form integration remains incomplete. Implementing the visual form, validation and email/phone links can proceed independently. Request the necessary backend details when the integration choice requires them; do not simulate successful delivery.

## Implementation sequence

1. Research: capture source pages, preserve original copy and assets, identify brand and integration issues. Completed for the publicly discovered content; rendered visual checks remain outstanding.
2. Foundation: scaffold the requested Vite stack, tokens, shared layout, route metadata, legacy URL handling and content modules.
3. Assets: download and inspect original images; generate appropriate responsive variants and preserve aspect ratios. Select the hero from verified suitable originals.
4. Homepage: implement the complete composition and shared navigation/footer; check readable responsive layouts before extending the system.
5. Inner pages: implement About, Services, Sectors, Contact and existing sample-page compatibility with original content.
6. Integration: wire the confirmed backend, validate submission states and perform an authorized delivery test.
7. Verification: run a production build and meaningful route/content/link checks; inspect desktop, tablet and mobile layouts and keyboard behavior. Fix observed defects.
8. Handoff: report actual implemented routes, build results, verified interactions and remaining limitations. Any preview publication must use the built artifact; live-domain cutover is a separate operation.

## Acceptance checks

- All five business pages contain their preserved original substantive content; no invented business claims or Aramco assets.
- All old page IDs and readable routes resolve on initial load and navigation; unknown routes display a useful 404 page.
- Navigation and mobile menu work with keyboard, touch, Escape and predictable focus; skip link, landmarks and visible focus are present.
- Layouts work at representative 375, 768, 1024 and 1440 px widths, including landscape and 200% zoom; no horizontal overflow or clipped text.
- One descriptive primary heading per business page, proper hierarchy, sufficient contrast, labeled fields and announced form errors/status.
- Reduced motion disables nonessential animation. Route changes restore sensible focus and scroll behavior.
- Images have dimensions, responsive sources, suitable compression and lazy loading below the fold. The hero receives loading priority.
- Internal links and contact targets are checked. Placeholder social links are excluded from active controls until real destinations are verified.
- Production build succeeds; direct route hosting, unique metadata, canonical tags and a business-page sitemap are checked.
- Contact success/error behavior and actual message delivery are verified before calling integration complete.

## Current outstanding information

No screenshot or content upload is needed for the successfully accessed business pages. Backend configuration and delivery verification are still needed for the contact form. Higher-resolution original imagery or an official image logo may improve the final result if the owner has assets beyond those publicly available; do not invent substitutes for official branding.
