<?php /* @var $this Controller */ ?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	<meta name="language" content="en" />

	<!-- blueprint CSS framework -->
	<link rel="stylesheet" type="text/css" href="<?php echo Yii::app()->request->baseUrl; ?>/css/screen1.css" media="screen, projection" />
	<link rel="stylesheet" type="text/css" href="<?php echo Yii::app()->request->baseUrl; ?>/css/print.css" media="print" />
	<link rel="stylesheet" type="text/css" href="<?php echo Yii::app()->request->baseUrl; ?>/css/main.css" />
	<link rel="stylesheet" type="text/css" href="<?php echo Yii::app()->request->baseUrl; ?>/css/form.css" />

	<title><?php echo CHtml::encode($this->pageTitle); ?></title>
</head>

<body>
<div id="wrap">
<div id="main">

			<div class="header">
				
				<a class="left" href="?">Back</a>
				<h1 class="title"><?php echo CHtml::encode(Yii::app()->name); ?></h1>
				<a class="right" href="?">Next</a>
				
			</div><!--header-->

	<?php if(isset($this->breadcrumbs)):?>
		<?php $this->widget('zii.widgets.CBreadcrumbs', array(
			'links'=>$this->breadcrumbs,
		)); ?><!-- breadcrumbs -->
	<?php endif?>

	<?php echo $content; ?>

<div id="sidebar">
			
			<div class="header">
				<p class="title">Vibroarthrography</p>
			</div><!--header-->
			
			<div class="content">
				
				<ul class="nav">
				<li class="info"><?php $this->widget('zii.widgets.CMenu',array(
			'items'=>array(
				array('label'=>'Home', 'url'=>array('/site/index')),
				array('label'=>'About', 'url'=>array('/site/page', 'view'=>'about')),
				array('label'=>'Contact', 'url'=>array('/site/contact')),
				array('label'=>'Patients', 'url'=>array('/patients')),
				array('label'=>'Login', 'url'=>array('/site/login'), 'visible'=>Yii::app()->user->isGuest),
				array('label'=>'Logout ('.Yii::app()->user->name.')', 'url'=>array('/site/logout'), 'visible'=>!Yii::app()->user->isGuest)
			),
		)); ?></li><!-- some alternative menu here
					<li><a href="?"><span class="ico msg"></span>Normal item</a></li>
					<li><a href="?" class="active"><span class="ico msg"></span>Active section</a></li>
					<li><a href="?"><span class="ico msg"></span>Red circle<span class="info">5</span></a></li>
					<li><a href="?"><span class="ico msg"></span>Status indicator <span>On</span></a></li>
				</ul>-->
			</div><!--content-->
			
</div><!--sidebar-->

	<div class="clear"></div>

	<div id="footer">
		Copyright &copy; <?php echo date('Y'); ?> by Leysan.<br/>
		All Rights Reserved.<br/>
	</div><!-- footer -->

</div></div><!-- page -->

</body>
</html>
