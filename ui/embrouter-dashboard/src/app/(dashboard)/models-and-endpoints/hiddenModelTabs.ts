// Models + Endpoints tabs hidden from the EmbRouter UI for now. Delete an entry to bring the tab back.
export const HIDDEN_MODEL_TABS: ReadonlySet<string> = new Set([
  "auto-routers",
  "pass-through",
  "retry-settings",
  "model-group-alias",
  "access-group-budgets",
  "price-data",
]);
