
document.addEventListener('DOMContentLoaded', function(){

   
    var CourseModal = document.querySelector(".CourseDetails");
    var modal = document.getElementById("answersModal");
    var answerScreen=document.querySelector("#answersScreen")
    var username = document.getElementById("username").innerHTML;
    let selectedCourse;
    


    let joinButtons=document.querySelectorAll("#joinButton")
    
    for(let i=0;i<joinButtons.length;i++)
    {
        joinButtons[i].onclick=function(){
            courseName=joinButtons[i].previousElementSibling.innerHTML;
            $.ajax(
                {
                    status_code : 200 ,
                    url : "/get_details" ,
                    data : {
                        "course_name" :courseName
                        
                    },
                    dataType: 'json' ,
                    success :  function(data){
                        fillTheDetails(data)
                        document.getElementById("courseName").value=courseName
                        CourseModal.style.display = "block";
                        
                    }
                }
            )
            
        }
    }

    // When the user clicks anywhere outside of the CourseModal, close it
    window.onclick = function(event) {
        
        if (event.target == CourseModal) {
            CourseModal.style.display = "none";
        }
        
    }

    goBack = document.querySelector("#goBack")
    goBack.onclick= function(){
        CourseModal.style.display = "none";
        
        return false
    }

    AMgoBack=document.querySelector("#AMgoBack")
    AMgoBack.onclick= function(){
        modal.style.display = "none";
        return false
    }

    joinCourse=document.querySelector("#joinCourse")
    joinCourse.onclick= function(){
    let button=document.createElement("button");
    button.className="course";
    courseName=joinButtons[selectedCourse].previousElementSibling.innerHTML;
    button.innerHTML=courseName;
    button.onclick=function(){
        let title=document.querySelector("#groupTitle")
        title.innerHTML=button.innerHTML
        }   
    courseList=document.querySelector(".sidenav");
    courseList.appendChild(button);
        
    let parent=joinButtons[selectedCourse].parentElement;
    parent.remove()

    CourseModal.style.display = "none";
        }
    
    
    function fillTheDetails(data)
    {
        document.getElementById("nameOfCourse").innerHTML=data.title
        document.getElementById("Description").innerHTML=data.description
        document.getElementById("Level").innerHTML=data.level
        document.getElementById("Takeaways").innerHTML=data.takeaways
        document.getElementById("Creator").innerHTML=data.creator
    }

    document.querySelector("#showAnswers").onclick =function(){
        console.log("hello")
        answersScreen.innerHTML=""
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
                        answerScreen.appendChild(div)
                    }
                }
            }
        )
        modal.style.display = "block";

        return false
    }

    
    function createDoubtCard(data)
    {
        let div=document.createElement("div")
        div.className="panel panel-default doubtBox"
        div.setAttribute("data-id",data.id)
        {let span=document.createElement("spam")
        span.innerHTML=data.sender
        div.appendChild(span)}
        {let span=document.createElement("spam")
        span.innerHTML=data.course
        div.appendChild(span)}
        let divDoubt=document.createElement("div")
        divDoubt.className="panel-body"
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
        button.onclick= function(){
            addTextArea(div)
            button.disabled= true
        }
        div.appendChild(button)}
            
        return div
    }

    function addTextArea(parent)
    {
        let textarea=document.createElement("textarea")
        let submit=document.createElement("button")
        submit.innerHTML="Submit"
        submit.setAttribute("class","btn btn-outline-info")
        textarea.setAttribute("rows",3)
        textarea.setAttribute("cols",70)
        parent.appendChild(document.createElement("br"))
        parent.appendChild(textarea)
        parent.appendChild(submit)
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

    
})





            