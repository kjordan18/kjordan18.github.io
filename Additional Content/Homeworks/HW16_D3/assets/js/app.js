// D3 Scatterplot Assignment

// Students:
// =========
// Follow your written instructions and create a scatter plot with D3.js.

var svgWidth = 960;
var svgHeight = 500;

var margin = {
  top: 20,
  right: 40,
  bottom: 80,
  left: 100
};

var width = svgWidth - margin.left - margin.right;
var height = svgHeight - margin.top - margin.bottom;

// Create an SVG wrapper, append an SVG group that will hold our chart,
// and shift the latter by left and top margins.
var svg = d3
  .select(".chart")
  .append("svg")
  .attr("width", svgWidth)
  .attr("height", svgHeight);

// Append an SVG group
var chartGroup = svg.append("g")
  .attr("transform", `translate(${margin.left}, ${margin.top})`);

// Initial Params
var chosenXAxis = "lesshs";
var chosenYAxis = "more5";

// function used for updating x-scale var upon click on axis label
function xScale(dataSet, chosenXAxis) {
  // create scales
  var xLinearScale = d3.scaleLinear()
    .domain([d3.min(dataSet, d => d[chosenXAxis]) * 0.8,
      d3.max(dataSet, d => d[chosenXAxis]) * 1.2
    ])
    .range([0, width]);

  return xLinearScale;

}
// function used for updating y-scale var upon click on axis label
function yScale(dataSet, chosenYAxis) {
  // create scales
  var yLinearScale = d3.scaleLinear()
    .domain([d3.min(dataSet, d => d[chosenYAxis]) * 0.8,
      d3.max(dataSet, d => d[chosenYAxis]) * 1.2
    ])
    .range([height, 0]);

  return yLinearScale;

}

// function used for updating xAxis var upon click on axis label
function renderXAxes(newXScale, xAxis) {
  var bottomAxis = d3.axisBottom(newXScale);

  xAxis.transition()
    .duration(1000)
    .call(bottomAxis);

  return xAxis;
}
// function used for updating yAxis var upon click on axis label
function renderYAxes(newYScale, yAxis) {
  var leftAxis = d3.axisLeft(newYScale);

  yAxis.transition()
    .duration(1000)
    .call(leftAxis);

  return yAxis;
}

// function used for updating circles group with a transition to
// new circles
function renderCircles(circlesGroup, newXScale, newYScale, chosenXAxis, chosenYAxis) {

  circlesGroup.transition()
    .duration(1000)
    .attr("cx", d => newXScale(d[chosenXAxis]))
    .attr("cy", d => newYScale(d[chosenYAxis]));

  return circlesGroup;
}

// function used for updating circles group with new tooltip
function updateToolTip(chosenXAxis, chosenYAxis, circlesGroup) {

  if (chosenXAxis === "college" && chosenYAxis === 'more5') {
    var label = "% Attended College";
    var labely = "% Women 5+ Children";
  } else if (chosenXAxis === 'college' && chosenYAxis === 'three'){
    var label = "% Attended College";
    var labely = "% Women 3 Children";
  } else if (chosenXAxis === 'lesshs' && chosenYAxis === 'more5') {
    var label = "% Not Graduated High School";
    var labely = "% Women 5+ Children";
  } else  {
    var label = "% Not Graduated High School";
    var labely = "% Women 3 Children";
  }

  var toolTip = d3.tip()
    .attr("class", "tooltip")
    .offset([80, -60])
    .html(function(d) {
      return (`${d.State}<br>${label} ${d[chosenXAxis]}<hr> ${labely} ${d[chosenYAxis]}`);
    });

  circlesGroup.call(toolTip);

  circlesGroup.on("mouseover", function(data) {
    toolTip.show(data);
  })
    // onmouseout event
    .on("mouseout", function(data, index) {
      toolTip.hide(data);
    });

  return circlesGroup;
}



