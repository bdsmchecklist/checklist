// Parse the URL parameter
function getParameterByName(name, url) {
    if (!url) url = window.location.href;
    name = name.replace(/[\[\]]/g, "\\$&");
    var regex = new RegExp("[?&]" + name + "(=([^&#]*)|&|#|$)");
    results = regex.exec(url);
    if (!results) return null;
    if (!results[2]) return '';
    return decodeURIComponent(results[2].replace(/\+/g, " "));
}
// Give the parameter a variable name
var dom_set = getParameterByName('dom');
if (dom_set == null) {
    dom_set = "";
    for (i = 0; i < num_rows + 1; i++) {
	dom_set += '0';
    }
}
var sub_set = getParameterByName('sub');
if (sub_set == null) {
    sub_set = "";
    for (i =0; i < num_rows + 1; i++) {
	sub_set += '0';
    }
}


$(document).ready(function() {
    sum_dom = 0;
    sum_sub = 0;
    for (i = 0; i < num_rows; i++) {
	var result = parseInt(dom_set[num_rows - i - 1], 36);
	sum_dom += result;
	var a_result = result % 7;
	var e_result = Math.floor(result / 7);
	var e_group = "c1e" + i;
	if (e_result > 0)
	    $('input[name="' + e_group + '"]')[e_result - 1].checked = true;
	var a_group = "c1a" + i;
	if (a_result > 0)
	    $('input[name="' + a_group + '"]')[a_result - 1].checked = true;

	var result = parseInt(sub_set[num_rows - i - 1], 36);
	sum_sub += result;
	var a_result = result % 7;
	var e_result = Math.floor(result / 7);
	var e_group = "c2e" + i;
	if (e_result > 0)
	    $('input[name="' + e_group + '"]')[e_result - 1].checked = true;
	var a_group = "c2a" + i;
	if (a_result > 0)
	    $('input[name="' + a_group + '"]')[a_result - 1].checked = true;
    }
    if (sum_dom % 36 != parseInt(dom_set[num_rows], 36))
    	alert("Bad check digit for dom");
    if (sum_sub % 36 != parseInt(sub_set[num_rows], 36))
    	alert("Bad check digit for sub");
    if (sum_dom > 0) {
	for (i = 0; i < num_rows; i++) {
	    var e_group = "c1e" + i;
	    for (j = 0; j < 4; j++) {
		$('input[name="' + e_group + '"]')[j].disabled = true;
	    }
	    var a_group = "c1a" + i;
	    for (j = 0; j < 6; j++) {
		$('input[name="' + a_group + '"]')[j].disabled = true;
	    }
	}
    }
    if (sum_sub > 0) {
	for (i = 0; i < num_rows; i++) {
	    var e_group = "c2e" + i;
	    for (j = 0; j < 4; j++) {
		$('input[name="' + e_group + '"]')[j].disabled = true;
	    }
	    var a_group = "c2a" + i;
	    for (j = 0; j < 6; j++) {
		$('input[name="' + a_group + '"]')[j].disabled = true;
	    }
	}
    }
});


$(document).ready(function(){
    $('#submit').click(function() {
	var dom = ""
	var sub = ""
	var sum_dom = 0
	var sum_sub = 0
	for (i = 0; i < num_rows; i++) {
	    var e_group = 'c1e' + i;
	    var e_result = parseInt($('input[name="' + e_group + '"]:checked').val());
	    if (isNaN(e_result))
		e_result = 0;
	    var a_group = 'c1a' + i;
	    var a_result = parseInt($('input[name="' + a_group + '"]:checked').val());
	    if (isNaN(a_result))
		a_result = 0;
	    var component = e_result * 7 + a_result;
	    dom = component.toString(36) + dom;
	    sum_dom += component;

	    var e_group = 'c2e' + i;
	    var e_result = parseInt($('input[name="' + e_group + '"]:checked').val());
	    if (isNaN(e_result))
		e_result = 0;
	    var a_group = 'c2a' + i;
	    var a_result = parseInt($('input[name="' + a_group + '"]:checked').val());
	    if (isNaN(a_result))
		a_result = 0;
	    var component = e_result * 7 + a_result;
	    sub = component.toString(36) + sub;
	    sum_sub += component;
	}
	dom_checkdigit = sum_dom % 36;
	sub_checkdigit = sum_sub % 36;
	dom += dom_checkdigit.toString(36);
	sub += sub_checkdigit.toString(36);
	var url = window.location.href.split("?")[0];
	if (parseInt(dom, 36) > 0 & parseInt(sub, 36) > 0)
	    alert(url + "?dom=" + dom + "&sub=" + sub);
	else if (parseInt(dom, 36) > 0)
	    alert(url + "?dom=" + dom);
	else if (parseInt(sub, 36) > 0)
	    alert(url + "?sub=" + sub);
    });
});
