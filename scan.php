
<?php
$result = shell_exec('python3 test.py');
// $var = json_decode($result, true);
$file_name = 'result_scan.txt';
$person_scanned = fgets(fopen($file_name,'r'));
echo $person_scanned
?>