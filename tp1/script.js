var data = [{'p': 'make', 'c': 2}, {'p': 'describing', 'c': 2}, {'p': 'this', 'c': 2}, {'p': 'unstructured', 'c': 2}, {'p': 'properties', 'c': 2}, {'p': 'user', 'c': 3}, {'p': 'large', 'c': 3}, {'p': 'Card', 'c': 3}, {'p': 'such', 'c': 3}, {'p': 'human', 'c': 3}, {'p': 'important', 'c': 3}, {'p': 'sometimes', 'c': 3}, {'p': 'visualizations', 'c': 3}, {'p': 'attributes', 'c': 3}, {'p': 'more', 'c': 3}, {'p': 'science', 'c': 3}, {'p': 'image', 'c': 3}, {'p': 'al', 'c': 3}, {'p': 'coordinates', 'c': 3}, {'p': 'do', 'c': 3}, {'p': 'items', 'c': 3}, {'p': 'charts', 'c': 3}, {'p': 'which', 'c': 3}, {'p': 'et', 'c': 3}, {'p': 'Examples', 'c': 3}, {'p': 'scientific', 'c': 3}, {'p': 'each', 'c': 3}, {'p': 'In', 'c': 3}, {'p': 'makes', 'c': 3}, {'p': 'kind', 'c': 3}, {'p': 'different', 'c': 3}, {'p': 'screen', 'c': 3}, {'p': 'graphics', 'c': 4}, {'p': 'called', 'c': 4}, {'p': 'amplify', 'c': 4}, {'p': 'criteria', 'c': 4}, {'p': 'interactive', 'c': 4}, {'p': 'interaction', 'c': 4}, {'p': 'techniques', 'c': 4}, {'p': 'not', 'c': 5}, {'p': 'cognition', 'c': 5}, {'p': 'on', 'c': 5}, {'p': 'has', 'c': 5}, {'p': 'be', 'c': 5}, {'p': 'can', 'c': 5}, {'p': 'use', 'c': 5}, {'p': 'records', 'c': 5}, {'p': 'it', 'c': 6}, {'p': 'that', 'c': 6}, {'p': 'This', 'c': 6}, {'p': 'representations', 'c': 6}, {'p': 'Visualization', 'c': 6}, {'p': 'as', 'c': 6}, {'p': 'graphical', 'c': 6}, {'p': 'an', 'c': 6}, {'p': 'with', 'c': 6}, {'p': 'computer', 'c': 7}, {'p': 'eg', 'c': 7}, {'p': 'space', 'c': 8}, {'p': 'visual', 'c': 8}, {'p': 'The', 'c': 9}, {'p': 'Information', 'c': 10}, {'p': 'or', 'c': 10}, {'p': 'for', 'c': 11}, {'p': 'abstract', 'c': 11}, {'p': 'are', 'c': 12}, {'p': 'information', 'c': 19}, {'p': 'is', 'c': 21}, {'p': 'visualization', 'c': 22}, {'p': 'in', 'c': 24}, {'p': 'a', 'c': 24}, {'p': 'and', 'c': 27}, {'p': 'to', 'c': 31}, {'p': 'the', 'c': 32}, {'p': 'data', 'c': 34}, {'p': 'of', 'c': 51}]
;

var sizeScale = d3.scale.linear()
                      .domain([1,100])
                      .range([10,50]);

var colorScale = d3.scale.linear()
                         .domain([1,100])
                         .range(["#ff4d4d", "#000000"]);

d3.select("div#data")
  .selectAll("span")
  .data(data)
  .enter()
  .append("span")
  .text(function(d){return d.p+" ";})
  .style("font-size", function(d){return sizeScale(d.c)+"px";})
  .style("color", function(d){ return colorScale(d.c);});

