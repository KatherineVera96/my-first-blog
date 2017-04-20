var numero, representacion;

$(function(){

	$('#i_decimal').keyup(function(){		
		numero = $('#i_decimal').val();
		representacion = 'decimal';
		ajax();
	});
	$('.32').keyup(function(){
		if($('#input_signo32').val().length == 1 && $('#input_exponente32').val().length == 8 && $('#input_mantisa32').val().length == 23){
			console.log('32BIT SUCCESS');
			numero = $('#input_signo32').val() + $('#input_exponente32').val() + $('#input_mantisa32').val();
			representacion = 'ieee32';
			ajax();
		}
		});

	$('.64').keyup(function(){
		if($('#input_signo64').val().length == 1 && $('#input_exponente64').val().length == 11 && $('#input_mantisa64').val().length == 52){
			console.log('64BIT SUCCESS');
			numero = $('#input_signo64').val() + $('#input_exponente64').val() + $('#input_mantisa64').val();
			representacion = 'ieee64';
			ajax();
		}
	});

});

function ajax(){
	$.ajax({
		type : 'POST',
		url : 'calcular',
		data : {
			'numero' : numero,
			'representacion' : representacion,
		},
		success : answer,
		error : error,
		dataType: 'json'
	});
}

function answer(data, textStatus, jqXHR){	
	console.log("Json: " + data);	
	var arr = Object.values(data);
	console.log("HOLAAAA");
	if(arr[0] == 'decimal' && arr[0] != false){
		$('#input_signo32').attr('value', arr[2].split("-")[0]);
		$('#input_exponente32').attr('value', arr[2].split("-")[1]);
		$('#input_mantisa32').attr('value', arr[2].split("-")[2]);
		$('#input_signo64').attr('value', arr[3].split("-")[0]);
		$('#input_exponente64').attr('value', arr[3].split("-")[1]);
		$('#input_mantisa64').attr('value', arr[3].split("-")[2]);
	}
	if(arr[0] == 'ieee32'){
		$('#i_decimal').attr('value', arr[1]);
		$('#i_octal').attr('value', arr[3]);
	}
	if(arr[0] == 'ieee64'){
		$('#i_decimal').attr('value', arr[1]);
		$('#i_binaria').attr('value', arr[2]);		
	}
}

function error (xhr, ajaxOptions, thrownError) {
    alert(xhr.status);
    alert(thrownError);
}