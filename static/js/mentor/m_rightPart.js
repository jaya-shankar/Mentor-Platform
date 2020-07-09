document.addEventListener('DOMContentLoaded', function(){

    var modal = document.getElementById("doubtModal");
    var username = document.getElementById("username").innerHTML;
    var doubtScreen=document.querySelector("#doubtScreen")

    document.querySelector("#showDoubts").onclick =function(){
        doubtScreen.innerHTML=""
        $.ajax(
            {
                status_code : 200 ,
                url : "/get_doubts" ,
                data : {
                    "user_name" : username
                },
                dataType: 'json' ,
                success :  function(data){
                    for(let i=0;i<data.doubts.length;i++)
                    {
                        let div=createDoubtCard(data.doubts[i])
                        
                        doubtScreen.appendChild(div)
                        
                    }
                }
            }
        )
        modal.style.display = "block";

        return false
    }

    function createDoubtCard(data)
    {
        console.log(data)
        let div=document.createElement("div")
        div.className="panel panel-default doubtBox"
        div.setAttribute("data-id",data.id)
        {let span=document.createElement("spam")
        span.innerHTML="<b>Course : </b>"+data.course
        div.appendChild(span)}
        {let div1=document.createElement("div")
        div1.innerHTML="<b>From : </b>"+ data.sender
        div.appendChild(div1)}
        let divDoubt=document.createElement("div")
        divDoubt.className="panel-body"
        divDoubt.style.background="aqua"
        divDoubt.innerHTML=data.message
        div.appendChild(divDoubt)
        {
            let button=document.createElement("button")
            button.className="btn btn-outline-danger"
            button.innerHTML="Remove"
            button.setAttribute("id","remove")
            button.onclick = function(){
                removeDoubtButton(div)
            }
            div.appendChild(button)
        }
        {let button=document.createElement("button")
        button.className="btn btn-outline-info"
        button.innerHTML="Reply"
        button.setAttribute("id","reply")
        div.appendChild(button)
        let reply=addTextArea(div)
        button.onclick= function(){
            reply.toggleAttribute("hidden")
            }
        }

            
        return div
    }

    function addTextArea(parent)
    {
        let div=document.createElement("div")
        div.setAttribute("hidden",true)
        let textarea=document.createElement("textarea")
        let submit=document.createElement("button")
        submit.innerHTML="Submit"
        submit.setAttribute("class","btn btn-outline-info")
        textarea.setAttribute("rows",3)
        textarea.setAttribute("cols",70)
        parent.appendChild(document.createElement("br"))
        div.appendChild(textarea)
        submit.onclick=function(){
            doubtID=parent.dataset.id
            submitDoubt(textarea.value,doubtID)
            textarea.remove()
            submit.remove()
        }
        div.appendChild(submit)
        parent.appendChild(div)
        return div
    }

    function removeDoubtButton(parent)
    {

        doubtID=parent.dataset.id
        $.ajax({
                status_code : 200 ,
                url : "/remove_doubt" ,
                data : {
                    "doubt_id" : doubtID
                },
                dataType: 'json' ,
                success :  function(data){
                    console.log("done changed")
                }
            })
        parent.remove();
    }

    function submitDoubt(message,doubtID)
    {
        $.ajax({
            status_code : 200 ,
            url : "/send_doubt" ,
            data : {
                "doubt_id" : doubtID ,
                "message" : message
            },
            dataType: 'json' ,
            success :  function(data){
                console.log("done changed")
            }
        })
    }

    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
            }
        }
    
   

    
})