# QtDesigner で WebView を設定する方法

PyQt5 にて、簡易的なブラウザを作成しようと思い立ったのですが、
WebView を表示するのに必要な WebView の設定方法がわからず、
ググっても日本語の記事がなかなか見つからなかったため、備忘録としてここに残しておきます。

## 環境

- OS: MacOS Catalina 10.15.3

- QtDesigner: version 5.9.6

- PyQt5: version 5.15.0


## 結論

- WebView は、Qt5.6 で削除された。

- 代わりに、QwebEngineView を使用する必要がある。

- QWebEngineView を使用するには、QWidget を拡張して、QWebEngineView クラスを作成する必要がある。

## QWidget を設置する

まずは、QtDesigner で新しいプロジェクトを作成する。
今回は、MainWindow を選択しています。



次に、作成した MainWindow に Widget を設置する。




設置した Widget 上で右クリックして、「Promote to」を選択する。

ダイアログが表示されるので、する。
Global include にはチェックを入れる。

保存し、ターミナルから pyuic5 を用いて、.ui ファイルを .py ファイルに変換する。

## .py 形式のファイルを修正する

.ui 形式のファイルを .py 形式に変換すると、QtDesigner で設置した Widget がクラスの中に定義されている。

QWebEngineView Widget に、url を設定することで起動時に開く Web ページを設定することができる。




私のググり力が貧困な可能性もありますが。。。