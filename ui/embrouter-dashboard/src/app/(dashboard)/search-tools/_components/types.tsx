import type { components } from "@/lib/http/schema";

export type SearchToolEmbRouterParams = components["schemas"]["SearchToolEmbRouterParams"];

export interface SearchToolInfo {
  description?: string | null;
}

export interface SearchTool {
  search_tool_id?: string;
  search_tool_name: string;
  embrouter_params: SearchToolEmbRouterParams;
  search_tool_info?: SearchToolInfo;
  created_at?: string;
  updated_at?: string;
  is_from_config?: boolean;
}

export interface SearchToolsResponse {
  search_tools: SearchTool[];
}

export interface AvailableSearchProvider {
  provider_name: string;
  ui_friendly_name: string;
}

export interface AvailableSearchProvidersResponse {
  providers: AvailableSearchProvider[];
}
