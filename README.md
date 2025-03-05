# roblox template
[![continuous integration](https://github.com/magicchex/roblox-template/actions/workflows/ci.yaml/badge.svg)](https://github.com/magicchex/roblox-template/actions/workflows/ci.yaml)

My roblox workflow
# Setup
## Configure GitHub Workflows
### `ci.yaml`
Add two variables:
1. `UNIVERSE_ID` : `number`
2. `PLACE_ID` : `number`

Add a secret:
1. `PLACE_PUBLISHING_KEY` : `string`
   * This will be your [api key](https://create.roblox.com/docs/reference/cloud/universes-api/v1).
## Install toolkit manager
Install *(Recommended)* [Rokit](https://github.com/rojo-rbx/rokit) or [aftman](https://github.com/LPGhatguy/aftman) as your tool manager on your system.
### Rokit
1. Run `rokit update` to update tools before development.

2. Run `rokit install` and agree to trust the tools found in `rokit.toml`.
### Aftman
1. TODO

## Visual Studio Code
Install the recommended extensions found in `extensions.json`

### Configure `Moonwave.toml`
Refer to [Moonwave](https://github.com/evaera/moonwave?tab=readme-ov-file#moonwave)
### Configure `default.project.json`
Refer to Rojo's [Project Format](https://rojo.space/docs/)
