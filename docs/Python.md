# pythonでの設定

- python sourceとpython testをつかって、どのpythonファイルが実行されるか、、やメタデータの設定することを知る。
- 定型文を減らすため、python sourcesはsource fieldにある各々のファイルを対象に生成する。
- これらのターゲットは `pants tailor ::`を実行すれば生成される。

## lockfile

- pants.tomlで [python].enable_resolvesをtrueにする

```toml
[python]
enable_resolves = true
```

- デフォルトは `3rdparty/python/default.lock` に保存されるが、変更するときは下記のように変える

```toml
[python.resolves]
python-default = "lockfile_path.lock"
```

- `pants generate-lockfiles` でlockfileを生成する。

### 複数のlockfileを設定する

- プロジェクト間でバージョンコンフリクトがあるような場合は、複数のlockfileにわける必要がある
- 次のようにtomlを設定する

```toml
[python]
enable_resolves = true

[python.resolves]
logic1 = "logic1.lock"
logic2 = "logic2.lock"

```

- その上で各BUILDファイルでどちらに属するかを明記する

```
# Often, you will want to set `resolve` on the 
# `poetry_requirements` and `python_requirements`
# target generators.
poetry_requirements(
    name="poetry",
    resolve="logic1",
    # You can use `overrides` if you only want to change
    # some targets.
    overrides={"requests": {"resolve": "logic1"}},
)
```
