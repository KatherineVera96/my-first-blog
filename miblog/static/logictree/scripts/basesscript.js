$(function(){
	$('#i_decimal').keyup(function(){		
		$.ajax({
			type : 'POST',
			url : 'calcular',
			data : {
				'numero' : $('#i_decimal').val(),
				'base' : 'decimal',
			},
			success : answer,
			error : error,
			dataType: 'json'
		});
	});
	$('#i_binaria').keyup(function(){
		$.ajax({
			type : 'POST',
			url : 'calcular',
			data : {
				'numero' : $('#i_binaria').val(),
				'base' : 'binaria'
			},
			success : answer,
			error : error,
			dataType: 'json'
		});
	});
	$('#i_octal').keyup(function(){
		$.ajax({
			type : 'POST',
			url : 'calcular',
			error : error,
			data : {
				'numero' : $('#i_octal').val(),
				'base' : 'octal'
			},
			success : answer,
			error : error,
			dataType: 'json'
		});
	});
	$('#i_hexadecimal').keyup(function(){
		$.ajax({
			type : 'POST',
			url : 'calcular',
			data : {
				'numero' : $('#i_hexadecimal').val(),
				'base' : 'hexadecimal'
			},
			success : answer,
			error : error,
			dataType: 'json'
		});
	});
});

function answer(data, textStatus, jqXHR){	
	console.log("Json: " + data);	
	var arr = Object.values(data);
	if(arr[0] == 'decimal' && arr[0] != false){
		$('#i_binaria').attr('value', arr[2]);
		$('#i_octal').attr('value', arr[3]);
		$('#i_hexadecimal').attr('value', arr[4]);
	}
	if(arr[0] == 'binaria'){
		$('#i_decimal').attr('value', arr[1]);
		$('#i_octal').attr('value', arr[3]);
		$('#i_hexadecimal').attr('value', arr[4]);
	}
	if(arr[0] == 'octal'){
		$('#i_decimal').attr('value', arr[1]);
		$('#i_binaria').attr('value', arr[2]);		
		$('#i_hexadecimal').attr('value', arr[4]);
	}
	if(arr[0] == 'hexadecimal'){
		$('#i_decimal').attr('value', arr[1]);
		$('#i_binaria').attr('value', arr[2]);
		$('#i_octal').attr('value', arr[3]);		
	}
}

function error (xhr, ajaxOptions, thrownError) {
    alert(xhr.status);
    alert(thrownError);
}