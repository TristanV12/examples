/*
	checkBase is a helper function for checking if the base is between 2 and 16 (inclusive)
*/
function checkBase(base, function_name){
	if(!Number.isInteger(base) || base < 2 || base > 16){
		throw "Error: base must be an integer between 2 and 16 (inclusive).";
	}
}

/*
	toDecimal is meant to be a helper function that converts a number represented
		as a string into an integer
	num must be a string representation of the to be converted (must represent a non-negative
		integer)
	from_base must be a base between 2 and 16 (inclusive)
*/
function toDecimal(num, from_base){
	var multiplier = 1;
	var output = 0;

	// Error checking
	checkBase(from_base);
	for (var i = num.length - 1; i >= 0; --i){
		var digit = num[i].charCodeAt(0) - 48;
		if(digit > 9){
			digit = digit - 7;
		}

		if(digit >= from_base || digit < 0){
			throw "Something is wrong: num is invalid for that base. In toDecimal.";
		}
		output = output + (digit * multiplier);
		multiplier = multiplier * from_base;
	}
	return output;
}

/*
	stringify is a helper function for converting a digit to its string representation.
*/
function stringify(num){
	if(num > 9){
		return String.charCodeAt(num);
	}else{
		return num.toString();
	}
}

/*
	baseConvert is a function that converts a string representation of a number num
		from base from_base to a base to_base
*/
function baseConvert(num, from_base, to_base){
	var tmp_num = toDecimal(num, from_base);
	var string = "";
	checkBase(to_base);
	while(tmp_num > 0){
		string = stringify(tmp_num % to_base) + string;
		tmp_num = Math.floor(tmp_num/to_base);
	}
	return string;
}

// All code below this line is for visualization on my website

// Use JQuery
$("#from_base").selectmenu();
$("#to_base").selectmenu();

// When button has been clicked, convert the number
$("#convert").click(function(){
	var num = $("#from_value").val();
	var from_base = parseInt($("#from_base").val());
	var to_base = parseInt($("#to_base").val());
	// Show
	$("#base_convert").html(baseConvert(num, from_base, to_base));
});