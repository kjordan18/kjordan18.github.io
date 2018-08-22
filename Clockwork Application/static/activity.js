
function buildPlot() {
  var url = "/test";

      Plotly.d3.json(url, function(error, response) {
        console.log(response[1])
      // var x1 = response[0]['x']
      // var y1=response[0]['y']
      var sumLength1=0
        for(var i=0; i<(response[0]['y']).length; i++){
          sumLength1=sumLength1+(response[0]['y'][i]);
          // console.log(response[0]['y'][i])
        }
  
        if(sumLength1>0){
          
          var data1 = [{
            x:response[0]['x'],
            y:response[0]['y'],
            type: 'bar',
          }]

          var layout = {
            title: "1st User Activity (Count vs Activity Type)",
            xaxis: {
            // title: "Activity Type"
         },
            yaxis: {
            title: "Count"
          }
        };

          Plotly.newPlot("plotter1", data1, layout)

          // var pieData1 = [{
          //   labels:response[0]['x'],
          //   values:response[0]['y'],
          //   type: 'pie',
          //   name: "User 1:"
          // }]
          // var layoutPie1 = {
          //   title: "1st User Activity",
          //   height: 400,
          //   width: 500
          // };
          // // console.log(pieData2)
          
          // Plotly.newPlot('piePlotter1', pieData1,layoutPie1);
        }

  var sumLength=0
      for(var i=0; i<(response[1]['y']).length; i++){
        sumLength=sumLength+(response[1]['y'][i]);
        console.log(response[1]['y'][i])
      }

      if(sumLength>0){


        var data2 = [{
          x:response[1]['x'],
          y:response[1]['y'],
          type: 'bar',
        }]
        
      var layout = {
          title: "2nd User Activity (Count vs Activity Type)",
          xaxis: {
          // title: "Activity Type"
       },
          yaxis: {
          title: "Count"
        }
      };
      
      // var data = [[data1], [data2]]
      // console.log(data)
      // Plotly.newPlot("plotter", data1, layout);
      Plotly.newPlot("plotter2", data2, layout)



        // var pieData2 = [{
        //   labels:response[1]['x'],
        //   values:response[1]['y'],
        //   type: 'pie',
        //   title: "User 2:"
        // }]
        // var layoutPie2 = {
        //   title: "2nd User Activity",
        //   height: 400,
        //   width: 500
        // };
        // Plotly.newPlot('piePlotter2', pieData2,layoutPie2);
        // console.log(sumLength)
      }

      var data = [{
        values: response[0]['y'],
        labels: response[0]['x'],
        domain: {
          x: [0, .48]
        },
        name: '1st User Activity',
        hoverinfo: 'label+percent+name',
        hole: .4,
        type: 'pie',
        marker: {'color': ['#009cf6']}
      },{
        values: response[1]['y'],
        labels: response[1]['x'],
        // text: 'CO2',
        // textposition: 'inside',
        domain: {x: [.52, 1]},
        name: '2nd User Activity',
        hoverinfo: 'label+percent+name',
        hole: .4,
        type: 'pie'
      }];
      
      var layout = {
        title: 'User Activity',
        // annotations: [
        //   {
        //     font: {
        //       size: 14
        //     },
        //     showarrow: false,
        //     // text: 'User 1',
        //     x: 0.19,
        //     y: 0.5
        //   },
        //   {
        //     font: {
        //       size: 14
        //     },
        //     showarrow: false,
        //     // text: 'User 2',
        //     x: 0.8,
        //     y: 0.5
        //   }
        // ]
      };
      
      Plotly.newPlot('piePlotter2', data, layout);
      
    });

}
buildPlot()

