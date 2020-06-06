document.addEventListener('DOMContentLoaded', function(){


    let courses=document.querySelectorAll(".course");
    
    
    
    for(let i=0;i<courses.length;i++)
    {
        
        courses[i].onclick=function(){
            let title=document.querySelector("#groupTitle")
            document.querySelector(".chatBox").hidden=false;
            title.innerHTML=courses[i].innerHTML
            $.ajax(
                {
                    status_code : 200 ,
                    url : "/get_chats" ,
                    data : {
                        "course_name" : title.innerHTML
                        
                    },
                    dataType: 'json' ,
                    success :  function(data){
                        document.querySelector("#creatorName").innerHTML=data.creatorName
                        let chatBox=document.getElementById("ChatBox")
                        chatBox.innerHTML=""
                        let prevDate=""
                        for(let i=0;i<data.chats.length;i++)
                        {
                            if(prevDate!=data.chats[i].date)
                            {
                                let div=document.createElement("div")
                                div.className="dateBox"
                                div.innerHTML=data.chats[i].date
                                chatBox.appendChild(div)
                            }
                            let div=document.createElement("div")
                            let timDiv=document.createElement("div")
                            timDiv.setAttribute("class","timeStamp")
                            div.setAttribute("class","textMsg")
                            timDiv.innerHTML=data.chats[i].time
                            div.innerHTML=data.chats[i].message
                            div.appendChild(timDiv)
                            chatBox.appendChild(div)
                            prevDate=data.chats[i].date
                            document.getElementById("view").scrollIntoView();
                        }
                        
                    }
                }
            )

        }
    }

   
    
})