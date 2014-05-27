<?php
/* @var $this PatientsController */
/* @var $model Patients */

$this->breadcrumbs=array(
	'Patients'=>array('index'),
	$model->idPatients=>array('view','id'=>$model->idPatients),
	'Update',
);

$this->menu=array(
	array('label'=>'List Patients', 'url'=>array('index')),
	array('label'=>'Create Patients', 'url'=>array('create')),
	array('label'=>'View Patients', 'url'=>array('view', 'id'=>$model->idPatients)),
	array('label'=>'Manage Patients', 'url'=>array('admin')),
);
?>

<h1>Update Patients <?php echo $model->idPatients; ?></h1>

<?php echo $this->renderPartial('_form', array('model'=>$model)); ?>