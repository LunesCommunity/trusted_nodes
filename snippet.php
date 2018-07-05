echo '<!DOCTYPE html>
<html lang="en">
<head>
  <title>Professional LUNES nodes</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.1.0/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.0/umd/popper.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.1.0/js/bootstrap.min.js"></script>
</head>
<body> 
<p></p>
<div class="container">
  <div class="card-columns"> ';




$leer_nodes = file_get_contents("https://lunes.in/trust.json");
$datos_nodes = json_decode($leer_nodes,true);

    
 
foreach ($datos_nodes["node"] as $key => $value) {
    echo '<div class="card bg-light">';
    echo '<div class="card-body text-center">';
    echo '<img src="https://'.$value["domain"].'/nodeimage.png" alt="Node image" width="50px" height="50px">';
    echo '<h4 class="card-title">'.$value["domain"]."</h4>";

    
    echo  '<p class="card-text"><b>Blocks: </b>'.$value["blocks"]."</p>";
    echo  '<p class="card-text"><b>Leasing address: </b><br><font size=2>'.$value["address"]."</font></p>";
    echo  '<p class="card-text"><b>Share: </b>'.$value["share"]." %</p>";
    echo  '<p class="card-text"><b>Fees: </b>'.$value["fees"]."</p>";
    echo  '<p class="card-text"><b>Balance: </b>'.$value["balance"]."</p>";
    echo  '<a href="https://'.$value["domain"].'/" class="btn btn-primary">Web</a>';
    echo "</div>";
    echo "</div>";
    }
