<!DOCTYPE html>
<html>
  <head>
    <!-- meta -->
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0,minimum-scale=1.0">
<link rel="icon" type="image/x-icon" href="/images/dibx_custom_logo.png">
<link rel="stylesheet" type="text/css" href="/css/common.css">

<script type="text/javascript" src="/js/jquery-1.9.0.min.js"></script>
<script type="text/javascript" src="/js/google-code-prettify/prettify.js"></script>
<link  type="text/css" rel="stylesheet" href="/js/google-code-prettify/prettify.css"/>
<script>
  $(function(){
    // google code prettifyの有効化
    $("pre").addClass("prettyprint");
    function init(event){
      prettyPrint();
    }
    if(window.addEventListener)window.addEventListener("load",init,false);
    else if(window.attachEvent)window.attachEvent("onload",init);
    
    $(".to-top").click(function() {
      // ページの一番上までスクロールさせます。
      $('body, html').animate({scrollTop: 0}, 300, 'linear');;
    });
  });
</script>

<title>Title - DBIx::Custom - SQLの実行が簡単なPerlのO/Rマッパー</title>
<meta name="description" content="#!/usr/bin/env perl">
  </head>
  <body>
    <div class="container">
      <div class="header">
        <!-- header -->
<h1>
  <a href="/">DBIx::Custom<span class="hide-smartphone"> - SQLの実行が簡単なPerlのO/Rマッパー</span></a>
</h1>

      </div>
      <div class="main">
        <div class="content">
          <div class="entry">
  <div class="top">
    <!-- top -->

  </div>
  <div class="middle">
    <p>
  #!/usr/bin/env perl
</p>
<p>
  use strict;
</p>
<p>
  use warnings;
</p>
<p>
  use utf8;
</p>
<p>
  use Encode 'encode';
</p>
<p>
  # Title mail form
</p>
<p>
  my $title = 'Mail form';
</p>
<p>
  # Content mail form
</p>
<p>
  my $content = <<"EOS";
</p>
<h2><a href="/test.cgi">Title</a></h2>
<div>
  Content
</div>
<p>
  EOS
</p>
<p>
  $content = build_html($title, $content);
</p>
<p>
  my $html = <<"EOS";
</p>
<p>
  Content-type: text/html; charset=UTF-8
</p>
<p>
  $content
</p>
<p>
  EOS
</p>
<p>
  print encode('UTF-8', $html);
</p>
<p>
  sub build_html {
</p>
  my ($title, $content) = @_;
  
  local $/;
  my $html = <DATA>;
  
  $html =~ s/\$TITLE/$title/;
  $html =~ s/\$CONTENT/$content/;
  
  return $html;
<p>
  }
</p>
<p>
  __DATA__
</p>

  </div>
  <div class="bottom">
    
  </div>
</div>

        </div>
        <div class="side">
          <!-- side -->
<div class="side-list">
  <div class="side-list-title">
    ドキュメント
  </div>
  <ul>
    <li><a href="/blog/20110508130736.html">インストール</a></li>
    <li><a href="/blog/20110516130787.html">データベースへの接続</a></li>
    <li><a href="/blog/20110816131802.html">モデルの作成</a></li>
    <li><a href="/blog/20110210130016.html">select - 行の選択</a></li>
    <li><a href="/blog/20110129130016.html">insert - 行の挿入</a></li>
    <li><a href="/blog/20110130130016.html">update - 行の更新</a></li>
    <li><a href="/blog/20110202130016.html">delete - 行の削除</a></li>
    <li><a href="/blog/20110708131364.html">execute - SQLの実行</a></li>
    <li><a href="/blog/20110924132031.html">where - 条件の作成</a></li>
    <li><a href="/blog/20110709131364.html">行データの取得</a></li>
    <li><a href="/blog/20200127081842.html">その他の機能</a></li>
  </ul>
</div>

<div class="side-list" style="margin-top:30px;">
  <div class="side-list-title">
    案内
  </div>
  <ul>
    <li><a href="https://web.perlzemi.com/">DBIx::CustomをWeb開発で実践するならMojoliciousスタートアップ</a></li>
    <li><a href="https://tutorial.perlzemi.com/">Perlをもっと理解したいならPerl入門ゼミ</a></li>
    <li><a href="https://mariadb.perlzemi.com/">SQLやデータベースを理解するならMariaDB入門</a></li>
  </ul>
</div>


        </div>
      </div>
      <div class="footer">
        <!-- footer -->
<a href="https://kimoto-system.co.jp/">サイト運営 木本システム <br>Copyright © 2020-2020 Yuki Kimoto</a>

      </div>
    </div>
  </body>
</html>
