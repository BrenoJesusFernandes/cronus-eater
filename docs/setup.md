# Set Up Environment

## Basic Check List

- Make sure you have `python >= 3.7.1` installed.
- Install poetry: `pip install poetry`
- Install the project dependencies: `poetry update`
- Enter the virtual environment: `poetry shell`
- Run all tests: `poe test_all`
- Do you want to add a new dependency? `poetry add --dev foo-pkg`

## VS Code Configuration

To configure auto code format on auto save with blue and isort, install the extension [Run on Save](https://marketplace.visualstudio.com/items?itemName=pucelle.run-on-save) and make sure your `.vscode\settings.json` file is like below:

```json
{
    "editor.formatOnSave": true,
    "files.autoSave": "afterDelay",
    "python.formatting.provider": "black",
    "python.formatting.blackPath": "absolute_path_to_your_poetry_virtual_environment\\Scripts\\blue",
    "[python]": {
        "editor.codeActionsOnSave": {
            "source.organizeImports": true
        },
    },
    "runOnSave.commands": [
        {
            "match": ".py",
            "command": "editor.action.organizeImports",
            "runIn": "vscode"
        },
        {
            "match": ".py",
            "command": "editor.action.formatDocument",
            "runIn": "vscode"
        }
    ],
}
```