$(document).ready(function() {

	// $('#detailView').hide();
    $('#flip-card').hide();
	$('#profile-detailView').hide();
    $('#addCommentWin').hide();
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
    var frontPage_url = '/postView/' + id + '/';
    var backPage_url = '/comments/' + id + '/';

    $('#flip-card').slideDown('slow');
    $('#front').load(frontPage_url);
    $('#back').load(backPage_url);
}

function postView_Close_Button() {
    // $('#detailView').fadeOut('slow');
    $('#back').css('transform', 'rotateY(-180deg)');
    $('#back').css('z-index', '-1');

    $('#front').css('transform', 'rotateY(0deg)');
    $('#front').css('z-index', '10');

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
    $('#back').css('transform', 'rotateY(0deg)');
    $('#back').css('z-index', '10');

    $('#front').css('transform', 'rotateY(180deg)');
    $('#front').css('z-index', '-1');

}
function flipCardBack() {
    $('#back').css('transform', 'rotateY(-180deg)');
    $('#back').css('z-index', '-1');

    $('#front').css('transform', 'rotateY(0deg)');
    $('#front').css('z-index', '10');
}

function addCommentWin(post_id) {
    $('#addCommentWin').slideDown();
    $('#addCommentWin').load('/comments/addcomment/' + post_id + '/');
}
