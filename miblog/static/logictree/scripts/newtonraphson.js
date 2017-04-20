$(function(){
	$('#btnCalcular').click(function(){				
		$.ajax({
			type : 'POST',
			url : 'calcular',
			data : {
				'funcion' : $('#i_funcion').val(),
				'x0' : $('#i_x0').val(),
				'error' : $('#i_er').val(),				
			},
			success : answer,
			error : error,
			dataType: 'json'
		});
	});
});

function answer(data, textStatus, jqXHR){	
	var arr = Object.values(data);
	console.log("Resultado: " + data);	

	document.getElementById("i_resultado").value = arr[arr.length-1][1];	


	for (var i = 0; i < arr.length; i++) {
		for (var j = 0; j < arr[i].length; j++) {

			var p = document.createElement("P");
			var t = document.createTextNode(arr[i][j] + '-');  
			p.appendChild(t);
			p.className += " " + 'inline';
			document.getElementById("div_tabla").appendChild(p); 
		}
		document.getElementById("div_tabla").appendChild(document.createElement("BR")); 
	}
	
	
}

function error (xhr, ajaxOptions, thrownError) {
    console.log(xhr.status);
    console.log(thrownError);
}