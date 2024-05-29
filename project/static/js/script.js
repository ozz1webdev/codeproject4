$(document).ready(function() {

	$('#detailViewPage').hide(); //Hide div with id=detailViewPage

	$('.card').on('click',function() {
        var id = $(this).data('id');
        var image = $(this).data('image');

		// $('h1').addClass('textColorRed');

		$('#detailViewPage').slideToggle('slow');
						//slideToggle, fadeToggle

        $('#detailViewPage').html(
            + "<h1 id='detailViewPageTitle'> " + id + " </h1>"
            + "<img id='detailViewPageImage' src='" + "{{post.image.url}}" + image + "'>"
        );
	});

});