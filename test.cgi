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
    <div style="text-align:center;">
  <a href="https://www.perlri.com/book/perl_text_essense" rel="nofollow"><img src="https://tutorial.perlzemi.com/images/book/perl_text_essence.jpg" style="width:80px;margin:0 auto;"></a><br><a href="https://www.perlri.com/book/perl_text_essense" rel="nofollow" style="font-size:20px;">Perlテキスト処理のエッセンス発売中</a>

</div>
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
    <div class="youtube_block">
  <div class="youtube">
    <iframe width="560" height="315" src="https://www.youtube.com/embed/mFe8K0YdSOg" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
  </div>
</div>

<div style="text-align:center;margin-top:30px;font-weight:bold;font-size:22px;">
データベースアクセスの基礎としてのPerlテキスト処理プログラミングを学べる教材
</div>
<div style="text-align:center;margin-top:30px;">
  <a href="https://www.perlri.com/book/perl_text_essense" rel="nofollow"><img src="https://tutorial.perlzemi.com/images/book/perl_text_essence.jpg" style="width:260px;margin:0 auto;"></a><br><a href="https://www.perlri.com/book/perl_text_essense" rel="nofollow" style="font-size:20px;">Perlテキスト処理のエッセンス発売中</a>

</div>

  </div>
</div>

        </div>
        <div class="side">
          <!-- side -->
<div class="side-list">
  <div class="side-list-title">
    講座作成
  </div>
  <ul>
    <li style="text-align:center;padding-left:0"><a href="http://www.perlri.com/"><img width="120" src="https://tutorial.perlzemi.com/images/kaeru_w_01.png"><br>Perl元気塾</a></li>
  </ul>
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
  <div class="side-list-title" style="margin-top:30px;">
    Perlテキスト処理のエッセンス
  </div>
  <ul>
    <li style="text-align:center;">
      <a rel="nofollow" href="https://www.perlri.com/book/perl_text_essense"><img src="https://tutorial.perlzemi.com/images/book/perl_text_essence.jpg" width="160"></a><br>
      <a rel="nofollow" href="https://www.perlri.com/book/perl_text_essense">Perlテキスト処理のエッセンス</a><br>
     データベースアクセスの基礎としてのPerlテキスト処理プログラミングを学べる教材
    </li>
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
        <div class="what_is_this_site">
  <div class="inside">
    DBIx::Customは、<a href="https://tutorial.perlzemi.com/">Perl</a>のデータベースアクセスモジュールの一つです。insert,update,delete,selectのSQLを簡単に実行できる機能があります。DBIx::Connectorをデフォルトで搭載、接続管理も自動的に行います。where句のand,orを柔軟に書け、プレイスホルダー機能を提供。<a href="https://websystem.perlzemi.com/">Webシステム開発</a>では、外部キーのjoinを頻繁に記述しますが、join句をモデルに定義して、簡単に外部キーを接続できます。<a href="https://mariadb.perlzemi.com/">MariaDB</a>, MySQL, PostgreSQL, SQLite, Microsoft SQL Server, Oracle Database, Microsoft Accessにも対応。
  </div>
</div>

<div class="perlri_link">
  <a href="http://www.perlri.com">
    Copyright © Perl総合研究所
  </a>
</div>

      </div>
    </div>
  </body>
</html>
