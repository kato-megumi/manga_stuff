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
      $root ="/mnt/tool/Project/xmanga/";
      if(isset($_GET["dir"])){
         $get = $_GET["dir"];
         $dir = $root.$get;
         $scan = scandir($dir);
         for ($i=1; $i < count($scan)-1; $i++) { 
            echo '<img src="/xmanga/'.$get.'/'.strval($i).'.jpg"><br>';
         }
         for ($i=1; $i < count($scan)-1; $i++) { 
            echo '<img src="/xmanga/'.$get.'/'.strval($i).'.png"><br>';
         }
      } else {
         $scan = scandir($root);
         foreach ($scan as $v) {
           echo '<a href="?dir='.$v.'">'.$v.'</a><br>';
      }
   }
      ?> 
   </center>
</body>

</html>