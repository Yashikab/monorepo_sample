# Advanced target selection

## Running over changed files with `--changed-since`

pantsはgitを理解しているため、`--changed-since`を通して特定のコミットからの変更されたファイルを見つけることができる。

- uncommittedファイルのlintをするなら `pants --changed-since=HEAD lint` をすれば良い
- --no-pantsdオプションをつけないと実行できないので、原因を探る <https://www.pantsbuild.org/v2.14/docs/troubleshooting#cache-or-pantsd-invalidation-issues>
  - これはどうやらバグらしい。<https://github.com/pantsbuild/pants/issues/18563>
  - 2.17.xでなおるとのこと -> アップグレードで対応した
- --changed-sinceはデフォルトではファイルディレクトリが変更されたときのみ動く。
- 一方で関係する依存先が変更された場合も動くようにしたいこともある。その時は --changed-dependees=direct か --changed-dependees=transitiveを使う。
