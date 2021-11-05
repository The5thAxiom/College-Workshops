<?php

         $d = date("D");
         if ($d == "Fri")
            echo "Have a nice weekend!";
         elseif ($d == "Sun")
            echo "Have a nice Sunday!"; 
         else
            echo "Have a nice day!";

		for($i=0;$i<10;$i++)
			echo " ".$i;
		echo "<br>";
		
		//number array
		$value=array(1,2,3,4,5,6);
		for($i=0;$i<5;$i++)
			echo " ".$value[$i];
		
		//associate array
		$details=array("name"=>"vit","location"=>"chennai","status"=>"closed");
		echo "<br>";
		echo "name ".$details["name"];
		echo "<br>";
		echo "location". $details["location"];
?>
