// Placeholder IDs the proxy records in spend data instead of a real virtual key
// (litellm/constants.py): master-key requests, health checks, the CLI and internal jobs.
// Their spend still counts in the totals; per-key lists leave them out.
export const INTERNAL_KEY_IDS: ReadonlySet<string> = new Set([
  "litellm_proxy_master_key",
  "litellm-internal-health-check",
  "litellm-cli",
  "litellm_internal_jobs",
]);

export const isInternalKeyId = (keyId: string): boolean => INTERNAL_KEY_IDS.has(keyId);
