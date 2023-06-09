# Using Pants in CI

- [サンプル](https://github.com/pantsbuild/example-python/blob/main/.github/workflows/pants.yaml)

Cacheを次のディレクトリですることをすすめる(linuxの場合)

- `$HOME/.cache/nce`

CIではキャッシュがいつでもULDLされるべき。
ただ、あまりにキャッシュサイズが大きすぎると逆に遅くなるので、nukeする必要がある場合はスクリプトをつかう。
cacheのスタッツは `[stats].log` で調べられる

CIを早く回すために差分のみちぇっくするのもひとつ。 `--changed-since`を使う。

CI用にtoml設定を帰る場合は、pants.ci.tomlを別途用意する。
CIの設定で、環境変数PANTS_CONFIG_FILES=pants.ci.tomlを設定することでこのファイルが参照される。