// Retrieve data from the CSV file and execute everything below
d3.csv("/assets/data/data.csv", function(err, dataSet) {
  if (err) throw err;
  // parse data
  dataSet.forEach(function(data) {
    data.lesshs = +data.lesshs;
    data.college = +data.college;
    data.three = +data.three;
    data.four = +data.four;
    data.more5 = +data.more5;
    data.none = +data.none;

    console.log(data.Abbr)
  });

  // xLinearScale function above csv import
  var xLinearScale = xScale(dataSet, chosenXAxis);

  // Create y scale function
  var yLinearScale = d3.scaleLinear(dataSet, chosenYAxis)
    .domain([0, d3.max(dataSet, d => d.more5)])
    .range([height, 0]);

  // Create initial axis functions
  var bottomAxis = d3.axisBottom(xLinearScale);
  var leftAxis = d3.axisLeft(yLinearScale);

  // append x axis
  var xAxis = chartGroup.append("g")
    .classed("x-axis", true)
    .attr("transform", `translate(0, ${height})`)
    .call(bottomAxis);

  // append y axis
  var yAxis = chartGroup.append("g")
    .call(leftAxis);

  // append initial circles
  var circlesGroup = chartGroup.selectAll("circle")
    .data(dataSet)
    .enter()
    .append("circle")
    .attr("cx", d => xLinearScale(d[chosenXAxis]))
    .attr("cy", d => yLinearScale(d[chosenYAxis]))
    .attr("r", 20)
    .attr("fill", "blue")
    .attr("opacity", ".75");

  // append text
  // var circlesGroup = chartGroup.selectAll("text.abbr")
  // .data(dataSet)
  // .enter()
  // .append("text")
  // .text(d => d.Abbr)
  // .attr("dx", d => xLinearScale(d[chosenXAxis]))
  // .attr("dy", d => yLinearScale(d[chosenYAxis]))
  // .style("font", "10px sans serif")
  // .style("text-align", 'middle')
  // .style("fill", "black")

  // Create group for  2 x and y - axis labels
  var labelsGroupX = chartGroup.append("g")
    .attr("transform", `translate(${width / 2}, ${height + 20})`)
  
  // append 
  var collegeLabel = labelsGroupX.append("text")
    .attr("x", 0)
    .attr("y", 20)
    .attr("value", "college") // value to grab for event listener
    .classed("active", true)
    .text("% of Women > College");

  var hsLabel = labelsGroupX.append("text")
    .attr("x", 0)
    .attr("y", 40)
    .attr("value", "lesshs") // value to grab for event listener
    .classed("inactive", true)
    .text("% of Women with < HS");

  // label group y
  labelsGroupY = chartGroup.append("g")
    .attr("transform", `translate(${width - 770}, ${height / 3})`);
  
  // append y axis
  var more5label = labelsGroupY.append("text")
    .attr("transform", "rotate(-90)")
    .attr("y", 0 - margin.left)
    .attr("x", 0 - (height / 2))
    .attr("dy", "1em")
    .attr("value", "more5") // event listener for more5
    .classed("axis-text", true)
    .text("% of Women with 5+ Children");

  var fourlabel = labelsGroupY.append("text")
    .attr("transform", "rotate(-90)")
    .attr("y", 0 - margin.left - 20)
    .attr("x", 0 - (height / 2))
    .attr("dy", "1em")
    .attr("value", "four") // event listener for three
    .classed("inactive", true)
    .text("% of Women with 4 Children");

  var threelabel = labelsGroupY.append("text")
    .attr("transform", "rotate(-90)")
    .attr("y", 0 - margin.left - 40)
    .attr("x", 0 - (height / 2))
    .attr("dy", "1em")
    .attr("value", "three") // event listener for three
    .classed("inactive", true)
    .text("% of Women with 3 Children");

  // updateToolTip function above csv import
  var circlesGroup = updateToolTip(chosenXAxis, chosenYAxis, circlesGroup);

  // x axis labels event listener
  labelsGroupX.selectAll("text")
    .on("click", function() {
      // get value of selection
      var value = d3.select(this).attr("value");
      if (value !== chosenXAxis) {
        if (value === "college" || value === 'lesshs'){
          // replaces chosenXAxis with value
          chosenXAxis = value;

          console.log(chosenXAxis)
  
          // updates x scale for new data
          xLinearScale = xScale(dataSet, chosenXAxis);
  
          // updates x + y axis with transition
          xAxis = renderXAxes(xLinearScale, xAxis);
  
          // updates circles with new x values
          circlesGroup = renderCircles(circlesGroup, xLinearScale, yLinearScale, chosenXAxis, chosenYAxis);
  
          // updates tooltips with new info
          circlesGroup = updateToolTip(chosenXAxis, chosenYAxis, circlesGroup);
  
          // changes X classes to change bold text
          if (chosenXAxis === "lesshs") {
            hsLabel
              .classed("active", true)
              .classed("inactive", false);
            collegeLabel
              .classed("active", false)
              .classed("inactive", true);
          }
          else {
            collegeLabel
              .classed("active", false)
              .classed("inactive", true);
            hsLabel
              .classed("active", true)
              .classed("inactive", false);
          }
        }
      }
    });
        
        
  labelsGroupY.selectAll("text")
    .on("click", function() {
      // get value of selection
      var value = d3.select(this).attr("value");
      if (value !== chosenYAxis) {
        if (value === "four" || value === 'three' || value === 'more5'){
          chosenYAxis = value;
          console.log(chosenYAxis)
          yLinearScale = yScale(dataSet, chosenYAxis);
          yAxis = renderYAxes(yLinearScale, yAxis);
    
          // updates circles with new x values
          circlesGroup = renderCircles(circlesGroup, xLinearScale, yLinearScale, chosenXAxis, chosenYAxis);
    
          // updates tooltips with new info
          circlesGroup = updateToolTip(chosenXAxis, chosenYAxis, circlesGroup);
    
          // changes Y classes to change bold text
          if (chosenYAxis === "more5") { //more5 label true
            more5label
              .classed("active", true)
              .classed("inactive", false);
            fourlabel
              .classed('active', false)
              .classed('inactive', true);
            threelabel
              .classed("active", false)
              .classed("inactive", true);
          } else if (chosenYAxis === 'four') { // fourlabel true
            more5label
              .classed("active", false)
              .classed("inactive", true);
            fourlabel
              .classed('active', true)
              .classed('inactive', false);
            threelabel
              .classed("active", false)
              .classed("inactive", true);
          } else { //threelabel true
            more5label
              .classed("active", false)
              .classed("inactive", true);
            fourlabel
              .classed('active', false)
              .classed('inactive', true);
            threelabel
              .classed("active", true)
              .classed("inactive", false);
          }
        }
      }  
    });
  });

