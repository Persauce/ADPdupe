
<?php
/*this is to retrieve the name variable 
from the face detection code
*/
$result = shell_exec('python facedect.py');
$var = json_decode($result, true);
echo $resultData["name"]

?>