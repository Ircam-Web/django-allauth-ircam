# django-allauth-ircam
 Ircam OAuth2 provider for django-allauth
# related to feature/oauth2 in Mezzo
Mezzo, user authentication vs ircam_auth success workflow
[![](https://mermaid.ink/img/eyJjb2RlIjoic2VxdWVuY2VEaWFncmFtXG5cbiAgICBwYXJ0aWNpcGFudCBVc2VyXG4gICAgcGFydGljaXBhbnQgTWV6em9cbiAgICBwYXJ0aWNpcGFudCBJcmNhbV9BdXRoXG4gXG4gICAgVXNlci0-PitNZXp6byA6IGNsaWNrcyBvbiBcIkxvZ2luXCJcbiAgICBNZXp6by0tPj4rVXNlciA6IHJlZGlyZWN0IHRvIE9hdXRoIHNlcnZlclxuICAgIFVzZXItPj4rSXJjYW1fQXV0aCA6IHNpZ25zIGluIGFuZCBhdXRob3JpemUgTWV6em9cbiAgICBJcmNhbV9BdXRoLT4-LVVzZXIgOiBnaXZlIHRva2VuIGFuZCByZWRpcmVjdCB0byBNZXp6b1xuICAgIFVzZXItPj4rTWV6em8gOiBnaXZlIHRva2VuXG4gICAgTWV6em8tPj4rSXJjYW1fQXV0aCA6IHZlcmlmeSB0b2tlbi9nZXQgcHJvZmlsZVxuICAgIElyY2FtX0F1dGgtPj4tTWV6em8gOiBBQ0svZ2l2ZSBwcm9maWxlXG4gICAgbG9vcFxuICAgICAgICBNZXp6by0tPj5NZXp6byA6IE9BVVRIMmNhbGxCYWNrVmlldy5jb21wbGV0ZV9sb2dpbigpXG4gICAgZW5kXG4gICAgTWV6em8tLT4-LVVzZXIgOiByZWRpcmVjdCB0byAvcGVyc29uXG4gICAgVXNlci0-PitNZXp6byA6IC9wZXJzb25cbiAgICBsb29wXG4gICAgICAgIE1lenpvLS0-Pk1lenpvIDogY3JlYXRlIG9yIHVwZGF0ZSBQZXJzb25cbiAgICBlbmRcbiAgICBNZXp6by0tPj4tVXNlciA6IEhUVFAgMjAwIE9LIiwidXBkYXRlRWRpdG9yIjpmYWxzZX0)](http://localhost:8080/#/edit/eyJjb2RlIjoic2VxdWVuY2VEaWFncmFtXG5cbiAgICBwYXJ0aWNpcGFudCBVc2VyXG4gICAgcGFydGljaXBhbnQgTWV6em9cbiAgICBwYXJ0aWNpcGFudCBJcmNhbV9BdXRoXG4gXG4gICAgVXNlci0-PitNZXp6byA6IGNsaWNrcyBvbiBcIkxvZ2luXCJcbiAgICBNZXp6by0tPj4rVXNlciA6IHJlZGlyZWN0IHRvIE9hdXRoIHNlcnZlclxuICAgIFVzZXItPj4rSXJjYW1fQXV0aCA6IHNpZ25zIGluIGFuZCBhdXRob3JpemUgTWV6em9cbiAgICBJcmNhbV9BdXRoLT4-LVVzZXIgOiBnaXZlIHRva2VuIGFuZCByZWRpcmVjdCB0byBNZXp6b1xuICAgIFVzZXItPj4rTWV6em8gOiBnaXZlIHRva2VuXG4gICAgTWV6em8tPj4rSXJjYW1fQXV0aCA6IHZlcmlmeSB0b2tlbi9nZXQgcHJvZmlsZVxuICAgIElyY2FtX0F1dGgtPj4tTWV6em8gOiBBQ0svZ2l2ZSBwcm9maWxlXG4gICAgbG9vcFxuICAgICAgICBNZXp6by0tPj5NZXp6byA6IE9BVVRIMmNhbGxCYWNrVmlldy5jb21wbGV0ZV9sb2dpbigpXG4gICAgZW5kXG4gICAgTWV6em8tLT4-LVVzZXIgOiByZWRpcmVjdCB0byAvcGVyc29uXG4gICAgVXNlci0-PitNZXp6byA6IC9wZXJzb25cbiAgICBsb29wXG4gICAgICAgIE1lenpvLS0-Pk1lenpvIDogY3JlYXRlIG9yIHVwZGF0ZSBQZXJzb25cbiAgICBlbmRcbiAgICBNZXp6by0tPj4tVXNlciA6IEhUVFAgMjAwIE9LIiwidXBkYXRlRWRpdG9yIjpmYWxzZX0)
# OAUTH2CallBackView.complete_login(request)
[![](https://mermaid.ink/img/eyJjb2RlIjoiZ3JhcGggVERcblxuICAgIEJbXCJleHRyYV9kYXRhcyA9IHJlc3AuanNvbihyZXF1ZXN0KTxici8-ZXh0X2lkID0gZXh0cmFfZGF0YXNbJ2V4dF9pZCddPGJyLz51c2VybmFtZSA9IGV4dHJhX2RhdGFzWyd1c2VybmFtZSddPGJyLz5lbWFpbCA9IGV4dHJhX2RhdGFzWydlbWFpbCddXCJdXG4gICAgQ1tcInNvY2lhbF91c2VyID0gc29jaWFsbG9naW5fZnJvbV9yZXNwb25zZShleHRfdWlkKTxici8-cmV0dXJuIHNvY2lhbF91c2VyXCJdXG4gICAgQiAtLT4gRHtcIlNvY2lhbEFjY291bnQoZXh0X2lkKTxici8-ZXhpc3RzP1wifVxuICAgIEQgLS0-fFllc3wgRVtcIkdldCBVc2VyIGJ5IFNvY2lhbEFjY291bnQudXNlcl9pZDxici8-VXBkYXRlIFVzZXJcIl0gLS0-IENcbiAgICBEIC0tPnxOb3wgRntcInVuaXF1ZTxici8-IFVzZXIodXNlcm5hbWUpIDxici8-ZXhpc3RzP1wifVxuICAgIEYgLS0-fE5vbmV8IEdbXCJjcmVhdGUgVXNlclwiXSAtLT4gSFxuICAgIEYgLS0-fE5vdCB1bmlxdWV8IFhbXCJSZXNwIHNlcnZlciA1MDBcIl1cbiAgICBGIC0tPnxZZXN8IElbXCJVcGRhdGUgVXNlclwiXSAtLT4gSFtcImNyZWF0ZSBTb2NpYWxBY2NvdW50KHVzZXIuaWQsZXh0X2lkKTxici8-Y3JlYXRlIEVtYWlsKGVtYWlsKVwiXSAtLT4gQ1xuIFxuIiwidXBkYXRlRWRpdG9yIjpmYWxzZX0)](http://localhost:8080/#/edit/eyJjb2RlIjoiZ3JhcGggVERcblxuICAgIEJbXCJleHRyYV9kYXRhcyA9IHJlc3AuanNvbihyZXF1ZXN0KTxici8-ZXh0X2lkID0gZXh0cmFfZGF0YXNbJ2V4dF9pZCddPGJyLz51c2VybmFtZSA9IGV4dHJhX2RhdGFzWyd1c2VybmFtZSddPGJyLz5lbWFpbCA9IGV4dHJhX2RhdGFzWydlbWFpbCddXCJdXG4gICAgQ1tcInNvY2lhbF91c2VyID0gc29jaWFsbG9naW5fZnJvbV9yZXNwb25zZShleHRfdWlkKTxici8-cmV0dXJuIHNvY2lhbF91c2VyXCJdXG4gICAgQiAtLT4gRHtcIlNvY2lhbEFjY291bnQoZXh0X2lkKTxici8-ZXhpc3RzP1wifVxuICAgIEQgLS0-fFllc3wgRVtcIkdldCBVc2VyIGJ5IFNvY2lhbEFjY291bnQudXNlcl9pZDxici8-VXBkYXRlIFVzZXJcIl0gLS0-IENcbiAgICBEIC0tPnxOb3wgRntcInVuaXF1ZTxici8-IFVzZXIodXNlcm5hbWUpIDxici8-ZXhpc3RzP1wifVxuICAgIEYgLS0-fE5vbmV8IEdbXCJjcmVhdGUgVXNlclwiXSAtLT4gSFxuICAgIEYgLS0-fE5vdCB1bmlxdWV8IFhbXCJSZXNwIHNlcnZlciA1MDBcIl1cbiAgICBGIC0tPnxZZXN8IElbXCJVcGRhdGUgVXNlclwiXSAtLT4gSFtcImNyZWF0ZSBTb2NpYWxBY2NvdW50KHVzZXIuaWQsZXh0X2lkKTxici8-Y3JlYXRlIEVtYWlsKGVtYWlsKVwiXSAtLT4gQ1xuIFxuIiwidXBkYXRlRWRpdG9yIjpmYWxzZX0)
