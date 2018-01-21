<?php
$action = $_GET['action'];
$result = `/home/pi/Desktop/test/$action 2>&1`;
echo $result, PHP_EOL;
