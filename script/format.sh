#!/bin/bash

TARGET_DIR=$(git rev-parse --show-toplevel)/src/cp4bal

uvx ruff format $TARGET_DIR
uvx ruff check --fix $TARGET_DIR
