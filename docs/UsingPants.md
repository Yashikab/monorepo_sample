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

- ほとんどのGoalはコードに関するメタデータを必要とする
- Targetsはコードを記述することのメタデータのアクセスできる集合である
例えば
- `shell_source`や`python_test`は自分自身のコードを記述する
- `python_requirement`はサードパーティのrequirementを記述する
- `pex_binary`や`archive`はpantsにビルドしてほしいartifactを記述する。

定型文を減らすため、他のターゲットを生成するターゲットも存在する

- `python_tests` -> `python_test`
- `shell_sources` -> `shell_source`
- `go_mod` -> `go_third_party_package`

### BUILD files

TargetはBULDと名付けられたファイルに定義される。

### Target addresses

- targetはユニークなアドレスによって区別される。(`path/to/dir:name` の形)
- addressは`dependencies`フィールドでどのほかのターゲットに依存しているかを識別するために使われる
- addressはコマンドラインの引数としても使われる (`pants fmt path/to:tgt`)
- nameフィールドのデフォルトはディレクトリ名になっている。

### `source` and `sources` field

- `python_test`や`resource`のようはターゲットは sourceフィールドを持っている
- sourceフィールドはどのソースファイルをターゲットに属させるかを決定する
- 親を遡ることはできない
- `_`や`**`に対応している。

- sourceが複数のターゲットで重複することは許されている
  - しかし、メタデータが同じソースファイルでコンフリクトを起こす場合がある
  - testをしたときに2度独立に回ってしまう可能性がある
  - このファイルに関する依存関係を推測できなくなる可能性がある

## あしたはここから<https://www.pantsbuild.org/docs/targets#dependencies-field>
