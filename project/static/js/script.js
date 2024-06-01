$(document).ready(function() {

	// $('#detailView').hide();
    $('#flip-card').hide();
	$('#profile-detailView').hide();
/*
	$('#card-button').on('click',function() {
        var id = $(this).data('id');
        var page_url = '/postView/' + id + '/';

        $('#flip-card').slideDown('slow');
        $('#flip-card-front').load(page_url);

        $('#detailView').slideToggle('slow');
						//slideToggle, fadeToggle
        $('#detailView').load(page_url);

    });
*/
});

function cardButtonClick(id) {
    var page_url = '/postView/' + id + '/';
    $('#flip-card').slideDown('slow');
    $('#flip-card-front').load(page_url);
}

function postView_Close_Button() {
    // $('#detailView').fadeOut('slow');
    $('#flip-card').fadeOut('slow');
    $('#profile-detailView').fadeOut('slow');
    //$('#detailView').hide();
}

function postView(id) {
    var page_url = '/postView/' + id + '/';

    $('#profile-detailView').slideToggle('slow');
                    //slideToggle, fadeToggle

    $('#profile-detailView').load(page_url);
}

function postViewFlip() {
    $('#flip-card').addClass('flip-card-rotate');
    $('#flip-card-inner').addClass('flip-card-rotate');
}