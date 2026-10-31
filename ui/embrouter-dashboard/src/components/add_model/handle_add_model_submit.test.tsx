import { describe, expect, it, vi } from "vitest";
import { prepareModelAddRequest } from "./handle_add_model_submit";

vi.mock("../networking", () => ({
  modelCreateCall: vi.fn(),
}));

describe("prepareModelAddRequest", () => {
  it("returns deployment data for the most basic form", async () => {
    const formValues = {
      model_mappings: [
        {
          public_name: "Public Model",
          embrouter_model: "embrouter/public",
        },
      ],
      model_name: "custom-model-name",
      base_model: "gpt-4",
      team_id: "team-123",
      model_access_group: ["group-1"],
      input_cost_per_token: "2000000",
      output_cost_per_token: "1000000",
    };

    const deployments = await prepareModelAddRequest({ ...formValues }, "token", null);

    expect(deployments).toHaveLength(1);
    const [deployment] = deployments!;
    expect(deployment.modelName).toBe("Public Model");
    expect(deployment.embrouterParamsObj.model).toBe("custom-model-name");
    expect(deployment.embrouterParamsObj.input_cost_per_token).toBe(2);
    expect(deployment.embrouterParamsObj.output_cost_per_token).toBe(1);
    expect(deployment.modelInfoObj.base_model).toBe("gpt-4");
    expect(deployment.modelInfoObj.access_groups).toEqual(["group-1"]);
    expect(deployment.modelInfoObj.team_id).toBe("team-123");
  });

  it("uses a lowercase fallback for unrecognized custom providers", async () => {
    const fallbackValues = {
      model_mappings: [
        {
          public_name: "Petals Model",
          embrouter_model: "petals/model",
        },
      ],
      model_name: "petals/model",
      custom_llm_provider: "Petals",
    };

    const deployments = await prepareModelAddRequest({ ...fallbackValues }, "token", null);

    expect(deployments).toHaveLength(1);
    const [deployment] = deployments!;
    expect(deployment.embrouterParamsObj.custom_llm_provider).toBe("petals");
  });

  it("ignores embrouter_credential_name inside EmbRouter Params JSON", async () => {
    const formValues = {
      model_mappings: [
        {
          public_name: "Public Model",
          embrouter_model: "embrouter/public",
        },
      ],
      model_name: "custom-model-name",
      embrouter_credential_name: "selected-credential",
      embrouter_extra_params: JSON.stringify({
        embrouter_credential_name: "from-json",
        timeout: 5,
      }),
    };

    const deployments = await prepareModelAddRequest({ ...formValues }, "token", null);

    expect(deployments).toHaveLength(1);
    const [deployment] = deployments!;
    expect(deployment.embrouterParamsObj.embrouter_credential_name).toBe("selected-credential");
    expect(deployment.embrouterParamsObj.timeout).toBe(5);
  });

  it("keeps embrouter_credential_name from EmbRouter Params JSON when no credential is selected", async () => {
    const formValues = {
      model_mappings: [
        {
          public_name: "Public Model",
          embrouter_model: "embrouter/public",
        },
      ],
      model_name: "custom-model-name",
      embrouter_extra_params: JSON.stringify({
        embrouter_credential_name: "from-json",
        timeout: 5,
      }),
      embrouter_credential_name: null,
    };

    const deployments = await prepareModelAddRequest({ ...formValues }, "token", null);

    expect(deployments).toHaveLength(1);
    const [deployment] = deployments!;
    expect(deployment.embrouterParamsObj.embrouter_credential_name).toBe("from-json");
    expect(deployment.embrouterParamsObj.timeout).toBe(5);
  });

  it.each([
    ["OpenAI", "openai/*"],
    ["Azure_AI_Studio", "azure_ai/*"],
    ["Petals", "petals/*"],
  ])("composes wildcard names for the all-model selection", async (custom_llm_provider, wildcardModel) => {
    const formValues = {
      model_mappings: [],
      model: "all-wildcard",
      custom_llm_provider,
    };

    const deployments = await prepareModelAddRequest({ ...formValues }, "token", null);

    expect(deployments).toHaveLength(1);
    const [deployment] = deployments!;
    expect(deployment.modelName).toBe(wildcardModel);
    expect(deployment.embrouterParamsObj.model).toBe(wildcardModel);
  });
});
