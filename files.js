function upload() {
	var imgcanvas = document.getElementById("canvas");
	var fileinput = document.getElementById("finput");
	//var image = new SimpleImage(fileinput);
	//image.drawTo(imgcanvas);
	//console.log(imgcanvas);
	console.log(fileinput.value);
	var canvas = document.getElementById("myCanvas");
	var ctx = canvas.getContext("2d");
	var img = document.getElementById(fileinput.value);
  ctx.drawImage(img, 10, 10);
}

function readURL(input) {
			 if (input.files && input.files[0]) {
					 var reader = new FileReader();
					 reader.onload = function (e) {
							 $('#blah').attr('src', e.target.result);
					 };
					 reader.readAsDataURL(input.files[0]);
			 }
			 var fileinput = document.getElementById("finput");
			 console.log(fileinput.value + " has been uploaded");
	 }
