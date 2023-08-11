
async function saveArticle(){
    console.log('startsave')
    fd= getFormdata() ;
    let token = "{{ csrf_token }}";
    try {
          let response = await fetch("/add/", {
          method: "POST",
          headers: {
             "X-CSRFToken": token,
          },
          body: fd,
    });
       if (response.status==201){
        window.location.href = '/startpage/';}
       else{
        alert("An Error occured");
        }
    } catch (error) {
        alert("An Error occured");
      }
    }

   
function getFormdata() {
    let fd = new FormData();
    let token = "{{ csrf_token }}";
    console.log(token)
    fd.append("text", textfield.value);
    fd.append("author", author.value);
    fd.append("title", title.value);
    fd.append("csrfmiddlewaretoken", "{{ csrf_token }}")
    return fd;
  }


  async function filter(event){
    if (event.key=='Enter'){
    input=document.getElementById("search-input");
    const inputValue = input.value.toLowerCase();
    const inputArray = inputValue.split(" ").filter(item => item.trim() !== "");
    let body=JSON.stringify({'search_terms':inputArray})
    console.log(body)
    let token = "{{ csrf_token }}";
    let response= await fetch("/startpage/", {
      method: "POST",
      headers: {
         "X-CSRFToken": token,
         "Content-Type":"application/json",
         "Accept":"application/json"

         
    },
      body: body
    });
    if (response.ok) {
      
      const responseData = await response.json();
      console.log(responseData)
      const articlesContainer = document.getElementById('allArticles');
      articlesContainer.innerHTML = responseData;
  } else {
      console.error("Fehler bei der Anfrage:", response.status);
  }
   

    
    

   
  }
  }
 