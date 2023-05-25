# pantsの始め方

## pantsのインストール方法

```shell
# スクリプトをダウンロード
mkdir bin
curl --proto '=https' --tlsv1.2 -fsSL https://static.pantsbuild.org/setup/get-pants.sh > bin/pants_install.sh

# linuxの場合は インストールディレクトリを/usr/local/binにするのが良さそう（すでにパスがあるため)
sudo bash bin/pants_install.sh --bin-dir=/usr/local/bin
```

## pantsの初期設定

1. pants.tomlを作成する
    - リポジトリのルートに配置
    - pants_versionを変えたいときは、下記を変えると勝手にアップグレードされる

    ```toml
    [GLOBAL]
    pants_version = "2.15.1"
    ```

2. ソースルートの設定
    - pythonなどは設定が必要(デフォルトはリポジトリのルート)
    - 複数のプロジェクトがトップレベルにある場合でも互いにインポートできてしまう。これを制限したい場合は dependenciesを設定する
    - FYI: <https://www.pantsbuild.org/docs/source-roots#multiple-top-level-projects>

3. backendの有効化
    - <https://www.pantsbuild.org/docs/enabling-backends> のプラグインを入れることで機能が使えるようになる

    ```toml
    [GLOBAL]
    backend_packages = [
        "pants.backend.shell",
        "pants.backend.python",
        "pants.backend.python.lint.black",
        "pants.backend.python.lint.isort",
        "pants.backend.python.docker"
    ]
    ```

4. .gitignoreの更新

    ```.gitignore
    # Pants workspace files
    /.pants.*
    /dist/
    /.pids
    ```

5. BUILDファイルの作成
    - `pants tailor ::` で初期のBUILDセットを作成できる。
    - ソースコードがあると自動で検出してそのディレクトリ配下にBUILDファイルをおいてくれるみたい。
    - CIでは `pants tailor --check ::` をすることでBUILDの置き忘れがないかをチェックすると良いらしい。
