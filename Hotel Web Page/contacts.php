<?php

$con = mysqli_connect('127.0.0.1','root','');

if(!$con)
{
	echo 'not connected to database';
} 

if(!mysqli_select_db($con, 'heritage'))
{
	echo 'database not selected';
}

$Name = $_POST['name'];
$Email = $_POST['email'];
$Message = $_POST['message'];


$sql = "INSERT INTO contacts (name,email,message) VALUES ('$Name','$Email','$Message')";

if(!mysqli_query($con,$sql))
{
	echo "TRY AGAIN";
}

else
{
	echo "WE'LL GET BACK TO YOU SOON! :)" ;
}

header("refresh:3; url=contacts.html");

?>