$("#submit").click(function (e) {
	e.preventDefault();
	var name  = $("#id_name").val();
	url  = $("#id_full_url").val();
	if( !name ) {
		alert('Enter the Name field');
		return false;
	}
	if( !url ) {
		alert('Enter the URL field');
		return false;
	}
	if ( !(/^(http|https|ftp):\/\/[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(\/.*)?$/i.test(url))){
		alert('Invalid');
		return false;
	} 
	var form = $(this).closest("form");
	$.ajax({
		url: form.attr("data-validate-username-url"),
		data: form.serialize(),
		dataType: 'json',
		method:"POST",
		success: function (data) {
			console.log(data)
			if (data.is_taken) {
				alert(data.error_message);
			}
			$("#url").html("<p>Short URL is :<a target='_blank' href='"+data.short_url+"'>"+data.short_url+"</p>")
		}
	});
});