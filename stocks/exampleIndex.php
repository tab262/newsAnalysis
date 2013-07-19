<html>
<head>
<title>News</title>
<style type="text/css">
table {
    border : 2px solid redl
    background-color: #FTC;
    }
th {
    border-bottom: 5px solid #000;
    }
    
td {
    border-bottom: 2px solid #666;
    }
</style>
<head>
<body>
<img src="newsHeader2.png">

<?php

include('connect-mysql.php');

$sqlget = "SELECT * FROM news";
$sqldata = mysqli_query($dbcon, $sqlget) or die('oops-error');

echo "<table>";
  echo "<tr><th>Source</th><th>Headline</th><th>Summary</th><th>Link</th><th>Date</th></tr>";

while ($row = mysqli_fetch_array($sqldata, MYSQLI_ASSOC)) {
    echo "<tr><td>";
    echo $row['source'];
    echo "</td><td>";
    echo $row['headline'];
    echo "</td><td>";
    echo $row['summary'];
    echo "</td><td>";
    echo "<a href ='";
    echo $row['link'];
    echo "'>Link</a>";
    echo "</td><td>";
    echo $row['date'];
    echo "</td></tr>";
}

echo "</table>";

?>


</body>
  </html>
