Knowledge App

App for storing articles about any theme at server:

For Using clone git-repository to environment and install requirements.txt.
Set superuser and you can loggin at /admin.
Then you can save new articles at /add/ and view them at /startpage/.
Also you can search authors, content and title at startpage.

Therefore views StartpageView and AddView are created.
Both can handle get and post requests:
StartpageView:
    get:Gets all articles and renders in template
    post: Search-request, renders response to template

AddView:
    get:Renders add-form
    post: Saves new article (in case data is valid)to server