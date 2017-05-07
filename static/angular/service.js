(function(){
    'use strict';

    scanApp.factory('indexFactory', function($http){
        var url = '/api/info/';
        return {
            list: function(){
                return $http.get(url);
            },
            post: function(data){
                return $http.post(url, data);
            }
        }
    })
}());