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
$OGcheckindate = $_POST['checkindate'];
$Checkin = date("Y-m-d", strtotime($OGcheckindate)); 

$OGcheckoutdate = $_POST['checkoutdate'];
$Checkout = date("Y-m-d", strtotime($OGcheckoutdate)); 


$sql =  "SELECT Check_in FROM reservation WHERE Check_in = '$Checkin'"; 
		
if(mysqli_num_rows(mysqli_query($con, $sql)) > 0) {
	echo "NOT AVAILABLE";
	echo "              ";
	echo "              ";
	echo "              ";
	echo "CHOOSE ANOTHER DATES :)";
	header('Refresh:3; url="home.html"');
}
else {
	echo "AVAILABLE";
	echo "              ";
	echo "              ";
	echo "RESERVE NOW! :)";
	header('Refresh:3; url="reservation.html"');
}





?>