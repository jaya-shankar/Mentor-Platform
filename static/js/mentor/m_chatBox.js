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
    const url = '/add_photos'
    document.querySelector('#uploadButton').onclick= function(e){
        e.preventDefault()
        const files = document.querySelector("#upload").files
        //console.log(files)
        const form = new FormData()
        let csrf=document.getElementsByName("csrfmiddlewaretoken")
        csrf=csrf[0].value
        csrflis=[]
        csrflis.push(csrf)

        for (let i = 0; i < files.length; i++) {
            let file = files[i]
            console.log(file)
            form.append('files', file,"image.png")
        }
        form.append('csrfmiddlewaretoken',csrflis)
        form.append("test","testing")

        for (var key of form.entries()) {
            console.log(key[0] + ', ' + key[1]);
        }
        
        fetch(url, {
            method: 'POST',
            body: form,
        }).then(response => {
            console.log(response)
            })
        
    }
    
        
    
})