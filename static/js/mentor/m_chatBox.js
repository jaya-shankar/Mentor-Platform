document.addEventListener('DOMContentLoaded', function(){
    
    document.querySelector(".submitButton").onclick=function(){
        let message=document.querySelector(".textBox").value;
        document.querySelector(".textBox").value=""
        if(message!=""){

            let div=document.createElement("div");
            let courseName=document.querySelector("#groupTitle").innerHTML
            div.className="textMsg";
            div.innerHTML=message;
            let screen=document.querySelector(".Screen");
            screen.appendChild(div);
            
            $.ajax(
                {
                    status_code : 200 ,
                    url : "/add_message" ,
                    data : {
                        "message" : message ,
                        "course_name" : courseName 
                        
                    },
                    dataType: 'json' ,
                    success :  function(data){
                        console.log("sucess")
                    }
                }
            )
        }
        return false;
    }
        
    
})