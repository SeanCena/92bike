const parse = require('csv-parse')
const fs = require('fs')

const file = "./Crime_Data_from_2010_to_Present.csv";

let index = 0;
const readStream = fs.createReadStream(file);

var writeStream = fs.createWriteStream('points.py', { flags : 'w' });
//writeStream.write("function getPoints() { return [");
writeStream.write("points = [");

//let map = {};
let data = [];

let count = 0;
readStream
  .on('data', function (chunk) {
    //if (index++ == 10) {
      //readStream.destroy();
      //onEnd();
    //}

    let strChunk = chunk.toString();
    strChunk.split('\n')
      .forEach(row => {
        let coordinates = row.slice(row.indexOf("\"(")).slice(1,-1)
        if (coordinates) {
          //if (map[coordinates]) {
            //map[coordinates]++;
          //} else {
            //map[coordinates] = 0;
          //}
          data.push(coordinates);
        }
      })
  })
  .on('end', function () {
      onEnd();
  })


function onEnd() {
  for (let i = 0; i < data.length; i++)
  {
    let coord = data[i];
    if (coord.indexOf(",") >= 0 && coord.indexOf(")") >= 0)
    {
      //let result = "new google.maps.LatLng" + coord + "," + "\n";
      writeStream.write("[" + coord.slice(1,-1) + "],\n");
    }
  }
  //writeStream.write("] }");
  writeStream.write("]");
}
