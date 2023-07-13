$(document).ready(function(){
    $(".add_to_playlist").on('click',function(){
        var _playlist_name=$(this).text();
        var _music_pk =$(this).data('music');
        $.ajax({
            url:"/music/add/",
            type:"post",
            data:{
                playlist_name:_playlist_name,
                music_pk:_music_pk,
                csrfmiddlewaretoken:"{{csrf_token}}"
            },
            dataType:'json',
            beforeSend:function(){
                $(this).addClass('disabled').text('Adding...');
            },
            success:function(res){
                if(res.bool==true){
                    location.reload();
                }
                $(this).removeClass('disabled').text('Add To Playlist');
            }
        });
    });
});
