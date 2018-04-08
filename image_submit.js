//var i = 0;

//function hello() {
//  i = i + 1;
//  console.log("hello" + i);

//}
import { fileinput.value } from './image_upload.js';
const Clarifai = require('clarifai');

const app = new Clarifai.App({
  apiKey: 'c4406989d7624ad0aa336616ea3e4ada'
});

app.models.predict(Clarifai.GENERAL_MODEL, fileinput.value).then(
  function(response) {
    console.log(response);
  }
  function(err) {

  }
);
