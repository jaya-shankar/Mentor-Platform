document.addEventListener('DOMContentLoaded', function(){

    document.getElementById("mentor_active").className="nav-item nav-link active"
    document.getElementById("student_active").className="nav-item nav-link"
    
    document.querySelector("#submit").onclick=function(event){
        let message=document.querySelector(".textBox").value;
        let screen=document.querySelector(".Screen");
        document.querySelector(".textBox").value=""
        const files = document.querySelector("#upload").files
        let courseName=document.querySelector("#groupTitle").innerHTML
        const form = new FormData()
        let csrf=document.getElementsByName("csrfmiddlewaretoken")
        csrf=csrf[0].value
        csrflis=[]
        csrflis.push(csrf)
        form.append('csrfmiddlewaretoken',csrflis)
        form.append("course_name" , courseName)
        if(message!="")
        {
            let div=document.createElement("div");
            div.className="textMsg";
            div.innerHTML=message;
            screen.appendChild(div);
            form.append("message" , message)
        }
        if(files.length!=0)
        {
            let img=document.createElement("img")
            img.className="imgMsg"
            let reader= new FileReader()
            reader.addEventListener("load" ,function(){
                img.setAttribute("src",this.result)
            });
            reader.readAsDataURL(files[0])
            screen.appendChild(img)
            for (let i = 0; i < files.length; i++) {
                let file = files[i]
                form.append('files', file,"image.png")
            }
        }
            
            const url = '/add_message'
            fetch(url, {
                method: 'POST',
                body: form,
            }).then(response => {
                console.log(response)
                })
            
            
        
        return false;
    }
    
        
    
})