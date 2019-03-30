const parse = require('csv-parse')
const fs = require('fs')
const child_process =  require('child_process');

const file = "./Crime_Data_from_2010_to_Present.csv";
const outputFile = "getpoints.js"

const outputStream = fs.createWriteStream('getpoints.js', { flags: 'w' });
outputStream.write('function getPoints(time) {\n');

function dataExtractor(time) {
  return new Promise((res, rej) => {
    const readStream = fs.createReadStream(file);
    const writeStream = fs.createWriteStream('points.py', { flags : 'w' });
    writeStream.write("points = [");
    outputStream.write("if (time == '" + time + "') { return [\n");

    let data = [];

    readStream
      .on('data', function (chunk) {
        let strChunk = chunk.toString();
        strChunk.split('\n')
          .forEach(row => {
            let t = row.split(",")[3];
            if (t) {
              if (t[0] == time[0] && t[1] == time[1])
              {
                let coordinates = row.slice(row.indexOf("\"(")).slice(1,-1)
                if (coordinates) {
                  data.push(coordinates);
                }
              }
            }
          })
      })
      .on('end', function () {
        onEnd();
      });

    function onEnd() {
      for (let i = 0; i < data.length; i++)
      {
        let coord = data[i];
        if (coord.indexOf(",") >= 0 && coord.indexOf(")") >= 0)
        {
          writeStream.write("[" + coord.slice(1,-1) + "],\n");
        }
      }

      writeStream.write("]");

      writeStream.end();

      writeStream.on('finish', function() {
        child_process.exec("python analysis.py", (err, stdout, stderr) => {
          if (err) {
            console.log(err);
            rej();
            return;
          }

          outputStream.write(stdout);

          res();
        });
      });
    }
  });
}

dataExtractor("00")
.then(() => dataExtractor("01"))
.then(() => dataExtractor("02"))
.then(() => dataExtractor("03"))
.then(() => dataExtractor("04"))
.then(() => dataExtractor("05"))
.then(() => dataExtractor("06"))
.then(() => dataExtractor("07"))
.then(() => dataExtractor("08"))
.then(() => dataExtractor("09"))
.then(() => dataExtractor("10"))
.then(() => dataExtractor("11"))
.then(() => dataExtractor("12"))
.then(() => dataExtractor("13"))
.then(() => dataExtractor("14"))
.then(() => dataExtractor("15"))
.then(() => dataExtractor("16"))
.then(() => dataExtractor("17"))
.then(() => dataExtractor("18"))
.then(() => dataExtractor("19"))
.then(() => dataExtractor("20"))
.then(() => dataExtractor("21"))
.then(() => dataExtractor("22"))
.then(() => dataExtractor("23"))
.then(() => outputStream.write("}"))
