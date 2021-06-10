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
