# Tests


[Poe](https://github.com/nat-n/poethepoet) is used to run all tests.

Here are the most important options. Fore more details, please use `poe --help`.

## Local Tests

- Run all tests (against both source and installed stubs): `poe test_all`
- Run tests against the source code: `poe test` 
  - Run only mypy: `poe mypy`
  - Run only pyright: `poe pyright`
  - Run only pytest: `poe pytest`
  - Run only pre-commit: `poe style`

## Continuous Integration

When you do a pull request, all tests is going to run through GitHub Actions in all Python versions and OS's that we support.

## Continuous Delivery

In progress ... It's going to be avaible in the first software deployment.


