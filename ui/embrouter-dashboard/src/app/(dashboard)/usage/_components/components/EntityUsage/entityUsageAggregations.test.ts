import { describe, expect, it } from "vitest";
import type { DailyData, KeyMetricWithMetadata, SpendMetrics } from "@/components/UsagePage/types";
import { getGlobalTopKeys } from "./entityUsageAggregations";

const metrics = (spend: number): SpendMetrics => ({
  spend,
  prompt_tokens: 0,
  completion_tokens: 0,
  total_tokens: 0,
  api_requests: 1,
  successful_requests: 1,
  failed_requests: 0,
  cache_read_input_tokens: 0,
  cache_creation_input_tokens: 0,
});

const keyEntry = (spend: number, key_alias: string | null = null): KeyMetricWithMetadata =>
  ({ metrics: metrics(spend), metadata: { key_alias, team_id: null } }) as KeyMetricWithMetadata;

const day = (api_keys: Record<string, KeyMetricWithMetadata>): DailyData =>
  ({
    date: "2026-10-01",
    metrics: metrics(0),
    breakdown: { models: {}, model_groups: {}, mcp_servers: {}, providers: {}, entities: {}, api_keys },
  }) as DailyData;

describe("getGlobalTopKeys", () => {
  it("leaves the proxy's placeholder key ids out of Top Virtual Keys", () => {
    const top = getGlobalTopKeys(
      [
        day({
          embrouter_proxy_master_key: keyEntry(9),
          "embrouter-internal-health-check": keyEntry(8),
          "sk-hash-1": keyEntry(1, "real-key"),
        }),
      ],
      5,
    );

    expect(top.map((k) => k.api_key)).toEqual(["sk-hash-1"]);
  });
});
