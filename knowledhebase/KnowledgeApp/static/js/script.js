
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
    let searchTerms = inputArray.join(',');
    let url = `/startpage/?search_terms=${searchTerms}`;
    window.location.href = url;

  }
  }
 