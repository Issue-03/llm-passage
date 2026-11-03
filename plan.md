# EmbRouter: plan

EmbRouter is a rebranded, trimmed copy of [LiteLLM](https://github.com/BerriAI/litellm) v1.105.0 (MIT), run locally.

**Source:** `~/Documents/litellm-main` (a zip download with no git history)
**Target:** this repo (`llm-passage`)

## Order of work

```
Phase 0  Baseline      copy the kept parts, run as-is under the LiteLLM name, commit
Phase 1  UI rebrand    only what a user sees changes; the backend is untouched
Phase 2  UI trimming   hide or remove pages you don't need, one at a time
Phase 3  Code rebrand  rename package, env vars, DB tables, config keys (later)
Phase 4  Finish        license notice, cleanup, final checks
```

Rule for every phase: the app has to run at the end of it, and each phase gets its own commit (or several), so any step can be undone.

---

## Phase 0: Baseline copy (no renaming)

### Keep

| Path | Why |
|---|---|
| `litellm/` | Python SDK and proxy server (FastAPI) |
| `litellm-proxy-extras/` (without its `dist/`) | Prisma DB migrations and Prisma helpers. The proxy imports it directly (`proxy_cli.py`, `db/prisma_client.py`) and applies the migrations on startup. It's required. |
| `ui/litellm-dashboard/` | Admin UI (Next.js 16 / React 19) |
| `schema.prisma` | DB schema (PostgreSQL) |
| ~~`model_prices_and_context_window.json`~~, ~~`provider_endpoints_support.json`~~ | deleted 2026-11-04; the app and tests use the bundled `embrouter/model_prices_and_context_window_backup.json` and `embrouter/provider_endpoints_support_backup.json` (the 30 providers and `sandbox` endpoint only in the root copy were merged in first) |
| `pyproject.toml`, `uv.lock` | Python build and dependencies (uv). The `Makefile` was deleted 2026-11-04 |
| `docker-compose.yml`, `Dockerfile`, `docker/` | local Postgres (the proxy image is optional; `docker/` holds the Dockerfile's entrypoint scripts) |
| ~~`policy_templates.json`~~ | deleted 2026-11-04: nothing read it; `GET /policy/templates` serves `embrouter/policy_templates_backup.json` |
| `db_scripts/` | optional SQL helpers (spend backfills, views), 44 KB |
| Tool configs: `ruff*.toml`, `pyrightconfig.json`, `.gitignore`, `.dockerignore`, `.npmrc` | lint and build settings |
| `proxy_server_config.yaml`, `.env.example` | sample config |
| `tests/unit/`, `tests/test_litellm/`, plus the root-level helper files `tests/*.py` (the unit tests may import them) | ~2,000 offline unit tests (no network or API keys). Used to check each phase, especially the Phase 3 rename. |
| `LICENSE` | MIT; keeping it is required |

### Drop

- `litellm-rust/`, `tests/test_litellm_rust`: the Rust rewrite, not needed.
- `enterprise/`: under BerriAI's commercial license, and most of its features are also locked behind a paid license check (`_license_check.is_premium()`).
- `gateway/`, `backend/`, `migrations/`: alternative split entry points; we use the single proxy.
- `helm/`, `terraform/`, `packaging/`, `render.yaml`: deployment for other platforms.
- `vscode-extension/`, `cookbook/`, `examples/`: not needed.
- `.circleci/`, `.github/workflows`, `.semgrep`, `cosign.pub`, `codecov.yaml`, `osv-scanner.toml`, `.grype.yaml`, the `*-budget.json` files: upstream CI.
- `AGENTS.md`, `GEMINI.md`, `ARCHITECTURE.md`: upstream contributor docs.
- `litellm-proxy-extras/dist/`: 5.5 MB of old published package files, not used.
- `scripts/`, `ci_cd/`: upstream CI checks, benchmarks, GitHub issue bots.
- `.cargo/`, `rust-toolchain.toml`, `.devcontainer/`, `.githooks/`, `.gitguardian.yaml`, `.git-blame-ignore-revs`, `taplo.toml`: Rust and upstream dev tooling.
- `docker-compose.hardened.yml`, `qa_sticky_session.sh`, `CONTRIBUTING.md`, `security.md`, `codspeed` configs: upstream only.
- Root files that nothing reads at runtime: `router_plugins.json`, `mcp_servers.json`, `whitelisted_bedrock_models.txt`, `license_cache.json`, `model_prices_and_context_window.schema.json`, the root `package.json` / `package-lock.json`.
- `prometheus.yml` and the `prometheus` service in `docker-compose.yml` (optional; can be added back later).
- The rest of `tests/` (about 30 MB): integration, e2e and provider tests that need real API keys, a running proxy, Redis or cloud accounts, plus the Rust and enterprise test harnesses.

### Code changes needed after dropping `enterprise/`

1. **`pyproject.toml`:** remove the `litellm-enterprise` dependency and the `enterprise` workspace member. Point `litellm-proxy-extras` at the local workspace copy instead of the PyPI pin.
2. **`litellm/proxy/response_api_endpoints/endpoints.py:391`:** this `litellm_enterprise` import has no guard. Without the package, a Responses API request with `background: true` fails. Wrap the import in `try/except ImportError` and skip that step.
3. **`GenericAPILogger`:** it's imported inside the same `try` block as the enterprise email loggers ([litellm_logging.py:241](../litellm-main/litellm/litellm_core_utils/litellm_logging.py), `custom_logger_registry.py:118`). Without enterprise, the `generic_api` callback silently does nothing. Move its import out of that block.

Features you lose: email alerts (SendGrid, SMTP, Resend), PagerDuty, audit-log endpoints, managed files and batches, secret-detection and LLM Guard hooks, some SSO extras. You don't lose: routing, virtual keys, teams, budgets, spend tracking, the admin UI, or the standard logging integrations.

### What Phase 0 turned up (done 2026-10-01)

- **Build backend switched from `maturin` to `uv_build`.** Upstream builds the package through the Rust bridge. The Python code works without it: `litellm/rust_bridge/loader.py` returns `None` and falls back to Python.
- **Removed the `litellm/proxy/enterprise` link**, which pointed at the deleted `enterprise/` folder. The `from enterprise.enterprise_hooks…` imports are all guarded.
- **Prisma:** it needs `--extra extra_proxy` plus `uv run prisma generate` (the Dockerfile does the same).
- **Postgres uses host port 5433**, because a local `postgres16` container already uses 5432.
- **Tracked `config.example.yaml`:** `config.yaml` and `.env` are gitignored.
- **`uv` 0.10.9 or newer is required** (`uv self update`).

### Run locally (still named LiteLLM)

See [README.md](README.md) for the exact commands.

### Done when

- The proxy starts and migrations apply.
- `POST /v1/chat/completions` works with a real provider key.
- `/ui` loads, you can log in with the master key, create a virtual key, and see the call in spend logs.
- Committed as **"upstream baseline (LiteLLM v1.105.0, trimmed)"**.

---

## Phase 1: UI rebrand (only what users see)

### How the UI works

- `ui/litellm-dashboard` is a Next.js app built as a static export (`output: "export"`).
- `npm run build` produces `out/`, which is copied to `litellm/proxy/_experimental/out/`. The proxy serves those files at `/ui`.
- For development, `npm run dev` gives hot reload against the proxy on :4000. The exact dev setup (`NEXT_PUBLIC_BASE_URL` / `NEXT_PUBLIC_USE_REWRITES`) gets confirmed during Phase 0.
- The logo comes from the backend: the navbar loads `/get_image`, which serves `litellm/proxy/logo.jpg` and `logo_dark.png`. The favicon comes from `/get_favicon`.

### Brand (from https://emb.global)

**Assets** are in `branding/`:

| File | Size | Use |
|---|---|---|
| `logo-light.png` | 1220×537 | dark text on a light background → replaces `litellm/proxy/logo.jpg` |
| `logo-dark.png` | 1173×516 | white text for dark mode → replaces `litellm/proxy/logo_dark.png` |
| `favicon.ico` | 32×32 | green mark → replaces `_experimental/out/favicon.ico` and the UI source favicon |

**Colors**, sampled from the logo and the site's CSS:

| Role | Color | Source |
|---|---|---|
| Primary (brand green) | `#47BF72` | logo mark and favicon |
| Primary hover / strong | `#16A34A` | site `--green-600` |
| Primary accent | `#22C55E` / `#4ADE80` | site `--green-500` / `--green-400` |
| Primary tint (backgrounds) | `#F0FDF4` | site `--green-50` |
| Logo text / near-black | `#282828` | logo |
| Text | `#0F172A`, secondary `#334155`, muted `#64748B` | site grays |
| Borders / surfaces | `#E2E8F0`, `#F1F5F9`, `#F8FAFC` | site grays |
| Dark mode background | `#05080F`, `#090E1A`, cards `#0E1726` | site `--dark*` |
| Warning / highlight | `#F59E0B` | site `--amber` |

**Font:** the site uses Inter (plus Geist / Geist Mono).

**How it applies:** swap the UI's primary accent (buttons, links, active nav) for the green, and use the slate grays for text and borders. Check the result in both light and dark mode.

### Key rule: the backend still says "litellm" at this point

In `ui/litellm-dashboard/src` there are about 4,600 mentions of "litellm" across about 570 files. **Most are part of how the UI talks to the backend, not text users see.** If we change them in Phase 1, the UI breaks. So in Phase 1 we change only what is visible on screen.

| Change in Phase 1 | Don't touch until Phase 3 |
|---|---|
| Page title and description (`src/app/layout.tsx`: "LiteLLM Dashboard") | Type and table names (`LiteLLM_TeamTable`, `LiteLLM_SpendLogs`, …) |
| Navbar and header text (`🚅 LiteLLM`) | API fields (`litellm_params`, `litellm_model_name`, …) |
| Labels, help text, tooltips, empty states, modals ("What is LiteLLM?", "LiteLLM Model Name", "Thanks for using LiteLLM!", …) | API paths and headers (`x-litellm-*`) |
| Logo and favicon files: replace `litellm/proxy/logo.jpg`, `logo_dark.png` and the favicon, same file names | `assetPrefix: "/litellm-asset-prefix"` in `next.config.mjs` (the backend expects it) |
| Theme colors, if wanted | localStorage keys (`litellm_*`) and the `token` cookie |
| Code snippets shown to users (e.g. "use with the OpenAI SDK"): brand wording only, not import names | Folder name `ui/litellm-dashboard` |
| | Test files' internal identifiers |
| | **Docs links** (219 links to `docs.litellm.ai`): moved to Phase 3, still undecided |

### Method

1. Build a list of candidate lines: `LiteLLM` inside JSX text, and string props (`title`, `label`, `placeholder`, `tooltip`, `description`). Leave `docs.litellm.ai` URLs for Phase 3. Exclude `LiteLLM_*` identifiers and `*Params` types.
2. Review the list, then replace. Visible text becomes **"EmbRouter"**.
3. Update the unit tests that check those visible strings (`*.test.tsx`).
4. `npm run lint && npm run test:unit`, then `npm run build`, copy `out/` into `litellm/proxy/_experimental/out/`, and restart the proxy.
5. Click through every page and check for leftovers:
   `grep -rIn "LiteLLM" src | grep -v "LiteLLM_" | grep -v test` should show only identifiers.

### Done when

- No "LiteLLM" text or logo is visible anywhere in the UI. Docs links still point to `docs.litellm.ai` until Phase 3.
- The UI works the same as in the baseline: login, keys, models, teams, spend, playground.
- Committed.

### Status: done (commit `ada1ef5`, pushed 2026-10-01; you clicked through on 2026-10-03)

- **Text:** 198 source lines in 94 files, plus 88 test lines, rebranded. The rules live in the script `rebrand_ui.py` (session scratchpad), in this order:
  - `🚅 LiteLLM` → `EmbRouter`
  - `LiteLLM Enterprise` → `Enterprise`
  - `LiteLLM Proxy` → `EmbRouter`
  - other visible `LiteLLM` / `Litellm` → `EmbRouter`
  - `a EmbRouter` → `an EmbRouter`
  - code comments skipped
- **Kept on purpose** (the backend matches on them, or they link to real LiteLLM sites):
  - guardrail provider names ("LiteLLM Content Filter", "LiteLLM LLM as a Judge")
  - the `GuardrailsOverview` provider key `LiteLLM`
  - the `PgVector` enum "(LiteLLM Connector)"
  - the routing keyword `LITELLM ESCALATE` and the `LITELLM_API_KEY` env var
  - the "LiteLLM Slack community" / "LiteLLM on GitHub" buttons (Phase 2: hide?)
  - "LiteLLM Docs: …" link text (Phase 3, with the docs links)
- **Colors** (`src/app/globals.css`):
  - light mode: `--primary` / `--sidebar-primary` = `#15803D` (5.0:1 contrast with white text); `--ring` / `--chart-1` = brand `#47BF72`
  - dark mode: primary, ring, chart-1 and sidebar-primary = `#47BF72`, with foreground `#05080F`
- **Logo and favicon:**
  - `litellm/proxy/logo.jpg`: the EMB light logo, flattened onto white, 1000×440
  - `logo_dark.png`: the EMB dark logo
  - `ui/litellm-dashboard/src/app/favicon.ico`: the EMB favicon
- **Checks:**
  - 90 affected UI test files pass (1,606 tests), run with `LANG=en_US.UTF-8`.
  - The machine locale `en-IN` formats numbers as "10,00,000", which breaks 3 tests that don't involve the rebrand.
  - ESLint: 0 errors.
  - `npm run build` succeeds; the output is copied to `_experimental/out/`, and title, logos and favicon are served correctly.
- **Still showing "LiteLLM":** text that comes **from the backend** (guardrail names, some error messages, `litellm_version` labels) until Phase 3. The collapsed sidebar squeezes the logo into a 28px square.

---

## Phase 2: UI trimming (you choose what goes)

Goal: a smaller admin UI with only the pages you use. The backend endpoints stay in place, so nothing breaks.

**Two kinds of change:**
- **Removed:** the code is deleted. Used for things that are LiteLLM-specific or useless here.
- **Hidden:** the code stays and a single setting hides it. Used for features you may want back later; each change below says where its switch lives. Since 2026-10-04 a hidden page's URL shows a 404 instead of the page (see "Hidden pages show 404").

After each batch: tests for the touched files (`LANG=en_US.UTF-8`), lint, build, copy into `litellm/proxy/_experimental/out/`, then you click through.

### Removed (commit `c2afca9`, pushed 2026-10-03)

| Area | What | Where |
|---|---|---|
| Top bar (`DashboardHeader.tsx`) and older navbar (`navbar.tsx`) | Docs link, Blog dropdown, Slack and GitHub buttons, notifications bell | the components themselves are deleted from `components/Navbar/` |
| Sidebar header and both account menus | `v1.105.0` version badge (linked to LiteLLM release notes) | `leftnav.tsx`, `SidebarAccountMenu.tsx`, `UserDropdown.tsx` |
| Account menus | Tier (Standard/Premium), the 🌴 bouncing icon, and the switches Hide New Feature Indicators, Hide All Prompts, Hide Blog Posts, Hide Bouncing Icon and Hide LiteAdmin | `SidebarAccountMenu.tsx`, `UserDropdown.tsx`; the hooks behind the switches are deleted |
| Whole UI | every Beta / New tag (sidebar, Models tabs, chat MCP panel, Create Key agent option, "[BETA]" settings labels, "(beta)" dark-mode tooltip, "MongoDB (BETA)") | the `BetaBadge` component is deleted |
| Whole UI | LiteAdmin AI assistant | `components/liteadmin/` deleted, no longer mounted in `(dashboard)/layout.tsx` |
| Sidebar | Learning Resources (external link to `models.litellm.ai/cookbook`) | `leftnav.tsx`, `page_metadata.ts` |
| Policies page | "Learn more in the documentation ->" (Templates and Policies tabs) and "Learn more about attachments ->" | `policies/_components/index.tsx` |
| Cost Optimization page | the "This is an experimental dashboard / Join the discussion" box (all 4 tabs) | `CostOptimizationView.tsx` |

27 files deleted, including the dead components and hooks and their tests. The affected tests were updated.

### Removed after `c2afca9` (commit `80f1424`, pushed 2026-10-04)

- **Models + Endpoints page:** the "Help shape cost optimization / Share Feedback" banner (it linked to a LiteLLM GitHub discussion). The component `molecules/cost_optimization_feedback_banner.tsx` and its test are deleted.
- **Test fixes:** two tests still expected old text the commits had already changed: "Auto-Routers Beta" on the Models tabs (from `c2afca9`) and the "LiteLLM Parameters" button on agents (from `ada1ef5`). Both are fixed. A wider run of every test in the folders touched since the baseline now passes: 452 files, 6,484 tests.

### Hidden (commit `80f1424`, pushed 2026-10-04; Agent Builder added later, see below)

**Sidebar:** these lists sit at the top of `ui/litellm-dashboard/src/components/leftnav.tsx`; delete an entry to bring it back.
- `HIDDEN_GROUPS`: two whole sections (Observability was here too until 2026-10-12, see below):
  - **Developer Tools** (API Reference, AI Hub, Response Cache, Experimental)
  - **Settings** (Router Settings, Logging & Alerts, Admin Settings, Cost Tracking, UI Theme)
- `HIDDEN_ITEMS`:
  - Platform (was AI Gateway): Agentic, MCP Servers, Skills, Policies, Tools, Guardrails (hidden 2026-10-04, after `8563f42`)
  - Teams & Users (was Access Control): Projects, Organizations, Access Groups, Budgets
  - Observability: Model Leaderboard, Cost Optimization, Logs, Guardrails Monitor (2026-10-12: the section is shown again with **Usage** only)

**What's still in the sidebar:**
- Platform: Virtual Keys, Playground, Models + Endpoints
- Observability: Usage (brought back 2026-10-12; `/ui/usage` works again, the other Observability URLs still 404)
  - Inside Usage, hidden through `USAGE_PAGE_VISIBILITY` in `usage/_components/components/usageVisibility.ts`: the "MCP Server Activity" tab and the "Ask AI" button + chat panel. Removed: the "Get Started by Tracking cost per … here" line in the team/tag views (it linked to `docs.litellm.ai`). Left for Phase 3: the internal team id `litellm-dashboard` filter in `EntityUsage.tsx` (not shown to users).
  - The "Usage View" picker hides Organization, Agent (A2A), Customer and User Agent Activity through `HIDDEN_USAGE_VIEWS` in the same file (`UsageViewSelect` takes a `hiddenOptions` prop; its role tests pass an empty set). Left: Global / Your Usage, Team, Tag, User.
  - Later (2026-10-19) the whole "Usage View" picker was hidden (`USAGE_PAGE_VISIBILITY.viewSelect = false`; `UsagePageView` takes a `showViewSelect` prop, which the view tests set). The page always opens on Global Usage; for a non-admin that is their own usage. The date range picker stays on the right.
  - The Cost / Model Activity / Key Activity / Endpoint Activity tab strip is hidden too (`USAGE_PAGE_VISIBILITY.activityTabs = false`, `showActivityTabs` prop), so the page shows only the Cost view; the other three views are not rendered. Export Data stays on the right.
  - Spend by Provider: the "Show Zero Spend" and "Show Unknown" toggles are hidden (`USAGE_PAGE_VISIBILITY.providerFilterToggles = false`, `showFilterToggles` prop). Both stay off, so zero-spend and "unknown" (failed-to-route) providers are left out of that table.
  - Usage Metrics → Total Tokens breakdown: the "Cache Read Tokens" and "Cache Write Tokens" cards are hidden (`USAGE_PAGE_VISIBILITY.cacheTokens = false`); Input and Output Tokens remain.
  - Per-key lists (Top Virtual Keys in Global and Team/Tag views, Key Activity tab, per-model "Top Virtual Keys by Spend") leave out the proxy's placeholder key ids: `litellm_proxy_master_key` (master-key requests), `litellm-internal-health-check` (health checks), `litellm-cli`, `litellm_internal_jobs`. The list is `INTERNAL_KEY_IDS` in `components/UsagePage/internalKeys.ts`. Their spend still counts in the totals. Phase 3 renames these constants in `litellm/constants.py`; update this list to the new names then.
- Teams & Users: Teams, Internal Users

`Sidebar` accepts `hiddenGroups` / `hiddenItems` props. The sidebar tests pass empty sets so the role and permission rules are still tested against the full menu, and a separate test checks the default hiding.

**Top bar app switcher** (AI Gateway / Chat dropdown): hidden through `showViewSwitcher = false` in `DashboardHeader.tsx`, so the breadcrumb shows only the page name. The Chat page's own navbar keeps the switcher, so you can get back if Chat is ever enabled.

**Playground** (`playground/components/chat_ui/chatConstants.ts`):
- `PLAYGROUND_FIELD_VISIBILITY`: MCP Servers, Vector Store and Policies fields hidden; Guardrails hidden too (2026-10-04, after `3b3875c`). The Compliance tab still has its own guardrails picker.
- `HIDDEN_ENDPOINT_TYPES`: the `/mcp-rest/tools/call` (MCP) and `/v1/a2a/message/send` (agents) endpoints are hidden.
- **Safeguards:**
  - a hidden field's selection always starts empty, ignoring anything saved in the session, so it is never sent in requests or "Get Code" snippets (for MCP this includes the per-server tool limits)
  - a saved MCP or A2A endpoint falls back to `/v1/chat/completions`
- The two MCP-picker tests use `it.skipIf(!PLAYGROUND_FIELD_VISIBILITY.mcpServers)`, so they come back on when the field is shown.

### Recolored (commit `80f1424`, pushed 2026-10-04)

23 elements were styled with the theme's **info** color (LiteLLM's blue) instead of **primary**, so the Phase 1 theme change missed them. They now use the brand green:
- **Buttons:** Add Guardrail, plus Playground chat/compliance, MCP submissions and the credential modal
- **Controls:** the guardrail toggle's "on" state, checkboxes, active tab underlines
- **Progress markers:** step circles and dots, progress bars
- **Chat:** the user's chat bubbles

Info-blue was **kept** where it means something rather than being branding: "running"/"reachable" status dots, loading pulses, trace timeline bars, the personal-vs-team marker, and the light-blue info notice boxes. (Later the `--info` color itself became teal, see "Look and feel".)

### Look and feel (done 2026-10-04)

Mostly theme values, so the whole UI follows without touching page layouts.

- **Fonts** (`app/layout.tsx`, `--font-sans` / `--font-mono` in `globals.css`): Inter → **Plus Jakarta Sans** for text, **JetBrains Mono** for keys, IDs and code.
- **Neutrals** (`globals.css`): the cool blue-grays now have a faint green tint (hue ~155–160), in light and dark mode.
- **Surfaces:** off-white page background with white cards; the sidebar is a light green-gray (deep green-black in dark mode). Dark-mode cards sit slightly above the page. Bare form fields use `--card` so they stay white on the off-white page.
- **Corners:** `--radius` 0.5rem → 0.75rem.
- **Accent:** `--info` (LiteLLM blue, used ~610 times for links, active tabs, tags and focus borders) → deep teal, distinct from the success green. Info alerts are teal too.
- **Compliance tab** (`complianceUI/ComplianceUI.tsx`): hard-coded indigo chips and `ring-blue-500` focus rings → the `info` accent.
- **Sidebar section names** (`leftnav.tsx`): AI GATEWAY → **PLATFORM**, ACCESS CONTROL → **TEAMS & USERS** (the breadcrumb follows).
- **Sidebar toggle:** panel icons → hamburger (`Menu`), same icon in both states.
- **Selected sidebar item** (`shared/Sidebar.tsx`): grey fill + left green bar → light green pill with green text and icon, semibold; the keyboard focus ring is now a thin inset line.
- **Account menu** moved from the sidebar footer to the top-right of the top bar (`DashboardHeader.tsx`), via `placement="header"` on `SidebarAccountMenu` (compact avatar + name trigger, opens downward). The sidebar footer now shows only the admin usage card.
- **Playground:** the Agent Builder (Experimental) tab is hidden through `HIDDEN_PLAYGROUND_TABS` in `playground/page.tsx`; `?tab=agent-builder` falls back to Chat. The Compliance tab was added to the same list later (after `fe646cf`), so the Playground shows only Chat and Compare.

Tests added or updated for the header account menu, the Agent Builder tab, the sidebar active style and the breadcrumb names.

### Removed upstream links on visible pages (2026-10-04)

- **"Need Help?"** links to LiteLLM's GitHub issues: Add Model, Auto Router tab, Add Credential and Reuse Credentials (the buttons stay right-aligned).
- **"Talk to our team"** (a LiteLLM sales Calendly page) on the Auto Router: View limits popover, exhausted routing choices, and the blocked-allowance alert. `AUTO_ROUTER_CONTACT_URL` / `AutoRouterContactLink` are deleted; the limits and messages themselves stay.
- **Playground → Code Interpreter:** the "Request support for other providers" link (the OpenAI-only note stays).
- **Create Key → Logging Settings tooltip:** the `www.litellm.ai/enterprise` link (the note stays).
- **Kept:** the Azure base-model link to LiteLLM's `model_prices_and_context_window.json`, as a useful reference.
- **Left for later:** upstream GitHub, `litellm.ai` and `models.litellm.ai` links on hidden pages (Search Tools, Transform Request, Tags, Vector Stores, Guardrails, Organizations, Cost Optimization, the deprecation banner, the Chat app), plus the 181 `docs.litellm.ai` links (Phase 3).

### Hidden pages show 404 (2026-10-04)

- `isHiddenRoute()` in `leftnav.tsx` treats any dashboard URL whose page is not in the visible sidebar as hidden. It is built from the same `HIDDEN_GROUPS` / `HIDDEN_ITEMS` lists, so un-hiding a sidebar entry also makes its URL work again. `change-password` (and the root `/ui/`) always stay reachable.
- `(dashboard)/layout.tsx` calls Next.js `notFound()` for those URLs, so they show Next's built-in "404 | This page could not be found." page, the same one unknown URLs get. No custom 404 page.
- Links on visible pages that point at hidden pages (for example "view logs") now land on the 404.
- Not covered: the separate apps outside the dashboard (`/ui/chat`, `/ui/model_hub`, `/ui/model_hub_table`, `/ui/mcp`, `/ui/connect`).

### Proxy startup output (2026-10-04)

- `proxy_server.py` no longer prints the LITELLM ASCII banner or the feedback box ("Thank you for using LiteLLM! - Krrish & Ishaan", "Give Feedback / Get Help" links) at startup. `generate_feedback_box()`, its messages and the `LITELLM_DONT_SHOW_FEEDBACK_BOX` check are deleted.
- `common_utils/banner.py` stays for now: the `litellm-proxy` client CLI and the CLI SSO success page still use `LITELLM_BANNER` (rename in Phase 3).
- Still in the log until Phase 3: the `LiteLLM Proxy` logger name and "LiteLLM: Proxy initialized with Config" lines.
- The DB migration progress lines from `litellm_proxy_extras` ("Preparing the Prisma CLI toolchain", "Found 192 migrations", "prisma migrate deploy stdout ...") are now debug output: `litellm_proxy_extras/_logging.py` defaults to `WARNING` instead of `INFO`. Set `LITELLM_LOG=INFO` (or `DEBUG`) to see them; warnings and errors from failed or stuck migrations still print.

### `embrouter` start command (2026-10-04)

- `pyproject.toml` `[project.scripts]` has `embrouter = "litellm:run_server"` next to `litellm`, so the proxy starts with `uv run --env-file .env embrouter --config config.yaml --port 4000` (README and `config.example.yaml` updated). Needs a `uv sync` once to install the command.
- `litellm` (and `lite`, `litellm-proxy`) still work; Phase 3 removes or renames them.
- `trusted_proxy_ranges: []` added to `general_settings` in `config.example.yaml`, so the startup warning about it is gone (clients connect directly).

### Login page (2026-10-04)

- Hidden through `LOGIN_PAGE_VISIBILITY` in `ui/litellm-dashboard/src/app/login/loginVisibility.ts` (set a flag to `true` to bring it back):
  - `ssoButton`: the "Login with SSO" button (disabled or active).
  - `defaultCredentialsHint`: the "Default Credentials" card (admin / `MASTER_KEY` hint and the docs link).
- The SSO auto-redirect and the "SSO is enabled" notice still follow the server config; they only appear once SSO is configured.
- The two SSO button tests use `it.skipIf(!LOGIN_PAGE_VISIBILITY.ssoButton)`; a new test checks both are hidden.

### Add Model fields (2026-10-04)

Hidden through `ADD_MODEL_FIELD_VISIBILITY` in `ui/litellm-dashboard/src/components/add_model/addModelVisibility.ts` (set a flag to `true` to bring it back):
- `teamByokSwitch`: "Team-BYOK Model" (lock a model + credential to one team). It needs a LiteLLM Enterprise licence (`premiumUser`), so it was always disabled with an "enterprise-only, upgrade to premium" tooltip. The "Select Team" dropdown that follows it goes too.
- `knowledgeBases`: Advanced Settings → "Attached Knowledge Bases (RAG)" (the Vector Stores page is hidden).
- `guardrails`: Advanced Settings → "Guardrails" (the Guardrails page is hidden).

The model **edit** form (`ModelInfoEditForm.tsx`) still shows its own Guardrails / knowledge-base fields. Team-BYOK tests use `skipIf`; new tests check the fields are hidden.

### Models + Endpoints tabs (2026-10-04)

Hidden through `HIDDEN_MODEL_TABS` in `ui/litellm-dashboard/src/app/(dashboard)/models-and-endpoints/hiddenModelTabs.ts` (delete an entry to bring a tab back): Auto-Routers, Pass-Through Endpoints, Model Retry Settings, Model Group Alias, Model Access Group Budgets, Price Data Reload. Left for an admin: Deployed Models, Add Model, LLM Credentials, Health Status. The page tests mock the list as empty so the role rules are still tested on the full tab set; one test checks the default hiding.

### Upgrade banner removed (2026-10-19)

- The "The latest version is v1.106.0 … Your current version is v1.105.0" banner is gone, along with what fed it: the proxy's `/get/latest_release_info` endpoint (`ui_crud_endpoints/latest_release_endpoints.py`), which fetched `https://api.github.com/repos/BerriAI/litellm/releases/latest`. So the proxy no longer contacts GitHub for this.
- Deleted: `UpgradeBanner.tsx`, `hooks/latestRelease/useLatestReleaseInfo.ts`, `utils/versionUtils.ts` (only the banner used it), and their tests; the route is out of `_types.py` and its route-check test.
- Left: the generated API types (`lib/http/schema.d.ts`) still list the endpoint until they are regenerated in Phase 3.
- To track upstream security fixes, check https://github.com/BerriAI/litellm/releases by hand.

### Parked (2026-10-26, revisit after Phase 3)

- Done 2026-11-04: the "Environment-credential login is enabled" and "No Redis configured" banners are removed from the UI (`EnvCredentialLoginWarningBanner`, `NoRedisWarningBanner` deleted; `layout.tsx` no longer renders them). The backend still reports the flags in `/health/readiness`; nothing shows them.

- Policies → Attachments still shows an "Enterprise Feature Notice" box.
- About 50 hard-coded `blue-*` / `indigo-*` classes remain on pages outside the Compliance tab; fix as they're spotted.
- Later: delete the code for hidden pages that stay unused, then run `npm run knip` for leftovers.

---

## Phase 3: Code rebrand (done 2026-10-31 on branch `phase-3-code-rebrand`, pushed, not merged into `main` yet)

**Decisions (2026-10-26):** names as proposed (display "EmbRouter"; package, CLI and DB `embrouter`; env vars `EMBROUTER_*`); **remove** all docs links; **one** fresh migration and a fresh database. Work happens in this folder (the proxy on :4000 from `main` stops working here until Phase 3 lands); checkpoint commits per step on the branch, no push until asked.

Measured scale: ~170,000 mentions (`litellm` 139k, `LiteLLM` 19k, `Litellm` 5k, `LITELLM` 3k, plus `liteLLM`, the typo `LITTELM`, `lite-llm`), ~7,000 paths, 939 `docs.litellm.ai` links, 537 `github.com/BerriAI/...` links.

**Step order** (each step is a checkpoint commit):
0. Baseline: record the failing tests and type errors before any change (kept outside the repo).
1. External references first, before the rename can turn them into fake domains: make the bundled cost map / beta headers / autorouter presets the only source (no BerriAI GitHub fetch), remove the license, `api.litellm.ai`, logo and model-map calls, and remove every `docs.litellm.ai` and `github.com/BerriAI/...` link.
2. Pre-scan for collisions (e.g. the existing `embrouter` script entry next to `litellm`) and third-party import paths that contain "litellm".
3. Path renames only (`git mv`), committed alone so git keeps file history.
4. Content rewrite with a case-sensitive map, then a case-insensitive leftover scan.
5. Database: rename the Prisma models, squash the 193 migration folders into one, prove nothing is lost (old migrations vs new one on scratch DBs, `pg_dump --schema-only` compared), new `embrouter` database in the existing container (nothing deleted).
6. Regenerate `uv.lock`, Prisma client, UI lockfile and build; update local `.env` / `config.yaml` names.
7. Verify against the baseline: tests, `git grep -i litellm` (only LICENSE / NOTICE), proxy chat + UI login on a fresh DB. Add `NOTICE`.

**Progress:**
- Step 0 (baseline) done: 67,467 pass, 712 fail + 416 errors before any Phase 3 change (missing local Postgres tools, timeouts, enterprise-only tests). Kept in `~/Documents/llm-passage-phase3-baseline/`. Two test files (`proxy/db/test_pgbouncer.py`, `unit/gateway/`) leave helper processes behind and hang full runs; run them separately.
- Step 1 (external references) done and verified (commit `ddf7e4e`):
  - No remote fetches from BerriAI: empty source URLs mean the bundled cost map, Anthropic beta headers, auto-router presets, blog feed and policy templates are used.
  - Removed: online license check (`license.litellm.ai`), hosted budget default (`api.litellm.ai`), LiteLLM logo and support email in alert emails, model-map link in the startup message.
  - All `docs.litellm.ai` and `github.com/BerriAI/...` links removed (backend messages, docstrings, comments, UI); leftover half-sentences tidied; UI links with meaningful text keep the text, generic docs/help links and buttons removed.
  - "File a bug on GitHub" log link: off unless `LITELLM_BUG_REPORT_ISSUE_URL` is set.
  - Berri AI example emails and support contacts replaced; copyright lines kept.
  - Found: `ui/litellm-dashboard/package.json` / `package-lock.json` are git-ignored (upstream `.gitignore`), so a clean clone can't build the UI. Fix during the rename.
  - Verified 2026-10-26: full run (without the two hanging files) 68,519 passed vs 67,467 in the baseline; the 22 failures not in the baseline all pass when re-run alone (flaky under parallel load). `test_pgbouncer.py` run alone: same 9 failures as the baseline. `tests/unit/gateway` can't be collected (imports a `gateway` module not in this copy), as in the baseline.
- Step 2 (pre-scan) done 2026-10-31:
  - No third-party package or import path contains "litellm" (only our own `litellm`, `litellm_proxy_extras`, and the not-installed `litellm_enterprise`, which stays not installed under its new name). No npm dependency either.
  - No name collisions: renaming every identifier never produces a name that already exists (only the display word "EmbRouter", already in the UI). Path dry run: 74 moves, 0 collisions. Content dry run: 5,079 files.
  - No unusual spellings beyond the map (no "Lite LLM", "lite_llm", etc.). No binary tracked files contain the name.
  - Fixed before the rename: removed the duplicate `litellm` start command (it would have become a second `embrouter` key in `pyproject.toml`) and the `lite` alias; removed `[project.urls]` (upstream homepage) in both pyprojects; remaining `litellm.ai` URLs (mock request URLs → `http://localhost`, OpenRouter/Vercel attribution default → empty, app name "EmbRouter"); email footer social/website links; "trial key / pricing" links in two backend messages and four UI notes; Docker images now build locally as `litellm:local` (becomes `embrouter:local`) instead of pulling `docker.litellm.ai` / `ghcr.io/berriai`.
  - `ui/litellm-dashboard/package.json` and `package-lock.json` are now tracked (removed from `.gitignore`; the lockfile only uses registry.npmjs.org). `next-env.d.ts` stays ignored (generated).
  - Left as is: test fixtures with fake domains (`litellm.com`, `proxy.litellm.ai`, `test.litellm.ai`, `berri.ai` emails, Bing/MCP fixtures quoting `BerriAI/litellm`). Both sides of each assertion are renamed together, so they stay consistent.
  - For step 5: Postgres names are already at the 63-character limit (`LiteLLM_DailyUserSpend_..._key` etc.); Prisma truncates the longer `EmbRouter_` names itself in the squashed migration, and no code refers to index or constraint names.
  - For steps 3–4: run them back to back before testing. Until `uv sync` (step 6) the venv still installs the `litellm` package (`litellm.pth`), so tests only work after step 6, or after a `uv sync` right after step 4.
- Step 3 (paths) done 2026-10-31, commit `c65a63a`: 6,977 files moved by 74 `git mv`s, nothing else in the commit.
- Step 4 (contents) done 2026-10-31, commit `4da5cdd`: 5,079 files, ~165k replacements. Leftover scan: only `plan.md` (by design) and the lockfiles (step 6). After it: `uv sync --frozen --extra proxy --extra extra_proxy` (plain `uv sync` drops the proxy extras).
- Step 5 (database) done 2026-10-31, commit `1437fef4`:
  - The 192 migration folders are replaced by one, `20261031000000_init`: `prisma migrate diff --from-empty` from `schema.prisma`, plus hand-written SQL for what `schema.prisma` can't express (2 `NOT NULL` array columns on `EmbRouter_ShadowEvalJob`, the `LOWER(user_email)` index, 2 partial indexes).
  - Proof: old migrations and the new one applied to scratch DBs `squash_old` / `squash_new`, `pg_dump --schema-only` compared ignoring column order: identical except 9 index names (Postgres/Prisma cut them at 63 characters differently; same columns; no code uses index names). The old migrations insert no data.
  - New container `embrouter_db` (port 5433, volume `embrouter_postgres_data`, database `embrouter`). Compose treated it as the same `db` service and **removed the old `litellm_db` container**; its data is still in the volume `litellm_postgres_data` (not deleted), so it can be reattached with a `postgres:16` container if ever needed.
- Step 6 done 2026-10-31, commit `4e0c401c`: `uv.lock` (same package versions, new names), `package-lock.json`, Prisma client, UI rebuilt into `embrouter/proxy/_experimental/out` (no "litellm" left in the bundle). Local `.env` keys now `EMBROUTER_*` and `DATABASE_URL` points at `/embrouter`; `config.yaml` uses `embrouter_params` etc. Pre-rename copies of both in `~/Documents/llm-passage-phase3-baseline/`.
  - Checked: proxy starts with `uv run --env-file .env embrouter --config config.yaml --port 4000`, applies `20261031000000_init`, 87 `EmbRouter_*` tables (0 `litellm`), chat (normal + streaming) works, headers are `x-embrouter-*`, UI login and pages work.
- Step 7 (verify) 2026-10-31:
  - First full run hung at 95% for 48 minutes (pytest-timeout's default signal method can't interrupt some blocking calls). Re-runs use `--timeout-method=thread`, `-n 6`, `-v`: ~8 minutes, no hang.
  - Squashed migration made re-runnable to match the project's migration rules (`IF NOT EXISTS` on tables and indexes, `DO $$` guards on constraints and the enum). Re-applying it to a migrated DB gives 0 errors; schema still identical to the old migrations. `_PRE_GUARD_MIGRATIONS` in the extras tests is now empty.
  - Rename side effects fixed in tests:
    - base64 fixtures that decode to `litellm:` / `litellm_proxy:` IDs: re-encoded with `~/Documents/llm-passage-phase3-baseline/scripts/rename_b64.py`, plus fixtures split over several string lines by hand. The longer name can make standard base64 need `=` padding where the old one didn't.
    - signed JWT fixtures: `test_jwt_user_api_key_auth_builder_enforce_rbac` now generates its RSA key and signs its token at test time (audience `api://EmbRouter_Proxy-dev`) instead of a pre-signed Azure token; the placeholder token in `test_jwt_non_admin_team_route_access` (never verified) has its claims re-encoded.
    - length-sensitive asserts (container id `< 110`, masked-exception 50-char prefix), a streamed path split across chunks.
    - tests that read old migration folders: one now reads `20261031000000_init`, one (backfill of pre-migration rows) removed.
  - Local git-ignored files the rename script skips (it only touches tracked files): three `_*secret_config.yaml` files and `tests/.../test_mcp_server_manager.py`, renamed in place.
  - Expected until merge: `tests/unit/proxy/test_db_schema_changes.py` compares `schema.prisma` with `main` and reports every renamed table as "removed".
  - Final backend run: 68,529 passed, 701 failed + 392 errors (baseline 67,467 / 712 / 416). Failures not in the baseline: 12 pass when re-run alone (flaky under parallel load) and `test_db_schema_changes.py` (expected until merge). Log: `~/Documents/llm-passage-phase3-baseline/pytest_step7b.txt`.
  - UI run (vitest): 11,248 passed, 12 failed. 3 were tests still looking for links removed in step 1 (guardrail pricing request, available-teams docs link): fixed in `50c19ef`. The other 9 are in `AddModelPanel.integration.test.tsx` and fail on the pre-rename code too (most likely since the Phase 2 Add Model field hiding): open.
  - Signed JWT test token replaced in `fa4e771` (see above).
- Found in step 7: the optional `semantic-router` extra depends on the PyPI `litellm` package. Before the rename our own package satisfied it; now installing that extra would download upstream LiteLLM next to EmbRouter, and it is the only `litellm` left in `uv.lock`. Not installed by default (`proxy`, `extra_proxy`). Proposed: drop the extra (auto-router, semantic guard and semantic tool filter are unused and already handle the library being missing). **Done 2026-11-04:** extra removed from `pyproject.toml` and the three Dockerfiles, `docker/install_auto_router.sh` deleted; `uv.lock` no longer contains `litellm`.
- Backup: branch `llm-passage-backup` = `main` before Phase 3 (`0ad6991`), pushed 2026-10-31.

**How to run after Phase 3:**
```bash
docker compose up -d db                                            # embrouter_db, port 5433, database embrouter
uv sync --extra proxy --extra extra_proxy                          # after pulling new code (plain `uv sync` drops the proxy extras)
uv run --env-file .env embrouter --config config.yaml --port 4000
```
UI at http://localhost:4000/ui, user `admin`, password `EMBROUTER_MASTER_KEY` from `.env`. The `litellm` command is gone. The database is fresh: models, keys and teams created in the UI before Phase 3 are not in it.

**Open after Phase 3:**
- Fix or update the 9 `AddModelPanel` integration tests.
- Merge `phase-3-code-rebrand` into `main` (then `test_db_schema_changes.py` passes again).
- Cleanup when no longer needed: scratch databases `squash_old` / `squash_new` in `embrouter_db`; old volume `litellm_postgres_data`; baseline worktree `~/Documents/llm-passage-baseline-wt`.

Original outline:

1. **Rename paths, deepest first:**
   - `litellm/` → `embrouter/`
   - `litellm_proxy_extras` → `embrouter_proxy_extras`
   - `ui/litellm-dashboard` → `ui/embrouter-dashboard`
   - `litellm_core_utils` → `embrouter_core_utils`, and so on.
2. **Rewrite contents with a script**, text files only, most specific first: `LiteLLM` → `EmbRouter`, `LITELLM` → `EMBROUTER`, `litellm` → `embrouter`, plus odd spellings. This covers:
   - Python imports and CLI entry points (`embrouter`, `embrouter-proxy`)
   - 263 `LITELLM_*` env vars
   - YAML keys `litellm_params` / `litellm_settings`
   - 85 `x-litellm-*` headers
   - the UI's remaining internal identifiers, `assetPrefix`, and localStorage keys
3. **Outside services** get their own handling, not the blanket rename:
   - Model price list: it's normally fetched from BerriAI's GitHub, so switch to the bundled local file.
   - Telemetry and license checks that call BerriAI: turn them off or remove them. (The GitHub latest-release check is already removed, Phase 2.)
   - `docker.litellm.ai` URLs: remove.
   - **Docs links:** remove them all (decided 2026-10-26).
4. **Database:**
   - Rename the 87 `LiteLLM_*` Prisma models to `EmbRouter_*` in all 3 copies of `schema.prisma` and in the raw SQL (65 Python files).
   - Squash the 193 migrations into one starting migration (`prisma migrate diff --from-empty`).
   - This needs a **fresh local database**, so drop the Phase 0–2 dev database.
5. **Startup and log output:**
   - Decide the final log level for the migration progress lines (made debug-only in Phase 2; `LITELLM_LOG` becomes `EMBROUTER_LOG`), and rename the `litellm_proxy_extras` / `LiteLLM Proxy` logger names.
   - Rename the Postgres database from `litellm` to `embrouter` (`DATABASE_URL`, `docker-compose.yml`), together with the fresh database above.
   - Remove the `litellm` start command, keeping `embrouter`; rename `lite` / `litellm-proxy`.
6. **Regenerate** `uv.lock` and the Prisma client, rebuild the UI, and update `docker-compose.yml`, `.env.example`, the Makefile and the README.

**Done when:**
- `grep -ri litellm` finds nothing outside `LICENSE` and `NOTICE`.
- `import embrouter` works.
- 87 `EmbRouter_*` tables exist.
- Chat completions (streaming and non-streaming) work.
- The UI flows work.
- The unit tests pass, or any failures are listed.

---

## Phase 4: Finish

- **License:** `NOTICE` was added in Phase 3; `LICENSE` and `NOTICE` were then removed on 2026-11-04 (`8cdd2f8`).
- **Makefile:** deleted 2026-11-04 (most targets called the missing `scripts/` folder) together with `ruff-strict.toml` and its test; not replaced. The run commands go in the README instead.
- **README:** a "run locally" guide.

## Trade-off

After Phase 3, merging upstream LiteLLM changes is basically impossible. Security fixes would have to be ported by hand. Until Phase 3, upstream diffs can still be applied fairly easily, since only UI text has changed.

## Open questions

1. **Name casing:** answered 2026-10-26: OK as proposed.
2. **Logo:** answered. The EMB Global logo is used as is (Phase 1).
3. **Docs links (Phase 3):** answered 2026-10-26: remove them all.
4. **Phase 3 database:** answered 2026-10-26: yes, one migration and a fresh database.
