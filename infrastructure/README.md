# Project Setup
This page guides you through the setup of all necessary tools which are used for data processing and analysis in this project.

## Mambaforge
Our recommended tool for environment managemt is [Mambaforge](https://conda-forge.org/miniforge/).
Please download the latest version and install it if you have not done so already.

### Build environment
An environment is a collection of tools, packages and dependencies which are required to execute a script.
With mambaforge we have an environment manager which we can use to build envrionments by providing an environment recipe stored as `.yaml` file.

```{attention}
Make sure that you are in the root-directory of your project.
```

With the following command a new envrionment is created with the name `demo-project`.
The packages which are installed are defined in the file `infrastructure/env-yamls/demo-project-env.yaml`.

```bash
mamba env create -f infrastructure/env-yamls/demo-project-env.yaml --always-copy
```

### Activate environment
Once an envrionment is created it must be activated such that we can use the installed packages.

```bash
mamba activate demo-project
```

Once the environment is activate your CLI prompt will be prefixed with the environment name e.g.:
`(demo-project)$ `
