<?php
/* @var $this SiteController */

$this->pageTitle=Yii::app()->name;
?>

<div id="wrap">

		<div id="main">
		
			<div class="header">
				
				<a class="left" href="?">Back</a>
				<h1 class="title">Vibroarthrography</h1>
				<a class="right" href="?">Next</a>
				
			</div><!--header-->
			
			<div class="content">
			
				<h2 class="title-c">Vibroarthrography Sign in</h2>
				<div class="login-box">
				<div class="box-white1">
					<p>Mr. Some One<span class="detail">Details here</p>
				</div><!--box-white-->
				<span class="input-msg show"> 
					<a class="IdURL" href="#">Forgot your login?</a>
				</span>
				<div class="login-box">
				<div class="box-white1">
					<p>Mr. Some One<span class="detail">Details here</p>
				</div><!--box-white-->
				</div>
				<span class="input-msg show"> 
					<a class="IdURL" href="#">Forgot your password?</a>
				</span>
							
			</div><!--content-->
		
		</div><!--main-->
	
		<div id="sidebar">
			
			<div class="header">

			</div><!--header-->
			
			<div class="content">
				
				<ul class="nav1">
					<li><p class="txt">Sign in with your Apple ID to access Apple Support. If you don't have an Apple ID, you can create one now.</p></li>
				</ul>

			</div><!--content-->
			
		</div><!--sidebar-->
	
		
		

	</div><!--wrap-->

<h1>Welcome to <i><?php echo CHtml::encode(Yii::app()->name); ?></i></h1>

<p>Congratulations! You have successfully created your Yii application.</p>

<p>You may change the content of this page by modifying the following two files:</p>
<ul>
	<li>View file: <code><?php echo __FILE__; ?></code></li>
	<li>Layout file: <code><?php echo $this->getLayoutFile('main'); ?></code></li>
</ul>

<p>For more details on how to further develop this application, please read
the <a href="http://www.yiiframework.com/doc/">documentation</a>.
Feel free to ask in the <a href="http://www.yiiframework.com/forum/">forum</a>,
should you have any questions.</p>
