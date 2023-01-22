anychart.onDocumentReady(function () {
  fetch("./anygraph.json")
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
      // var chart = anychart.graph(data);
      // var nodes = chart.nodes();
      // var edges = chart.edges();
      console.log("Number of Nodes:");
      // chart.title("UBC Course Dependencies Graph");

      /**
       * APPEARANCE
       */
      // EDGES
      var chart = anychart.graph();
      chart.data(data);
      // chart.title().enabled(true).text("UBC Coursemap");

      var edgeConfig = {
        normal: {stroke: {thickness: 2, color: 'orange'}},
        hovered: {stroke: {thickness: 4, color: 'blue'}},
        tooltip: {enabled:true, format: 'edge id: {%id}'}
      };
      var nodeConfig = {
        normal: {stroke: {thickness: 2, color: "#F3F3F5"}, fill: "#F0F0F0"},
        hoevered: {stroke: {thickness: 3, color: "#CFCFCF"}},
        selected: {stroke: {thickness: 3, color: "#CFCFCF"}}
        // size:
      }
      chart.edges(edgeConfig);
      chart.nodes(nodeConfig);
      // edges.normal().height(1)
      // edges.normal().stroke("#F3F3F5", 2);
      // edges.selected().fill("#000000", 2);
      // edges.selected().stroke("#000000", 2);

      // NODES
      // nodes.normal().height(5);
      // nodes.normal().stroke(null);

      // nodes.normal().fill("#F0F0F0"); // unselected fill
      // nodes.hovered().stroke("#CFCFCF", 3);
      // nodes.selected().stroke("#CFCFCF", 3);
      // chart.layout().iterationCount(0); // set circle shape
      chart.layout().type('fixed');
      chart.interactivity().nodes(false); // disallow moving nodes
      // chart.interactivity().enabled(false);

      chart.container("container").draw();
    });
});
