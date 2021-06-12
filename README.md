# Overview

Poetry の実験。

インストールされるライブラリ。

## Poetry Setup

先祖ディレクトリで Python 3.9.1 が有効になっている。

```bash
$ python -V
Python 3.9.1
$ curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
...
(シェル再起動)
$ poetry completions bash > $(brew --prefix)/etc/bash_completion.d/poetry.bash-completion
$ poetry config virtualenvs.in-project true
```

## Project Setup

パッケージ名はアンダースコアを使わずに `samplelib` とする。

```bash
$ poetry init
$ poetry install # .venv がまだ作られてないならここで作られる
```

Venv は現在の pyenv バージョンから作られるみたい。Pipenv と少し違う。
依存ライブラリとして Pandas と autopep8 (こちらは dev 用) を足してみる。

```bash
$ poetry add pandas
$ poetry add -D autopep8
$ poetry show
```

## Coding

```shell
poetry run pytest test
poetry run autopep8 -iar src test
```

ここまでやったところで `sample-app` からのインストールを試してみる。

## Build

やはり、このままでは動かなかった。
のでビルドしてみる。

```shell
$ poetry build
```

`dist/` 以下に source dist と wheel ができた。

これでインポートを試してみる。

なお、ビルド前のバージョンにはタグ `v1` を、ビルド後には `v2` を付けておくことにする。

## Dynamic Versioning

Poetry には現時点で Pipenv の `attr: __init__.py:__version__` みたいな、ソース中の値を動的に取ってくる仕組みがない。

代替手段として `poetry-dynamic-versioning` がある。これは git のタグから `pyproject.toml` やその他のファイル内の文字列を動的に置換してくれる。基本的には `poetry build` の実行時に動作すると思われるが、CLI ツールとして明示的に起動することもできる。

ファイルのほうの置換が動かない…
