# Advanced target selection

## Running over changed files with `--changed-since`

pantsはgitを理解しているため、`--changed-since`を通して特定のコミットからの変更されたファイルを見つけることができる。

- uncommittedファイルのlintをするなら `pants --changed-since=HEAD lint` をすれば良い
- --no-pantsdオプションをつけないと実行できないので、原因を探る <https://www.pantsbuild.org/v2.14/docs/troubleshooting#cache-or-pantsd-invalidation-issues>
