$(document).ready(function(){
    $(".save-comment").on('click',function(){
        var _musicid=$(this).data('music');
        var _comment=$(".comment-text-"+_musicid).val();
        if (_comment != ''){
            $.ajax({
                url:"/save-comment/",
                type:"post",
                data:{
                    comment:_comment,
                    musicid:_musicid,
                    csrfmiddlewaretoken:"{{csrf_token}}"
                },
                dataType:'json',
                beforeSend:function(){
                    $(".save-comment").addClass('disabled').text('Saving...');
                },
                success:function(res){
                    if(res.bool==true){
                        $(".comment-text-"+_musicid).val('');
                        var _html='<div class="card mb-2 animate__animated animate__fadeInUp">\
                        <div class="card-body">\
                            <p>'+'<i class="fas fa-quote-right"></i>'+" "+_comment+'</p>\
                            <p>\
                                <h4><i class="fas fa-music"></i> {{request.user}}</h4>\
                            </p>\
                        </div>\
                    </div>';
                    $(".comment-wrapper-"+_musicid).append(_html);
                    }
                    $(".save-comment").removeClass('disabled').text('Add');
                }
            });
        }
    });
});
