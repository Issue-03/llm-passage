import pytest


@pytest.mark.asyncio
async def test_claude_code_plugin_table_schema_exists():

    with open("schema.prisma", "r") as f:
        schema = f.read()
    assert "EmbRouter_ClaudeCodePluginTable" in schema, (
        "EmbRouter_ClaudeCodePluginTable model missing from schema.prisma - "
        "this causes AttributeError on all /claude-code/plugins endpoints"
    )

    with open("embrouter/proxy/schema.prisma", "r") as f:
        proxy_schema = f.read()
    assert (
        "EmbRouter_ClaudeCodePluginTable" in proxy_schema
    ), "EmbRouter_ClaudeCodePluginTable model missing from embrouter/proxy/schema.prisma"
