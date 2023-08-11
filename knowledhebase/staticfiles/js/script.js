async function saveArticle(){
    console.log('startsave')
    fd=getFormdata();
    try {
    
        let response = await fetch("/startpage/", {
          method: "POST",
          body: fd,
        });
       let json = await response.json();
       console.log(json)
       console.log('endsave') 

    } catch (error) {
        alert("An Error occured");
      }
    }

function getFormdata() {
    let fd = new FormData();
    //let token = "{{ csrf_token }}";
    fd.append("text", textfield.value);
    fd.append("author", author.value);
    fd.append("title", title.value);
    return fd;
  }