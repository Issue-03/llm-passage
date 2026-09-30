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
| `model_prices_and_context_window.json`, `provider_endpoints_support.json` | model price and capability data |
| `pyproject.toml`, `uv.lock`, `Makefile` | Python build and dependencies (uv) |
| `docker-compose.yml`, `Dockerfile`, `docker/` | local Postgres (the proxy image is optional; `docker/` holds the Dockerfile's entrypoint scripts) |
| `policy_templates.json` | read at runtime by `proxy/management_endpoints/policy_endpoints` |
| `db_scripts/` | optional SQL helpers (spend backfills, views), 44 KB |
| Tool configs: `ruff*.toml`, `pyrightconfig.json`, `.gitignore`, `.gitattributes`, `.dockerignore`, `.npmrc` | lint and build settings |
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

### Status (2026-10-01): done except a click-through check

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

1. **List the pages.** I'll produce a list of every left-nav item and its route (from `src/components/leftnav.tsx` and `src/app/(dashboard)/`) so you can mark each one keep / hide / remove.
2. **Hide first.** Remove the nav entry and redirect the route. This is cheap and easy to undo.
3. **Remove later.** Once a hidden page has gone unused for a while, delete its route folder and components. Then run `npm run knip` to find leftover unused code.
4. **After each batch:** lint, unit tests, build, click through, commit.

Likely candidates to hide (you decide): guardrails garden, MCP servers, agents, vector stores, prompt management, batches and files, audit logs (they need enterprise anyway), onboarding and "what's new" banners, the model hub, and admin settings for enterprise-only features.

---

## Phase 3: Code rebrand (later)

Done as a separate project once the UI is settled. Scale: about 90,000 mentions and 383 paths.

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
   - Telemetry and license checks that call BerriAI: turn them off or remove them.
   - `docker.litellm.ai` URLs: remove.
   - **Docs links** (219 in the UI, plus backend help text): remove them, or point them at your own docs site. **Undecided.**
4. **Database:**
   - Rename the 87 `LiteLLM_*` Prisma models to `EmbRouter_*` in all 3 copies of `schema.prisma` and in the raw SQL (65 Python files).
   - Squash the 193 migrations into one starting migration (`prisma migrate diff --from-empty`).
   - This needs a **fresh local database**, so drop the Phase 0–2 dev database.
5. **Regenerate** `uv.lock` and the Prisma client, rebuild the UI, and update `docker-compose.yml`, `.env.example`, the Makefile and the README.

**Done when:**
- `grep -ri litellm` finds nothing outside `LICENSE` and `NOTICE`.
- `import embrouter` works.
- 87 `EmbRouter_*` tables exist.
- Chat completions (streaming and non-streaming) work.
- The UI flows work.
- The unit tests pass, or any failures are listed.

---

## Phase 4: Finish

- **License:** keep `LICENSE` with Berri AI's MIT copyright (required), and add a `NOTICE` saying "EmbRouter is derived from LiteLLM (MIT)".
- **Makefile targets:**
  - `make db`, `make install`, `make migrate`, `make run`
  - `make ui-dev`, `make ui-build` (which also copies the build into the proxy)
- **README:** a "run locally" guide.

## Trade-off

After Phase 3, merging upstream LiteLLM changes is basically impossible. Security fixes would have to be ported by hand. Until Phase 3, upstream diffs can still be applied fairly easily, since only UI text has changed.

## Open questions

1. **Name casing:** display name "EmbRouter"; package, CLI and DB `embrouter`; env vars `EMBROUTER_*`. OK?
2. **Logo:** do you have logo files (light and dark) and a favicon, or should I make a text placeholder?
3. **Docs links (Phase 3):** remove them, or point them at your own docs site? Still open.
4. **Phase 3 database:** OK to squash the migrations and start with a fresh local database?
