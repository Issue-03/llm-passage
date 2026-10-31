import { EmbRouterParams, ModelData, ModelInfo, PerSecondCostTier } from "@/components/model_dashboard/types";

const PER_SECOND_TIER_KEY = /^output_cost_per_second_(.+)$/;

export const perSecondCostTiers = (modelInfo: Record<string, unknown> | null | undefined): PerSecondCostTier[] =>
  Object.entries(modelInfo ?? {}).flatMap(([key, value]) => {
    const resolution = PER_SECOND_TIER_KEY.exec(key)?.[1];
    return resolution !== undefined && typeof value === "number" ? [{ resolution, cost: value }] : [];
  });

interface RawEmbrouterParams extends EmbRouterParams {
  output_cost_per_second?: number;
}

interface RawModelInfo extends ModelInfo {
  input_cost_per_token?: number | null;
  output_cost_per_token?: number | null;
  output_cost_per_second?: number;
  max_tokens?: number;
  max_input_tokens?: number;
  [key: string]: unknown;
}

export interface RawModel {
  model_name: string;
  embrouter_params: RawEmbrouterParams;
  model_info: RawModelInfo;
  [key: string]: unknown;
}

const costPerMillionTokens = (costPerToken: number | null | undefined): string | null =>
  costPerToken == null ? null : (Number(costPerToken) * 1000000).toFixed(2);

const resolveProvider = (
  embrouterModelName: string | null | undefined,
  customLlmProvider: string | null | undefined,
  getProviderFromModel: (model: string) => string,
): string => {
  if (!embrouterModelName) return "-";
  if (customLlmProvider) return customLlmProvider;
  const splitModel = embrouterModelName.split("/");
  return splitModel.length === 1 ? getProviderFromModel(embrouterModelName) : splitModel[0];
};

const transformModel = (rawModel: RawModel, getProviderFromModel: (model: string) => string): ModelData => {
  const model: RawModel = JSON.parse(JSON.stringify(rawModel));
  const embrouterParams = model.embrouter_params;
  const modelInfo = model.model_info;

  return {
    ...model,
    provider: resolveProvider(embrouterParams.model, embrouterParams.custom_llm_provider, getProviderFromModel),
    input_cost: costPerMillionTokens(modelInfo?.input_cost_per_token),
    output_cost: costPerMillionTokens(modelInfo?.output_cost_per_token),
    output_cost_per_second: embrouterParams.output_cost_per_second ?? modelInfo?.output_cost_per_second ?? null,
    output_cost_per_second_tiers: perSecondCostTiers(modelInfo),
    embrouter_model_name: embrouterParams.model,
    max_tokens: modelInfo?.max_tokens,
    max_input_tokens: modelInfo?.max_input_tokens,
    api_base: embrouterParams.api_base,
    cleanedEmbrouterParams: Object.fromEntries(
      Object.entries(embrouterParams).filter(([key]) => key !== "model" && key !== "api_base"),
    ),
  };
};

export const transformModelData = (
  rawModelData: { data?: RawModel[] | null } | null | undefined,
  getProviderFromModel: (model: string) => string,
): { data: ModelData[] } => {
  if (!rawModelData?.data) return { data: [] };

  return { data: rawModelData.data.map((rawModel) => transformModel(rawModel, getProviderFromModel)) };
};
