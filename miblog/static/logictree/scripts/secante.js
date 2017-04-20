$(function(){
	$('#btnCalcular').click(function(){
		//console.log($('#i_funcion').val())
		//console.log($('#i_a').val())
		$.ajax({
			type : 'POST',
			url : 'calcular',
			data : {
				'funcion' : $('#i_funcion').val(),
				'a' : $('#i_a').val(),
				'b' : $('#i_b').val(),
				'tolerancia' : $('#i_err').val(),
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
			var t = document.createTextNode(arr[i][j]);
			p.appendChild(t);
			p.className += " " + 'inline';
			document.getElementById("div_tabla").appendChild(p);
		}
		document.getElementById("div_tabla").appendChild(document.createElement("BR"));
	}


}

function error (xhr, ajaxOptions, thrownError) {
    alert(xhr.status);
    alert(thrownError);
}
