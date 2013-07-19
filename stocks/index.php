<!DOCTYPE html>
<html lang="en-GB">
  <head>
    <meta charset="utf-8">
    <title>D3 Test</title>
    <script type="text/javascript" src="d3/d3.v3.js"></script>
    <style>

    </style>
  </head>
  <body>
    <script type="text/javascript">
    
<?php
include('connect-mysql.php');

$sqlget = "SELECT * FROM tutorial";
$sqldata = mysqli_query($dbcon, $sqlget) or die('oops-error');
      
?>
  
  
  var data_set = [1,2,3,4,5,6,7,8,9,10,11,12];
      /*for (var i = 0; i < 25; i++) {
       var new_number = Math.floor(Math.random() * 100);
       data_set = data_set.concat(new_number);
      }*/
      
      var svg_width = 500;
      var svg_height = 150;
      var bar_pad = 2;

      var temp_val = 0;

      var new_svg = d3.select("body")
                      .append("svg")
                      .attr("width", svg_width)
                      .attr("height", svg_height);

      new_svg.selectAll("rect")
             .data(data_set)
             .enter()
             .append("rect")
             .attr("x", function(d, i) {
                 return i * (svg_width / data_set.length);
             })
             .attr("y", function(d) {
                 return svg_height - d;
             })
             .attr("width", svg_width / data_set.length - bar_pad)
             .attr("height", function(d) {
                 return d * 100;
             })
             .attr("fill", function(d) {
                 if (d <= 155 && d >= 50) {
                  return "rgb(0, 100, " + d + ")" ;
                  }
                 else
                  return "purple";
             });
    new_svg.selectAll("text")
           .data(data_set)
           .enter()
           .append("text")
           .text(function(d) {
               return d;
               })
           .attr("x", function(d, i) {
               return i * (svg_width / data_set.length) + 3;
               })
           .attr("y", function(d) {
               return svg_height - (d) + 15;
             })
           .attr("fill", "white")
           .attr("font-family", "sans-serif")
           .attr("font-size", "11px")
    </script>
  </body>
</html>


