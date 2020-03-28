●できること
コンテナを介してJupyterlabを使うよ。

●使い方
buildした後に下記を実行して、ブラウザから「localhost:8888」にアクセスして。
$ docker run -p 8888:8888 -v /Users/yoshimura.keta/Desktop/work/study/econml:/work --name econml study/econml

「work」ディレクトリが、ローカルとマウントされているよ。

●参考
下記を参考に一部変更した(anacondaを使わないようにしたかったのだ...)
https://datawokagaku.com/startjupyternote/