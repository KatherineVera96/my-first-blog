$(function(){
	$('#btnCalcular').click(function(){
		if($('#i_funcion').val() != '' && $('#i_a').val() != '' && $('#i_b').val() != '' && $('#i_n').val() != ''){
			if(parseFloat($('#i_a').val()) < parseFloat($('#i_b').val())){
				$.ajax({
					type : 'POST',
					url : 'calcular',
					data : {
						'funcion' : $('#i_funcion').val(),
						'a' : $('#i_a').val(),
						'b' : $('#i_b').val(),
						'n' : $('#i_n').val(),
					},
					success : answer,
					error : error,
					dataType: 'json'
				});
			}else{
				alert('El lÃ­mite a debe ser menor que b.');
			}
		} else {
			alert('Todos los campos deben estar llenos.');
		}
	});
});

function answer(data, textStatus, jqXHR){
	var arr = Object.values(data);
	console.log("Resultado: " + data);

	document.getElementById("i_izquierda").value = arr[0];
	document.getElementById("i_medio").value = arr[1];
	document.getElementById("i_derecha").value = arr[2];
	document.getElementById("i_integral").value = arr[3];
	document.getElementById("i_real").value = arr[4];
	document.getElementById("i_difizquierda").value = Math.abs(parseFloat(arr[0])-parseFloat(arr[4]))
	document.getElementById("i_difmedio").value = Math.abs(parseFloat(arr[1])-parseFloat(arr[4]))
	document.getElementById("i_difderecha").value = Math.abs(parseFloat(arr[2])-parseFloat(arr[4]))
}

function error (xhr, ajaxOptions, thrownError) {
    console.log(xhr.status);
    console.log(thrownError);
}
