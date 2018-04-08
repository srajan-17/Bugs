function gifSearch(searchTerm) {
	fetch(
		"https://api.giphy.com/v1/gifs/search?api_key=FILLERFORAPIKEY&q="+encodeURIComponent(searchTerm),
		{
			mode:"cors"
		}
	)
	.then(response => response.json())

	.then(giphyResponse => {
		console.log(giphyResponse);
		var entities = document.querySelectorAll('a-entity');
		for (var i=0; i<entities.length; i++){
			var entity = entities[i];
			console.log(entity);
			var url = giphyResponse.data[0].images.original.url;
			console.log(url);
			console.log(entity.setAttribute('material', 'src', 'url('+url+')'));
		}
	})
}

document.querySelector('a-scene').addEventListener('loaded', function(){
	setTimeout(function() {
		var a = "ants";
		gifSearch(a);
	}, 1000);
})
