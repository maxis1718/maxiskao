$(document).ready(function(){
	events();
});


function events()
{
	$('.socialnetwork-block').hover(function(){
		// alert('!');
		$(this).find('img').toggleClass('hide');
	});
	// $('.nav-item').find('span').hover(function(){ $(this).parent().find('.tri').hide(); });
	// $('.nav-item').find('span').hover(function(){ $(this).siblings('.tri').toggleClass('hide'); });
}
