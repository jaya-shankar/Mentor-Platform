document.addEventListener('DOMContentLoaded', function(){
    var modal = document.getElementById("doubtModal");

    var btn = document.querySelector(".doubt");
    
    btn.onclick = function() {
    modal.style.display = "block";

    }
    
    
    document.querySelector("#submitDoubt").onclick= function(){
        let message=document.querySelector("#doubtText").value
        let user=document.querySelector("#username").innerHTML
        let course=document.querySelector("#groupTitle").innerHTML
        let mentor = document.querySelector("#creatorName").innerHTML
        $.ajax(
            {
                status_code : 200 ,
                url : "/send_doubt" ,
                data : {
                    "message" : message,
                    "user" : user,
                    "course" : course,
                    "mentor" : mentor
                },
                dataType: 'json' ,
                success :  function(data){
                    console.log("sucess")
                }
            }
        )
        document.querySelector("#doubtText").value=""
        modal.style.display = "none";

    }





    // When the user clicks anywhere outside of the modal, close it
    window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
        }
    }

    document.querySelector("#cancelDoubt").onclick= function(){
        modal.style.display = "none";
    }

    
    
    
        
    
})