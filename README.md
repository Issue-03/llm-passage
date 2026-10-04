# llm-passage

## Prerequisites

- Docker Desktop (running)
- [uv](https://docs.astral.sh/uv/) 0.10.9 or newer (`uv self update`). It downloads Python 3.12 by itself.
- Node 24, only if you want to rebuild the admin UI (not needed to run it)

## First-time setup

```bash
# 1. Config files (both are gitignored)
cp .env.example .env                 # then fill in the values below
cp config.example.yaml config.yaml

#    In .env, set at least:
#      LITELLM_MASTER_KEY=sk-...     # your admin password for the API and UI
#      LITELLM_SALT_KEY=sk-...       # encrypts stored credentials; never change it later
#    Generate each with: echo "sk-$(openssl rand -hex 24)"

# 2. Database: Postgres 16 on localhost:5433
docker compose up -d db

# 3. Python dependencies and the Prisma DB client
uv sync --extra proxy --extra extra_proxy
uv run prisma generate --schema=./schema.prisma
```

## Run

```bash
docker compose up -d db              # if it isn't already running
uv run --env-file .env embrouter --config config.yaml --port 4000
```

On first start the proxy applies the DB migrations, which takes about 15 seconds. (`embrouter` is the new name for the start command; the old `litellm` command still works until the Phase 3 code rename.)

- **API:** http://localhost:4000 (OpenAI-compatible, e.g. `/v1/chat/completions`)
- **Admin UI:** http://localhost:4000/ui. Log in with username `admin` and your `LITELLM_MASTER_KEY` as the password.
- **API docs:** http://localhost:4000/docs

Quick test with the offline `mock-gpt` model from `config.example.yaml`:

```bash
curl localhost:4000/v1/chat/completions \
  -H "Authorization: Bearer $LITELLM_MASTER_KEY" -H "Content-Type: application/json" \
  -d '{"model":"mock-gpt","messages":[{"role":"user","content":"hi"}]}'
```

To use a real model, add its API key to `.env` (e.g. `OPENAI_API_KEY`) and uncomment the example in `config.yaml`, or add it from the UI under **Models**.

## Stop

- Proxy: `Ctrl+C`
- Database: `docker compose stop db`. Data is kept in the `litellm_postgres_data` volume. `docker compose down -v` deletes it.

## Rebuild the admin UI

After changing anything in `ui/litellm-dashboard/src`:

```bash
cd ui/litellm-dashboard
nvm use                 # Node 24 from .nvmrc
npm ci                  # first time only
npm run build
rm -rf ../../litellm/proxy/_experimental/out/* && cp -r out/* ../../litellm/proxy/_experimental/out/ && rm -rf out
```

Then restart the proxy. For UI tests, run only the files you touched (the full suite is very large), with a US locale:
`LANG=en_US.UTF-8 npx vitest run <test files>`.

## Tests

Offline unit tests (no API keys or network needed):

```bash
uv run pytest tests/unit tests/test_litellm -n 8 -q -m "not requires_rust_extension" \
  --ignore=tests/test_litellm/proxy/test_custom_proxy.py
```

`test_custom_proxy.py` is skipped because it starts the proxy with `SERVER_ROOT_PATH=/my-custom-path`, which rewrites the built UI files in `litellm/proxy/_experimental/out/` in place and breaks the UI (unstyled page, assets 404).

## License

MIT, see [LICENSE](LICENSE).
