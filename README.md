# EDJ : API Stereopub

Cette API vous permet d'enregistrer et de consulter les votes dans le cadre du 
projet Stéréopub.

## Consulter les votes

Tous les votes sont visibles au format [JSON](http://fr.wikipedia.org/wiki/JavaScript_Object_Notation) à l'adresse suivante :<br />
http://edj-stereopub.herokuapp.com/vote

Les données retournées prennent cette forme :
```JSON
[
  {
    "_updated": "Thu, 01 Jan 1970 00:00:00 GMT",
    "media": 0,
    "age": 25,
    "sex": "male",
    "_created": "Thu, 01 Jan 1970 00:00:00 GMT",
    "_id": "53360a98f4d8a6cb0139abc0",
    "_etag": "83996ada84711be65e89a9efaf8ea6ed7caf27a8"
  }
]
```

Avec Angular, vous pouvez récupérer les données depuis votre controlleur de cette façon:
```js
function VoteCtrl($http, $scope) {
    $http.get("http://edj-stereopub.herokuapp.com/vote").success(function(data)        
        $scope.votes = data;
    );    

    // ...
}

VoteCtrl.$inject = ["$http", "$scope"]
```

Pour obtenir des résultats plus précis (filter par age ou par sexe), je vous
invite à consulter [la documentation de Eve](http://python-eve.org/features.html#filtering-and-sorting), l'outil utilisé par cette API.

## Envoyer un vote

L'API vous permet d'envoyer des votes sans authentification avec une limite 
drastique pour chaque IP de 60 votes par plage de 20 minutes.

**Cette limitation permet d'éviter les votes abusifs et peu au besoin être élevée.**

Pour envoyer un vote, utilisez le code suivant depuis votre controlleur :

```js
function VoteCtrl($http, $scope) {
    // ...
    var vote = {
        sex      : "male", // Le sexe de l'utilisateur
        age      : 25,     // Son age
        media    : 10,     // L'identifiant UNIQUE du media (image, vidéo) évalué
        is_sexist: true    // La valeur du vote ("true" si le media est sexiste, "false" sinon)
    }
    $http.post("http://edj-stereopub.herokuapp.com/vote", vote);
}

VoteCtrl.$inject = ["$http", "$scope"]
```


