# CP4BAL: Confidence Propagation for Batch Active Learning on Graphs


## About this repo

This repository contains the code for my master's thesis project.
Please be aware that it is still a work in progress.

Part of this implementation is based on [the official implementation of ``Uncertainty for Active Learning on Graphs'' (Fuchsgruber+, ICML 2024)](https://github.com/dfuchsgruber/uq-for-al-on-graphs).


## How to run

Please check [script/job.sh](./script/job.sh) for details.
Config files can be found in [config/](./config/).

For active learning experiments, the entry point is the `main` function in [src/cp4bal/main.py](./src/cp4bal/main.py)


### Example

```bash
$ bash script/job.sh 41 random 1 28 config/dataset/cora_ml.yaml config/model/gcn.yaml
```
