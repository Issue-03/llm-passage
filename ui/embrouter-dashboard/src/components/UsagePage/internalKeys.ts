// Placeholder IDs the proxy records in spend data instead of a real virtual key
// (embrouter/constants.py): master-key requests, health checks, the CLI and internal jobs.
// Their spend still counts in the totals; per-key lists leave them out.
export const INTERNAL_KEY_IDS: ReadonlySet<string> = new Set([
  "embrouter_proxy_master_key",
  "embrouter-internal-health-check",
  "embrouter-cli",
  "embrouter_internal_jobs",
]);

export const isInternalKeyId = (keyId: string): boolean => INTERNAL_KEY_IDS.has(keyId);
