<?php
/* @var $this PatientsController */
/* @var $dataProvider CActiveDataProvider */

$this->breadcrumbs=array(
	'Patients',
);

$this->menu=array(
	array('label'=>'Create Patients', 'url'=>array('create')),
	array('label'=>'Manage Patients', 'url'=>array('admin')),
);
?>

<h1>Patients</h1>
<p>Some random text about patients here. Btw, secret data</p>
<div class="content">
			
				<h2 class="title">Patient's data</h2>
				<div class="box-white">
					<p>Mr. Some One<span class="detail">Details here</span><span>Edit</span></p>
				</div><!--box-white-->

				<!-- <h2 class="title2">Account details</h2>-->
				<p>Me got forms too:</p>
				
				<div class="box-white">
					<p><label for="field1">Apple ID</label><input id="field1" type="text" value="xavi@example.com" /></p>
					<p><label for="field2">Password</label><input id="field2" type="password" value="xavixavi" /></p>
					<p><label for="field3">Country</label><select id="field3"><option>Spain</option><option>United Kingdom</option></select></p>
				</div>
				<h2 class="title2">Heading second</h2>			
<p><?php
//run puthon script
$output = null; 
exec('python VAG_FEsignalplots_15me.py', $output, $return); 

//print output, just for testing
print_r($output); 
print_r($return); 
echo"<br \>";

//display the output picture
echo '<img src="test.png">';
?></p>
				<h2 class="title">Sensors data</h2>
				<div class="box-white">
					<p>Parameter 1<span>Value</span></p>
					<p>Parameter 2<span>Value</span></p>
					<p>Parameter 3<span>Value</span></p>
					<p><a href="?">PNG picture<span>Show<span class="arrow">&gt;</span></span></a></p>
					<!-- some more fields
					<p>Foo <span>Bar</span></p>
					<p>Lorem ipsum <span><a href="?">Click only this</a></span></p>
					-->
				</div><!--box-white-->
				
				
				<table>
					<thead>
						<tr><th>Table heading</th><th>Tweets</th><th>Following</th><th>Followers</th></tr>
					</thead>
					<tbody>
						<tr><td><a href="?">@xaviesteve</a></td><td><a href="?">Click</a></td><td>131</td><td>195</td></tr>
						<tr><td>@xaviesteve</td><td>622</td><td><a href="?">Click</a></td><td>195</td></tr>
						<tr><td>@xaviesteve</td><td>622</td><td>131</td><td><a href="?">Click</a></td></tr>
					</tbody>
				</table>
				
				<p class="note">You can follow me on Twitter for updates on this template at <a href="http://www.twitter.com/xaviesteve">@xaviesteve</a>.</p>
						
				<h2 class="title">Heading first</h2>

				<div class="box-white">
					<p class="center">Centered text in a white box</p>
				</div><!--box-white-->
				
		
				
				<p><input type="submit" class="button red" value="Delete Account" /></p>
							
			</div><!--content-->

<?php $this->widget('zii.widgets.CListView', array(
	'dataProvider'=>$dataProvider,
	'itemView'=>'_view',
)); ?>
