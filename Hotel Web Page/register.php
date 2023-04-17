<?php

$con = mysqli_connect('127.0.0.1','root','');

if(!$con)
{
	echo 'not connected to database';
} 

if(!mysqli_select_db($con, 'demo'))
{
	echo 'database not selected';
}

$User_name = $_POST['username'];
$Email = $_POST['email'];
$Mobile_no = $_POST['mobile_no'];
$Address = $_POST['address'];
$Password = $_POST['password'];

$sql = "INSERT INTO user (user_name,email,mobile,address,password) VALUES ('$User_name','$Email','$Mobile_no','$Address','$Password')";

if(!mysqli_query($con,$sql))
{
	echo 'not registered';
}

else
{
	echo 'registered';
}

header("refresh:2; url=registerform.html");

?>