Additional files for the proxy. Reduces the size of the main embrouter package.

Currently, only stores the migration.sql files for embrouter-proxy.

To install, run:

```bash
uv add embrouter-proxy-extras
```
OR 

```bash
uv tool install 'embrouter[proxy]' # installs embrouter-proxy-extras and other proxy dependencies
```

To use the migrations, run:

```bash
embrouter --use_prisma_migrate
```
