# Set Up Environment

## Basic Check List

- Make sure you have `python >= 3.7.1` installed.
- Install poetry: `pip install poetry`
- Install the project dependencies: `poetry update`
- Enter the virtual environment: `poetry shell`
- Run all tests: `pytest`
- Do you want to add a new dependency? `poetry add --dev foo-pkg@latest`

## VS Code Configuration

To configure blue and isort format in vscode just add in your `.vscode\settings.json` file:

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
    
}
```

If you want to auto format your code on auto save, install the extension [Run on Save](https://marketplace.visualstudio.com/items?itemName=pucelle.run-on-save) and make sure to add in your `.vscode\settings.json` file:

```json
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

```

In addition you can setup the tests in your `.vscode\settings.json` file:

```json
{
    "python.testing.pytestArgs": [
        "tests"
    ],
    "python.testing.unittestEnabled": false,
    "python.testing.pytestEnabled": true
}
```

Finally, to get tips from mypy while writing your code add the bellow configurations in your `.vscode\settings.json` file:

```json
{
    "python.linting.enabled": true,
    "python.linting.mypyEnabled": true,
    "python.linting.pylintEnabled": false,
    "python.languageServer": "Pylance",
    "python.analysis.typeCheckingMode": "basic",
    "python.analysis.diagnosticSeverityOverrides": {
        "reportMissingModuleSource": "none"
    }
}
```

To config `.vscode\launch.json` :

```json
{
  "version": "0.1.0",
  "configurations": [
    {
      "name": "Tests",
      "type": "python",
      "request": "launch",
      "module": "pytest",
      "justMyCode": true
    },
    {
      "name": "Blue",
      "type": "python",
      "request": "launch",
      "module": "blue",
      "justMyCode": true,
      "args": [
        "--check",
        "cronus_eater"
      ]
    },
    {
      "name": "Isort",
      "type": "python",
      "request": "launch",
      "module": "isort",
      "justMyCode": true,
      "args": [
        "--check",
        "cronus_eater"
      ]
    },
    {
      "name": "Python: Module",
      "type": "python",
      "request": "launch",
      "module": "cronus_eater",
      "justMyCode": true
    }
  ],
  "compounds": [
    {
      "name": "All tests",
      "configurations": [
        "Tests",
        "Blue",
        "Isort"
      ],
      "stopAll": true,
      "presentation": {
        "hidden": false,
        "group": "",
        "order": 1,
      }
    }
  ]
}
```