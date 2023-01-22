anychart.onDocumentReady(function () {
  fetch("./anygraph.json")
    .then((response) => response.json())
    .then((data) => {
      var chart = anychart.graph(data);
      chart.layout().iterationCount(100);
      // set the title
      chart.title("Network Graph showing the battles in Game of Thrones");
      // draw the chart
      chart.container("container").draw();
    });
});
