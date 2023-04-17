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

//convert dd/mm/yyyy to yyyy-mm-dd
$OGcheckin = $_POST['checkindate'];
$Check_in = date("Y-m-d", strtotime($OGcheckin)); 

$OGcheckout = $_POST['checkoutdate'];
$Check_out = date("Y-m-d", strtotime($OGcheckout)); 


$Name = $_POST['username'];
$Phone = $_POST['phone'];
$Email = $_POST['email'];
$Adults = $_POST['adults'];
$Children = $_POST['children'];
$Notes = $_POST['notes'];

$sql = "INSERT INTO reservation (name,phone,email,check_in,check_out,adults,children,notes) VALUES ('$Name','$Phone','$Email','$Check_in','$Check_out','$Adults','$Children','$Notes')";

if(!mysqli_query($con,$sql))
{
	echo "FILL DETAILS AGAIN!";
	header("refresh:3; url=reservation.html");
}

else
{
	echo "CHOOSE YOUR ROOMS PERSONALLY :)";
}

header("refresh:3; url=rooms.html");

?>