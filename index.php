<!DOCTYPE html> 
<html lang="en"> 
<head> 
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8"> 
</head>
<style type="text/css">
body {
  background-color: black;
}

h1 {
  color: white;
  text-align: center;
}

p {
  font-family: verdana;
  font-size: 20px;
}
img {max-width:100%; height:auto}
</style>
<body>
  <center>
   <?php
   $dir =getcwd();
   if(isset($_GET["dir"])){
     $dir = $_GET["dir"];
   }	 
   $scan = scandir($dir);
   $b = explode('/', $dir);
   array_splice($b, count($b)-1);
   $father = implode('/', $b);
   echo '<a href="?dir='.$father.'">'."../ ( UP )".'</a><br>';
   // echo '<a href="?dir='.$dir."../".'">'."../ ( UP() )".'</a><br>';
   foreach ($scan as $v) {
    $a = explode('.', $v);
    $tail = $a[count($a)-1];
    $full = $dir.'/'.$v;
    if ($v != '.' && $v != ".." && is_dir($full)){
      echo '<a href="?dir='.$full.'">'.$v.'</a><br>';
    }
    else {
      echo $tail;
    }
    if ($tail == "jpg" || $tail == "png" ) {
      echo '<img src="image.php?img='.$full.'" />';
    }
  }
  ?> 
</center>
</body>

</html>