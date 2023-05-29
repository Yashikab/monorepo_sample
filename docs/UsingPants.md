# UsingPants

## Goals

- pantsのコマンドはgoalsとして知られていて、`test`とか`lint` とかである。
- 現状のgoalのリストは pants help goals で検索できる
- 複数のgoalを一回の実行ででき、これらはシーケンシャルで実行される。
- `--loop` をつかうと、対象や対象の依存関係が変更されるまで待ち続け、継続的に実行される

### goal arguments

- filepath: pants test project/tests.py
- directory path: pants test project/utils
- :: globs: pants test project ::
- target addresses : pants package project:tests
  - targetはBUILDで指定するやつ

## Targets and BUILD files
