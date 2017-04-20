$(function(){

	//decimal
	$('.decimal').on("keydown", function(event){
		//console.log(event.which);
		if (!((event.which >= 48 && event.which <= 57) || (event.which >= 96 && event.which <= 105) || (event.which >=33 && event.which <= 35) || (event.which == 46) || (event.which == 8) || (event.which == 190) || (event.which >=37 && event.which <= 40))) {     		   		
    		event.preventDefault();
		}		
	});
	//binario
	$('.binario').on("keydown", function(event){
		//console.log(event.which);
		if (!((event.which >= 48 && event.which <= 49) || (event.which >= 96 && event.which <= 97) || (event.which >=33 && event.which <= 35) || (event.which == 46) || (event.which == 8) || (event.which == 190) || (event.which >=37 && event.which <= 40) || (event.which == 189) || (event.which == 109))) {     		   		
    		event.preventDefault();
		}		
	});
	//octal
	$('.octal').on("keydown", function(event){
		//console.log(event.which);
		if (!((event.which >= 48 && event.which <= 55) || (event.which >= 96 && event.which <= 105) || (event.which >=33 && event.which <= 35) || (event.which == 46) || (event.which == 8) || (event.which == 190) || (event.which >=37 && event.which <= 40))) {     		   		
    		event.preventDefault();
		}		
	});
	//hexadecimal
	$('.hexadecimal').on("keydown", function(event){
		//console.log(event.which);
		if (!((event.which >= 48 && event.which <= 57) || (event.which >= 65 && event.which <= 70) || (event.which >= 96 && event.which <= 105) || (event.which >=33 && event.which <= 35) || (event.which == 46) || (event.which == 8) || (event.which == 190) || (event.which >=37 && event.which <= 40))) {     		   		
    		event.preventDefault();
		}		
	});
	//ieee
	$('.ieee').on("keydown", function(event){
		//console.log(event.which);
		if (!((event.which >= 48 && event.which <= 49) || (event.which >= 96 && event.which <= 105) || (event.which >=33 && event.which <= 35) || (event.which == 46) || (event.which == 8) || (event.which >=37 && event.which <= 40))) {     		   					
    		event.preventDefault();
		}	
		//console.log(String($("#input_signo32").val()).length);
		//console.log(event.target.id);
		if(event.target.id == 'input_signo32' &&  String($('#input_signo32').val()).length > 0 && event.which == 46 && (event.which <=37 && event.which >= 40)){
			event.stopPropagation();	
			event.preventDefault();
		}		
	});
	//funcion
	$('.funcion').on("keydown", function(event){
				
	});
	$('#btnLimpiar').click(function(){
		console.log("ssad");
		var i = 1;
		while(i < document.getElementsByTagName("input").length) {
			document.getElementsByTagName("input")[i].value = '';
			console.log(document.getElementsByTagName("input")[i].id);
			i++;
		}
	});
	
});