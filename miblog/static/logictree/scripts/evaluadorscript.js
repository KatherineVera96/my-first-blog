$(function(){
	$('#btnCalcular').click(function(){		
		console.log($('#i_funcion').val())
		console.log($('#i_x').val())
		$.ajax({
			type : 'POST',
			url : 'calcular',
			data : {
				'funcion' : $('#i_funcion').val(),
				'x' : $('#i_x').val(),
			},
			success : answer,
			error : error,
			dataType: 'json'
		});
	});
});

function answer(data, textStatus, jqXHR){	
	var arr = Object.values(data);
	console.log("Resultado: " + arr[0]);	

	document.getElementById("i_resultado").value = arr[0];	
}

function error (xhr, ajaxOptions, thrownError) {
    alert(xhr.status);
    alert(thrownError);
}