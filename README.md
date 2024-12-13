# fast_api_todo_app

## 参考

https://zenn.dev/sh0nk/books/537bb028709ab9

## 環境構築

```shell
# イメージの作成
$ docker-compose build
# pyprojectに含まれるパッケージのインストール
$ docker-compose run --entrypoint "poetry install --no-root" demo-app
# 再度ビルド
$ docker-compose build --no-cache
# コンテナの起動
$ docker-compose up -d
# コンテナに入る
$ docker-compose exec demo-app bash
```

Swagger UI: http://localhost:8000/docs
