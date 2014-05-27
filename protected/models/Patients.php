<?php

/**
 * This is the model class for table "Patients".
 *
 * The followings are the available columns in table 'Patients':
 * @property integer $idPatients
 * @property string $md5hash
 * @property string $birthdate
 * @property integer $female
 *
 * The followings are the available model relations:
 * @property AKSS[] $aKSSes
 * @property DataAcquisition[] $dataAcquisitions
 * @property MRIDataSets[] $mRIDataSets
 * @property OussNamForm[] $oussNamForms
 * @property PatientsOxfordScores[] $patientsOxfordScores
 * @property SessionReports[] $sessionReports
 */
class Patients extends CActiveRecord
{
	/**
	 * Returns the static model of the specified AR class.
	 * @param string $className active record class name.
	 * @return Patients the static model class
	 */
	public static function model($className=__CLASS__)
	{
		return parent::model($className);
	}

	/**
	 * @return string the associated database table name
	 */
	public function tableName()
	{
		return 'Patients';
	}

	/**
	 * @return array validation rules for model attributes.
	 */
	public function rules()
	{
		// NOTE: you should only define rules for those attributes that
		// will receive user inputs.
		return array(
			array('md5hash, birthdate, female', 'required'),
			array('female', 'numerical', 'integerOnly'=>true),
			array('md5hash', 'length', 'max'=>64),
			array('birthdate', 'length', 'max'=>45),
			// The following rule is used by search().
			// Please remove those attributes that should not be searched.
			array('idPatients, md5hash, birthdate, female', 'safe', 'on'=>'search'),
		);
	}

	/**
	 * @return array relational rules.
	 */
	public function relations()
	{
		// NOTE: you may need to adjust the relation name and the related
		// class name for the relations automatically generated below.
		return array(
			'aKSSes' => array(self::HAS_MANY, 'AKSS', 'Patients_idPatients'),
			'dataAcquisitions' => array(self::HAS_MANY, 'DataAcquisition', 'Patients_idPatients'),
			'mRIDataSets' => array(self::HAS_MANY, 'MRIDataSets', 'Patients_idPatients'),
			'oussNamForms' => array(self::HAS_MANY, 'OussNamForm', 'Patients_idPatients'),
			'patientsOxfordScores' => array(self::HAS_MANY, 'PatientsOxfordScores', 'Patients_idPatients'),
			'sessionReports' => array(self::HAS_MANY, 'SessionReports', 'Patients_Patients_idPatients'),
		);
	}

	/**
	 * @return array customized attribute labels (name=>label)
	 */
	public function attributeLabels()
	{
		return array(
			'idPatients' => 'Id Patients',
			'md5hash' => 'Md5hash',
			'birthdate' => 'Birthdate',
			'female' => 'Female',
		);
	}

	/**
	 * Retrieves a list of models based on the current search/filter conditions.
	 * @return CActiveDataProvider the data provider that can return the models based on the search/filter conditions.
	 */
	public function search()
	{
		// Warning: Please modify the following code to remove attributes that
		// should not be searched.

		$criteria=new CDbCriteria;

		$criteria->compare('idPatients',$this->idPatients);
		$criteria->compare('md5hash',$this->md5hash,true);
		$criteria->compare('birthdate',$this->birthdate,true);
		$criteria->compare('female',$this->female);

		return new CActiveDataProvider($this, array(
			'criteria'=>$criteria,
		));
	}
}