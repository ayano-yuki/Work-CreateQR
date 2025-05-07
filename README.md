# Work-CreateQR
- 入力した情報を基にQRコードを生成するアプリ
- チームで開発した
  - 役割：UIデザインを除く全ての開発工程を担当

# 概要
SNSのアカウントやWIFI情報等の雑多な情報の共有をする際に、「一々アカウント名を検索するのは面倒」や「打ち間違えて間違い探ししたくない」と思ったことはありませんか？

このアプリはこれらの問題を解決するために、QRコードを簡単に生成し、画面を見せるだけで共有ができるようにしました。
リリースもしているので、[こちら](https://work-create-qr.vercel.app/)からどうぞ！

# 主な機能
- QRコードの生成
- 生成したQRコードの保存（ブラウザのストレージに保存）
- 保存されたQRの削除
- 指定したQRのポップアップ

# 技術スタック
- Python（Flask）
    - チームメンバーの技術スタックに合わせるために使用

# インストール方法
1. プロジェクトをcloneする
    ```bash
    git clone https://github.com/ayano-yuki/Work-CreateQR.git
    cd Work-CreateQR.git
    ```
2. 必要な依存パッケージのインストール
   ```bash
   pip install -r requirements.txt
   ```
3. 開発サーバーの起動
   ```bash
   python app.py
   ```

# 課題・今後の予定（TODO）
- 保存したQRコードに名前を付けれるようにする
- オフライン環境でも使えるようにする
- 複雑な情報でも共有できるようにする

# 参考
- デプロイの設定方法
  - https://medium.com/@nohanabil/how-to-deploy-flask-app-using-vercel-885ce034624
