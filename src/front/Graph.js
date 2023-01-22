anychart.onDocumentReady(function () {
  fetch("./anygraph.json")
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
      var chart = anychart.graph(data);
      var nodes = chart.nodes();
      var edges = chart.edges();
      console.log("Number of Nodes:");
      chart.title("UBC Course Dependencies Graph");

      /**
       * APPEARANCE
       */
      // EDGES
      edges.normal().stroke("#F3F3F5", 2);
      edges.selected().fill("#000000", 2);
      edges.selected().stroke("#000000", 2);

      // NODES
      nodes.normal().height(5);
      nodes.normal().stroke(null);

      nodes.normal().fill("#F0F0F0"); // unselected fill
      nodes.hovered().stroke("#CFCFCF", 3);
      nodes.selected().stroke("#CFCFCF", 3);
      chart.layout().iterationCount(0); // set circle shape
      chart.interactivity().nodes(false); // disallow moving nodes

      chart.container("container").draw();
    });
});
