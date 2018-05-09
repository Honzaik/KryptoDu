<?php
ini_set('max_execution_time', 500); 
error_reporting(E_ALL);
ini_set('display_errors', 1);
$db = new PDO("mysql:host=localhost;dbname=adolf", "root", "");

function isInDb($db, $hash){
    $first40 = substr($hash, 0, 14);
    $statement = $db->prepare("SELECT COUNT(*) AS pocet FROM brute WHERE first40 = :hash40 LIMIT 1");
    $statement->bindParam(":hash40", $first40, PDO::PARAM_STR);
    if($statement->execute()){
        $row = $statement->fetch(PDO::FETCH_OBJ);
        if($row->pocet > 0) return true;
        else return false;
    }else{
        return die("error");
    }
}

function saveToDb($db, $str ,$hash){
    $first40 = substr($hash, 0, 14);
    $statement = $db->prepare("INSERT INTO brute VALUES (:string, :first40, :hash)");
    $statement->bindParam(":string", $str, PDO::PARAM_STR);
    $statement->bindParam(":first40", $first40, PDO::PARAM_STR);
    $statement->bindParam(":hash", $hash, PDO::PARAM_STR);
    if(!$statement->execute()){
        return die("error while saving");
    }
}

$prefix = "JanOupicky";

$counter = 0;

$currentHash = hash("sha256", $prefix.$counter);
/*
while(!isInDb($db, $currentHash)){
    saveToDb($db, $prefix.$counter, $currentHash);
    $counter++;
    $currentHash = hash("sha256", $prefix.$counter);
}
*/

echo substr($currentHash, 0, 14);
echo $currentHash . PHP_EOL;
echo $prefix.$counter;