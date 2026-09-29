# OrbitKit

A collection of loading indicators animated with CSS. Dependency-free, themeable, and accessible.

**[Live demo](https://karma1911.github.io/orbitkit/)**

## Install

```bash
npm install orbitkit
```

Or grab `dist/orbitkit.css` / `dist/orbitkit.min.css` directly, or use a CDN:

```html
<link rel="stylesheet" href="https://unpkg.com/orbitkit/dist/orbitkit.min.css">
```

## Usage

1. Include the CSS.
2. Paste a spinner's HTML (see below).
3. Theme it with CSS variables.

```html
<div class="ok-orbit"></div>

<style>
  :root {
    --ok-size: 64px;    /* default: 48px */
    --ok-color: #8b5cf6; /* default: #6366f1 */
    --ok-speed: 1s;      /* default: per-spinner */
  }
</style>
```

Center a spinner with the `ok-center` utility class.

### Import only what you need

```js
import "orbitkit/spinners/ring.css";
import "orbitkit/spinners/dots.css";
```

## Spinners

| Spinner | HTML |
|---|---|
| orbit | `<div class="ok-orbit"></div>` |
| ring | `<div class="ok-ring"></div>` |
| dual-ring | `<div class="ok-dual-ring"></div>` |
| pulse-ring | `<div class="ok-pulse-ring"></div>` |
| comet | `<div class="ok-comet"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></div>` |
| bars | `<div class="ok-bars"><span></span><span></span><span></span><span></span><span></span></div>` |
| dots | `<div class="ok-dots"><span></span><span></span><span></span></div>` |
| typing | `<div class="ok-typing"><span></span><span></span><span></span></div>` |
| grid | `<div class="ok-grid"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></div>` |
| morph | `<div class="ok-morph"></div>` |
| flip | `<div class="ok-flip"></div>` |
| progress | `<div class="ok-progress"><span></span></div>` |

## Accessibility

OrbitKit respects `prefers-reduced-motion`: when a user asks for reduced motion, every spinner automatically slows down instead of stopping entirely, so a loading state is still communicated.

## Browser support

All modern browsers (Chrome, Edge, Firefox, Safari — last 2 versions). Only `transform` and `opacity` are animated, so spinners stay GPU-smooth.

## Contributing

New spinner idea? Please follow these rules so the library stays coherent:

1. One spinner = one file in `src/spinners/`, class prefix `ok-`, keyframes prefixed `ok-`.
2. Self-contained: no shared classes between spinners (only the CSS variables).
3. Animate only `transform` and `opacity`.
4. Theme with `var(--ok-size, …)`, `var(--ok-color, …)`, `var(--ok-speed, …)`.
5. Document the HTML snippet in the file header comment, README table, and demo page.
6. Run `python3 scripts/build.py` and `npm run lint` before opening a PR.

## License

MIT — see [LICENSE](LICENSE). All spinner designs and code are original to this project.
