$(document).ready(function() {

	$('#detailView').hide();
	$('#profile-detailView').hide();

	$('.card').on('click',function() {
        var id = $(this).data('id');
        var page_url = '/postView/' + id + '/';

		// $('h1').addClass('textColorRed');

		$('#detailView').slideToggle('slow');
						//slideToggle, fadeToggle

        //$('#detailView').html(
        //    + "iframe src='http://localhost:8000/postView/' + id +'/' "
        //);
        $('#detailView').load(page_url);
	});

/*    $('#postView_Close_Button').on('click',function() {
        $('#detailView').fadeToggle('slow');
        $('#detailView').hide();
    });
*/
});

function postView_Close_Button() {
    $('#detailView').fadeOut('slow');
    $('#profile-detailView').fadeOut('slow');
    //$('#detailView').hide();
}

function postView(id) {
    var page_url = '/postView/' + id + '/';

    $('#profile-detailView').slideToggle('slow');
                    //slideToggle, fadeToggle

    $('#profile-detailView').load(page_url);
}