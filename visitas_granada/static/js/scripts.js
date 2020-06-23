$(function() {
	document.body.setAttribute('data-theme', localStorage.getItem('data-theme'));

	if(localStorage.getItem('data-theme') === 'dark'){
		$('#darkmode').prop('checked', false).change();
	}

	$('#darkmode').change(function() {
		if($(this).prop("checked")){
			document.body.setAttribute('data-theme', '');
			localStorage.setItem('data-theme', '');
		}
		else{
			document.body.setAttribute('data-theme', 'dark');
			localStorage.setItem('data-theme', 'dark');
		}
	})
})
