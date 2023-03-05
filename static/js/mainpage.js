function initDate(){
    $.ajax({
        type: "post",
        url: "/post",
        data: '',
        success: function (response) {
            var lastdate = response['lastdate'];
            var nextday = new Date(lastdate);

            nextday.setDate(nextday.getDate() + 1);

            ntd = nextday.toJSON().slice(0,10);
            $('#date').val(ntd);

        }
    });
}
function upload(){
    if ($('#date').val()){
        var dataframe = new FormData();
        dataframe.append('date',$('#date').val());
        dataframe.append('content',$('#content').val());
        $.ajax({
            type: "post",
            url: "/upload",
            contentType : false,
            processData : false,
            data: dataframe,
            success: function (response) {
                console.log('Upload succeed!');
            }
        });
        init();
    }
    else{
        alert('Please choose a date')
    }
    
}
function init(){
    initDate();
    $('#date').val('');
    $('#content').val('');
    $('#content').focus();
}
window.onload = function(){
    init()
    var content = document.getElementById('content');
    content.onkeyup = function(e){
        var e = window.event || e;
        if (e.code=='Enter'){
            upload();
        }
    }
    
}